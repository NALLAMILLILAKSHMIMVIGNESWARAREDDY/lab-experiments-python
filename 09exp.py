'''Write a program that asks the user to enter two strings of the same length. The program should then check to see if the strings are
of the same length. If they are not, the program should print an appropriate message and exit. If they are of the samelength, the
program should alternate the characters of the two strings. For example, if the user enters abcde and ABCDE the program should
print out AaBbCcDdEe.'''
n1=input("Enter a string")
n2=input("Enter a string")
l1=len(n1)
l2=len(n2)
if l1!=l2:
    print("Both strings are not having same length")
else:
    for i in range(l1):
        print(n2[i]+n1[i],end="")
