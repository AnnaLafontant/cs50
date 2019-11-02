from cs50 import get_int
from cs50 import get_string
import re

def main():
    alph = 0
    s = get_string("Enter text: ")

    for i in s:
        if i.isalpha():
            alph += 1

    words = len(s.split())
    sent = len(re.findall(r'\?|\!|\.', s))
    score = round((0.0588 * (alph/words*100)) - (0.296 * (sent/words*100)) - 15.8)
    if (score >= 16):
        print("Grade 16+\n")
    elif (score < 1):
        print("Before Grade 1\n")
    else:
        print("Grade:", score)


main()
