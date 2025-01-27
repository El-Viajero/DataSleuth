**DataSleuth** is a powerful and versatile forensic investigation toolkit designed to assist investigators in analyzing logs, recovering files, analyzing network traffic, and generating comprehensive reports. Whether you're a seasoned forensic investigator or just starting out, DataSleuth provides the tools you need to uncover critical insights and evidence.

#### Key Features:
- **Log Analysis**: Quickly analyze log files to identify patterns, anomalies, and key events.
- **File Recovery**: Recover deleted or lost files from disk images with ease.
- **Network Traffic Analysis**: Examine network traffic to detect suspicious activities and trace connections.
- **Report Generation**: Generate professional and detailed PDF reports, complete with your custom branding and logo.

#### How It Works:
1. **Log Analysis**: DataSleuth reads and analyzes log files, providing a summary of key metrics and events.
2. **File Recovery**: The toolkit attempts to recover files from provided disk images, listing the recovered files in the report.
3. **Network Analysis**: DataSleuth processes pcap files to analyze network traffic, identifying source and destination IP addresses.
4. **Report Generation**: A comprehensive report is generated, including log analysis, recovered files, and network analysis, formatted professionally with your custom logo.

#### Usage:
DataSleuth can be run in both demo mode and normal mode. In demo mode, it uses sample files to demonstrate its capabilities. In normal mode, users can provide their own files and specify the name of the generated report.

**Example Command**:
```sh
python datasleuth.py logs.csv disk.img network.pcap mysecretkey custom_report.pdf
```

#### Why Choose DataSleuth?
- **User-Friendly**: Easy to use with clear instructions and error handling.
- **Customizable**: Allows for custom branding and report naming.
- **Comprehensive**: Covers multiple aspects of forensic investigation in one toolkit.
