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
