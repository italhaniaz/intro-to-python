class Stack:
    def __init__(self):
        self.l = []

    def push(self, val):
        self.l.append(val)

    def pop(self):
        return self.l.pop()

    def peak(self):
        return self.l[-1]

    def is_empty(self):
        if len(self.l) == 0:
            return True
        else:
            return False

class Calculator:
    def __init__(self):
        self.results_lst = []
    
    def addition(self, num1, num2):
        is_str = isinstance(num1, str) or isinstance(num2, str)
        if is_str:
            raise TypeError("Given datatype incorrect")
        
        result = num1 + num2
        return result
    
    def subtraction(self, num1, num2):
        is_str = isinstance(num1, str) or isinstance(num2, str)
        if is_str:
            raise TypeError("Given datatype incorrect")
            
        result = num1 - num2
        return result

    def multiplication(self, num1, num2):
        is_str = isinstance(num1, str) or isinstance(num2, str)
        if is_str:
            raise TypeError("Given datatype incorrect")
            
        result = num1 * num2
        return result

    def division(self, num1, num2):
        is_str = isinstance(num1, str) or isinstance(num2, str)
        if is_str:
            raise TypeError("Given datatype incorrent")

        if num2 == 0:
            raise ZeroDivisionError("Cannot divide with zero")

        result = num1 / num2
        return result

    def show_history(self):
        if not self.results_lst:
            print("--Empty--")
            return 

        # prints all results except last one
        stop_at_sec_last = -1
        for i in self.results_lst[:stop_at_sec_last]:
            print("Previos result: ", i)

        print("recnet result --> ", self.results_lst[-1])



    # Evaluate fuction for only one exp
    def evaluate(self, exp):
        if not exp:
            return None

        exp_stack = Stack()

        # pushing the first element
        exp_stack.push(exp[0])

        # calculated values of mul and div and pushing it.
        for current in exp[1:]:
            if exp_stack.peak() == '*' or exp_stack.peak() == '/':
                operator = exp_stack.pop()
                previous_val = exp_stack.pop()
                
                if operator == '*':
                    calculated_val = self.multiplication(int(previous_val), int(current))
                if operator == '/':
                    calculated_val = self.division(int(previous_val), int(current))

                exp_stack.push(calculated_val)
                    
            else:
                exp_stack.push(current)

        # print(exp_stack)
            
        while exp_stack:
            current = exp_stack.pop()
            
            # if pop and stack is empty so current is my final result.
            stack_is_empty = exp_stack.is_empty()
            if stack_is_empty:
                self.results_lst.append(current)
                calculated_val = int(current)
                break
            
            if exp_stack.peak() == '+' or exp_stack.peak() == '-':
                operator = exp_stack.pop()
                previous_val = exp_stack.pop()
                
                if operator == '+':
                    calculated_val = self.addition(int(previous_val), int(current))
                if operator == '-':
                    calculated_val = self.subtraction(int(previous_val), int(current))

                exp_stack.push(calculated_val)

        return calculated_val


    def infix_to_postfix(self, infix_exp):
        prec = {
            '*' : 3,
            '/' : 3,
            '+' : 2,
            '-' : 2,
            '(' : 1
        }

        op_stack = Stack()
        postfix_list = []
        token_list = infix_exp.split()

        for token in token_list:
            if token in '0123456789':
                postfix_list.append(token)
            elif token == '(':
                op_stack.push(token)
            elif token == ')':
                top_token = op_stack.pop()
                while top_token != '(':
                    postfix_list.append(top_token)
                    top_token = op_stack.pop()
            else:
                while (not op_stack.is_empty()) and (prec[op_stack.peak()] >= prec[token]):
                    postfix_list.append(op_stack.pop())
                op_stack.push(token)

        while not op_stack.is_empty():
            postfix_list.append(op_stack.pop())

        return " ".join(postfix_list)


    def postfix_eval(self, postfix_exp):
        operand_stack = Stack()
        token_list = postfix_exp.split()

        for token in token_list:
            if token in '0123456789':
                operand_stack.push(int(token))
            else:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = self.do_math(token, operand1, operand2)
                operand_stack.push(result)

        result = operand_stack.pop()
        return result

    def do_math(self, op, num1, num2):
        if op == '*':
            result = self.multiplication(num1, num2)
        elif op == '/':
            result = self.division(num1, num2)
        elif op == '+':
            result = self.addition(num1, num2)
        else:
            result = self.subtraction(num1, num2)

        return result


if __name__ == "__main__":
    c = Calculator()

    print("postfix exp evaluation")
    postfix_exp = c.infix_to_postfix("( 4 + 2 ) * ( 2 + 2 )")
    result = c.postfix_eval(postfix_exp)
    print(result)