import sys
if len(sys.argv) == 2:
    print("Usage: input4.py 'First name and last name'")
    sys.exit()

first_name = sys.argv[1]
last_name = sys.argv[2]

email = first_name.lower().replace(" ",".")+"@company.com"



print(first_name+" "+last_name)
print(email)