from win10toast import ToastNotifier
import time

notifier = ToastNotifier()
notifier.show_toast("Reminder", "Hello there CJ, I think you have some tasks to complete.", duration=10)
time.sleep(5)
notifier.show_toast("Reminder", "Don't forget to check your Messenger and attend the Class at 3 PM.", duration=10)