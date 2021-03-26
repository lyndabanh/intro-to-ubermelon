log_file = open("um-server-01.txt")


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)


sales_reports(log_file)

#opens data file
#reads each line
    #removes blank space trailing the line, assigns stripped line to variable "line"
    #assigns first day abrreviation to "day" variable
    #checks if day is Tue, prints value stored in "line" variable if day is Tue
        #To change to Mon, (if day == "Mon":)

