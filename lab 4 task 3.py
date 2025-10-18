class Power:
    def __init__(self, x, n):
        self.x = x
        self.n = n
def calculate(self):
        result = 1
        if self.n > 0:
            for i in range(self.n):
                result *= self.x
        elif self.n < 0:
            for i in range(-self.n):
                result *= self.x
            result = 1 / result
        else:
            result = 1
        return result
x = float(input("Enter the base number (x): "))
n = int(input("Enter the power (n): "))

power_obj = Power(x, n)
print(f"{x} raised to the power {n} is: {power_obj.calculate()}")
