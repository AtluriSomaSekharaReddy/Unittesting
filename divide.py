def divide(x,y):
    if y==0:
        raise ValueError("U cant divide number by 0")
    elif type(x) and type(y) not in [int,float]:
        raise ValueError("Please enter int or float values")
    else:
        return x/y 
print(divide(0,22))