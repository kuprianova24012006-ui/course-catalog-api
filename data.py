from models import Course


courses = [
    Course(
        id=1,
        title="Python Basics",
        description="Introduction to Python programming",
        credits=5,
        is_elective=False,
        likes=12,
    ),
    Course(
        id=2,
        title="Web Development",
        description="Building websites and web applications",
        credits=6,
        is_elective=False,
        likes=25,
    ),
    Course(
        id=3,
        title="Database Systems",
        description="Working with databases and SQL",
        credits=5,
        is_elective=False,
        likes=18,
    ),
    Course(
        id=4,
        title="Machine Learning",
        description="Introduction to machine learning",
        credits=6,
        is_elective=True,
        likes=40,
    ),
    Course(
        id=5,
        title="Mobile Development",
        description="Building mobile applications",
        credits=4,
        is_elective=True,
        likes=15,
    ),
    Course(
        id=6,
        title="Cybersecurity",
        description="Fundamentals of information security",
        credits=5,
        is_elective=True,
        likes=30,
    ),
]


def get_all_courses() -> list[Course]:
    return courses


def find_course(course_id: int) -> Course | None:
    for course in courses:
        if course.id == course_id:
            return course
    return None
