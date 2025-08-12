x= 100
y= 200  
z= 300
print(locals())
print(globals())    

print(globals().get("z"))
globals()["z"] = 400
print(globals().get("z"))
print(z)
globals().clear()
print(globals().get("z"))  # This will return None since globals are cleared
globals()["user"] = type("User", (object, ), {"name": "Brandon"})  # This will raise a KeyError since globals are cleared

print(globals().get("user")().name)  # This will return None since globals are cleared

locals()["x"] = 500
print(locals().get("x"))  # This will return 500 since we set it
print(x)
locals()["__file__"] = None
globals()["__file__"] = None
print(__file__)  # This will raise a NameError since __file__ is not defined