import heapq
from collections import Counter


class Node:
    def __init__(self, character=None, left=None, right=None):
        self.character = character
        self.left = left
        self.right = right


def build_huffman_tree(text):
    frequencies = Counter(text)
    heap = []
    order = 0

    for character, frequency in frequencies.items():
        heapq.heappush(heap, (frequency, order, Node(character)))
        order += 1

    while len(heap) > 1:
        left_frequency, _, left_node = heapq.heappop(heap)
        right_frequency, _, right_node = heapq.heappop(heap)

        parent = Node(left=left_node, right=right_node)
        heapq.heappush(
            heap,
            (left_frequency + right_frequency, order, parent),
        )
        order += 1

    return heap[0][2]


def generate_codes(node, code="", codes=None):
    if codes is None:
        codes = {}

    if node.character is not None:
        codes[node.character] = code or "0"
        return codes

    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)
    return codes


def main():
    text = input("Enter text to encode: ")

    if not text:
        print("Please enter at least one character.")
        return

    tree = build_huffman_tree(text)
    codes = generate_codes(tree)
    encoded_text = "".join(codes[character] for character in text)

    print("\nCharacter frequencies:")
    for character, frequency in Counter(text).items():
        print(f"{repr(character)}: {frequency}")

    print("\nHuffman codes:")
    for character, code in codes.items():
        print(f"{repr(character)}: {code}")

    print("\nEncoded text:")
    print(encoded_text)


if __name__ == "__main__":
    main()


# Sample input:
# hello huffman
#
# The program displays character frequencies, Huffman codes,
# and the encoded binary text.
