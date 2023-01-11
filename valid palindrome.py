#주어진 문자열이 회문인지 확인. 대소문자를 구분하지 않으며 영문자와 숫자만을 대상으로 한다.

class Solution(object):
    def isPalindrome(self, s):
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True