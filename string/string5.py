#split function

message = 'Your uber id : OK7541. Please keeo it confidential'

booking_id = (message.split(":")[1]).split(".")[0]

print(booking_id)