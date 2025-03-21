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
        else:
            return False


    def push(self,data:int):
        if self.full():
            raise IndexError("push from full stack")
        else:
            self.top += 1
            self.arr[self.top] = data

    def pop(self):
        if self.empty():
            raise IndexError("stack is empty")
        else:
            data = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
        return data



    def peek(self):
        if self.empty():
            raise IndexError("stack is empty")
        else:
            return self.arr[self.top]                    
    
        
                

    def __repr__(self):
        return str(self.arr[:self.top+1])
        
    

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
    logging.basicConfig(level=logging.DEBUG)
    try:
        expr = "6523+8*+3+*"
        postfix = PostFixEval(expr)
        res = postfix.eval()
        logging.info(f"PostFix({expr}).eval = {res}")
        expr = "34*25*+"
        postfix = PostFixEval(expr)
        res = postfix.eval()
        logging.info(f"PostFix({expr}).eval = {res}")
    except Exception as e:
        logging.exception(e)
        
                
           
