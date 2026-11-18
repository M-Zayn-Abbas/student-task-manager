"""Unit tests for the TaskManager class."""

import unittest

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Finish DevOps lab")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Finish DevOps lab")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_add_empty_task_is_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")
        self.assertEqual(len(self.manager.get_tasks()), 0)

    def test_complete_task(self):
        task = self.manager.add_task("Read notes")
        result = self.manager.complete_task(task.id)
        self.assertTrue(result)
        self.assertTrue(task.completed)

    def test_complete_invalid_task(self):
        self.assertFalse(self.manager.complete_task(99))

    def test_delete_task(self):
        task = self.manager.add_task("Submit assignment")
        result = self.manager.delete_task(task.id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_delete_invalid_task(self):
        self.manager.add_task("Keep me")
        self.assertFalse(self.manager.delete_task(99))
        self.assertEqual(len(self.manager.get_tasks()), 1)


if __name__ == "__main__":
    unittest.main()
