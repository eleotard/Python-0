def NULL_not_found(object: any) -> int:
	res = type(object)
	if res.__name__ == "str":
		if len(object):
			print("Type not found")
			return 1
	print(f"{res.__name__.title()} : {res}")
	return 0