class Solution:
    def isPalindrome(self, number: int) -> bool:
        
        str_number = str(number)

        if str_number[::-1] == str_number:
            return True
        else:
            return False

