import adam_library     # imports function 
def main():

 user_name = adam_library.ask_name()        # uses premade function to save input as user_name  

 adam_library.say_hello(user_name)

 add_to_list = input("do you want to add your name to list? y/n")

 if add_to_list == "y":          # allows the user to refuse data collection 
     adam_library.save_name(user_name)
     print("name added to list")
 else: print("Name not added")



 last_input = adam_library.read_last_enrty()
 print("last entry:", last_input)

 ask_again = input("do you want to add another entry? y/n")
 if ask_again == "y":
   main()
 else: print("session expired, Have a nice day")  

if __name__ == "__main__":
 main()
