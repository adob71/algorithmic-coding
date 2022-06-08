#usage
#python3 balanced-parentheses.py
#output
#{[]{()}}
#Balanced
#[{}{})(]
#Unbalanced
#((()
#Unbalanced

#functions

def check(myStr):
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []
    for i in myStr:
#        print("stack:", stack)
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

#driver code

string = "{[]{()}}"
print(string)
print(check(string))

string = "[{}{})(]"
print(string)
print(check(string))

string = "((()"
print(string)
print(check(string))

