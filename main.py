from fastapi import FastAPI, HTTPException, Depends, Query
from models import Course
from data import get_all_courses, find_course
from dependencies import pagination

app = FastAPI(title="Course Catalog API")


@app.get("/")
def home():
    return {"message": "Welcome to Course Catalog API"}


@app.get("/courses", response_model=list[Course])
def list_courses(
    is_elective: bool | None = None,
    sort: str | None = Query(default=None, pattern="^(popular|title)$"),
    page: dict = Depends(pagination),
):
    courses = get_all_courses()

    if is_elective is not None:
        courses = [
            course for course in courses
            if course.is_elective == is_elective
        ]

    if sort == "popular":
        courses = sorted(courses, key=lambda course: course.likes, reverse=True)
    elif sort == "title":
        courses = sorted(courses, key=lambda course: course.title.lower())

    skip = page["skip"]
    limit = page["limit"]

    return courses[skip:skip + limit]


@app.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int):
    course = find_course(course_id)

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    return course
