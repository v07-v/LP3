class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def get_max_value(items, capacity):
    items.sort(key=lambda item: item.value / item.weight, reverse=True)
    total_value = 0.0

    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.value * capacity / item.weight
            break

    return total_value


def main():
    item_count = int(input("Enter the number of items: "))
    items = []

    for index in range(item_count):
        value, weight = map(
            int,
            input(
                f"Enter value and weight for item {index + 1}: "
            ).split(),
        )
        if weight <= 0:
            print("Weight must be greater than zero.")
            return
        items.append(Item(value, weight))

    capacity = int(input("Enter the knapsack capacity: "))
    if capacity < 0:
        print("Capacity cannot be negative.")
        return

    maximum_value = get_max_value(items, capacity)
    print(f"Maximum value we can obtain = {maximum_value:.2f}")


if __name__ == "__main__":
    main()


# Sample input:
# 3
# 60 10
# 100 20
# 120 30
# 50
