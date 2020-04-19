"""
Robin Karp string matching algorithm. It is used to find a pattern match inside of a text.
A better approach of this kind of problem is KMP.
Robin Karp use the Rolling Hash algorithm. But thanks to python for having a O(k) complexity hash function,
where k is the length of the string for which we are making a hash.

Robin Karp algorithm hashes the pattern string at first. Then generates hash of the substrings of the text
equal to length of the pattern. If two hash values(pattern hash and substring hash) are equal then it try to
match the pattern and the substring having a complexity O(m) where m is the length of the pattern. The reason
for doing this is there can be Hash Collision. Which means the hash of the pattern and the hash of a substring
which is not same as the pattern can be same. It happens because the hash values are moded value up to 64bit
integer.

"""


pattern=input()
text=input()

#Find the hash of the pattern
patHash=0
for i in pattern:
    patHash+=hash(i)

ll=len(text)
l=len(pattern)


#Find the hash of the each substring of the text string having a equal length of the pattern
Hash=0
for i in range((ll-l)+1):
    if i==0:
        #If no substring hash is not done yet then calculate the first substring equal to pattern length
        for j in range(l):
            Hash+=hash(text[j])
    else:
        #Subtract the hash of the first character of the previous string and add the hash of the last character of the
        #current string
        Hash-=hash(text[i-1])
        Hash+=hash(text[(i+l)-1])
    
    if Hash==patHash:
        if pattern==text[i:i+l]:
            print('Match found at index: ',i)


'''
Complexity
----------
Worst Case: O(n*m) where n is the length of the text and m is the length of the pattern
Best Case: O(n+m) when there is no hash collision and a single match inside or a yes no question

'''
