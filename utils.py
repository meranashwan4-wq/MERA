from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status

from app.dbs.deps import get_db
from app.models import Student, Major
from app.schemas.student import StudentRead, StudentCreate
from app.utilities.logging_client import logger

router = APIRouter(prefix="/students", tags=["students"])


@router.post("", response_model=StudentRead, status_code=status.HTTP_201_CREATED)  # add response
def create_student(payload: StudentCreate, db: Session = Depends(get_db)):  # add input/request

    logger.info(f"Payload: {payload.model_dump()}")

    if not db.get(Major, payload.major_id):
        raise HTTPException(status_code=404, detail="Major not found")

    logger.info(f"Major found: {payload.major_id}")

    student = Student(**payload.model_dump())
    db.add(student)
    try:
        db.commit()
        logger.info(f"Student created: {student.id}")
    except Exception as e:
        db.rollback()
        logger.info(f"Student creation failed: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    db.refresh(student)
    return student


@router.get("/{student_id}", response_model=StudentRead)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")


@router.get("", response_model=StudentRead)
def get_student(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    if not students:
        raise HTTPException(status_code=404, detail="No student found")

    return students


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()

