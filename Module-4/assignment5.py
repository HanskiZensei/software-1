correct_pass = "rules"
correct_user = "python"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_user and password == correct_pass:
        print("Welcome")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print("Incorrect username or password. Please try again. ")
        else:
            print("Access denied")
