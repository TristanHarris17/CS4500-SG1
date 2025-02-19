"""
Programming Language: Python 3.12 IDE: Visual Studio Code

Execution Instructions:
Run this code within a Python compiler and use the console for inputs

Group members: Logan Lindsay, Tristan Harris
Submission date: 02/21/2025
CS 4500
This program is designed to take the information from a specially formatted csv file,
seperate its values, and place those values into their respective DatedData.txt
Names.txt, and PresentAbsent.txt files

Packages/Data structures:
Only imports the csv module to read the csv file input, mainly uses arrays to handle
data

Sources:
W3schools.com/python/ - Used for syntax and module explanation
https://www.geeksforgeeks.org/working-csv-files-python/ - csv file manipulation

"""
import csv


def main():
    
    #Explanation of the program
    print('Hello, this program will take a csv file within the same directory as this program\nand seperate the names and dates into respective text files within this directory')
    print('This program will also be able to create a binary code of numbers within the given\ncsv file and put them into a PresentAbsent text file\n')
    input('Press ENTER to continue')
    
    x=1
    while(x==1): #Creates a loop for the user to continue inputting different files
        try:     #if the file names previously inputted do not exist
            user_file = input('Enter the file name: ')
            filename_check = False
            
            #checks to see if the file name contains any combination of the letters
            #"CSV" with a period in front of those letters
            #reprompts user input until a file with the postfix .csv is given
            if(user_file.casefold().endswith(".csv")):
                filename_check = True
                
            while(filename_check == False):
                new_user_file = input('That file is not a csv file, please enter a csv file name: ')
                
                if(new_user_file.casefold().endswith(".csv")):
                    filename_check = True
                    user_file = new_user_file
                    
            # Store header and dates
            header = []
            dates = []

            with open(user_file, mode = 'r')as file:
                csv_file = csv.reader(file)
                header = next(csv_file)
                for row in csv_file:
                    dates.append(row[0])
            header.pop(0) # removes the blank cell in the header row
            file.close()
            # write names to Names.txt and Dates to DatedData.txt
            
            with open('Names.txt', mode= 'w')as f:
                for item in header:
                    f.write(item + '\n')
            f.close()
            
            with open('DatedData.txt', mode= 'w') as f:
                for item in dates:
                    f.write(item + '\n')
            f.close()
            
            # Count number of lines in file
            line_count = 0
            with open(user_file, mode= 'r')as file:
                csv_file = csv.reader(file)
                line_count = sum(1 for row in csv_file)
            file.close()
            
            #combs through each line of the file, skipping the first number
            #(the date column) and checks to see if the number is 0
            #or something else, then writes its verdict to PresentAbsent.txt
            with open('PresentAbsent.txt', mode= 'w')as f:
                with open(user_file, mode= 'r')as file:
                    csv_file = csv.reader(file)
                    line = next(csv_file)
                    for i in range(line_count -1):
                        line = next(csv_file)
                        i=1
                        while(i < len(line)):
                            if(int(line[i]) > 0):
                                f.write('1')      
                            else:
                                f.write('0')
                            if(not(i==len(line)-1)):
                                f.write(',')
                            i+=1
                        f.write("\n")
                file.close()
            f.close()
                        
            input('Press ENTER to end the program')
            exit()
            
        except FileNotFoundError:
            print("Oops, that file does not exist,\nplease try a different file name")
main()
