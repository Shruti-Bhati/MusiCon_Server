def bmp_ranges(bmp):
	bmp = int(bmp)
	if 59 < bmp <= 72:
		return "gym1"
	elif 72 < bmp <= 78:
		return "gym2"
	elif 78 < bmp <= 84:
		return "gym3"
	elif 84 < bmp <= 90:
		return "gym4"


def get_bmp_songs():
	