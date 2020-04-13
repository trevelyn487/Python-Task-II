import string
import random


is_user_validation = True

#creating "ultimate container" where all users' details are stored 
database = {}

#initialising number of users
user = 1

while True:

    #collecting user details
    first_name = input("\nEnter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")   

    #creating temporary container for each user
    user_details = {
        "First Name": first_name, 
        "Last Name": last_name, 
        "Email": email}

    #random password generation
    list1 = [first_name]
    list2 = [last_name]
    random_string_length = 5
    random.choice(string.ascii_lowercase)
    random_string = "".join(random.choice(string.ascii_lowercase) for i in range(random_string_length))
    gen_password = (first_name[:2] + random_string + last_name[-2:])

    #user opinion on generated password check
    print("\nRecommended password is - " + gen_password + ''' 
\nWould you like to use this as your password? 
If so, respond with a "Yes". If not, respond with a "No".''')

    answer = input("\nResponse: ").lower()
    if answer == "yes":
        print("Your registration was successful.")

        #adding recommended password to user's details if user finds it satisfactory
        if "Password" not in user_details.keys():
            user_details["Password"] = gen_password
            database[user] = user_details
                
    #allowing user come up with password   
    else:
        print('''
\nYou can enter your preferred password below. 
NOTE: Password must be at least 7 characters long.''')
        user_password = input("Enter your preferred password: ")
        while len(user_password) < 7:
            print("Entry error! Password has less than 7 characters.")
            user_password = input("Re-enter password: ")
        else:
            print("Password has been registered and your registration, successful.")

            #adding user preferred password to user's details
            if "Password" not in user_details.keys(): 
                user_details["Password"] = user_password
                database[user] = user_details

    #checking for new user           
    print('''
\nWould you like to register another user? Respond with a "Yes" or "No" below:''')

    new_user_query = input("Response: ").lower()
    if new_user_query == "yes":
        user += 1

    else:
        is_user_validation = False

        #output user(s') details
        print(
'''\nHere are all user(s) details:''')
        for user, details in database.items():
            print("\nUser Number", user)
            for key in details:
                print(key + ": " + details[key])
        break
