t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case int(_), str(autor), str(title), float(price), int(year), *_:
        print('Yes')
    case int(_), str(autor), str(title), int(year), *_:
        print('Yes')
    case int(_), str(autor), str(title), float(price), *_:
        print('Yes')
    case int(_), str(autor), str(title), *_:
        print('Yes')
    case _:
        print('No')
