#Removes extra spaces

dirty_Text= "        human             "
clean_text = dirty_Text.strip()
print(clean_text)

#strip is used to seperate words
Name = "Kandiah Anbalagan Sujanasrishayan"
split=Name.split()
print(split)

#Taking both initial letters from both word
name="sivananthi anbalagan"
initials = "".join([word[0].upper() for word in name.split()])
print(initials)

