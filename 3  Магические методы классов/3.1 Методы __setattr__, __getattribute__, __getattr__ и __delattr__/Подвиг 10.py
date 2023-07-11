import time


class Filter:
    def __init__(self, date: float):
        self.date = date

    def __setattr__(self, key, value):
        if key is 'date':
            if not hasattr(self, key):
                object.__setattr__(self, key, value) if value > 0 else None
        else:
            object.__setattr__(self, key, value)


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100  # Максимальное время работы фильтра (любого)

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, filter):
        validate = {1: Mechanical, 2: Aragon, 3: Calcium}
        if not getattr(self, f'slot_{slot_num}') and isinstance(filter, validate.get(slot_num)):
            setattr(self, f'slot_{slot_num}', filter)

    def remove_filter(self, slot_num):
        setattr(self, f'slot_{slot_num}', None)

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        return all(True if getattr(self, f'slot_{slot_num}') is not None else False for slot_num in range(1, 4)) and \
            all(0 <= time.time() - obj.date <= self.MAX_DATE_FILTER for obj in self.get_filters())
