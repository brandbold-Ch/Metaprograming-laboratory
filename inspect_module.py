import inspect

current_frame = inspect.currentframe()
print("Current frame:", current_frame)
print(current_frame.f_back)
print(current_frame.f_builtins)
print(current_frame.f_code.co_cellvars)
print(current_frame.f_code.co_names)
print(current_frame.f_globals)
print(current_frame.f_locals)
print(current_frame.f_lasti)
print(current_frame.f_lineno)
print(current_frame.f_trace)
print(current_frame.f_trace_lines)
print(current_frame.f_trace_opcodes)
print(current_frame.f_code.co_filename)
print(current_frame.f_code.co_name)
print(current_frame.f_code.co_consts)
print(current_frame.f_code.co_stacksize)

def a():
    b()
    
def b():
    c()
     
def c():
    stack = inspect.stack()
    print("Stack trace:")
    for frame_info in stack:
        print(f"Function: {frame_info.function}, Line: {frame_info.lineno}, File: {frame_info.filename}")

a()

def change_context():
    frame = inspect.currentframe().f_back
    exec("x=x+100", frame.f_globals, frame.f_locals)
    print(frame.f_locals)
    
    
def test():
    x = 134
    change_context()
    print("x = ", x)

test()
