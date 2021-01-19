x = False
y = 2000

while x == False:
    print("£",y)
    y = y * 0.9

    if y < 1000:
        x = True
 ##Program on how to make a cup of tea
cup_tea =("Get some kettle on and pour some hot water in the cup with a teabag.")
print(cup_tea)
milk = int(input("Do you want milk? Enter 3 if 'Yes' and 4 if not. "))
sugar = int(input("Do you want sugar? Enter 5 if 'Yes' and 6 if not. "))
if milk ==3 and sugar ==5:
    print("Add some Milk and Sugar. Your tea is ready!")
elif milk ==4 and sugar ==5:
    print("Add sugar. Your tea is ready!")
elif milk ==3 and sugar ==6:
    print("Add Milk. Your tea is ready!")
else:
    print("Your black tea is ready to drink!")
