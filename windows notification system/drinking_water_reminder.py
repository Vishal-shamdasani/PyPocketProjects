from win10toast import ToastNotifier
import time

occrence=int(input("no. "))

toast=ToastNotifier()

while occrence>0:

    toast.show_toast(title="reminder",msg="drink water",duration=5)
    occrence-=1
    print(occrence)
    time.sleep(10)