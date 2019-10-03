TimedRotatingFileHandler с возможностью изменения имени бэкапов и с возможностью указания папки для бэкапов

взят исходный код TimedRotatingFileHandler с https://github.com/python/cpython/blob/3.7/Lib/logging/handlers.py
оригиналы измененных функций сохранены рядом

при желании изменить суффикс, в __init__ нужно править для конкретного метода следующие строки
self.suffix = "%Y-%m-%d"
self.extMatch = r"^\d{4}-\d{2}-\d{2}(\.\w+)?$"