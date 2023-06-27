def reverse_equation(S):
    reversed_list = []
    reversed_equation = ''

    for i in S:
        if i == '-' or i == '/' or i == '*' or i == '+':
            reversed_list.append(reversed_equation)
            reversed_list.append(i)
            reversed_equation = ''
        else:
            reversed_equation = reversed_equation + i

    reversed_list.append(reversed_equation)

    return ''.join(reversed_list[::-1])


print(reverse_equation('20-3+5*2'))
