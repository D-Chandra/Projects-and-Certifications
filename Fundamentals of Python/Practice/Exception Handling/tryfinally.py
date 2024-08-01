try:
    a = 10
    a = a+20
except ValueError as i:
    print(i)
else:
    print("In the else block")
finally:
    print("Successful Excution")