from typing import List, Optional
import logging

class Stack:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.top = -1

    def __len__(self):
        return self.top + 1

    def empty(self):
        return self.top == -1

    def full(self):
        return len(self) == self.capacity

    def __repr__(self):
        return str(self.arr[:len(self)])

    def push(self, data:int):
        if self.full():
            raise IndexError("push from full stack")
        self.arr[self.top + 1] = data
        self.top += 1

    def peek(self):
        if self.empty():
            raise IndexError("peek from empty stack")
        return self.arr[self.top]

    def pop(self):
        if self.empty():
            raise IndexError("error")
        value = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return value
    
def infix_to_postfix(expr: str) -> str:
    OPS = {"+", "-", "*", "/", "^", "(", ")"}
    PREC = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, None: -9}
    stack = Stack(len(expr))
    ret = []
    #일단 숫자면 ret에 바로 넣기 ret이 최종 답임
    for chr in expr:
        if chr.isdigit():
            ret.append(chr)
        #"("면 그냥 스택에 넣기기
        elif chr == "(":
            stack.push(chr)
        #chr이 ")"면 현재 스택에 있는 값들을 전부 ret에 넣는데 만약 stack.peek()즉 계속 빼서 ret에 넣는과정에서 스택의 맨 윗값 즉 stack.peek()
        #값이 "("이면 넣는과정을 끝break해주고 그럼 아직 스택에 "("가 남아있으니 while문 밖에서 stack.pop()한번 해주면서 "("까지 빼주기기
        elif chr == ")":
            while not stack.empty():
                if stack.peek() == "(":
                    break
                else:
                    ret.append(stack.pop())
            stack.pop()

        #만약 연산자라면 우선순위를 봐야하는데 현재 스택에 있는 연산자의 우선순위가 현 chr의 연산자의 우선순위보다 낮으면 그냥 스택에 넣고
        # 스택에 있는 연산자의 우선순위가 현 chr의 연산자의 우선순위보다 높으면 스택에 있는 연산자를 pop하고 그 값을 ret에 넣고 현 chr의 연산자는
        # 스택에 넣는다.
        elif chr in OPS:
            while not stack.empty() and stack.peek() != "(" and PREC[stack.peek()] >= PREC[chr]:
                ret.append(stack.pop())
            stack.push(chr)

    #마지막으로 스택에 있는것들을 전부 ret에 넣어주기
    while not stack.empty():
        ret.append(stack.pop())
    
    return "".join(ret) 
    
class PostFixEval:
    OPS = ("+", "-", "*", "/")

    def __init__(self, expr):
        self.expr = expr

    def eval(self):
        stack = Stack(len(self.expr))
        for tok in self.expr:
            if tok.isdigit():
                stack.push(int(tok))
            else:
                v02 = int(stack.pop())
                v01 = int(stack.pop())
                stack.push(self.cal(tok, v01, v02))
        return stack.peek()        

    def cal(self, op ,v01:int, v02:int):
        ret = 0
        if op == "+":
            ret = v01 + v02

        elif op == "-":
            ret = v01 - v02

        elif op == "*":
            ret = v01 * v02

        elif op == "/":
            if v02 != 0:
                ret = v01 / v02 #교수님은 정수만 계산하는걸로 말하셨는데 진짜 정확히 계산을 한다고고 하자면 그냥 /이 맞는건가요?

        return ret
    



if __name__ == "__main__":
    expr = "1*(2+3)*4"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1*2+3*4"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1+2*3"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1*2+3"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")
    expr = "1+(2*3+4)*5"
    postfix = infix_to_postfix(expr)
    print(f"{expr} => {postfix}")

#왜 cal매서드안에서 내재적 함수인 eval()을 사용하지않는것이 좋을까?
#먼저 성능적으로 보면 eval()함수를 사용하면 문자열을 해석해서 실행하는 단계가 들어가기때문에 직접 연산하는것보다 느립니다.
#그리고 오류가 났을때 cal매서드를 통해서 하나하나 구현했을경우 어디서 오류가 났는지 확인을 할 수 있지만 eval()함수를 사용하면 어디서 어떻게 오류가 났는지 명확히 알수가 없습니다.
#가장 큰 이유는 보안 문제로 eval()은 문자열을 실행하는 개념이기에 혹시 후위수식이 아닌 코드나 시스템에 문제를 일으키는 문자열이 입력되었을때 문제가 발생할수 있습니다.    



                

