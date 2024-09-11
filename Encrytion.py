import time
import platform
import os
import subprocess
from subprocess import Popen, PIPE, check_output

cont = True
invalid = True
debug = True


# while user still wants to use program (while continue is true)
while cont:
    # promt user for encrypt or decript
    print("Welcome to Drew's basic encryption and decryption project for CS120")
    print("To use this program have the file need in the project directory")
    print("Also please confirm you are encrypting a txt file as this program will only work for txt files")
    print("Please remember the number you give program because this is not saved anywhere")
    print("To encrypt(e), To decrypt(d), to exit(x)")
    
    # validation for user input
    while invalid:
        user = input("Enter: ")
        if (user == 'e'):
            invalid = False
        elif (user == 'd'):
            invalid = False
        elif (user == 'x'):
            invalid = False
            cont = False
    invalid = True
    
    # if encrypt
    if user == 'e':
        # ask for file name and number of loops for encryption
        print("You have chosen to encrypt a file.")
        print("Before you continue this will not work unless the file is in the project directory please confirm this")
        print("You will be prompted for two things now")
        print("Please enter your file name including the extention(filename.txt)")
        print("After which you will be prompted for how many times you would like the encryption to happen")
        print("This is due to a very simple encryption version is used in this project.")
        print("You will need to remember this number assuming you want to decrypt your file later")
        print("Your file will be writen over with the encrypted version")
        print("This will not be a problem aslong as you remember the your number")
        
        
        # input validation for file name (ensureing it is a txt file)
        while invalid:
            filename = input("Please enter a valid file name: ")
            x = filename.split(".")
            if x[1] == 'txt':
                print("Valid file name proceding to next step")
                invalid = False
        invalid = True
        while invalid:
            num = input("Enter how many time you would like the algorithm to run: ")
            num = int(num)
            if num > 0:
                print("Valid number enter proceding to encryption")
                invalid = False
        invalid = True
        # start timer
        tic = time.time()
        # compile the c++ encryption file
        try:
            # This is Python's way of calling the command line. We use it to compile the C++ files.
            subprocess.check_output("g++ -std=c++1y Encryption.cpp",stdin=None,stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError as e:
            # There were compiler errors in BubbleSort.cpp. Print out the error message and exit the program.
            print("<p>",e.output,"</p>")
            raise SystemExit
            
        # run c++ passing the file name and number to the c++ through the command line calls
        # if windows is your operating system
        # number of time to loop is argv[1] and file name is argv[2] and Encrypt or decrypt is argv[3]
        
        if platform.system() == 'Windows':
            p = Popen('a.exe '+ str(num) + ' ' + str(filename) + ' ' + str(user), shell=True, stdout=PIPE, stdin=PIPE)
            # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
            if debug:
                print(p.stdout.read())
            os.remove("a.exe")
        else: 
            p = Popen(['./a.out '+str(num) + ' ' + str(filename) + ' ' + str(user)], shell=True, stdout=PIPE, stdin=PIPE)
            # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
            if debug:
                print(p.stdout.read())
            os.remove("a.out")
        # end timer (and print the time)
        toc = time.time()
        t = toc - tic
        
        print("File encryption complete")
        print("It took: ")
        print(t)
        print("to complete your encryption")
    # elif decription
    elif user == 'd':
        # ask for file name and number of time looped for the decription
        print("You have selected decrypt")
        print("Please ensure the file you would like to decrypt is in the project directory")
        print("Also please ensure that your file has a (.txt) extention")
        print("I hope you remember your number")
        print("You will again be prompted for the file name and number of times to run the encryption")
        while invalid:
            filename = input("Please enter a valid file name: ")
            x = filename.split(".")
            if x[1] == 'txt':
                print("Valid file name proceding to next step")
                invalid = False
        invalid = True
        while invalid:
            num = input("Enter how many time you would like the algorithm to run: ")
            num = int(num)
            if num > 0:
                print("Valid number enter proceding to encryption")
                invalid = False
        invalid = True
        # start timer
        tic = time.time()
        # compile c++ to run the decription passing values to c++ through the comand line calls
        try:
            # This is Python's way of calling the command line. We use it to compile the C++ files.
            subprocess.check_output("g++ -std=c++1y Encryption.cpp",stdin=None,stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError as e:
            # There were compiler errors in BubbleSort.cpp. Print out the error message and exit the program.
            print("<p>",e.output,"</p>")
            raise SystemExit
            
        
        # execute the c++ file
        if platform.system() == 'Windows':
            p = Popen('a.exe '+ str(num) + ' ' + str(filename) + ' ' + str(user), shell=True, stdout=PIPE, stdin=PIPE)
            # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
            if debug:
                print(p.stdout.read())
            os.remove("a.exe")
        else:
            p = Popen(['./a.out '+str(num) + ' ' + str(filename)], shell=True, stdout=PIPE, stdin=PIPE)
            # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
            if debug:
                print(p.stdout.read())
            os.remove("a.out")
        # end timer (and print the time)
        toc = time.time()
        print("Decription was sucessful")
        print("The process took: ")
        print(toc - tic)
        print("to run")