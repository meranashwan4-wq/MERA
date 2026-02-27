from sqlalchemy import Integer, Float, CheckConstraint, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, relationship, Mapped

from app.dbs.base import Base


class Mark(Base):
    __tablename__ = "marks"
    __table_args__ = (
        CheckConstraint("score >= 0 and score <= 100", name="mark_constraint"),
        {"extend_existing": True}
    )
    id = mapped_column(Integer(), primary_key=True)
    score = mapped_column(Float(), nullable=False)  # check_constraints="score >= 0 and score <= 100",

    student_id = mapped_column(ForeignKey("students.id"), nullable=False)
    subject_id = mapped_column(ForeignKey("subjects.id"), nullable=False)

    student: Mapped['Student'] = relationship(back_populates="marks")
    subject: Mapped['Subject'] = relationship(back_populates="marks")

    created_at = mapped_column(DateTime(timezone=False, ), nullable=False, default=func.now())
    updated_at = mapped_column(DateTime(timezone=False, ), nullable=False, onupdate=func.now())
