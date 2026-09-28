"""
==========================================
    модуль для утилит
==========================================
"""

"""подтверждение действия"""


def check_confirm(action: str):
    confirm = input("точно?"
                    "\n Y/N")
    if (confirm.capitalize() == "Y"
            or confirm.capitalize() == 'Д'):
        print(action)
        return False
    else:
        print("отмена")
        return True