class LessonItem:
    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == 'title' and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key in ('practices', 'duration') and (not isinstance(value, int) or value <= 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item not in ('title', 'practices', 'duration'):
            object.__delattr__(self, item)


class Module:
    def __init__(self, name: str):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class Course:
    def __init__(self, name: str):
        self.name = name
        self.modules = []

    def add_module(self, lesson):
        self.modules.append(lesson)

    def remove_module(self, indx):
        self.modules.pop(indx)