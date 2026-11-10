import java.util.PriorityQueue;
import java.util.Comparator;

// Node class for Huffman Tree
class Node {
    char character;
    int frequency;
    Node left, right;

    Node(char character, int frequency) {
        this.character = character;
        this.frequency = frequency;
        this.left = null;
        this.right = null;
    }
}

// Comparator for PriorityQueue
class NodeComparator implements Comparator<Node> {
    @Override
    public int compare(Node firstNode, Node secondNode) {
        return Integer.compare(firstNode.frequency, secondNode.frequency);
    }
}

public class HuffmanCoding {

    // Generate Huffman Codes
    public static void generateCodes(
            Node root, String code, StringBuilder result) {

        if (root == null) {
            return;
        }

        // Leaf node
        if (root.left == null && root.right == null) {
            result            .append(root.character)
                    .append(": ")
                    .append(code)
                    .append("\n");
            return;
        }

        generateCodes(root.left, code + "0", result);
        generateCodes(root.right, code + "1", result);
    }

    // Build Huffman Tree and encode
    public static void huffmanEncode(char[] characters, int[] frequencies) {
        PriorityQueue<Node> priorityQueue = new PriorityQueue<>(new NodeComparator());

        // Create leaf nodes and add them to PriorityQueue
        for (int index = 0; index < characters.length; index++) {
            priorityQueue.add(new Node(characters[index], frequencies[index]));
        }

        // Build the Huffman Tree
        while (priorityQueue.size() > 1) {
            Node leftNode = priorityQueue.poll();
            Node rightNode = priorityQueue.poll();

            Node parentNode = new Node('-', leftNode.frequency + rightNode.frequency);
            parentNode.left = leftNode;
            parentNode.right = rightNode;

            priorityQueue.add(parentNode);
        }

        // Root of the Huffman Tree
        Node root = priorityQueue.poll();

        // Generate and print Huffman Codes
        StringBuilder result = new StringBuilder();
        generateCodes(root, "", result);

        System.out.println(result);
    }

    public static void main(String[] args) {
        char[] characters = { 'a', 'b', 'c', 'd', 'e', 'f' };
        int[] frequencies = { 5, 9, 12, 13, 16, 45 };

        System.out.println("Huffman Codes:");
        huffmanEncode(characters, frequencies);
    }
}