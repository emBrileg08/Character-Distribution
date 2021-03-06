"""
distribution.py
Author: emBrileg08
Credit: stackoverflow.com for information on converting a string to lowercase
and information on how to sort a list of tuples by different criteria
With input from Max Low, Mrs. Kono, and Maia Reynolds because I was discussing the program with me and they gave me some advice on "unzipping" my strings
Emily Murphy informed me of the print(*) function to print something a certain number of times

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
    
tuples=list(zip(empty, letters))

def onlyfirst(thingy):
    return thingy[0]
sortit=sorted(tuples, key=onlyfirst,reverse=True)

empty2=[]
for x in range(0,25):
    empty2.append(int(sortit[x][0]))

empty3=[]
for x in range (0,25):
    empty3.append(sortit[x][1])
    
y=1

for x in range(0,25):
   print(empty3[x]*empty2[x],end="")
   print("")