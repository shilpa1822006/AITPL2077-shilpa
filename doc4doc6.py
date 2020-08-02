def ispalindrome(s):
    return s == s[::-1]


s = "shilpa"
ans = ispalindrome(s)

if ans:
    print("it is a palindrome")
else:
    print("it is not a palindrome")