"""
distribution.py
Author: emBrileg08
Credit: stackoverflow.com for information on converting a string to lowercase

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string

upper= str(input("Please enter a string of text (the bigger the better): "))
lower= upper.lower()
print('The distribution of characters in "'+ upper +'" is:')

letters=list(string.ascii_lowercase)

empty=[]
for x in letters:
    empty.append(lower.count(x))
    
#tuples=zip(letters,empty)
#sortit=empty.sort()
#sortwell=sortit[::-1]

#print(sortwell)

    
#y=1

#for x in range(0,25):
    #if y<= empty[x]:
        #print(letters[x])
        #y+=1
    

