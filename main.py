from config.database import Database
from services.student_service import StudentService
from services.course_service import CourseService
from services.enrollment_service import EnrollmentService

db = Database()
db.connect()

student_service = StudentService(db)
course_service = CourseService(db)
enrollment_service = EnrollmentService(db)

# Crear datos
student_service.create_student("Brayan Angarita", "hola@mastalentos.com")
course_service.create_course("POO en Python")

# Obtener datos
students = student_service.get_students()
courses = course_service.get_courses()

# Inscribir estudiante en curso
enrollment_service.enroll(students[0].id, courses[0].id)

print("🎓 Sistema funcionando correctamente")

db.close()