'''In algebraic expressions, the symbol for multiplication is often left out, as in 
3x+4y or 3(x+5). Computers prefer those expressions to include the multiplication 
symbol, like 3*x+4*y or 3*(x+5). Write a program that asks the user for an algebraic 
expression and then inserts multiplication symbols where appropriate'''
s=list(input())
res=""
i=0
while(i<len(s)):
 if(s[i]=='('):
 index=s.index(')')
 s2="".join(s[i:index+1])
 res+="*"+s2
 i+=len(s2)
 elif s[i].isalpha():
 res+='*'+s[i]
 i+=1
 else:
 res+=s[i]
 i+=1
print(res)
