import java.util.Arrays;
import java.util.Comparator;

class Item {
    int itemValue, itemWeight;

    Item(int itemValue, int itemWeight) {
        this.itemValue = itemValue;
        this.itemWeight = itemWeight;
    }
}
public class FractionalKnapsack {

    static double getMaxValue(Item[] items, int capacity) {

        // Sort items by value-to-weight ratio in descending order
        Arrays.sort(items, new Comparator<Item>() {
            @Override
            public int compare(Item firstItem, Item secondItem) {
                double firstRatio = (double) firstItem.itemValue / firstItem.itemWeight;
                double secondRatio = (double) secondItem.itemValue / secondItem.itemWeight;

                return Double.compare(secondRatio, firstRatio);
            }
        });
        double totalValue = 0.0;

        for (Item item : items) {
            if (capacity >= item.itemWeight) {
                // Take the whole item
                capacity -= item.itemWeight;
                totalValue += item.itemValue;
            } else {
                // Take the fractional part of the item
                totalValue += item.itemValue
                        * ((double) capacity / item.itemWeight);
                break;
            }
        }

        return totalValue;
    }
    public static void main(String[] args) {
        Item[] items = {
                new Item(60, 10),
                new Item(100, 20),
                new Item(120, 30)
        };
        int capacity = 50;

        double maxValue = getMaxValue(items, capacity);

        System.out.println(
                "Maximum value we can obtain = " + maxValue);
    }
}