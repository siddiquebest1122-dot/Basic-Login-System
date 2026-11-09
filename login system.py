
print ("    Log-in System    ")

users = {
    "user.com" : "1122",
    "admin.com" : "2233",
    "tel.com" : "3344"
}

username = input("Enter User Name: ")
password = input("Enter Password: ")

if username in users and users[username] == password:
    print ("Login Success Fully!")
else:
    print ("1st attempt Failed")

    username = input("Enter User Name: ")
    password = input("Enter Password: ")


    if username in users and users[username] == password:
        print ("Login Success Fully!")
    else:
        print ("2nd Attempt Failed\n Note: Your Account Locked for 'Temporary' If your last Attempt will be Wrong.")


    username = input("Enter User Name:")
    password = input("Enter Password:")

    if username in users and users[username] == password:
        print ("Login Success Fully!")
    else:
        print ("Your Account Locked For '30 Days!'")
