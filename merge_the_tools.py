def print_merge(target):
    print(*dict.fromkeys(target), sep="")


def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    x = 0
    while x < n:
        print_merge(string[x : x + k])
        x += k


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
