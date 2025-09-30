from multiprocessing import Process
from test import test_chatbot
import time

if __name__ == "__main__":
    processes = []
    for i in range(5): # number of parallel instances (adjust as necessary)
        p = Process(target=test_chatbot, args=(i,))
        p.start()
        processes.append(p)
        time.sleep(2) # slight delay to stagger startups

    for p in processes:
        p.join()
