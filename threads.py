import threading
import time
def print_numbers():
    for i in range(1,6):
        print(f"Number:{i}")
        time.sleep(3)
def print_letters():
    for letter in 'KLMNO':
        print(f"letter:{letter}")
        time.sleep(4)
thread1=threading.Thread(target=print_numbers)
thread2=threading.Thread(target=print_letters)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Both threads have finished execution.")