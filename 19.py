class ValidityCheck:
    def is_valid(self, str1):
        lst, di = [], {"(": ")", "{": "}", "[": "]"}
        for parentheses in str1:
            if parentheses in di:
                lst.append(parentheses)
            elif len(lst) == 0 or di[lst.pop()] != parentheses:
                return False
        return len(lst) == 0


print(ValidityCheck().is_valid("(){}[]"))
print(ValidityCheck().is_valid("()[{)}"))
