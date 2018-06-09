import os
def rename_files():
    file_list=os.listdir(r"C:\Users\sachin\Desktop\py udacity\my secret message")
    #print(file_list)
    saved_path=os.getcwd()
    #print("the current working directory is"+saved_path)
    os.chdir(r"C:\Users\sachin\Desktop\py udacity\my secret message")
    #print("after changing directory"+os.getcwd())
    print(os.getcwd())
    for file_name in file_list:
        os.rename(file_name, file_name.strip("0123456789"))
    os.chdir(saved_path)    
rename_files()
