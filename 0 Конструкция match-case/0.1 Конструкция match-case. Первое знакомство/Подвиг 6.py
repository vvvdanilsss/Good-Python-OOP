def get_data(value):
    match value:
        case bool():
            return None
        case int(val):
            return val
        case str(val):
            return val
        case float(val):
            return val

    return None
