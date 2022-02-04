########################################
# Name: Joe Tomlinson
# Collaborators: Luke Orona
# Estimated time spent (hr): 2
########################################

def digital_root(n):
    """Computes and returns the digital root of a given integer n.

    If you want to define any other function(s) to help you
    out, feel more than free, just make sure this is the main
    function, as this is what will be tested against.

    Inputs:
        n (int): The number to take the digital root of
    Outputs:
        int: The digital root of the provided number
    """
    # Add your code below!
    num = str(n)
    if (num == "0"):
        return 0
    ans = 0
    for i in range (0, len((num))):
        ans = (ans + int(num[i])) % 9
    return ans % 9
    if(ans == 0):
        return 9
    else:
        return ans % 9




if __name__ == '__main__':
    # You can alter the below value to test your function with a variety
    # of numeric inputs!

    test_input = 1729
    print("The digital root of ", test_input, " is ", digital_root(test_input))
