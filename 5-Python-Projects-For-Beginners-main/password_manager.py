from cryptography.fernet import Fernet

# 
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key) 
        

# write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() # the rstrip will remove carriage return 
            user, passw = data.split("|") # .split will split our data were ever there is a | 
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

# with keyword helps you open a file and closes it automatically
    #the a mode helps you add something to an existing file
    # in this case the 'a' create file named password.txt if it does not exist but if it exist it will wright at the end of it, we name as 'f'
    with open('passwords.txt', 'a') as f:   
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
