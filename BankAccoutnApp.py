def setupInitMoney():
    while True:
        initialMoney = float(input("Please input the initial amount of money you have in your bank account:"))
        if initialMoney < 0:
            print ("Please try again.","\n","Do not input a negative number!")
        else:
            return initialMoney


def setupPercent():
    while True:
        Percent = int(input("Please input the interest rate as an integer from 0 to 100:"))
        if Percent < 100 and Percent > 0:
            return Percent
        else:
            print ("Please try again.","\n","This time input the number in the integer form in the range of 0 to 100.")            


def setupYears():
    while True:
        Years = int(input("Please input the years between 1 to 20 after which you want to calculate you balance:"))
        if Years < 20 and Years >1:
            return Years
        else:
            print ("Please try again.","\n","This time input the years in the range of 1 to 20")


def calculateTheResultMoney(Money, Percent, Years):
    Percent = (Percent/100) + 1
    while Years>0:
        Money = Money * Percent
        Years = Years-1
    return Money


def main():
    print ("Dear user,","\n","This application is made in order to calculate the balance you will have","\n","in your bank account after some years with an amount of interest rate.")
    print ("To do so,","\n","We will use your initial amount of money, the years after which you","\n","want to calculate your balance and the interest rate.")
    initMoney = setupInitMoney()
    Percent = setupPercent()
    Years = setupYears()
    result = calculateTheResultMoney(initMoney, Percent, Years)
    print ("After", Years,"years your initial balance of",initMoney,"\n","with the interest rate of",Percent,"has become your final balance of",result)


main()    
