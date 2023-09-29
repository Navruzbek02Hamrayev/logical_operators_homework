def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """

    return (n%10==1)+(n//10%10==1)+(n//100%10==1)+(n//1000==1)+(n//10000==1)>(n%10==0)+(n//10%10==0)+(n//100%10==0)+(n//1000==0)+(n//10000==0)
print(main(1100))
print(main(10011))