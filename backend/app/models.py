from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from .database import Base

CATEGORIES = [
    "Marketing Experiments",
    "Marketing × Tech",
    "Building on the Internet",
    "Projects & Behind-the-Scenes",
    "Career & Learning",
]


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    excerpt = Column(String, nullable=False)
    body = Column(Text, nullable=False)  # Markdown
    cover_image = Column(String, nullable=True)
    read_time_minutes = Column(Integer, nullable=False, default=1)
    status = Column(String, nullable=False, default="draft")  # draft | scheduled | published
    scheduled_at = Column(DateTime, nullable=True)  # required when status == "scheduled"


    meta_title = Column(String, nullable=True)
    meta_description = Column(String, nullable=True)
    meta_keywords = Column(String, nullable=True)  # comma-separated
    og_image = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = Column(DateTime, nullable=True)

    # Resolved SEO values — what the frontend should actually render.
    # Falls back to the main content fields when no SEO override is set,
    # so the frontend never has to duplicate this logic.
    @property
    def effective_meta_title(self) -> str:
        return self.meta_title or self.title

    @property
    def effective_meta_description(self) -> str:
        return self.meta_description or self.excerpt

    @property
    def effective_og_image(self) -> str | None:
        return self.og_image or self.cover_image
