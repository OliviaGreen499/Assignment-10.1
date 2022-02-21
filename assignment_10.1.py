import os
import csv

def file_system():
    """Display information about users"""
    direc = input("Enter name directory to save a file: ")
    filename = input("Enter name of the file they want to save to the directory: ") 
    
    print  (direc, filename)

    



    if os.path.isdir(direc):
        writeFile = open(os.path.join(direc,filename),'w') 
        writeFile.write (direc, + filename)
        writeFile.close() 
        
        print("File contents:")


        readFile = open(os.path.join(direc,filename),'r') 
        for line in readFile:
            print(line)

        readFile.close()
    
        with open('Userdata.csv', 'w',
              newline='') as outfile:
              w = csv.writer(outfile)
              name = input("Enter your name : ")
              address = input("Enter your address : ")
              phone_number = input("Enter your phone number : ")
              for line in outfile:

                w.writerow(name, address, phone_number) 
              print(outfile)    
            
    else:
        print("Directory doesn't exist, please enter again")
    
    
 
        

file_system()


   

         
    

  

