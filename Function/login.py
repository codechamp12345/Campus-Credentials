def login():
    username = input("Enter Your Username:")
    password = input("Enter Your Password:")
    if username == password:
        print('login successfully!')
    else:
        print("You have enetered wrong credentials")

login()