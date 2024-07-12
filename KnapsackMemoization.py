def knapsack(weight,values,capacity):
    n = len(weight)
    memo = [[-1 for i in range(capacity + 1)] for j in range(n)]
    return knapsack_recursive(weight, values,capacity,n-1,memo)

def knapsack_recursive(weight, values,capacity,index,memo):
    if index < 0 or capacity == 0:
        return 0
    if memo[index][capacity] != -1:
        return memo[index][capacity]
    if weight[index] > capacity:
        memo[index][capacity] = knapsack_recursive(weight,values,capacity,index-1,memo)
    else:
        exclude = knapsack_recursive(weight,values,capacity,index-1,memo)
        include = values[index] + knapsack_recursive(weight,values,capacity - weight[index],index-1,memo)
        memo[index][capacity] = max(exclude,include)
    return memo[index][capacity] 


if __name__ == "__main__":
    weight = [1,3,4,5]
    values = [1,4,5,7]
    capacity = 7
    print(knapsack(weight,values,capacity))