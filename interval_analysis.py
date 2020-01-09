import matplotlib.pyplot as plt

class Interval:
    """
    A class that implements interval analysis. The class is initialized with two
    real numbers that represent the left and the right endpoints:
    parameters:
    left endpoint: real number 
    right endpoint: real number
    """
    
    def __init__(self, left_endpoint, right_endpoint=None):
        """
        initialize the class with two real numbers
        if only one real number is provided, set the right endpoint equals to the left endpoint
        """
        if right_endpoint is None:
            self.left = left_endpoint
            self.right = left_endpoint
        else:
            self.left = left_endpoint
            self.right = right_endpoint
        
    def __add__(self, other_interval):
        """
        method that implements the addition of two intervals
        if the second (right) object is not an Interval instance but a real number 
        we define an addition of an Interval instance and a real number
        """
        if not isinstance(other_interval, Interval):
            left = self.left + other_interval
            right = self.right + other_interval
        else:
            left = self.left + other_interval.left
            right = self.right + other_interval.right
        return Interval(left, right)
    
    def __sub__(self, other_interval):
        """
        method that implements subtraction of two intervals
        """
        if not isinstance(other_interval, Interval):
            left = self.left - other_interval
            right = self.right - other_interval
        else:
            left = self.left - other_interval.right
            right = self.right - other_interval.left
        return Interval(left, right)
    
    def __mul__(self, other_interval):
        """
        method that implements multiplication of two intervals
        """
        if not isinstance(other_interval, Interval):
            L = [self.left*other_interval, self.right*other_interval]
        else:
            L = [
                self.left*other_interval.left, 
                self.left*other_interval.right, 
                self.right*other_interval.left, 
                self.right*other_interval.right
            ]
        left = min(L)
        right = max(L)
        return Interval(left, right)
    
    def __truediv__(self, other_interval):
        """
        method that implements divison of two intervals
        """
        try:
            L = [
                self.left/other_interval.left, 
                self.left/other_interval.right, 
                self.right/other_interval.left, 
                self.right/other_interval.right]
        except ZeroDivisionError:
            raise ZeroDivisionError ("Division by zero is undefined!" + 
                    "Interval {} cannot be denominator.".format(other_interval))
        left = min(L)
        right = max(L)
        return Interval(left, right)
    
    def __radd__(self, val):
        """
        method that implements right addition (the first (left) object is a real nuber (int or float))
        """
        left = self.left + val
        right = self.right + val
        return Interval(left, right)
    
    def __rsub__(self, val):
        """
        method that implements right substitution
        """
        right = val - self.left
        left = val - self.right
        return Interval(left, right)
    
    def __rmul__(self, val):
        """
        method that implements right multiplication
        """
        L = [self.left*val, self.right*val]
        left = min(L)
        right = max(L)
        return Interval(left, right)
    
    def __pow__(self, n):
        """
        method that implements the power function
        n: exponent
        """
        if n%2==1:
            left = self.left**n
            right = self.right**n
        elif n%2==0:
            if self.left >= 0:
                left = self.left**n
                right = self.right**n
            elif self.right < 0:
                left= self.right**n
                right = self.left**n
            else:
                left = 0
                right = max(self.left**n, self.right**n)
        return Interval(left, right)
        
    def __contains__(self, value):
        """
        method for checking if a real value is within the given interval
        value: real number
        """
        if (value >= self.left and value <= self.right):
            return True
        return False
    
    def __repr__(self):
        """
        method for representing an instance of Interval class
        for example:
        print(Interval(3,4)) ---> [3,4]
        """
        return "[{0}, {1}]".format(self.left, self.right)
    
I1 = Interval(1, 4) 
I2 = Interval(-2, -1) 
print("I1 =", I1) # [1, 4]
print("I2 =", I2) # [-2, -1]
print("I1 + I2 =", I1 + I2) # [-1, 3] 
print("I1 - I2 =", I1 - I2)  # [2, 6]
print("I1*I2 =", I1*I2) # [-8, -1]
print("I1/I2 =", I1/I2) # [-4.,-0.5] 

print("\n1 + Interval(2,3) =", 1 + Interval(2,3)) # [3, 4] 
print("Interval(2,3) + 1 =", Interval(2,3) + 1) # [3, 4] 
print("1.0 + Interval(2,3) =", 1.0 + Interval(2,3)) # [3.0, 4.0] 
print("Interval(2,3) + 1.0 =", Interval(2,3) + 1.0) # [3.0, 4.0] 
print("1 - Interval(2,3) =", 1 - Interval(2,3)) # [-2, -1]
print("Interval(2,3) - 1 =", Interval(2,3) - 1) # [1, 2] 
print("1.0 - Interval(2,3) =", 1.0 - Interval(2,3)) # [-2.0, -1.0] 
print("Interval(2,3) - 1.0 =", Interval(2,3) - 1.0) # [1.0, 2.0] 
print("Interval(2,3) * 1 =", Interval(2,3) * 1) # [2, 3] 
print("1 * Interval(2,3) =", 1 * Interval(2,3)) # [2, 3] 
print("1.0 * Interval(2,3) =", 1.0 * Interval(2,3)) # [2.0, 3.0] 
print("Interval(2,3) * 1.0 =", Interval(2,3) * 1.0) # [2.0, 3.0]

x = Interval(-2,2) 
print("\nx =", x) # [-2, 2]
print("x**2 =", x**2) # [0, 4]
print("x**3 =", x**3) # [-8, 8]

xl = [0.001*i for i in range(1001)]
xr = [0.001*i + 0.5 for i in range(1001)]
other_intervals = [Interval(left, right) for left, right in zip(xl, xr)]
other_intervals_poly = [3*I**3 - 2*I**2 - 5*I - 1 for I in other_intervals]

yl = [I.left for I in other_intervals_poly]
yu = [I.right for I in other_intervals_poly]

plt.xkcd(scale=0.5)
plt.figure(figsize=(9,6))
plt.plot(xl, yu, color="green", label="upper boundaries")
plt.plot(xl, yl, color="blue", label="lower boundaries")
plt.xlim(0, 1)
plt.ylim(-10, 4)
plt.xlabel("$x$")
plt.ylabel("$p(I)$")
plt.title("$p(I) = 3I^3 - 2I^2 - 5I - 1 = Interval(x, x+0.5)$", fontsize=14)
plt.legend()
plt.savefig("figure.png")
plt.show()
