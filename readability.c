#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{

    int alph,words,sent;
    alph=words=sent=0;
    char sent_char[] ={'.','?','!'};
    string s = get_string("Text: ");
    int score;

    for (int i = 0; i < strlen(s); i++)
    {
        if((s[i]>='a' && s[i]<='z') || (s[i]>='A' && s[i]<='Z'))
        {
            alph++;
        }

        if((s[i+1]=='\0') || (s[i+1]==' '))
        {
            words++;
        }

        if(strchr(sent_char,s[i+1]) && ((s[i]>='a' && s[i]<='z') || (s[i]>='A' && s[i]<='Z')))
        {
            sent++;
        }

    }

    {
    score= lround((0.0588 * (alph/words*100)) - (0.296 * (sent/words*100)) - 15.8 );
        {
            if (score >=16)
            {
                printf("Grade 16+\n");

            }
            else if (score <1)
            {
                printf("Before Grade 1\n");
            }
            else
            {
                printf("Grade: %i\n",score);
            }
        }
    }

printf("raw: %f\n", (0.0588 * (alph/words*100) - 0.296 * (sent/words*100) - 15.8 ));
printf("letter(s): %d\n", alph);
printf("word(s): %d\n", words);
printf("sentence(s): %d\n", sent);
printf("t1: %f\n",(0.0588 * (alph/words*100)));
printf("t2: %f\n",((0.0588 * (alph/words*100)) - (0.296 * (sent/words*100))));

}


