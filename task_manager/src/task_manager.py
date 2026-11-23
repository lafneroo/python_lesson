"""
==============================
    фасад приложения (CRUD + run)
==============================
"""
from storage import StorageManager
from task import Task
from ui.Interface import Interface


class TaskManager:
    """Фасад: связывает хранилище и интерфейс, содержит CRUD-логику"""

    def __init__(self, storage=None):
        self.storage = storage if storage is not None else StorageManager()
        self.ui = None

    "создать задачу"
    def create_task(self, title, description="", author=""):
        task = Task(title=title, description=description, author=author)
        return self.storage.add(task)

    "изменить задачу"
    def edit_task(self, task_id, title=None, description=None, author=None):
        task = self.storage.get(task_id)
        if task is None:
            return None
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if author is not None:
            task.author = author
        return self.storage.update(task)

    "удалить задачу"
    def delete_task(self, task_id):
        return self.storage.delete(task_id)

    "переключить статус задачи"
    def toggle_status(self, task_id):
        task = self.storage.get(task_id)
        if task is None:
            return None
        task.status = "done" if task.status == "todo" else "todo"
        return self.storage.update(task)

    "запуск приложения"
    def run(self):
        self.storage.load()
        self.ui = Interface(self)
        self.ui.build()
        self.ui.root.mainloop()
