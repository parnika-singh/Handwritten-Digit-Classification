import sys
class Solution:
    def __init__(self):
        st=[]
        q=[]
        self.st=st
        self.q=q
    def pushCharacter(s):
        st.insert(0, s)
    def enqueueCharacter(s):
        q=q.append(s)
    def popCharacter():
        return (st.pop(0))
    def dequeueCharacter():
        return (q.pop())
        
    # Write your code here
         

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    print(s[i])
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.") 
