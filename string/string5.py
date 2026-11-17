#split function

message = 'Your uber id : OK7541. Please keeo it confidential'

booking_id = (message.split(":")[1]).split(".")[0].strip()

print(booking_id)

#to extract some known text

promo_message = 'Use CV232 as promo code'

if 'CV212' in promo_message:
    print("Offer applied")
else:
    print('Offer Denied')