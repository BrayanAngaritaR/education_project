class EnrollmentService:
    def __init__(self, db):
        self.db = db

    def enroll(self, student_id, course_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)",
            (student_id, course_id)
        )
        conn.commit()
        cursor.close()