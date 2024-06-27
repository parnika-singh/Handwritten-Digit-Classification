from collections import deque

def palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Initialize stack and queue
    stack = []
    queue = deque()
    
    # Populate stack and queue with characters
    for char in cleaned:
        stack.append(char)
        queue.append(char)
    
    # Compare elements from stack and queue
    while stack:
        if stack.pop() != queue.popleft():
            return False
            
    return True

# Example usage
word_or_sentence = input("Enter a word or sentence: ")
if palindrome(word_or_sentence):
    print("The entered word/sentence is a palindrome.")
else:
    print("The entered word/sentence is not a palindrome.")
