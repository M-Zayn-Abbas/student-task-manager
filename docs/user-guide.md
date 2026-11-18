# Student Task Manager: User Guide

This guide explains how to use the Student Task Manager console application.

## Starting the Application

Open a terminal in the project folder and run:

```bash
python main.py
```

The main menu appears:

```
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
Choose an option (1-5):
```

Type the number of an option and press **Enter**.

## 1. Adding a Task

1. Choose option `1`.
2. Type the task title, for example `Finish DevOps lab`, and press Enter.
3. The new task is shown with its ID:
   ```
   Task added: 1. [ ] Finish DevOps lab
   ```

> An empty title, or one made only of spaces, is rejected with:
> `Error: Task title cannot be empty.`

## 2. Displaying Tasks

Choose option `2` to list all tasks:

```
1. [x] Finish DevOps lab
2. [ ] Read cloud computing notes
```

- `[ ]` means the task is pending
- `[x]` means the task is completed

If there are no tasks, you will see `No tasks found.`

## 3. Completing a Task

1. Choose option `3`. Your current tasks are listed first.
2. Enter the ID of the task to complete.
3. You will see `Task marked as completed.`

## 4. Deleting a Task

1. Choose option `4`.
2. Enter the ID of the task to delete.
3. You will see `Task deleted.`

## Error Messages

| Message | Meaning |
|---|---|
| `Error: Task title cannot be empty.` | You tried to add a task with no title. |
| `Error: Please enter a valid numeric task ID.` | You typed something that is not a number. |
| `Error: No task found with ID N.` | No task has that ID. Use option 2 to check the IDs. |
| `Invalid option, please try again.` | The menu choice was not between 1 and 5. |

## 5. Exiting

Choose option `5` to close the application.

> **Note:** Tasks are stored in memory only, so they are cleared when the application exits.
