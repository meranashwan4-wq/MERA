from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    # created_at = mapped_column(DateTime(timezone=False, ), nullable=False, default=func.now())
    # updated_at = mapped_column(DateTime(timezone=False, ), nullable=False, onupdate=func.now())
    # __abstract__ = True
    pass