from datetime import datetime, timedelta, date, time

def convert_timedelta(delta):
    days, seconds = delta.days, delta.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds

print("Looping. Use CTRL + C to exit.")
sameday = input("(Y/n) Same day? ")
while True:
	if sameday == "n":
		f = input("(YYYY-MM-DD HH:MM:SS) from: ")
		t = input("(YYYY-MM-DD HH:MM:SS) to: ")
		_from = datetime.strptime(f, "%Y-%m-%d %H:%M:%S")
		_to = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
	else:
		f = input("(HH:MM:SS) from: ")
		t = input("(HH:MM:SS) to: ")
		_from = datetime.strptime(f, "%H:%M:%S")
		_to = datetime.strptime(t, "%H:%M:%S")
	
	delta = _to - _from
	delta_tuple = convert_timedelta(delta)
	
	print("\nDelta ms: {}".format(delta.total_seconds() * 1000))
	print("Delta HH:MM:SS: {:02}:{:02}:{:02}".format(delta_tuple[0], delta_tuple[1], delta_tuple[2]))
	input()