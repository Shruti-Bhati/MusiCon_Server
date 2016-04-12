def bmp_ranges(bmp):
	bmp = int(bmp)
	if 59 < bmp <= 75:
		return "gym1"
	elif 75 < bmp <= 95:
		return "gym2"
	elif 95 < bmp <= 120:
		return "gym3"
	else:
		return "gym4"
