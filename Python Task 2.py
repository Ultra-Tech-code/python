### Generating random No.
import random
import math

User_Database = []

digits = [i for i in range(0, 10)]

random_no = ""

for i in range(5):
    index = math.floor(random.random() * 10)
    random_no += str(digits[index])
###################

print("SlackUsername - BlackAdam")
print("Hello User")
status = True

while status:
    ######## Getting User Details.
    First_Name = input("Please Enter Your Firstname: ")
    Last_Name = input("Please Enter Your Lastname: ")
    Email = input("Please Enter Your Email: ")
    #####
    User_Details = [First_Name, Last_Name, Email]
    #########
    User_Password = (str(First_Name[0:2]) + str(Last_Name[0:2]) + random_no)
    print("Your Password is: ", User_Password)

    User_Response = input("Are you satisfied with the password: Enter YES or NO: ").lower()
    if User_Response == "no":
        while True:
            print("Password should be longer than 6 characters")
            User_New_Password = input("Enter the password you will love to use:-  ")
            if len(User_New_Password) < 7:
                print("Oops! Password Not Accepted.  Try again...")
            else:
                print("Your new password is: ", User_New_Password)
                print("Password accepted \n Welcome")
                User_Details.append(User_New_Password)
                User_Database.append(User_Details)
                break
    else:
        print("Welcome")
        User_Details.append(User_Password)
        User_Database.append(User_Details)

    NewUser = input("Would you like to add a new user: Enter YES or NO: ").lower()
    if NewUser == "no":
        status = False
        for details in User_Database:
            print(details)

    else:
        status = True











