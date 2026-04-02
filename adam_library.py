
def ask_name():  #creates function, askes user name and saves it 
    user_name =input("what is your name?")
    return user_name


def say_hello(user_name): # crates function, prints hello and the previously saved user_name
    print("hello", user_name)

def save_name(user_name):
    with open ("names_list.txt","a") as file: # opens / crates .txt file to append. (with ensures it closes itself)
        file.write(user_name + "\n")  # adds new name to file and creates a new line
        print("saved")

        
def read_last_enrty():
    with open ("names_list.txt", "r") as file:   # reads the names_list.txt file
        last_entry = file.readlines()
        return last_entry[-1]  #[-1] indexes the bottom (most recent) entry