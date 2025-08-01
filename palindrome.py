def is_palindrome(word):
    word=word.lower()
    return word==word[::-1]
word=input("Enter a word:")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")    
