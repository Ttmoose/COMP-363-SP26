import heapq
from collections import defaultdict
from pympler import asizeof
from node import Node

class HuffmanCoding:
    def __init__(self):
        self.codes = {}
        self.reverse_mapping = {}

    def build_frequency_table(self, text: str) -> dict:
        """Build frequency table for the input text."""
        freq = defaultdict(int)
        for char in text:
            freq[char] += 1
        return freq

    def build_huffman_tree(self, freq_table: dict) -> Node:
        """Build Huffman tree using the Node class."""
        heap = [Node(symbol, freq) for symbol, freq in freq_table.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = Node(None, left.get_frequency() + right.get_frequency())
            merged.set_left(left)
            merged.set_right(right)
            heapq.heappush(heap, merged)

        return heap[0]

    def generate_codes(self, root: Node, current_code: str = ""):
        """Generate Huffman codes by traversing the tree."""
        if root.is_leaf():
            self.codes[root.get_symbol()] = current_code
            self.reverse_mapping[current_code] = root.get_symbol()
            return

        if root.has_left():
            self.generate_codes(root.get_left(), current_code + "0")
        if root.has_right():
            self.generate_codes(root.get_right(), current_code + "1")

    def encode(self, text: str) -> tuple[str, Node]:
        """Encode the input text into a binary string."""
        freq_table = self.build_frequency_table(text)
        root = self.build_huffman_tree(freq_table)
        self.generate_codes(root)

        encoded_text = "".join(self.codes[char] for char in text)
        return encoded_text, root

    def decode(self, encoded_text: str, root: Node) -> str:
        """Decode the binary string back into the original text."""
        current_node = root
        decoded_text = []

        for bit in encoded_text:
            current_node = current_node.get_left() if bit == "0" else current_node.get_right()
            if current_node.is_leaf():
                decoded_text.append(current_node.get_symbol())
                current_node = root

        return "".join(decoded_text)

    def measure_efficiency(self, text: str, encoded_text: str, root: Node) -> dict:
        """Measure the efficiency of Huffman encoding."""
        original_bits = len(text) * 8
        encoded_bits = len(encoded_text)
        tree_size = asizeof.asizeof(root)

        return {
            "original_bits": original_bits,
            "encoded_bits": encoded_bits,
            "tree_size_bits": tree_size * 8,
            "total_bits": encoded_bits + tree_size * 8,
            "space_saved": original_bits - (encoded_bits + tree_size * 8)
        }

# Example Usage
if __name__ == "__main__":
    text = "HELLO WORLD"
    huffman = HuffmanCoding()
    encoded_text, root = huffman.encode(text)
    decoded_text = huffman.decode(encoded_text, root)
    efficiency = huffman.measure_efficiency(text, encoded_text, root)

    print("Original Text:", text)
    print("Encoded Text:", encoded_text)
    print("Decoded Text:", decoded_text)
    print("Efficiency:", efficiency)