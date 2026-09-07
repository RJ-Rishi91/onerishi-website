import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import auth, crud, models, schemas
from .database import Base, engine, get_db
from .webhook import trigger_github_rebuild

Base.metadata.create_all(bind=engine)

app = FastAPI(title="OneRishi Blog API")

# Restrict this to your real frontend origin(s) in production via CORS_ORIGINS env var,
# comma-separated, e.g. "https://onerishi.in,https://www.onerishi.in"
origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------- Public routes (Writing page + blog post template call these) ----------

@app.get("/api/posts", response_model=list[schemas.PostOut])
def list_published_posts(category: str | None = None, db: Session = Depends(get_db)):
    return crud.get_published_posts(db, category)


@app.get("/api/posts/{slug}", response_model=schemas.PostOut)
def get_published_post(slug: str, db: Session = Depends(get_db)):
    post = crud.get_post_by_slug(db, slug)
    if not post or post.status != "published":
        raise HTTPException(status_code=404, detail="Post not found")
    return post


# ---------- Auth ----------

@app.post("/api/admin/login", response_model=schemas.TokenResponse)
def login(payload: schemas.LoginRequest):
    if not auth.verify_admin_password(payload.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return schemas.TokenResponse(access_token=auth.create_access_token())


# ---------- Admin routes (require Bearer token — used by the admin dashboard UI) ----------

@app.get("/api/admin/posts", response_model=list[schemas.PostOut])
def list_all_posts(db: Session = Depends(get_db), _: bool = Depends(auth.get_current_admin)):
    return crud.get_all_posts(db)


@app.get("/api/admin/posts/{post_id}", response_model=schemas.PostOut)
def get_admin_post(
    post_id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(auth.get_current_admin),
):
    db_post = crud.get_post_by_id(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@app.post("/api/admin/posts", response_model=schemas.PostOut)
def create_post(
    post: schemas.PostCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    _: bool = Depends(auth.get_current_admin),
):
    created = crud.create_post(db, post)
    if created.status == "published":
        background_tasks.add_task(trigger_github_rebuild, "cms_post_published", {"post_id": created.id, "action": "created"})
    return created


@app.put("/api/admin/posts/{post_id}", response_model=schemas.PostOut)
def update_post(
    post_id: int,
    updates: schemas.PostUpdate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    _: bool = Depends(auth.get_current_admin),
):
    db_post = crud.get_post_by_id(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    was_published = db_post.status == "published"
    updated = crud.update_post(db, db_post, updates)
    if was_published or updated.status == "published":
        background_tasks.add_task(trigger_github_rebuild, "cms_post_published", {"post_id": updated.id, "action": "updated"})
    return updated


@app.delete("/api/admin/posts/{post_id}")
def delete_post(
    post_id: int,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    _: bool = Depends(auth.get_current_admin),
):
    db_post = crud.get_post_by_id(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    was_published = db_post.status == "published"
    crud.delete_post(db, db_post)
    if was_published:
        background_tasks.add_task(trigger_github_rebuild, "cms_post_published", {"post_id": post_id, "action": "deleted"})
    return {"deleted": True}


@app.get("/api/health")
def health():
    return {"status": "ok"}
