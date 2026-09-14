sname = input("Enter your name: ")

print("------------------------------------------------------------------------")
print(f"{sname}, Welcome to Student Budget Planner")
print("------------------------------------------------------------------------")

print("DISCLAIMER\n" 
"Your data is used for analysis of your budget and is not shared with anyone inside or outside the institute")
iname = input("Enter your institute name: ")


while True:
    cnf = input("Are you a hosteller? ")
    if cnf=='y'or cnf=='Y' or cnf=='Yes' or cnf=='YES' or cnf=='yes' :

        base = float(input("Enter the general amount credited to your bank acc in the beginning of a month: "))

        savper = float(input("\nFirst, we must make sure that there is some amount saved, we suggest to save 30%\n" 
                         "Enter the percentage of your monthly credit you want to save: "))
        sav = base*(savper/100)

        acdper = float(input("\nThen we must keep some amount aside for your academic expenses, we suggest 20%\n"
                       "Enter the percentage of your budget you would like to save for the above cause: "))
        acdsav = base*(acdper/100)

        healper = float(input("\nAfter that we must keep some amount aside for your health related expenses, we suggest 20%\n"
                       "Enter the percentage of your budget you would like to save for the above cause: "))
        healsav = base*(healper/100)

        print(f"\nYour credits in the beiginning of month: {base}\nAmount you saved for your future use: {sav}\n"
            f"Amount you saved for your academic uses: {acdsav} \nAmount you saved for your health related uses: {healsav} \n"
            f"Amount you are left with for yourself: {base-(sav+acdsav+healsav)}\nTry to stick to this plan\nand if theres any sudden requirement then you can go for withdrawl from your savings")
        break

    elif cnf=='n'or cnf=='N' or cnf=='No' or cnf=='NO' or cnf=='no' :
    

        base = float(input("Enter the general amount credited to your bank acc in the beginning of a month: "))

        savper = float(input("\nFirst, we must make sure that there is some amount saved, we suggest to save 30%\n" 
                         "Enter the percentage of your monthly credit you want to save: "))
        sav = base*(savper/100)

        acdper = float(input("\nThen we must keep some amount aside for your academic expenses, we suggest 20%\n"
                       "Enter the percentage of your budget you would like to save for the above cause: "))
        acdsav = base*(acdper/100)

        healper = float(input("\nAfter that we must keep some amount aside for your health related expenses, we suggest 20%\n"
                       "Enter the percentage of your budget you would like to save for the above cause: "))
        healsav = base*(healper/100)

        rent = float(input("\nNext we must set aside for your room rent"
                       "Enter the rent of your room: "))

        food = float(input("\nThen we must save for your daily meals"
                       "Enter the price of a full plate meal in general (all 4 meals): "))

        print(f"\nYour credits in the beiginning of month: {base}\nAmount you saved for your future use: {sav} \n"
            f"Amount you saved for your academic uses: {acdsav} \nAmount you saved for your health related uses: {healsav} \n"
            f"Amount you saved for your rent: {rent} \nAmount you saved for food: {food} \n"
            f"Amount you are left with for yourself: {base-(sav+acdsav+healsav+rent+food)}\nTry to stick to this plan\nand if theres any sudden requirement then you can go for withdrawl from your savings")
        break

    else:    
        print("Please answer in yes or no")