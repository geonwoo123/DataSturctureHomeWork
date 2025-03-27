from typing import List, Optional
import logging

class Stack:
    def __init__(self,capacity = 10):
        self.capacity = capacity
        self.arr:List[Optional[int]] = [None] * capacity
        self.top = -1

    def __len__(self):
        return self.top+1

    def empty(self):
        return self.top == -1

    def full(self):
        if self.top +1 >= self.capacity:
            return True
        return False

    def push(self,data:int):
        if self.full():
            raise IndexError("push from full stack")
        self.top += 1
        self.arr[self.top] = data

    def pop(self):
        if self.empty():
            raise IndexError("stack is empty")
        data = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return data

    def peek(self):
        if self.empty():
            raise IndexError("stack is empty")
        return self.arr[self.top]                    
    
    def __repr__(self):
        return str(self.arr[:self.top+1])
    
    def infix_to_postfix(expr: str) -> str:
        OPS = {"+", "-", "*", "/", "^", "(", ")"}
        PREC = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, None: -9}
        stack = Stack(len(expr))
        ret = []
        for ch in expr:
            if '0' <= ch <= '9':
                ret.append(ch)
            elif ch == "(":
                stack.push(ch)
            elif ch == ")":
                while not stack.empty() and stack.peek() != "(":
                    ret.append(stack.pop())
                stack.pop()
            elif ch in OPS:
                while not stack.empty() and PREC.get(stack.peek(), -1) >= PREC[ch]:
                    ret.append(stack.pop())
                stack.push(ch)
        
        while not stack.empty():
            ret.append(stack.pop())
        return "".join(ret)
        
    
class PostFixEval:
    OPS = ("+", "-", "*", "/")

    def __init__(self,expr):
        self.expr = expr

    def eval(self):
        stack = Stack(len(self.expr))
        for tok in self.expr:
            if tok in self.OPS:
                if len(stack)<2:
                    raise ValueError("not enough to pop in stack")
                v02 = stack.pop()
                v01 = stack.pop()
                result = self.cal(tok,v01,v02)
                stack.push(result)
            else:
                stack.push(int(tok))
        if not stack.empty():
            return stack.pop()
        raise ValueError("POSTFIX ERROR")            

    def cal(self,op,v01,v02):
        if op == "+":
            return v01+v02
        elif op=="-":
            return v01-v02
        elif op=="*":
            return v01*v02
        elif op=="/":
            if v02==0:
                raise ZeroDivisionError("Div 0 is error")
            return v01//v02

    
        
    
if __name__ == "__main__":
    expr = "1*(2+3)*4"
    postfix = Stack.infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1*2+3*4"
    postfix = Stack.infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1+2*3"
    postfix = Stack.infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1*2+3"
    postfix = Stack.infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1+(2*3+4)*5"
    postfix = Stack.infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    
        