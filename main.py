import pandas as pd
import dpkt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to analyze logs
def analyze_logs(log_file):
    try:
        df = pd.read_csv(log_file)
        log_analysis = df.describe().to_string()
        print("Log Analysis:")
        print(log_analysis)
        return log_analysis
    except Exception as e:
        print(f"Error analyzing logs: {e}")
        return "Log analysis failed."

# Function to recover deleted files (dummy function for illustration)
def recover_files(disk_image):
    try:
        print(f"Recovering files from {disk_image}...")
        # Implement file recovery logic here
        recovered_files = ["file1.txt", "file2.jpg"]
        return recovered_files
    except Exception as e:
        print(f"Error recovering files: {e}")
        return ["File recovery failed."]

# Function to analyze network traffic using dpkt
def analyze_network(pcap_file):
    try:
        with open(pcap_file, 'rb') as f:
            try:
                pcap = dpkt.pcap.Reader(f)
            except ValueError:
                f.seek(0)
                pcap = dpkt.pcapng.Reader(f)
            
            network_analysis = ""
            print("Network Analysis:")
            for timestamp, buf in pcap:
                eth = dpkt.ethernet.Ethernet(buf)
                if isinstance(eth.data, dpkt.ip.IP):
                    ip = eth.data
                    ip_src = ip.src
                    ip_dst = ip.dst
                    network_analysis += f"Packet: {ip_src} -> {ip_dst}\n"
                    print(f"Packet: {ip_src} -> {ip_dst}")
            return network_analysis
    except Exception as e:
        print(f"Error analyzing network traffic: {e}")
        return "Network analysis failed."

# Function to generate a report
def generate_report(log_analysis, recovered_files, network_analysis, report_file):
    try:
        c = canvas.Canvas(report_file, pagesize=letter)
        width, height = letter

        c.drawString(100, height - 50, "Forensic Investigation Report")
        c.drawString(100, height - 100, "Log Analysis:")
        c.drawString(100, height - 120, log_analysis)

        c.drawString(100, height - 160, "Recovered Files:")
        for i, file in enumerate(recovered_files):
            c.drawString(100, height - 180 - i*20, file)

        c.drawString(100, height - 220, "Network Analysis:")
        c.drawString(100, height - 240, network_analysis)

        c.save()
    except Exception as e:
        print(f"Error generating report: {e}")

# Main function
def main():
    import sys
    if len(sys.argv) != 5:
        print("Demo mode: Using sample files")
        log_file = "logs.csv"
        disk_image = "disk.img"
        pcap_file = "network.pcap"
        report_file = "report_demo.pdf"
        key = "mysecretkey"
    else:
        log_file = sys.argv[1]
        disk_image = sys.argv[2]
        pcap_file = sys.argv[3]
        key = sys.argv[4]
        report_file = "report.pdf"

    log_analysis = analyze_logs(log_file)
    recovered_files = recover_files(disk_image)
    network_analysis = analyze_network(pcap_file)

    generate_report(log_analysis, recovered_files, network_analysis, report_file)
    print(f"Report generated: {report_file}")

if __name__ == "__main__":
    main()
