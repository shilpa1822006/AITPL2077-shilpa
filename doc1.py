#python program to sort words in alphabetical order
my_str=input("enter a string")
words=my_str.split()
words.sort()
for word in words:
    print(word)