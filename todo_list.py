from typing import List, Optional


class Task:
    """
    A class to represent a Task.
    """

    def __init__(self, description: str):
        """
        Initialize a Task object.

        Args:
            description: The description of the task.
        """

        self.description = description
        self.completed = False


class TodoList:
    """
    A class to represent a Todo List.
    """

    def __init__(self):
        """
        Initialize a TodoList object.
        """

        self.tasks: List[Task] = []

    def add_task(self, description: str) -> None:
        """
        Add a new task to the list.

        Args:
            description: The description of the task.
        """

        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully.")

    def mark_task_complete(self, task_number: int) -> None:
        """
        Mark a task as complete.

        Args:
            task_number: The number of the task to mark as complete.
        """

        if not self.tasks:
            print("No tasks found.")
            return

        task = self._get_task_by_number(task_number)
        if task:
            task.completed = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")

    def list_tasks(self) -> None:
        """
        List all the tasks along with their status.
        """

        if self.tasks:
            for i, task in enumerate(self.tasks, 1):
                status = "Complete" if task.completed else "Incomplete"
                print(f"{i}. {task.description} - {status}")
        else:
            print("No tasks found.")

    def delete_task(self, task_number: int) -> None:
        """
        Delete a task from the list.

        Args:
            task_number: The number of the task to delete.
        """

        if not self.tasks:
            print("No tasks found.")
            return

        task = self._get_task_by_number(task_number)
        if task:
            self.tasks.remove(task)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

    def _get_task_by_number(self, task_number: int) -> Optional[Task]:
        """
        Retrieve a task object based on its number.

        Args:
            task_number: The number of the task to retrieve.

        Returns:
            The task object if found, None otherwise.
        """

        index = task_number - 1
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None


def show_menu()-> None:
    """
    Display the menu options.
    """

    print("Todo List Application")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. List Tasks")
    print("4. Delete Task")
    print("5. Quit")


def get_user_choice()-> int:
    """
    Get the user's choice from the menu.

    Returns:
        The user's choice as an integer.
    """

    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid choice. Please enter a number.")


def main()-> None:
    """
    Main function to run the Todo List Application.
    """

    todo_list = TodoList()

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == 1:
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == 2:
            if todo_list.tasks:
                task_number = int(input("Enter task number: "))
                todo_list.mark_task_complete(task_number)
            else:
                print("No tasks found.")
        elif choice == 3:
            todo_list.list_tasks()
        elif choice == 4:
            if todo_list.tasks:
                task_number = int(input("Enter task number: "))
                todo_list.delete_task(task_number)
            else:
                print("No tasks found.")
        elif choice == 5:
            print("Thank you for using the Todo List Application. Goodbye!")
            break


if __name__ == "__main__":
    main()
