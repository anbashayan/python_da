#split function

message = 'Your uber id : OK7541. Please keeo it confidential'

booking_id = (message.split(":")[1]).split(".")[0].strip()

print(booking_id)