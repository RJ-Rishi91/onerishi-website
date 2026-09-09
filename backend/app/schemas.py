from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PostBase(BaseModel):
    title: str
    category: str
    excerpt: str
    body: str
    cover_image: Optional[str] = None
    status: str = Field(default="draft", pattern="^(draft|scheduled|published)$")
    scheduled_at: Optional[datetime] = None  # required when status == "scheduled"

    # SEO — optional overrides. Leave blank to fall back to title/excerpt/cover_image.
    meta_title: Optional[str] = None
    meta_description: Optional[str] = None
    meta_keywords: Optional[str] = None
    og_image: Optional[str] = None


class PostCreate(PostBase):
    slug: Optional[str] = None  # auto-generated from title if omitted


class PostUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    category: Optional[str] = None
    excerpt: Optional[str] = None
    body: Optional[str] = None
    cover_image: Optional[str] = None
    status: Optional[str] = Field(default=None, pattern="^(draft|scheduled|published)$")
    scheduled_at: Optional[datetime] = None
    meta_title: Optional[str] = None
    meta_description: Optional[str] = None
    meta_keywords: Optional[str] = None
    og_image: Optional[str] = None


class PostOut(PostBase):
    id: int
    slug: str
    read_time_minutes: int
    created_at: datetime
    updated_at: datetime
    published_at: Optional[datetime] = None

    # Resolved values — always use these when rendering <title>/<meta> tags,
    # not the raw meta_title/meta_description/og_image above, which may be blank.
    effective_meta_title: str
    effective_meta_description: str
    effective_og_image: Optional[str] = None

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
