from win10toast import ToastNotifier

notifier = ToastNotifier()
notifier.icon_path = None  # You can specify an icon path if desired
def send_greeting(name):
    greeting_message = f"Hello sir/Developer {name}, hope you're having a great day and don't forget to sieg heil!"
    notifier.show_toast("StartUp Greeting to the Developer", greeting_message, duration=10)

if __name__ == "__main__":
    send_greeting("CJ")