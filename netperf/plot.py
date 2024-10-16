import json
import matplotlib.pyplot as plt
import argparse

def get_cpu_utilizations(file_path):
    """Parse the iperf3 log file and return times, bitrates, and CPU utilization."""
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extract host total CPU utilization
    cpu_utilization = data['end']['cpu_utilization_percent']['host_total']

    return cpu_utilization

def get_time_and_bitrate(file_path):
    """Parse the iperf3 log file and return times, bitrates, and CPU utilization."""
    with open(file_path, 'r') as file:
        data = json.load(file)

    times = []
    bitrates = []
    # Extract bitrate data
    for interval in data['intervals']:
        start = interval['sum']['start']
        bitrate = interval['sum']['bits_per_second'] / 1e6  # Convert to Mbps
        times.append(start)
        bitrates.append(bitrate)

    return times, bitrates


def plot_separate_graphs(logs):
    """Plot separate graphs for CPU utilization and bitrate in one figure."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Plot CPU Utilization
    cpu_utilizations = []
    for log_file, label in logs:
        cpu_utilizations.append(get_cpu_utilizations(log_file))

    bar_width = 0.35
    x_indices = range(len(logs))

    ax1.bar(x_indices, cpu_utilizations, width=bar_width, color='skyblue', label='CPU Utilization (%)', alpha=0.6)
    ax1.set_title('Host Total CPU Utilization')
    ax1.set_ylabel('CPU Utilization (%)')
    ax1.set_xticks(x_indices)
    ax1.set_xticklabels([label for _, label in logs])

    # Adjust y-axis limits for CPU utilization
    max_cpu = max(cpu_utilizations)
    ax1.set_ylim(0, min(max_cpu + 1, 100))  # Adjust based on max CPU utilization
    ax1.grid(axis='y')

    # Plot Bitrates
    for log_file, label in logs:
        times, bitrates = get_time_and_bitrate(log_file)
        ax2.plot(times, bitrates, marker='o', linestyle='-', label=label)

    ax2.set_title('Bitrate Comparison Over Time (Mbps)')
    ax2.set_xlabel('Time (seconds)')
    ax2.set_ylabel('Bitrate (Mbps)')
    ax2.grid()
    ax2.legend(loc='upper left')

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Plot comparision of bitrate and cpu utilization from two iperf3 json log files')
    parser.add_argument('file1', type=str, help='First log file path')
    parser.add_argument('label1', type=str, help='Label for first log')
    parser.add_argument('file2', type=str, help='Second log file path')
    parser.add_argument('label2', type=str, help='Label for second log')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Specify the paths and labels for the log files
    logs = [
        (args.file1, args.label1),  # Replace with your first log file path and label
        (args.file2, args.label2)   # Replace with your second log file path and label
    ]
    plot_separate_graphs(logs)
    # Plot the comparison
    #plot_bitrate_comparison(logs)
