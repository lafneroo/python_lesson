"""
==============================
    UI обёртка над tkinter
==============================
"""
import tkinter as tk

from .components.AppButton import AppButton
from .components.AppListbox import AppListbox
from .components.AppEntry import AppEntry
from .components.AppLabel import AppLabel


class Interface:
    """Обёртка над tk-виджетами: build, get_input, show_tasks, ask_confirm"""

    def __init__(self, manager, width=500, height=500):
        self.manager = manager
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title("Task Manager v0.2.0")
        self.root.configure(bg="black")
        self._map_index_to_id = {}  # {listbox_index: task_id}

    "создаёт интерфейс окна"
    def build(self):
        AppLabel(self.root, text="Менеджер задач v0.2.0",
                 bg="black", fg="white", font=("Arial", 12, "bold")).pack(pady=5)

        self.listbox = AppListbox(self.root, bg="black", fg="white", selectmode=tk.SINGLE)
        self.listbox.pack(pady=5, fill="both", expand=True)

        btn_frame = tk.Frame(self.root, bg="black")
        btn_frame.pack(pady=5)
        AppButton(btn_frame, "primary", "Новая", self._on_new).pack(side="left", padx=2)
        AppButton(btn_frame, "primary", "Изменить", self._on_edit).pack(side="left", padx=2)
        AppButton(btn_frame, "primary", "Статус", self._on_toggle).pack(side="left", padx=2)
        AppButton(btn_frame, "secondary", "Удалить", self._on_delete).pack(side="left", padx=2)

        btn_bottom = tk.Frame(self.root, bg="black")
        btn_bottom.pack(side="bottom", pady=5)
        AppButton(btn_bottom, "primary", "Сохранить", self._on_save).pack(side="left", padx=5)
        AppButton(btn_bottom, "secondary", "Выход", self._on_exit).pack(side="left", padx=5)

        self.show_tasks()

    "заполняет список задач"
    def show_tasks(self):
        self.listbox.delete(0, tk.END)
        self._map_index_to_id.clear()
        for index, task in enumerate(self.manager.storage.tasks):
            status_mark = "+" if task.status == "done" else "-"
            line = f"#{task.id} [{status_mark}] {task.title} — {task.author} ({task.created_at})"
            self.listbox.insert(tk.END, line)
            self._map_index_to_id[index] = task.id

    "диалог ввода / редактирования задачи"
    def get_input(self, title="", description="", author=""):
        dialog = tk.Toplevel(self.root)
        dialog.title("Задача")
        dialog.configure(bg="black")
        dialog.geometry("300x220")
        dialog.grab_set()

        result = {}

        AppLabel(dialog, text="Название:", bg="black", fg="white").pack(pady=(5, 0), padx=10, anchor="w")
        entry_title = AppEntry(dialog)
        entry_title.insert(0, title)
        entry_title.pack(padx=10, pady=2, fill="x")

        AppLabel(dialog, text="Описание:", bg="black", fg="white").pack(pady=(5, 0), padx=10, anchor="w")
        entry_desc = AppEntry(dialog)
        entry_desc.insert(0, description)
        entry_desc.pack(padx=10, pady=2, fill="x")

        AppLabel(dialog, text="Автор:", bg="black", fg="white").pack(pady=(5, 0), padx=10, anchor="w")
        entry_author = AppEntry(dialog)
        entry_author.insert(0, author)
        entry_author.pack(padx=10, pady=2, fill="x")

        def on_ok():
            result["title"] = entry_title.get().strip()
            result["description"] = entry_desc.get().strip()
            result["author"] = entry_author.get().strip()
            dialog.destroy()

        AppButton(dialog, "primary", "OK", on_ok).pack(pady=5)
        AppButton(dialog, "secondary", "Отмена", dialog.destroy).pack()

        dialog.wait_window()
        return result if result.get("title") else None

    "подтверждение действия"
    def ask_confirm(self, message):
        from tkinter import messagebox
        return messagebox.askyesno("Подтверждение", message)

    "кнопка — создать задачу"
    def _on_new(self):
        data = self.get_input()
        if data:
            self.manager.create_task(data["title"], data["description"], data["author"])
            self.show_tasks()

    "кнопка — редактировать задачу"
    def _on_edit(self):
        task_id = self._selected_id()
        if not task_id:
            return
        task = self.manager.storage.get(task_id)
        if not task:
            return
        data = self.get_input(task.title, task.description, task.author)
        if data:
            self.manager.edit_task(task_id, data["title"], data["description"], data["author"])
            self.show_tasks()

    "кнопка — переключить статус"
    def _on_toggle(self):
        task_id = self._selected_id()
        if task_id:
            self.manager.toggle_status(task_id)
            self.show_tasks()

    "кнопка — удалить задачу"
    def _on_delete(self):
        task_id = self._selected_id()
        if not task_id:
            return
        task = self.manager.storage.get(task_id)
        if task and self.ask_confirm(f'Удалить задачу #{task.id} "{task.title}"?'):
            self.manager.delete_task(task_id)
            self.show_tasks()

    "кнопка — сохранить"
    def _on_save(self):
        self.manager.storage.save()

    "кнопка — выход"
    def _on_exit(self):
        self.manager.storage.save()
        self.root.destroy()

    "id выбранной задачи"
    def _selected_id(self):
        selection = self.listbox.curselection()
        if not selection:
            return None
        return self._map_index_to_id.get(selection[0])


