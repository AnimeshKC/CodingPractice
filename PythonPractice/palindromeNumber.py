def numIsPalindrome(num):
        #0 is a palindrome
        if num == 0:
            return True
        #if a number ends with 0 and it is not 0, it is not a palindrome
        #if a number is negative, it cannot be a palindrome
        if (num < 0) or ((num % 10) == 0):
            return False
        reverse = 0

        #reverse half of the integer and store this in variable reverse
        #for even palindromes, reverse is less than num until the halfway point
        #by the halfway point, num and reverse are equal
        #for odd palindromes, reverse will be greater than num because it will contain the middle digit
        #for this case, floor divide one more time
        while num > reverse:
            reverse = (reverse * 10) + (num % 10)
            num = num // 10
        if (num == reverse) or (num == (reverse // 10)):
            return True
        else: 
            return False