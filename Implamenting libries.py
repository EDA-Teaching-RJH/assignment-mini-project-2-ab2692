import adam_library     # imports function 
import re 

def main():

  user_email = adam_library.ask_email()        # uses premade function to save input as user_name  

  def email_checker(user_email):
   pattern = r"^[a-zA-Z0-9.-_!@#$%^&*()_+=`~'/?,<>]+@[a-zA-Z.]+\.[.a-zA-Z0-9]"   
   if re.match(pattern, user_email):
     return True
   else: return False
 

 adam_library.say_hello(user_email)

 add_to_list = input("do you want to add your email to list? y/n")

 if add_to_list == "y":          # allows the user to refuse data collection 
     adam_library.save_email(user_email)
     print("email added to list")
 else: print("email not added")



 last_input = adam_library.read_last_enrty()  # calls read function from library 
 print("last entry:", last_input)             

 ask_again = input("do you want to add another entry? y/n") # loop function asks to add another name and loops back to name entry
 if ask_again == "y":
   main()
 else: print("session expired, Have a nice day")   # if selected anything but "y" code ends

if __name__ == "__main__":
 main()
