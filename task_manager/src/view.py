"""
======================================================
    модуль вывода информации в консоль
======================================================
"""

from ui.Interface import interface
from storage import save_collection, load_collection, save_collection

collection = load_collection([])
ui = interface(collection)
ui.show_menu()

ui.root.mainloop()

