
code = """
for i in range(10):
    x+=i
"""

globals_dict = {"x": 234}
locals_dict = {"x": 0}

exec(code, globals_dict, locals_dict)
print(globals_dict)  # Should print the sum of numbers from 0 to 9
print(locals_dict)  # Should also print the sum of numbers from 0 to 9
print(exec("sqrt = __import__('math').sqrt(16)", globals_dict, locals_dict))  # Should print 4.0
print(locals_dict)  # Should show x as 100