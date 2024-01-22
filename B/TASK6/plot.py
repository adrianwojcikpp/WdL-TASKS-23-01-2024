import argparse
import csv
import matplotlib.pyplot as plt

# Function to read data from CSV file
def read_csv(file_path):
    timestamps = []
    values = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row
        for row in csvreader:
            timestamp, value = map(float, row)
            timestamps.append(timestamp)
            values.append(value)
    return timestamps, values

# Function to plot data with lines
def plot_data(timestamps, values, output_file):
    plt.plot(timestamps, values, linestyle='-', marker='o', color='blue')
    plt.title('Data Plot')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.savefig(output_file)
    plt.close()

# Main function
def main():
    parser = argparse.ArgumentParser(description='Plot data from CSV file and save as PNG.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to the input CSV file')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path to the output PNG file')

    args = parser.parse_args()

    timestamps, values = read_csv(args.input)
    plot_data(timestamps, values, args.output)

if __name__ == "__main__":
    main()
