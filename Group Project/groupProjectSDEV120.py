import sqlite3
con = sqlite3.connect("sample.db")
cur = con.cursor()
#data = [
#    ("Carl", "Castle", 1, 2, 40, 14.5),
#    ("Samantha", "Castle", 2, 3, 20, 11),
#    ("Dan", "Stevens", 3, 6, 44, 23.4),
#    ("Alex", "Jones", 4, 2, 30 , 25.6),
#    ("Matt", "Farris", 5, 4, 65, 21),
#    ("George", "Soros", 6, 2, 15, 88),
#    ("Phil", "Wexler", 7, 1, 48, 32.25),
#    ("Will", "Arts", 8, 2, 38, 7.25),
#    ("Todd", "Wilkins", 9, 0, 4, 12.5),
#    ("Paul", "Wexler", 10, 1, 36, 35)
#]
#cur.execute("CREATE TABLE employees (firstname VARCHAR(30), lastname VARCHAR(30), id int, dependents int, hoursWorked int, hourlyRate float)")
#cur.executemany("INSERT INTO employees VALUES(?, ?, ?, ?, ?, ?)", data)
#con.commit()

# function to fetch data, using this to practice functions
def fetch(input: int) : # used placeholders to prevent SQL injection
        for row in cur.execute("SELECT dependents, hoursWorked, hourlyRate FROM employees WHERE id = ?", (inputID,)): #the (inputID,) is used to denote it as one character, whereas previously '10' was read as '1', '0' 
            response = row
        return response


inputID = 1 # this number also acts as our sentinel, this will be changed on first use
while inputID != 0:
    inputID = input("\nInput Employee ID to Generate Stub, or Enter 0 to Exit: ")
    response = 0
    if inputID == "":
        print("\nNo Input Found, exiting")
        break
    if inputID.isalpha(): # check if the user input a letter instead of number
        print("\nPlease enter a number next time, exiting")
        break
    if int(inputID) == 0: # check if the user input the exit character
        print("\nThank you for using this program!")
        break
    if int(inputID) > 10 or int(inputID) < 0: # check to be sure the user-entered integer is within range
        print("\nYou have input an invalid ID, exiting")
        break
    if inputID.isnumeric(): # check to be sure the user entered an integer
        row = fetch(inputID)
    else:
        row = [0, 0, 0] # in case something goes horribly wrong, this is a fallback

    
    
    dependents = row[0]
    hoursWorked = row[1]
    hourlyRate = row[2]

    overtimeHours = 0
    standardHours = 0
    overtimeRaiseConcern = 0

    if hoursWorked > 40:
        overtimeHours = hoursWorked - 40
        standardHours = 40
        overtimeRaiseConcern = 1 # bring up the hours being over 40
    else:
        standardHours = hoursWorked

    grossPay = standardHours * hourlyRate
    overtimePay = overtimeHours * (hourlyRate * 1.5)
    dependentCost = dependents * 25
    preTax = grossPay + overtimePay
    preTaxDepCost = preTax - dependentCost
    stateTax = preTaxDepCost * 0.056
    federalTax = preTaxDepCost * 0.079
    postTax = preTaxDepCost - (stateTax + federalTax)

    print("")
    if overtimeRaiseConcern == 1:
        print("This employee worked more than 40 hours this week.\n") # make EXCEPTIONALLY CLEAR that the user worked over 40 hours
    print("Hours Worked: " + str(hoursWorked))
    print("Hourly Rate: " + str(hourlyRate))
    print("Standard Hours Worked: " + str(standardHours))
    print("Overtime Hours Worked: " + str(overtimeHours))
    print("Standard Pay: " + str(round(grossPay, 2)))
    print("Overtime Pay: " + str(round(overtimePay, 2)))
    print("State Tax: " + str(round(stateTax, 2)))
    print("Federal Tax: " + str(round(federalTax, 2)))
    print("Dependent Cost: " + str(dependentCost))
    print("Pre-Tax Dependents Included: " + str(round(preTaxDepCost, 2)))
    print("\tPost-Tax: " + str(round(postTax, 2)))
    inputID = int(inputID)

con.close()
