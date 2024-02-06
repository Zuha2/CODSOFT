import os
import json
from datetime import datetime

class ToDoList:
    def __init__(self, filename='todo.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                tasks = json.load(file)
            return tasks
        else:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['title']} - {task['due_date']}")

    def add_task(self, title, due_date):
        task = {'title': title, 'due_date': due_date, 'completed': False}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def update_task(self, index, title, due_date, completed):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = {
                'title': title,
                'due_date': due_date,
                'completed': completed
            }
            self.save_tasks()
            print(f"Task {index} updated successfully.")
        else:
            print("Invalid task index.")

    def mark_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]['completed'] = True
            self.save_tasks()
            print(f"Task {index} marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Task '{deleted_task['title']}' deleted successfully.")
        else:
            print("Invalid task index.")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            todo_list.show_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(title, due_date)
        elif choice == '3':
            todo_list.show_tasks()
            index = int(input("Enter the task index to update: "))
            title = input("Enter new task title: ")
            due_date = input("Enter new due date (YYYY-MM-DD): ")
            completed = input("Is the task completed? (True/False): ").capitalize() == 'True'
            todo_list.update_task(index, title, due_date, completed)
        elif choice == '4':
            todo_list.show_tasks()
            index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == '5':
            todo_list.show_tasks()
            index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")