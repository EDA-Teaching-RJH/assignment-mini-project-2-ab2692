import adam_library     # imports function 


user_name = adam_library.ask_name()        # uses premade function to save input as user_name  

adam_library.say_hello(user_name)

add_to_list = input("do you want to add your name to list? y/n")

if add_to_list == "y":
    adam_library.save_name(user_name)
    print("name added to list")
else: print("Name not added, have a nice day")



