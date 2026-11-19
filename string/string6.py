#Removes extra spaces

dirty_Text= "        human             "
clean_text = dirty_Text.strip()
print(clean_text)

name = "anban shayan"
initials = [word[0].upper() for word in name.split()]
print(initials)

#strip is used to seperate words
Name = "Kandiah Anbalagan Sujanasrishayan"
split=Name.split()
print(split)