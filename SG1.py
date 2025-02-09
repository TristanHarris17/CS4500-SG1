
import csv

def main():
    # TODO write overview message
    #print('overview of program')
    #input('Press ENTER to continue')

    # TODO CHANGE USERFILE BACK TO INPUT
    #user_file = input('Enter the file name: ')
    user_file = 'file.csv'


    # Store header and dates
    header = []
    dates = []
    with open(user_file, mode = 'r')as file:
        csv_file = csv.reader(file)
        header = next(csv_file)
        for row in csv_file:
            dates.append(row[0])
    header.pop(0) # remoes the blank cell in the header row
    
    # write names to Names.txt and Dates to DatedData.txt
    # adds a extra blank line at the end idk if that will matter
    with open('Names.txt', mode= 'w')as f:
        for item in header:
            f.write(item + '\n')
    with open('DatedData.txt', mode= 'w') as f:
        for item in dates:
            f.write(item + '\n')

    # Count number of lines in file (not sure if this is needed yet)
    line_count = 0
    with open(user_file, mode= 'r')as file:
        csv_file = csv.reader(file)
        line_count = sum(1 for row in csv_file)
    print(line_count)

    with open('PresentAbsent.txt', mode= 'w')as f:
        with open(user_file, mode= 'r')as file:
            csv_file = csv.reader(file)
            line = next(csv_file)
            for i in range(line_count -1):
                line = next(csv_file)
                print(line)
                
main()