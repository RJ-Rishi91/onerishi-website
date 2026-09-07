from datetime import datetime

from slugify import slugify
from sqlalchemy.orm import Session

from . import models, schemas


def make_unique_slug(db: Session, title: str) -> str:
    base = slugify(title)
    slug = base
    i = 2
    while db.query(models.Post).filter(models.Post.slug == slug).first():
        slug = f"{base}-{i}"
        i += 1
    return slug


def calc_read_time(body: str) -> int:
    words = len(body.split())
    return max(1, round(words / 200))  # ~200 words/minute


def create_post(db: Session, post: schemas.PostCreate) -> models.Post:
    slug = post.slug or make_unique_slug(db, post.title)
    db_post = models.Post(
        slug=slug,
        title=post.title,
        category=post.category,
        excerpt=post.excerpt,
        body=post.body,
        cover_image=post.cover_image,
        status=post.status,
        read_time_minutes=calc_read_time(post.body),
        published_at=datetime.utcnow() if post.status == "published" else None,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(db: Session, db_post: models.Post, updates: schemas.PostUpdate) -> models.Post:
    data = updates.model_dump(exclude_unset=True)
    was_draft = db_post.status != "published"

    for field, value in data.items():
        setattr(db_post, field, value)

    if "body" in data:
        db_post.read_time_minutes = calc_read_time(db_post.body)

    if was_draft and db_post.status == "published" and not db_post.published_at:
        db_post.published_at = datetime.utcnow()

    db.commit()
    db.refresh(db_post)
    return db_post


def get_published_posts(db: Session, category: str | None = None):
    query = db.query(models.Post).filter(models.Post.status == "published")
    if category:
        query = query.filter(models.Post.category == category)
    return query.order_by(models.Post.published_at.desc()).all()


def get_all_posts(db: Session):
    return db.query(models.Post).order_by(models.Post.created_at.desc()).all()


def get_post_by_slug(db: Session, slug: str):
    return db.query(models.Post).filter(models.Post.slug == slug).first()


def get_post_by_id(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def delete_post(db: Session, db_post: models.Post):
    db.delete(db_post)
    db.commit()
