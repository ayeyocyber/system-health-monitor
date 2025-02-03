import psutil
import time

def get_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Disk Usage: {disk.percent}%")
    print("-" * 30)

def main():
    print("System Health Monitor - Press Ctrl+C to stop")
    try:
        while True:
            get_system_health()
            time.sleep(5)  # Refresh every 5 seconds
    except KeyboardInterrupt:
        print("Monitoring Stopped.")

if __name__ == "__main__":
    main()

