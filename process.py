log_file = open("um-server-01.txt") # open file to access

# create a funcion
def sales_reports(log_file):
    # start for loop - loop over the file line by line
    for line in log_file:
        line = line.rstrip() # strip away whitespace
        day = line[0:3] # first three characters of the line
        if day == "Mon": # if the day is Mon we want to print
            print(line)


sales_reports(log_file) # run the function w/ the file

# opens data file
# reads each line
#     removes blank space trailing the line, assigns stripped line to variable "line"
#     assigns first day abrreviation to "day" variable
#     checks if day is Tue, prints value stored in "line" variable if day is Tue
#         To change to Mon, (if day == "Mon":)

