from models.course import Course

class CourseService:
    def __init__(self, db):
        self.db = db

    def create_course(self, title):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO courses (title) VALUES (%s)",
            (title,)
        )
        conn.commit()
        cursor.close()

    def get_courses(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM courses")
        rows = cursor.fetchall()

        courses = []
        for row in rows:
            courses.append(Course(row['id'], row['title']))

        cursor.close()
        return courses