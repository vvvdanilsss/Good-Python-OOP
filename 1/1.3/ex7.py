class Dictionary:
    rus = 'Питон'
    eng = 'Python'


print(getattr(Dictionary, 'rus_word', False))