#store user entry as a string in file_name variable
file_name = input("Please enter the file name: ") 

#store user values in set variables 
name = input("Please enter your name: ") 
address = input("Please enter your street address: ") 
phone = input("Please enter your phone number: ") 

#open file set by file_name variable
with open(file_name, "w") as file:   
  file.write(f"{name},{address},{phone}\n") 
  
#read and display the contents set by file_name variable   
with open(file_name, "r") as file:   
    contents = file.read()   
    print(contents)
