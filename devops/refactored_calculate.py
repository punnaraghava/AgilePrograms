from abc import ABC,abstractmethod
class Operation(ABC):
    @abstractmethod
    def execute(self,a,b):
        pass
class Add(Operation):
    def execute(self,a,b):
        return a+b
class Subtract(Operation):
    def execute(self, a, b):
        return a-b
class Multiply(Operation):
    def execute(self,a,b):
        return a*b
class Divide(Operation):
    def execute(self,a,b):
        if b == 0:
            raise ValueError("Division by zeo!")
        return a/b
class Calculator:
    def __init__(self,operation:Operation):
        self.operation=operation
    def calculate(self,a,b):
        return self.operation.execute(a,b)
if __name__ == "__main__":
    add_calc =Calculator(Add())
    print("10+5=",add_calc.calculate(10,5))
    sub_calc =Calculator(Subtract())
    print("10-5",sub_calc.calculate(10,5))
    mul_calc =Calculator(Multiply())
    print("10*5=",mul_calc.calculate(10,5))
    divide_calc =Calculator(Divide())
    print("10/5",divide_calc.calculate(10,5))
    
        