'''
KMP algorithm matches a pattern inside a text. In normal brute force algorithm the complexity is O(n*m), where n is
the length of  the text and m is the length of the pattern. But KMP algorithm can do this in O(n+m). How? KMP algorithm
keeps tracks of the matched suffix and prefix by using a lps array. Now what is a lps array? A lps array keeps tracks
of the  number of matched suffix and prefix found up to the current index.

Video Link: https://www.youtube.com/watch?v=sMARZCTPyNI

'''




def lps(pattern):
    i=0;j=1;l=len(pattern)
    lps=[0 for i in range(l)]
    
    while(j<l):
        if pattern[i]==pattern[j]:
            lps[j]=i+1
            i+=1;j+=1
        else:
            if i!=0:
                i=lps[i-1]
            else:
                j+=1
        
    return lps



def kmp(text,pattern,lps):
    i=0;j=0;l=len(pattern);ll=len(text)

    while(j<l and i<ll):
        if text[i]==pattern[j]:
            i+=1;j+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1

        if j==l:
            print('found',i-l)
            j=j-1

                
    if j==l:
        return True
    return False



text,pat=map(str,input().split())

a=lps(pat)
print(kmp(text,pat,a))
