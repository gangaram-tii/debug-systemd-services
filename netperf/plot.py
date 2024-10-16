import json
import matplotlib.pyplot as plt

def parse_iperf3_log(file_path):
    """Parse the iperf3 log file and return times and bitrates."""
    with open(file_path, 'r') as file:
        data = json.load(file)

    times = []
    bitrates = []

    # Extract the relevant data
    for interval in data['intervals']:
        start = interval['sum']['start']
        bitrate = interval['sum']['bits_per_second'] / 1e6  # Convert to Mbps
        times.append(start)
        bitrates.append(bitrate)

    return times, bitrates

def plot_bitrate_comparison(logs):
    """Plot bitrate comparisons for multiple log files."""
    plt.figure(figsize=(10, 6))

    for log_file, label in logs:
        times, bitrates = parse_iperf3_log(log_file)
        plt.plot(times, bitrates, marker='o', linestyle='-', label=label)

    plt.title('Bitrate Comparison Over Time (Mbps)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Bitrate (Mbps)')
    plt.grid()
    plt.legend()
    plt.xticks()  # Show all time points
    plt.ylim(0, max(max(bitrates) for _, bitrates in logs) * 1.1)  # Set y-axis limit
    plt.show()

if __name__ == "__main__":
    # Specify the paths and labels for the log files
    logs = [
        ("iperf3_log1.json", "Test 1"),  # Replace with your first log file path and label
        ("iperf3_log2.json", "Test 2")   # Replace with your second log file path and label
    ]

    # Plot the comparison
    plot_bitrate_comparison(logs)

