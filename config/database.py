import mysql.connector

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="education_system"
        )
        print("✅ Conectado a MySQL")

    def get_connection(self):
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            print("🔌 Conexión cerrada")