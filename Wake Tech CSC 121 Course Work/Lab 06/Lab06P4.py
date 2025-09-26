# Nathanael Long
# 09/26/2025
# Problem 4 - MATPLOTLIB (It's not a Line Graph, it's a Bar Graph)

# Problem says at the start that this is going to make a Line Graph but then asks us for a Bar Graph.

def main():

    """
    This is a function that creates and displays a bar graph using matplotlib
    from provided input for titles, labels, and data to be plotted.

    Steps performed:
    1. Prompts the user for a graph title.
    2. Prompts the user for labels for the x-axis and y-axis.
    3. Prompts the user for the number of data points to plot.
    4. Collects user-entered labels (x-axis) and values (y-axis).
    5. Plots a bar graph with the given data.
    6. Displays the graph and then the program ends.

    """

    import matplotlib.pyplot as plt

    # Ask for the graph's title
    print("\n Step A : ")
    title = input("Please enter the bar graph title : ")

    # Ask for the axis labels
    print("\n Step B : ")
    x_label = input("Please enter the label for the x-axis : ")
    y_label = input("Please enter the label for the y-axis : ")

    # Ask for the number of data points
    print("\n Step C : ")
    n = int(input("Please enter the number of data points : "))

    # Get the labels and values
    print("\n Step D : ")
    labels = []
    values = []
    for data in range(1, n + 1):
        label = input(f"Please enter the label for X Axis #{data}: ")
        value = float(input(f"Please enter the value for Y Axis #{data}: "))
        labels.append(label)
        values.append(value)

    # Plot the bar graph
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Show the bar graph and terminate the program
    print("\n Goodbye! ")
    plt.show()

main()