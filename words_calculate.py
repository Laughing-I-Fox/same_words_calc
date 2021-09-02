mystery_string = str(input("please enter your string "))

word = str(input("input your word "))
count = 0
for i in range(len(mystery_string) - len(word) + 1):
    if mystery_string[i:i + len(word)] == word:
        count += 1
print(count)

