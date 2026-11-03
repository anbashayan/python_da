import sys
full_name = sys.argv[1]
last_name = sys.argv[2]

#Format the namne
email =  full_name.lower().replace(" ",".")+last_name+"@company.com"

#Output
print("\n----Your Profile-----")
print("Full name", full_name+last_name)
print("Generated email:", email)