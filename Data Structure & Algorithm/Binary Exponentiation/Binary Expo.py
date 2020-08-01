"""
This is a method that computes a^b really fast.
The idea behind this is to compute a^(b//2) and
then multiply by itself. It halfs the time in each
iteration.
"""



def power_recursive(a,b):
    """
    This is a recursive function that computes a^b
    """
    
    if b==0:return 1

    temp = power_recursive(a,b//2)
    result = temp*temp
    
    if b%2==1:
        result = result * a

    return result
    

def power_iterative(a,b):
    """
    This is an iterative function that computes a^b
    """

    result = 1
    while b>0:
        if b%2==1:
            result = result * a

        a = a*a
        b = b//2
        
    return result









    
