from cryptography.fernet import Fernet #module allows to encrypt text

'''def write_key():  #function to create key file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) #running this function once creates the key file & now no longer required
write_key()''''

def load_key():
    file = open("key.key", "rb") #opens file in read/bytes mode
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ") #Not made any password option for program yet
key = load_key() + master_pwd.encode() #encode() takes sting & converts to bytes
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:     #'if else' statement added to view function after bug detected
                user, passw = data.split("|")
                print ("user:", user, "| Password:", fer.decrypt(passw.encode()).decode()) #Bug- was initially meant to view username & encrypted password 
            else:
                print(f"Invalid format for line: {data}")  #returns message if seperator not present in data variable

def create():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f: #using 'with' closes the file automatically. 'a'(append) mode, adds to file if exists and creates file if doesnt exist  'w'(write) mode overides file that already exist with new one, 'r' mode (read only mode)
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n") # f is file name, encoding pwd converts to bytes

while True:
    mode = input("Would you like to view current passwords or create a new password? (type 'view', 'create' or 'Q' to quit)").lower()

    if mode == "q":
        break #exits loop if user decides to quit

    if mode == "view": #calls view passwords function
        view()
    elif mode == "create": #calls create password function
        create()
    else:
        print("Ivalid mode")
        continue
