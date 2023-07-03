class ValidateString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return type(string) == str and (self.min_length <= len(string) <= self.max_length)


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, string):
        if self.validator.validate(string):
            setattr(instance, self.name, string)


class RegisterForm:
    validate = ValidateString(min_length=3, max_length=100)

    login = StringValue(validator=validate)
    password = StringValue(validator=validate)
    email = StringValue(validator=validate)

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'<from>\nЛогин: {self.login}\nПароль: '
              f'{self.password}\nEmail: {self.email}\n</from>')
