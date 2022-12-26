# 简单的栈括号问题 但是每次访问栈顶的时候需要检查是否为空

def isValid(s: str) -> bool:
        stack = []
        parenthesesDict = {')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in ['(','[','{']:
                stack.append(ch)
            else:
                # 需要注意 stack是否为空
                if stack and parenthesesDict[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
        if len(stack):
            return False
        else:
            return True

isValid('()[]{}')