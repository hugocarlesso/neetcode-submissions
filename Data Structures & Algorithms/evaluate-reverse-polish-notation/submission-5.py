class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = set({"+", "-", "*", "/"})
        stack = []
        for token in tokens[:]:
            if token not in operators:
                stack.append(int(token))
            else:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    b,a = stack.pop(), stack.pop()
                    stack.append(a-b) 
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                elif token == "/":
                    b,a= stack.pop(), stack.pop()
                    stack.append(int(a /b))
        return stack[0]

                
                


        

        