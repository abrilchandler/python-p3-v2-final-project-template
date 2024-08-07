from .__init__ import CURSOR, CONN
import sqlite3

all = {}

class Muscle:
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    @property
    def name(self):
        return self._name 
    
    @name.setter 
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a string")
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self,location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError("Location must be a stirng")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS muscles (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
        print("Muscle table created successfully!")
        
   
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS muscles;
        """
        CURSOR.execute(sql)
        CONN.commit()
        print("Muscle deleted")
        
    def save(self):
        """ Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO muscles (name, location)
            VALUES (?, ?)
        """
        CURSOR.execute(sql (self.name, self.location))
        CONN.commit()
        print("Muscle saved successfully!")

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    #Initialize a new Department instance and save the object to the database
    def create(cls, name, location):
        muscle = cls(name, location)
        muscle.save()
        return muscle

    def delete(self):
        """Delete the table row corresponding to the current Department instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM muslces
            WHERE id = ?
        """    
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]
        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Department object having the attribute values from the table row."""
        muscle = cls.all.get(row[0])
        if muscle:
            #ensure attributes match row values in case local instance was modified
            muscle.name = row[1]
            muscle.location = row[2]
        else:
            #not in dictionary, create new instance and add to dictionary 
            muscle = cls(row[1], row[2])
            muscle.id = row[0]
            cls.all[muscle.id] = muscle
        return muscle


    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM muscles"""
        rows = CURSOR.execute(sql).fetchall()
        #list comprehension
        return [cls.instance_from_db(row) for row in rows]
        
    @classmethod
    def find_by_id(cls, id, muscle_id):
        sql = "SELECT * FROM muscles WHERE id = ?"
        params = (muscle_id,)
        try:
            CURSOR.execute(sql, params)
            row = CURSOR.fetchone()
            if row:
                muscle = Muscle(row[1], row[2])
                muscle.id = row[0]
                return muscle
            else:
                return None
        except sqlite3.Error as e:
            print("Error finding muscle:", str(e))
            return None

#property decorators with validations
#instance method call exercise