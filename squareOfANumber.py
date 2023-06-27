import math
import re


def check(number):
    pattern = re.compile(r'\d+\.0$')
    temp = math.sqrt(number)
    search = pattern.search(str(temp))

    if search is not None:
        return number

    return None


list1 = [i for i in range(1, 1000)]
list2 = [x for x in list1 if check(x) is not None]
print(list2)
