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

inputID = input("ID to run: ")
response = 0
if int(inputID) > 10 or int(inputID) < 1:
    inputID = "1"
for row in cur.execute("SELECT dependents, hoursWorked, hourlyRate FROM employees WHERE id = ?", inputID):
    response = row
dependents = row[0]
hoursWorked = row[1]
hourlyRate = row[2]

overtimeHours = 0
standardHours = 0

if hoursWorked > 40:
    overtimeHours = hoursWorked - 40
    standardHours = 40
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



con.close()