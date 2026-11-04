import sys

full_name = sys.argv[2]

email = full_name.lower().replace(" ", ".") + "@company.lk"

print("\n ##### Your Details #####")

print("Full Name : ", full_name)

print("e-mail : ",email)