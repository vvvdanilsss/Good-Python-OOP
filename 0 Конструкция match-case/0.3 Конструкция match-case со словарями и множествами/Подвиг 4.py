def parse_json(data):
    match data:
        case {'access': bool(access), 'data': list([data, *_])}:
            return access, data
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None


json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234',
                                                               'email': 'xxx@mail.com'},
                                                2000, 56.4]}
