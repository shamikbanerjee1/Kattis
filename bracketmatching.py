n=int(input())
arr=input()
open_brackets=['[','{','(']
closed_brackets=[']','}',')']
stack=[]
if n%2!=0 or arr[0] in closed_brackets or arr[-1] in open_brackets:
    print('Invalid')
else:
    for bracket in arr:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in closed_brackets:
            if len(stack)>0:
                if bracket==']':
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        break
                elif bracket=='}':
                    if stack[-1]=='{':
                        stack.pop()
                    else:
                        break
                elif bracket==')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        break
            else:
                break
    if len(stack)==0:
        print('Valid')
    else:
        print('Invalid')