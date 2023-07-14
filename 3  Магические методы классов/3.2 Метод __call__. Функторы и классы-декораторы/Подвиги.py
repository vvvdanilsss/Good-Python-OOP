from random import randint, sample


# Подвиг 2
class RandomPassword:
    def __init__(self, pwd_chars: str, min_length: int, max_length: int):
        self.pwd_chars = pwd_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        len_pwd = randint(self.min_length, self.max_length)
        pwd = ''.join(sample(self.pwd_chars, k=len_pwd))
        return pwd


rnd = RandomPassword('qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*', 5, 20)
lst_pass = [rnd() for _ in range(3)]
print(*lst_pass)


# Доп задание
def random_password(pwd_chars: str, min_length: int, max_length: int):
    def generate_pwd():
        len_pwd = randint(min_length, max_length)
        pwd = ''.join(sample(pwd_chars, k=len_pwd))
        return pwd

    return generate_pwd


gp = random_password('qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*', 5, 20)
lst = [gp() for _ in range(3)]
print(*lst)


# Подвиг 3
class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = tuple(f'.{_}' for _ in extensions)

    def __call__(self, *args, **kwargs):
        return args[0].endswith(self.extensions)


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]


# Подвиг 4
class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        if args:
            return self.min_length <= len(args[0]) <= self.max_length


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        if args:
            return all((_ in self.chars for _ in args[0]))


# Подвиг 5
class DigitRetrieve:
    def __call__(self, *args, **kwargs):
        if args:
            try:
                return int(args[0])
            except ValueError:
                return None


# Подвиг 6
class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, *args, **kwargs):
        if args:
            li_teg = '\n'.join(f'<li>{_}</li>' for _ in args[0])
            if self.type_list == 'ol':
                return f'<ol>\n{li_teg}\n</ol>'
            else:
                return f'<ul>\n{li_teg}\n</ul>'


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ul")
html = render(lst)
print(html)


# Подвиг 7
class HandlerGET:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        if args:
            return self.get(self.__func, args[0])

    @staticmethod
    def get(func, request, *args, **kwargs):
        if ('method' in request.keys() and request['method'] == 'GET') or ('method' not in request.keys()):
            return f'GET: {func(request)}'
        return None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
print(res)


# Подвиг 8
class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            method = request.get('method', 'GET')
            if method in self.methods:
                if method == 'GET':
                    return self.get(func, request, *args, **kwargs)
                elif method == 'POST':
                    return self.post(func, request, *args, **kwargs)
            return None

        return wrapper

    @staticmethod
    def get(func, request, *args, **kwargs):
        data = func(request, *args, **kwargs)
        return f'GET: {data}'

    @staticmethod
    def post(func, request, *args, **kwargs):
        data = func(request, *args, **kwargs)
        return f'POST: {data}'


@Handler(methods=('GET', 'POST'))  # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})
print(res)


# Подвиг 9
class InputDigits:
    def __init__(self, func):
        self.__func = func

    def __call__(self):
        return list(map(int, self.__func().split()))


@InputDigits
def input_dg():
    return input()


res = input_dg()
print(res)


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper():
            return list(map(self.render, func().split()))

        return wrapper


class RenderDigit:
    def __call__(self, value):
        try:
            return int(value)
        except:
            return None


@InputValues(RenderDigit())
def input_dg():
    return input()


res = input_dg()
print(res)