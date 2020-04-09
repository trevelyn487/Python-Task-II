import string
import random
def get_user_info():
    
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    info = [first_name, last_name, email]
    
    return info

def password_gen(info):

    random_len = 5
    random.choice(string.ascii_lowercase)
    random_string_gen = "".join(random.choice(string.ascii_lowercase) for i in range(random_len))
    recommended_password = (info[0][:2] + random_string_gen + info[1][-2:])

    return recommended_password
           

user_reg = True

#creating "container" to hold all users' details
data_bank = []

while True:


    info = get_user_info()

    recommended_password = password_gen(info)
    
    #User satisfaction with generated password check                                     
    print("Recommended Password is - " + recommended_password)

    response = input('''Respond with a "Yes" if Recommended Password is OK. If not, respond with a "No" Response: ''')

    password_check = True
    
    while True:
    
        if response == "yes" or "Yes" or "YES":
            
            #adding password to user's information
            info.append(recommended_password)
            data_bank.append(info)

            password_check = False;
        
        else: 

            ('''
You may enter your preferred password. Ensure it is at least 7 characters long, at least.''')                    
                                                            
            user_password = input("Enter your preferred Password: ")
        
            password_len = True
        
            while password_len :
                    
                if  len(user_password) >= 7: 

                    #adding preferred password to user's info
                    info.append(recommended_password)
                    data_bank.append(info)

                    password_len = False

                    password_check = False 
                
                else:
                    print("Entry error! The password entered has less than 7 characters.")
                    user_password = input("Re-enter Password with has at least 7 characters: ")


new_user_query = input('''Would you like to register another user? Respond with a "Yes or "No": ''')

if new_user_query == "no" or "No" or "NO":
    
    user_reg = False
    for item in data_bank:
        print(item)
        
else:
    user_reg = True
    