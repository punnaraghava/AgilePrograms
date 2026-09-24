class Calculator:
    def calculate(self,a,b,operation):
     if operation == "add":
         return a+b
     elif operation == "subtract":
         return a-b
     elif operation == "multiply":
         return a*b
     elif operation == "divide":
         if b == 0:
             raise ValueError("Division by zero!")
         return a/b
     else:
         raise ValueError("Invalidoperation")
#example usage
if __name__ == "__main__":
 calc = Calculator()
print("10+5=",calc.calculate(10,5,"add"))
print("10-5=",calc.calculate(10,5,"subtract"))
print("10*5=",calc.calculate(10,5,"multiply"))
print("10/5=",calc.calculate(10,5,"divide"))
             
         
        