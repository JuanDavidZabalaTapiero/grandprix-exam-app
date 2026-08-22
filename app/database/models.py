from sqlalchemy import func

from app.extensions import db


class LicenseCategory(db.Model):
    __tablename__ = "license_categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)


class DocumentType(db.Model):
    __tablename__ = "document_types"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=True)
    document_type_id = db.Column(
        db.Integer, db.ForeignKey("document_types.id"), nullable=False
    )
    document_number = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(
        db.DateTime, server_default=func.current_timestamp(), nullable=False
    )


class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    license_category_id = db.Column(
        db.Integer, db.ForeignKey("license_categories.id"), nullable=False
    )


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    text = db.Column(db.String(255), nullable=False)


class Option(db.Model):
    __tablename__ = "options"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)


class QuestionImage(db.Model):
    __tablename__ = "question_images"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    image_name = db.Column(db.String(255), nullable=False)


class Competence(db.Model):
    __tablename__ = "competences"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey("competences.id"), nullable=False)


class QuestionCompetence(db.Model):
    __tablename__ = "question_competences"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    competence_id = db.Column(
        db.Integer, db.ForeignKey("competences.id"), nullable=False
    )


class Response(db.Model):
    __tablename__ = "responses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey("options.id"), nullable=False)
