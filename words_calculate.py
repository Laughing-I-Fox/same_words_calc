my_string = str(input("please enter your string "))

word = str(input("please enter your word "))
count = 0

for i in range(len(my_string) - len(word) + 1):
    if my_string[i:i + len(word)] == word:
        count += 1
print(count)
