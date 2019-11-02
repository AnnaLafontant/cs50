from cs50 import get_int

def main():
    s=0

    while s==0:
        h=get_int("Enter height: ")
        if h >0 and h<9:
            height=range(h)
            for i in height:
                s="#"*(i+1)
                print(' '*(h-i)+s+'  '+s)
        else:
            print('Your number should be an integer between 1 and 8')

main()
