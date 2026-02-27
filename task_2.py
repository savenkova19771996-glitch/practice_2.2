import psutil
import time

def monitor_resources():
    while True:
        print("ОБНОВЛЕНИЕ КАЖДЫЕ 5 СЕКУНД")
        monitoring_CPU = psutil.cpu_percent(interval=1)
        monitoring_OZU = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        print(f"CPU загружен на: {monitoring_CPU}%")
        print(f"Памяти использовано: {monitoring_OZU.percent}%")
        print(f"Процентное соотношение загруженности диска: {disk.percent}%")
        print("-" * 30)
        time.sleep(5)

if __name__ == "__main__":
    monitor_resources()