import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Add app directory to sys.path so it can import app modules
current_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(current_dir))

from app.database import SessionLocal, engine, Base
from app import models, crud

Base.metadata.create_all(bind=engine)

def parse_markdown_file(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return None, content

    fm_text, body = match.groups()
    metadata = {}
    current_key = None
    for line in fm_text.splitlines():
        line_clean = line.strip()
        if not line_clean or line_clean.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            metadata[key] = val
            current_key = key

    return metadata, body.strip()

def parse_date(date_str: str | None) -> datetime:
    if not date_str:
        return datetime.utcnow()
    # Try various date formats
    for fmt in ("%B %d, %Y", "%b %d, %Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return datetime.utcnow()

def seed_posts():
    db = SessionLocal()
    writing_dir = None
    for d in [current_dir.parent / "src" / "content" / "writing", current_dir / "writing_backup"]:
        if d.exists() and list(d.glob("*.md")):
            writing_dir = d
            break
    if not writing_dir:
        print(f"No writing directory found")
        return

    md_files = list(writing_dir.glob("*.md"))
    print(f"Found {len(md_files)} markdown files in {writing_dir}")

    seeded_count = 0
    for file_path in md_files:
        slug = file_path.stem
        metadata, body = parse_markdown_file(file_path)
        if not metadata:
            print(f"Skipping {file_path.name} (no frontmatter)")
            continue

        existing = db.query(models.Post).filter(models.Post.slug == slug).first()
        if existing:
            print(f"Post already exists: {slug}")
            continue

        title = metadata.get("title", slug.replace("-", " ").title())
        category = metadata.get("category", "Building on the Internet")
        excerpt = metadata.get("description", "")
        cover_image = metadata.get("coverImage")
        published_at = parse_date(metadata.get("date"))

        post = models.Post(
            slug=slug,
            title=title,
            category=category,
            excerpt=excerpt,
            body=body,
            cover_image=cover_image,
            status="published",
            read_time_minutes=crud.calc_read_time(body),
            published_at=published_at,
        )
        db.add(post)
        seeded_count += 1
        print(f"Seeded: {slug} ({category})")

    db.commit()
    db.close()
    print(f"Successfully seeded {seeded_count} posts into the database.")

if __name__ == "__main__":
    seed_posts()
