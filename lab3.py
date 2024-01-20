
#lab3.py

# Starter code for lab 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Chloe Fabro
# xfabro@uci.edu
# xfabro


def print_message():
     print('Welcome to PyNote!')
     print('Here are your notes:')
     print()
     
def readFile():
    with open('pynote.txt','a+') as myfile:
        myfile.seek(0)
        #.readlines will read all content in the file 
        #.readline will only read one line
        content = myfile.readlines()

        for i, lines in enumerate(content):
            line = lines.strip()
            print(line)
            print()
            if i < len(content)-i:
                print()
    
                           
def wirte_content():
    
    while True:
        
        note = input("Please enter a new note (enter q to exit):")

        if note == 'q':
            break
        else:
             with open('pynote.txt', 'a') as myfile:
                myfile.write(note+'\n')  

if __name__ == '__main__':
    print_message()
    readFile()
    wirte_content()
