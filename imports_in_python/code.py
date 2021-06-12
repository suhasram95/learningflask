def divide(dividend, divisor):
    try:
        average = dividend / divisor
    except ZeroDivisionError as e:
        raise e
    return average

print (divide(7, 0))