def isPalindrome(x: int) -> bool:
    x = list(str(x))
    xx = list(reversed(x))
    if list(x) == xx:
        return True
    else:
        return False


print(isPalindrome(int(input())))

