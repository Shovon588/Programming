for I in range(int(input())):
    n = int(input())

    letters = {}
    for i in range(n):
        s = input()
        for char in s:
            if char not in letters:
                letters[char]=1
            else:
                letters[char]+=1

    result = "YES"
    for letter in letters:
        if letters[letter]%n!=0:
            result = "NO"

    print(result)
            
