import adam_library
def main():
 
 test_write()
def test_write():
    
    read_name = adam_library.read_last_enrty()
    assert read_name == "adam"
 
 
 
if __name__ == "__main__":
     main()    

