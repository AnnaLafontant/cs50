#a program that prompts the user for a credit card number and then reports (via print)
#whether it is a valid American Express, MasterCard, or Visa card number
import re

from cs50 import get_int
from cs50 import get_string

def main():
    counter=0
    while counter==0:
        card=get_int("Enter card number: " )
        if len(str(card))>12 and len(str(card))<17:
            counter+=1 #make sure that the while loop is not infinite
            #last=card%10
            first=[] #stores the integer as an array of digits
            n=card
            while n>0:
                rem=n%10 #identifies the last digit
                first.append(int(rem)) #add to the list
                n=(n-rem)/10 #subtract the last digit and repeat until the digit is zero
            first.reverse() #re-order the items in the list in line with the original integer
            #print('first: ',first)
            reduced=first[:-1] #workaround to get to the last second digit from the end
            #print('reduced: ',reduced)
            second=reduced[::-2] #a list with every other digit starting from the second last
            #print('second: ',second)

            not_m=first[::-2] # a list with every other digit starting from the last
            #print("not_m: ", not_m)
            mult=0
            mult_list=[]
            for s in second:
                mult_two=s*2
                mult_list.append(mult_two)
            #print(mult_list)
            for m in mult_list:
                for d in str(m):
                    mult+=int(d)
            #print("mult: ",mult)

            n_mult=0
            for n in not_m:
                n_mult+=n
            #print(n_mult)
            sum=n_mult+mult

            if sum%10==0 and len(str(card))==15 and re.search("^34|^37", str(card), re.IGNORECASE):
                print("AMEX\n")
            elif sum%10==0 and re.search("^4", str(card), re.IGNORECASE) and ((len(str(card))==13 or len(str(card))==16)) :
                print("VISA\n")
            elif sum%10==0 and re.search("^51|^52|^53|^54|^55", str(card)) and len(str(card))==16:
                print("MASTERCARD\n")
            else:
                print("INVALID\n")
        else:
            print('Please enter the correct length ')
main()
