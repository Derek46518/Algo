def lis(arr):
    n = len(arr)
    lis = [1] * n
    prev_index = [-1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                prev_index[i] = j

    max_length = max(lis)
    max_index = lis.index(max_length)

    lis_sequence = []
    while max_index != -1:
        lis_sequence.append(arr[max_index])
        max_index = prev_index[max_index]
    
    lis_sequence.reverse()

    return max_length, lis_sequence

def main():
    while True:
        input_line = input().strip()
        if input_line == '0':
            break

        arr = list(map(int, input_line.split()))
        length, sequence = lis(arr)
        print(f"Length of LIS = {length}")
        print("LIS = <", end="")
        print(", ".join(map(str, sequence)), end="")
        print(">\n")

if __name__ == "__main__":
    main()