"""
==============================
    Модель задачи
==============================
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    """POPO — модель задачи"""
    id: int = 0
    title: str = ""
    description: str = ""
    status: str = "todo"
    author: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def to_dict(self):
        """Сериализация в словарь"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "author": self.author,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        """Десериализация из словаря. Поддерживает старый формат (name/content)."""
        data = dict(data)
        data.setdefault("title", data.pop("name", ""))
        data.setdefault("description", data.pop("content", ""))
        data.setdefault("status", "todo")
        data.setdefault("author", "")
        data.setdefault("created_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        fields = cls.__dataclass_fields__
        return cls(**{key: value for key, value in data.items() if key in fields})
