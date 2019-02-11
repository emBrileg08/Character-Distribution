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

a=lower.count("a")
b=lower.count("b")
c=lower.count("c")
d=lower.count("d")
e=lower.count("e")
f=lower.count("f")
g=lower.count("g")
h=lower.count("h")
i=lower.count("i")
j=lower.count("j")
k=lower.count("k")
l=lower.count("l")
m=lower.count("m")
n=lower.count("n")
o=lower.count("o")
p=lower.count("p")
q=lower.count("q")
r=lower.count("r")
s=lower.count("s")
t=lower.count("t")
u=lower.count("u")
v=lower.count("v")
w=lower.count("w")
x=lower.count("x")
y