import time
from win10toast import ToastNotifier

toast = ToastNotifier()

if __name__ == "__main__":
    while True:
        toast.show_toast \
            ("Notification",
             "==WATER BREAK! FULL GETCHASELF A FULL BOTTLE!==",
             duration=10,
             icon_path="icon.ico"
             )
        time.sleep(10)
