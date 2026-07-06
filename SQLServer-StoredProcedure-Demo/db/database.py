import pyodbc as p
import config as cfg

class Database :
    def __init__(self):
        self.connection = p.connect(
            f"Driver={cfg.config.DRIVER};"
            f"Server={cfg.config.SERVER};"
            f"Database={cfg.config.DATABASE};"
            f"Trusted_Connection={cfg.config.TRUSTED_CONNECTION};"
        )

        self.cursor = self.connection.cursor()


    def execute_stored_procedure(self , sql , *parameters):
        self.cursor.execute(sql, *parameters)

    def fach_one (self):
        return self.cursor.fetchone()
    
    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self):
        self.cursor.close()
        self.connection.close()