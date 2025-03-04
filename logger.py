import datetime

def log_error(error_message):
    """Logs an error message to a file named 'log.txt'."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR: {error_message}\n"
    
    with open("log.txt", "a") as log_file:
        log_file.write(log_entry)
