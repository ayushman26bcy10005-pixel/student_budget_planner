sname = input("Enter your name: ")

print("------------------------------------------------------------------------")
print(f"{sname}, Welcome to Student Budget Planner")
print("------------------------------------------------------------------------")

print("DISCLAIMER" 
"Your data is used for analysis of your budget and is not shared with anyone inside or outside the institute")

cnf = input("Are you a hosteller? ")

if cnf=='y'or cnf=='Y' or cnf=='Yes' or cnf=='YES' or cnf=='yes' or cnf=='Y' :
    iname = input("Enter your institute name: ")

    base = float(input("Income can be from many sources like" \
    "" \
    "Enter the general amount credited to your bank acc in the beginning of a month: "))

    savper = float(input("First, we must make sure that there is some amount saved." \
    "Enter the percentage of your monthly credit you want to save: "))
    saving = base*(savper/100)


    print(f"Your savings are: {saving}")