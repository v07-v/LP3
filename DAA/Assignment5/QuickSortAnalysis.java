import java.util.Random;

public class QuickSortAnalysis {

    // Deterministic QuickSort
    public static void deterministicQuickSort(
            int[] array, int low, int high) {

        if (low < high) {
            int pivotIndex = partition(array, low, high);

            deterministicQuickSort(array, low, pivotIndex - 1);
            deterministicQuickSort(array, pivotIndex + 1, high);
        }
    }

    // Randomized QuickSort
    public static void randomizedQuickSort(
            int[] array, int low, int high) {

        if (low < high) {
            int pivotIndex = randomizedPartition(array, low, high);

            randomizedQuickSort(array, low, pivotIndex - 1);
            randomizedQuickSort(array, pivotIndex + 1, high);
        }
    }

    // Partition function for deterministic QuickSort
    private static int partition(int[] array, int low, int high) {

        int pivotValue = array[high];
        int smallerElementIndex = low - 1;

        for (int currentIndex = low; currentIndex < high; currentIndex++) {
            if (array[currentIndex] <= pivotValue) {
                smallerElementIndex++;
                swap(array, smallerElementIndex, currentIndex);
            }
        }

        swap(array, smallerElementIndex + 1, high);
        return smallerElementIndex + 1;
    }

    // Partition function for randomized QuickSort
    private static int randomizedPartition(
            int[] array, int low, int high) {

        Random rand = new Random();

        int randomPivotIndex =
                low + rand.nextInt(high - low + 1);

        swap(array, randomPivotIndex, high);

        return partition(array, low, high);
    }

    // Utility function to swap elements
    private static void swap(int[] array, int firstIndex, int secondIndex) {
        int temporaryValue = array[firstIndex];
        array[firstIndex] = array[secondIndex];
        array[secondIndex] = temporaryValue;
    }

    // Function to print the array
    private static void printArray(int[] array) {
        for (int value : array) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {

        int[] originalArray = {10, 7, 8, 9, 1, 5};
        int elementCount = originalArray.length;

        System.out.println("Original Array:");
        printArray(originalArray);

        // Deterministic QuickSort
        int[] deterministicArray = originalArray.clone();

        long startTime = System.nanoTime();

        deterministicQuickSort(deterministicArray, 0, elementCount - 1);

        long endTime = System.nanoTime();

        System.out.println(
                "Sorted Array using Deterministic QuickSort:");
        printArray(deterministicArray);

        System.out.println(
                "Time taken by Deterministic QuickSort: "
                + (endTime - startTime) + " ns");

        // Randomized QuickSort
        int[] randomizedArray = originalArray.clone();

        startTime = System.nanoTime();

        randomizedQuickSort(randomizedArray, 0, elementCount - 1);

        endTime = System.nanoTime();

        System.out.println(
                "Sorted Array using Randomized QuickSort:");
        printArray(randomizedArray);

        System.out.println(
                "Time taken by Randomized QuickSort: "
                + (endTime - startTime) + " ns");
    }
}