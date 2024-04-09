def NULL_not_found(object: any) -> int:
    d = {
        "NoneType": "Nothing",
        "float": "Cheese",
        "int": "Zero",
        "str": "Empty",
        "bool": "Fake"
    }
    res = type(object)
    if (object and object == object) or res.__name__ not in d.keys():
        print("Type not Found")
        return 1
    print(f"{d[res.__name__]}: {object} {res}")
    return 0
