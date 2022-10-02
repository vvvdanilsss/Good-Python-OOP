class Translator:
    d = {}

    def add(self, eng, rus):
        if eng not in self.d:
            self.d[eng] = [rus]
        elif eng in self.d and rus not in self.d[eng]:
            self.d[eng].append(rus)

    def remove(self, eng):
        del self.d[eng]

    def translate(self, eng):
        return self.d[eng]


tr = Translator()
words = [('tree', 'дерево'), ('car', 'машина'), (
    'car', 'автомобиль'), ('leaf', 'лист'), ('river', 'река'), (
    'go', 'идти'), ('go', 'ехать'), ('go', 'ходить'), ('milk', 'молоко')]
[tr.add(*w) for w in words]
tr.remove('car')
print(*tr.translate('go'))