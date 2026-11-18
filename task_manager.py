"""Core logic for the Student Task Manager."""


class Task:
    """A single task with an id, a title and a completion status."""

    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.completed = False

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{self.id}. {status} {self.title}"


class TaskManager:
    """Stores tasks in memory and provides operations on them."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        """Create a new task with the given title and return it."""
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_tasks(self):
        """Return the list of all tasks."""
        return self.tasks

    def display_tasks(self):
        """Print all tasks to the console."""
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            print(task)

    def complete_task(self, task_id):
        """Mark the task with the given id as completed."""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
