"""
==============================
    модуль хранилища задач (JSON)
==============================
"""
import json
import os

from config import FILE_NAME_SAVES
from task import Task


class StorageManager:
    """Хранилище списка задач в формате JSON"""

    def __init__(self, file_name=FILE_NAME_SAVES):
        self.file_name = file_name
        self.tasks = []

    "загрузка"
    def load(self):
        if not os.path.exists(self.file_name):
            self.tasks = []
            return self.tasks
        with open(self.file_name, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
        self.tasks = [Task.from_dict(item) for item in data]
        self.__migrate_ids()
        return self.tasks

    "сохранение"
    def save(self):
        data = [task.to_dict() for task in self.tasks]
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    "добавление задачи"
    def add(self, task: Task):
        task.id = self.next_id()
        self.tasks.append(task)
        self.save()
        return task

    "обновление задачи по id"
    def update(self, task: Task):
        for index, current in enumerate(self.tasks):
            if current.id == task.id:
                self.tasks[index] = task
                self.save()
                return task
        return None

    "удаление задачи по id"
    def delete(self, task_id: int):
        for index, current in enumerate(self.tasks):
            if current.id == task_id:
                removed = self.tasks.pop(index)
                self.save()
                return removed
        return None

    "поиск задачи по id"
    def get(self, task_id: int):
        for current in self.tasks:
            if current.id == task_id:
                return current
        return None

    "следующий свободный id"
    def next_id(self):
        return max((task.id for task in self.tasks), default=0) + 1

    "проставить уникальные id для загруженных задач"
    def __migrate_ids(self):
        used = set()
        for task in self.tasks:
            if task.id == 0 or task.id in used:
                task.id = self.next_id()
            used.add(task.id)
