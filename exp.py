import time
print "DIVISION PROGRAM"
num1=raw_input("Enter number1:")
num2=raw_input("Enter number2:")
print "before conversion:n1=%s,n2=%s"%(num1, num2)
try: 
    num1=float(num1)
    num2=float(num2)
    time.sleep(5)
    print "after conversion:n1=%s,n2=%s"%(num1, num2)
    res=num1/num2
    print "result=%s"%res
except ValueError as err:
    print "we are expecting only digits"
except ZeroDivisionError as err:
    print err
    print "b!=0"
except Exception as err:
    print "Invalid input"
    print err
except:
    print "except"
print "thank you"
print "Use me again"