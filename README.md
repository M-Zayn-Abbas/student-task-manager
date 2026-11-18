# student-task-manager

Project status: Completed

![Tests](https://github.com/M-Zayn-Abbas/student-task-manager/actions/workflows/tests.yml/badge.svg)

A simple Python console application for students to manage their tasks. It was built to practice a complete Git and GitHub workflow: commits, branches, pull requests, merge conflicts, automated testing and releases.

## Features

- **Add a task**: empty or whitespace-only titles are rejected
- **Display tasks**: shows every task with its ID and status (`[ ]` pending, `[x]` completed)
- **Complete a task**: marks a task as completed by its ID
- **Delete a task**: removes a task by its ID
- Friendly error messages for invalid or unknown task IDs

## Project Structure

```
student-task-manager/
├── main.py                  # Console menu (entry point)
├── task_manager.py          # Task and TaskManager classes (core logic)
├── tests/
│   └── test_task_manager.py # Unit tests
├── docs/
│   └── user-guide.md        # User guide
└── .github/workflows/
    └── tests.yml            # GitHub Actions CI workflow
```

## Setup

1. Install **Python 3.8 or newer**.
2. Clone the repository:
   ```bash
   git clone https://github.com/M-Zayn-Abbas/student-task-manager.git
   cd student-task-manager
   ```
3. No external packages are needed, because the app uses only the Python standard library.

## Usage

Run the application:

```bash
python main.py
```

Choose an option from the menu:

```
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
```

See the [User Guide](docs/user-guide.md) for a step-by-step walkthrough.

## Running Tests

The tests use Python's built-in `unittest` module:

```bash
python -m unittest discover -s tests -v
```

The tests also run automatically through **GitHub Actions** on every push to `main` and on every pull request to `main`.

## License

This project is licensed under the [MIT License](LICENSE).

Developed as part of the DevOps for Cloud Computing course (CSC418).

Author: M. Zayn Abbas
