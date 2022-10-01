class Notes:
    uid = 1005435
    title = 'Шутка'
    author = 'И.С. Бах'
    pages = 2


print(getattr(Notes, 'autor', False))