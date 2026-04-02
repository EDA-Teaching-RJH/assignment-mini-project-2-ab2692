
def main():
 
 test_write()
def test_write():
    def read_last_enrty():
     with open ("email_list.txt", "r") as file:   
        last_entry = file.readlines()
        return last_entry[-1] 
    read_email = read_last_enrty()  
    assert read_email == "adam@gmail.com\n"  # compares the read name to adam (i preset the last name for testing) \n is for starting new line
 
 
 
if __name__ == "__main__":
     main()    

