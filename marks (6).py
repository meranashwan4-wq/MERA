from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, relationship, Mapped

from app.dbs.base import Base


class Student(Base):
    __tablename__ = "students"

    id = mapped_column(Integer(), primary_key=True)
    name = mapped_column(String(length=100), index=True, nullable=False)
    age = mapped_column(Integer(), nullable=False)
    email = mapped_column(String(length=100), unique=True, index=True, nullable=False)

    phone = mapped_column(String(length=100), nullable=True)

    major_id = mapped_column(ForeignKey("majors.id", ondelete="CASCADE"), nullable=False, index=True)
    major: Mapped["Major"] = relationship(back_populates="students")

    marks: Mapped[list["Mark"]] = relationship(back_populates="student", cascade="all, delete-orphan")

    # extra information collected about the user # enrichments # target to optimize the system, enhance the business, and secure/audit
    created_at = mapped_column(DateTime(timezone=False,), nullable=False, default=func.now())
    updated_at = mapped_column(DateTime(timezone=False,), nullable=False, onupdate=func.now())


