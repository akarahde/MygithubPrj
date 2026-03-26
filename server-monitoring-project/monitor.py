Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
 
import psutil
import mysql.connector
from datetime import datetime
import time

while True:
...     cpu = psutil.cpu_percent()
...     ram = psutil.virtual_memory().percent
...     disk = psutil.disk_usage('/').percent
... 
...     now = datetime.now()
... 
...     print(f"{now} CPU:{cpu}% RAM:{ram}% Disk:{disk}%")
... 
...     if cpu > 50:
...         print("ALERT: CPU HIGH")
... 
...     if ram > 50:
...         print("ALERT: RAM HIGH")
... 
...     if disk > 50:
...         print("ALERT: DISK HIGH")
... 
...     with open("monitor.log", "a") as f:
...         f.write(f"{now} CPU:{cpu}% RAM:{ram}% Disk:{disk}%\n")
... 
...     db = mysql.connector.connect(
...         host="localhost",
...         user="monitor",
...         password="Your_password",
...         database="monitoring"
...     )
... 
...     cursor = db.cursor()
... 
...     query = "INSERT INTO system_stats (cpu, ram, disk) VALUES (%s, %s, %s)"
...     values = (cpu, ram, disk)
... 
...     cursor.execute(query, values)
...     db.commit()
... 
...     print("Saved to DB\n")
... 
...     time.sleep(10)
... 
