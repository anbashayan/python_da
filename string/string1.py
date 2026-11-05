driver_name = "a shayan"

#Change all letters into small
print(driver_name.lower())

#Change all letters into uppercse
print(driver_name.upper())


#Mask
mobile = '+94705226201'
print(mobile[:4]+'****'+mobile[-4:])


#Example of Mask
description = 'An OTP has been send to mobile number and email'
mail='anban@yahoo.com'
mobile = '+94773387868'
print(description+' '+ mail[:4]+'**********'+mail[-4:]+' '[-3:]+mobile[:3]+"*****"+mobile[-4:])