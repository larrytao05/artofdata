# Create a ComplexNumber class with a constructor method.
class ComplexNumber:
    def __init__(self, i, r) -> None:
        self.i = i
        self.r = r
    
    def add(self, num):
        return ComplexNumber(self.i + num.i, self.r + num.r)
    
    def sub(self, num):
        return ComplexNumber(self.i - num.i, self.r - num.r)

    def mult(self, num):
        return ComplexNumber(((self.i*num.r) + (self.r * num.i)), ((self.r*num.r) - (self.i*num.i)))

    def div(self, num):
        return ComplexNumber(self.mult(ComplexNumber(-num.i, num.r)).i / (num.r^2 + num.i^2), self.mult(ComplexNumber(-num.i, num.r)).r / (num.r^2 + num.i^2))

    def __str__(self) -> str:
        return str(self.r) + " + " + str(self.i) + "i"

num1 = ComplexNumber(5, 4)
num2 = ComplexNumber(2, 10)
print(num1)
print(num2)
print(num1.add(num2))
print(num1.sub(num2))
print(num1.mult(num2))
print(num1.div(num2))


class DataFrame:
    def __init__(self, rows, columns) -> None:
        self.rows = rows
        self.columns = columns
        self.values = {}
        for i in rows:
            for j in columns:
                self.values[(i, j)] = None

    def __init__(self, values) -> None:
        self.values = values
        

    
    def insert(self, value, row, column):
        coords = (row, column)
        self.values[coords] = value
    
    def remove(self, row, column):
        value = self.values[(row, column)]
        self.values[(row, column)] = None
        return value

        
    
