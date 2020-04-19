n, m = input().split()
a = set(input().split())
b = set(input().split())
print(min(a&b) if a&b else min(min(a)+min(b), min(b)+min(a)) )
