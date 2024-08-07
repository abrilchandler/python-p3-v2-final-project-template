from .__init__ import CURSOR, CONN
import sqlite3

class Exercise:
    def __init__(self, name, difficulty, muscle_id):
        self.name = name
        self.difficulty = difficulty
        self.muscle_id = muscle_id

    @classmethod
    def create_exercise_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY,
            name TEXT,
            difficulty TEXT,
            muscle_id INTEGER
            );
        """
        try:
            CURSOR.execute(sql)
            CONN.commit()
            print("Muscle table created successfully!")
        except sqlite3.Error as e:
            print("Error creating muscle table:", str(e))
    
    def save_exercise(self):
        sql = """
            INSERT INTO exercises (name, difficulty, muscle_id) 
            VALUES (?, ?, ?)
        """
        try:
            CURSOR.execute(sql)
            CONN.commit()
            print("Exercise saved successfully!")
        except sqlite3.Error as e:
            print("Error saving exercise:", str(e))

            
    @classmethod
    def delete_exercises(cls, exercise_id):
        sql = "DELETE FROM exercises WHERE id = ?"
        params = (exercise_id,)
        try:
            CURSOR.execute(sql, params)
            CONN.commit()
            print("Exercise deleted successfully!")
        except sqlite3.Error as e:
            print("Error deleting exercise:", str(e))

    @classmethod
    def get_all_exercise(cls):
        sql = "SELECT * FROM exercises"
        try:
            CURSOR.execute(sql)
            rows = CURSOR.fetchall()
            exercises = []
            for row in rows:
                exercise = Exercise(row[1], row[2], row[3])
                exercise.id = row[0]
                exercises.append(exercise)
            return exercises
        except sqlite3.Error as e:
            print("Error retrieving exercises:", str(e))
            return []

    @classmethod
    def find_by_id_exercise(cls, exercise_id):
        sql = "SELECT * FROM exercises WHERE id = ?"
        params = (exercise_id,)
        try:
            CURSOR.execute(sql, params)
            row = CURSOR.fetchone()
            if row:
                exercise = Exercise(row[1], row[2], row[3])
                exercise.id = row[0]
                return exercise
            else:
                return None
        except sqlite3.Error as e:
            print("Error finding exercise:", str(e))
            return None