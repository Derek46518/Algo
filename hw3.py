import heapq

# 定義樹節點
class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    # 定義比較函數
    def __lt__(self, other):
        return self.freq < other.freq

# 建立霍夫曼樹
def build_huffman_tree(frequencies):
    heap = [Node(freq, char) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

# 生成霍夫曼編碼
def generate_huffman_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node.char is not None:
        codebook[node.char] = prefix

    if node.left:
        generate_huffman_codes(node.left, prefix + "0", codebook)
    if node.right:
        generate_huffman_codes(node.right, prefix + "1", codebook)

    return codebook

# 解碼二元碼
def decode_huffman_code(encoded_str, root):
    decoded_str = ""
    node = root

    for bit in encoded_str:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char:
            decoded_str += node.char
            node = root

    return decoded_str

def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break

        frequencies = {}
        for _ in range(n):
            char, freq = input().strip().split()
            frequencies[char] = int(freq)

        encoded_str = input().strip()

        # 建立霍夫曼樹
        huffman_tree_root = build_huffman_tree(frequencies)
        # 生成霍夫曼編碼
        huffman_codes = generate_huffman_codes(huffman_tree_root)

        for char, code in sorted(huffman_codes.items()):
            print(f"{char} = {code}")

        # 解碼
        decoded_str = decode_huffman_code(encoded_str, huffman_tree_root)
        print(f"Decode = {decoded_str}\n")

if __name__ == "__main__":
    main()