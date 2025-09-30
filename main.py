from multiprocessing import Process
from test import test_chatbot   # replace with the actual filename (without .py)

if __name__ == "__main__":
    processes = []
    for i in range(5): # number of parallel instances (adjust as necessary)
        p = Process(target=test_chatbot)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
