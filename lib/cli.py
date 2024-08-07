# lib/cli.py

from models.muscle import Muscle
from models.exercise import Exercise


def main():
    while True:
        print("Main Menu:")
        print("1. Muscles")
        print("2. Exercises")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            muscle_menu()
        elif choice == "2":
            exercise_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

#add exercises in this menu
def muscle_menu():
    while True:
        print("Muscle Menu:")
        print("1. Create a muscle")
        print("2. Delete a muscle")
        print("3. Display all muscles") #take to different menu that allows CRUD of exercise to muscles
        print("4. Find a muscle by ID") #take out
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_muscle()
        elif choice == "2":
            delete_muscle()
        elif choice == "3":
            display_all_muscles()
        elif choice == "4":
            find_muscle_by_id()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

#find by name 
#display all
def exercise_menu():
    while True:
        print("Exercise Menu:")
        print("1. Create an exercise")
        print("2. Delete an exercise")
        print("3. Display all exercises")
        print("4. Find an exercise by ID")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_exercise()
        elif choice == "2":
            delete_exercise()
        elif choice == "3":
            display_all_exercises()
        elif choice == "4":
            find_exercise_by_id()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def create_muscle():
    name = input("Enter the name of the muscle: ")
    location = input("Enter the location of the muscle: ")
    muscle = Muscle(name, location)
    muscle.create()
    print("Muscle created successfully!")

def delete_muscle():
    muscle_id = input("Enter the ID of the muscle to delete: ")

    muscle = Muscle.find_by_id(muscle_id)
    if muscle:
        muscle.delete()
        print("Muscle deleted successfully!")
    else:
        print("Muscle not found.")

def display_all_muscles():
    muscles = Muscle.get_all()
    if muscles:
        print("All muscles:")
        for i, muscle in enumerate(muscles, start=1):
            print(f"{i}. Name: {muscle.name}, Location: {muscle.location}")
    else:
        print("No muscles found.")

#lose this
def find_muscle_by_id():
    muscle_id = input("Enter the ID of the muscle to find: ")

    muscle = Muscle.find_by_id(muscle_id)
    if muscle:
        print(f"ID: {muscle.id}, Name: {muscle.name}, Location: {muscle.location}")
    else:
        print("Muscle not found.")




def create_exercise():
    name = input("Enter the name of the exercise: ")
    difficulty = input("Enter the difficulty of the exercise: ")
    muscle_id = input("Enter the ID of the muscle associated with the exercise: ")

    exercise = Exercise(name, difficulty, muscle_id)
    exercise.create_exercise_table()
    print("Exercise created successfully!")


def delete_exercise():
    exercise_id = input("Enter the ID of the exercise to delete: ")

    exercise = Exercise.find_by_id_exercise(exercise_id)
    if exercise:
        exercise.delete_exercises()
        print("Exercise deleted successfully!")
    else:
        print("Exercise not found.")


def display_all_exercises():
    exercises = Exercise.get_all_exercise()
    if exercises:
        print("All exercises:")
        for i, exercise in enumerate(exercises, start=1):
            print(f"{i}. ID: {exercise.id}, Name: {exercise.name}, Difficulty: {exercise.difficulty}, Muscle ID: {exercise.muscle_id}")
    else:
        print("No exercises found.")

def find_exercise_by_id():
    exercise_id = input("Enter the ID of the exercise to find: ")

    exercise = Exercise.find_by_id_exercise(exercise_id)
    if exercise:
        print(f"ID: {exercise.id}, Name: {exercise.name}, Difficulty: {exercise.difficulty}, Muscle ID: {exercise.muscle_id}")
    else:
        print("Exercise not found.")



if __name__ == "__main__":
    main()
