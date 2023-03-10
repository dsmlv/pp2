import time
import math

def delayed_sqrt(num, delay_ms):
    time.sleep(delay_ms / 1000) 
    return math.sqrt(num)


result = delayed_sqrt(25100, 2123) 
print(result)