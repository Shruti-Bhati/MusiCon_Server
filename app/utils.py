def bmp_ranges(bmp):
	bmp = int(bmp)
	if 59 < bmp <= 72:
		return "gym1"
	elif 72 < bmp <= 80:
		return "gym2"
	elif 80 < bmp <= 90:
		return "gym3"
	else:
		return "gym4"
