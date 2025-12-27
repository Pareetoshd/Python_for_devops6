import psutil
def check_cpu_threshold() -> None:
    cpu_threshold= int(input("Enter CPU threshold value: "))

    current_cpu: float= psutil.cpu_percent(interval=1)
    
    if current_cpu > cpu_threshold:
        print("High CPU Usage")
        send_email_alert:(current_cpu, cpu_threshold)
    else: 
        print("CPU Usage is Normal")     
check_cpu_threshold()
 
