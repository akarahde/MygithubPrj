# Server Monitoring System

## Description
This project monitors server performance using Python. It tracks CPU, RAM, and Disk usage and provides alerts when usage exceeds threshold limits.

## Features
- Real-time CPU, RAM, Disk monitoring
- Alert system for high usage
- Log file generation
- MySQL database storage
- Continuous monitoring (every 10 seconds)

## Technologies Used
- Python
- MySQL
- Linux (Azure VM)

## How to Run
1. Install dependencies:
   pip install psutil mysql-connector-python

2. Run script:
   python monitor.py