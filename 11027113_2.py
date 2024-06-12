def knapsack(W, weights, values, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    items = [[[] for _ in range(W+1)] for _ in range(n+1)]
    
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                if values[i-1] + dp[i-1][w-weights[i-1]] > dp[i-1][w]:
                    dp[i][w] = values[i-1] + dp[i-1][w-weights[i-1]]
                    items[i][w] = items[i-1][w-weights[i-1]] + [i]
                else:
                    dp[i][w] = dp[i-1][w]
                    items[i][w] = items[i-1][w]
            else:
                dp[i][w] = dp[i-1][w]
                items[i][w] = items[i-1][w]
                
    return dp[n][W], sorted(items[n][W])

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
