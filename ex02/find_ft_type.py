def all_thing_is_obj(object: any) -> int:
    res = type(object)
    if res.__name__ == "int":
        print("Type not found")
    elif res.__name__ == "str":
        print(f"{object} is in the kitchen : {res}")
    else:
        print(f"{res.__name__.title()} : {res}")
    return 42
