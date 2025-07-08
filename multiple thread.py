import threading
import time
def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Both threads have finished.")
