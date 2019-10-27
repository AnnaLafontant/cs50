#a program that first asks the user how much change is owed and then spits out the minimum number of coins with which said change can be made
#Assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).

from cs50 import get_float

def main():
    count=0
    while count==0:
        h=get_float("Enter change amount in dollars: ")
        if h >=0:
            h=round(h*100)
            q=h//25
            d=(h-25*q)//10
            n=round((h-25*q-10*d),2)//5
            p=round((h-25*q-10*d -5*n),2)//1
            count=q+d+n+p
            print(count)
        else:
            print('Your number should be positive')

main()
