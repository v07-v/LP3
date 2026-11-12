
import heapq


class Node:
    def __init__(self, character=None, left=None, right=None):
        self.character = character
        self.left = left
        self.right = right


def build_huffman_tree(frequencies):
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
            (left_frequency + right_frequency, order, parent)
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
    n = int(input("Enter number of characters: "))

    if n <= 0:
        print("Number of characters must be positive.")
        return

    frequencies = {}

    print("\nEnter character and frequency:")

    for i in range(n):
        character, frequency = input(
            f"Character {i + 1}: "
        ).split()

        frequency = int(frequency)

        if len(character) != 1 or frequency <= 0:
            print("Enter a single character and positive frequency.")
            return

        if character in frequencies:
            print("Duplicate characters are not allowed.")
            return

        frequencies[character] = frequency

    tree = build_huffman_tree(frequencies)
    codes = generate_codes(tree)

    print("\nCharacter frequencies:")
    for character, frequency in frequencies.items():
        print(f"{character}: {frequency}")

    print("\nHuffman codes:")
    for character, code in codes.items():
        print(f"{character}: {code}")


if __name__ == "__main__":
    main()


# Enter number of characters: 4

# Enter character and frequency:
# Character 1: A 5
# Character 2: B 2
# Character 3: C 3
# Character 4: D 1
