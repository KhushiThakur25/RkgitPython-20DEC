def knapsack(weight,values,capacity):
    n = len(weight)
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
    for i in range(1,n+1):
        for w in range(capacity + 1):
            if weight[i-1] <= w:
                include = values[i-1] + dp[i-1][w - weight[i-1]]
                exclude =  dp[i - 1][w]
                dp[i][w] = max(include,exclude)
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]


if __name__ == "__main__":
    weight = [1,3,4,5]
    values = [1,4,5,7]
    capacity = 7
    print(knapsack(weight,values,capacity))