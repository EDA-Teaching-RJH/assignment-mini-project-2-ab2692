
def ask_email():  #creates function, askes user name and saves it 
    user_email =input("what is your email?")
    return user_email


def say_hello(user_email): # crates function, prints hello and the previously saved user_email
    print("hello", user_email)

def save_email(user_email):
    with open ("email_list.txt","a") as file: # opens / crates .txt file to append. (with ensures it closes itself)
        file.write(user_email + "\n")  # adds new name to file and creates a new line
        print("saved")

        
def read_last_enrty():
    with open ("email_list.txt", "r") as file:   # reads the names_list.txt file
        last_entry = file.readlines()
        return last_entry[-1]  #[-1] indexes the bottom (most recent) entry