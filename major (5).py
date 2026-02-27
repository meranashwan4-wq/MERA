from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship, Mapped

from app.dbs.base import Base


class Major(Base):
    __tablename__ = "majors"

    id = mapped_column(Integer(), primary_key=True, index=True)
    name = mapped_column(
        String(length=100), unique=True, index=True
    )
    subjects: Mapped["Subject"] = relationship(back_populates="major", cascade="all, delete-orphan")
    students: Mapped["Student"] = relationship(back_populates="major", cascade="all, delete-orphan")