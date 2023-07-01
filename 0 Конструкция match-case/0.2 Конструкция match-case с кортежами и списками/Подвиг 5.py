t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case int(_), str(autor), str(title), float(price), int(year) if price >= 0 \
                                                                        and year >= 2020:
        print('Yes')
    case int(_), str(autor), str(title), int(year) if year >= 2020:
        print('Yes')
    case int(_), str(autor), str(title), float(price) if len(autor) >= 6 and price > 0:
        print('Yes')
    case int(_), str(autor), str(title) if len(autor) >= 6 and len(title) >= 10:
        print('Yes')
    case _:
        print('No')