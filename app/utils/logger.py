from datetime import datetime
import os
class Logger:
    def errorLogs(message):
        with open("app/storage/logs/blog.log","a") as file:
            file.write(f"ERROR : [{datetime.now()}] {message}\n")
