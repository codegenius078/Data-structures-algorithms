def max_profit_recursive(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx+1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profit_recursive(weights, profits, capacity-weights[idx], idx+1)

        return max(option1, option2)


weights_list = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
profits_list = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
capacity = 165

print(max_profit_recursive(weights_list, profits_list, capacity))
