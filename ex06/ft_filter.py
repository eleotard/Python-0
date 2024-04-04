def ft_filter(funct, it):
	"""filter(function or None, iterable) --> filter object\n\nReturn an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true."""
	res = [x for x in it if funct(x)]
	return res 


