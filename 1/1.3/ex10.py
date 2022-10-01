class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
print('job' in p1.__dict__)