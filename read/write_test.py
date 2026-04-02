
def main():
 
 test_write()
def test_write():
    def read_last_enrty():
     with open ("names_list.txt", "r") as file:   # reads the names_list.txt file
        last_entry = file.readlines()
        return last_entry[-1] 
    read_name = read_last_enrty()
    assert read_name == "adam\n"
 
 
 
if __name__ == "__main__":
     main()    

