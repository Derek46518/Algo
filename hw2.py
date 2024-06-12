def knapsack(W, weights, values, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    max_value = dp[n][W]
    
    w = W
    items = []
    for i in range(n, 0, -1):
        if max_value <= 0:
            break
        if max_value == dp[i-1][w]:
            continue
        else:
            items.append(i)
            max_value -= values[i-1]
            w -= weights[i-1]

    items.reverse()
    return dp[n][W], items

def main():
    while True:
        W = int(input().strip())
        if W == 0:
            break
        n = int(input().strip())
        weights = []
        values = []
        for _ in range(n):
            weight, value = map(int, input().strip().split())
            weights.append(weight)
            values.append(value)

        total_value, items = knapsack(W, weights, values, n)
        print(f"Total Value = {total_value}")
        print("Items = ", end="")
        print(", ".join(map(str, items)), end="")
        print("\n")

if __name__ == "__main__":
    main()