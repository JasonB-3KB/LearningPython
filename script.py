first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name, last_name):
  return first_name[0:3] + last_name[0:3]


new_account = account_generator("Julie", "Blevins")
print(new_account)
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2]
print(second_to_last)
final_word = company_motto[-4:]
print(final_word)

#fixing Bob to Rob
first_name = "Bob"
last_name = "Daily"
fixed_first_name = "R" + first_name[-2:]

#creating a username and password generator
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

