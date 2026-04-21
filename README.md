# Sistema Educativo en Python (POO + MySQL)

Este proyecto es un ejemplo básico de cómo conectar Python a una base de datos MySQL utilizando Programación Orientada a Objetos (POO).

---

## Tecnologías utilizadas

- Python 3
- MySQL
- mysql-connector-python

---

## Estructura del proyecto

```
education_project/
│
├── config/
│   └── database.py
│
├── models/
│   ├── student.py
│   └── course.py
│
├── services/
│   ├── student_service.py
│   ├── course_service.py
│   └── enrollment_service.py
│
└── main.py
```

---

## Base de datos

Ejecuta el siguiente script en MySQL:

```sql
CREATE DATABASE education_system;

USE education_system;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100)
);

CREATE TABLE enrollments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);