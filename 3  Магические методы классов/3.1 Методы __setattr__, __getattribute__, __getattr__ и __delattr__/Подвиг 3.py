class Book:
    def __init__(self, title: str = '', author: str = '', pages: int = 0, year: int = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        match key, value:
            case 'title' | 'author', str():
                object.__setattr__(self, key, value)
            case 'pages' | 'year', int():
                object.__setattr__(self, key, value)
            case _:
                raise TypeError("Неверный тип присваиваемых данных.")


book = Book(author='Сергей Балакирев', title='Python ООП', pages=123, year=2022)
