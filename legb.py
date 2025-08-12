
def add(num1, num2):
    
    def multiply(x, y):
        print(locals())
        return x * y
        
    print(locals().get("multiply")(num1, num2))
    
    return num1 + num2

print(add(10, 20))
