import multiprocessing
import threading
import time
import os
from datetime import datetime

##########
#  GLOBAL CONSTS
##########

NO_OF_PROCESSES = 4
NO_OF_THREADS_PER_PROCESS = 2

##########
#  GLOBAL VARIABLES
##########


##########
#  FUNCTION DEFS
##########

# Time string for logging
def get_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Logging utility
def log(logText):
    print(get_time() + " ## " +logText)

# Function to be run in each thread (daemon)
def thread_task(name):
    while True:
        log(f"Thread = {name} | PID = {os.getpid()} | Thread name = {threading.current_thread().name}")
        time.sleep(1)

# Function to be run in each process
def process_task(proc_id):
    log(f"START - Process = {proc_id}; PID = {os.getpid()}")
    
    # Launch n threads per process
    for i in range(NO_OF_THREADS_PER_PROCESS):
        t = threading.Thread(target=thread_task, args=(f"{proc_id}-{i}",), daemon=True)
        t.start()

    # Threads will finish on the end of this scope
    time.sleep(10)
    log(f"FINISH - Process = {proc_id}")

##########
#  MAIN
##########
if __name__ == "__main__":
    log("START - Main")
    # Initialize variables
    processes = list()

    # Launch processes
    for i in range(NO_OF_PROCESSES):
        p = multiprocessing.Process(target=process_task, args=(i,))
        p.start()
        processes.append(p)

    # Wait for all processes to finish
    for p in processes:
        p.join()

    log(f"FINISH - Main")