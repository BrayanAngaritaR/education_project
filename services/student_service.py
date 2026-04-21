from models.student import Student

class StudentService:
    def __init__(self, db):
        self.db = db

    def create_student(self, name, email):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        cursor.close()

    def get_students(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        students = []
        for row in rows:
            students.append(Student(row['id'], row['name'], row['email']))

        cursor.close()
        return students