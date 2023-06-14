# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

word_dict = dict()
for _ in range(n):
    string = input()
    if string in word_dict:
        word_dict[string] += 1
    else:
        word_dict[string] = 1

print(len(word_dict))
print(*word_dict.values(), sep=" ")
