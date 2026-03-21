from sqlalchemy import Column, Integer, String, ForeignKey, Date, CheckConstraint
from sqlalchemy.orm import relationship
from database.db import Base


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True, index=True)

    students = relationship(
        "Student", back_populates="group", cascade="all, delete-orphan"
    )


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(150), nullable=False, index=True)

    subjects = relationship(
        "Subject", back_populates="teacher", cascade="all, delete-orphan"
    )


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(150), nullable=False, index=True)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), index=True)

    group = relationship("Group", back_populates="students")
    grades = relationship(
        "Grade", back_populates="student", cascade="all, delete-orphan"
    )


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, index=True)
    teacher_id = Column(
        Integer, ForeignKey("teachers.id", ondelete="CASCADE"), index=True
    )

    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship(
        "Grade", back_populates="subject", cascade="all, delete-orphan"
    )


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(
        Integer, ForeignKey("students.id", ondelete="CASCADE"), index=True
    )
    subject_id = Column(
        Integer, ForeignKey("subjects.id", ondelete="CASCADE"), index=True
    )
    grade = Column(Integer, CheckConstraint("grade >= 1 AND grade <= 100"), index=True)
    date_received = Column(Date, nullable=False, index=True)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
