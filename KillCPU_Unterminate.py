from multiprocessing import Process

def looping():
    try:
        while True:
            i = 0
            i += 1
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    Processes = None
    try:
        Processes = [Process(target=looping) for i in range(4)]
        
        for p in Processes:
            p.start()
        for p in Processes:
            p.join()
    except KeyboardInterrupt:
        for p in Processes:
            p.terminate
        print ("Kill all looping!!")
        