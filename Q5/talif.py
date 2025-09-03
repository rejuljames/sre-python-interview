import time

def tail_log_and_alert(file_path, error_keywords):
    with open(file_path, "r") as f:
        f.seek(0, 2)  # go to the end
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            for keyword in error_keywords:
                if keyword in line:
                    print(f"ALERT: Found error '{keyword}' in log")
