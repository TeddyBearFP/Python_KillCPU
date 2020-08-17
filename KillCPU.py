import multiprocessing

def looping():
    try:
        while True:
            i = 0
            i += 1
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    #這句打包exe一定要有以免memory爆掉
    multiprocessing.freeze_support()
    Processes = None
    try:
        Processes = [multiprocessing.Process(target=looping) for i in range(4)]
        
        for p in Processes:
            p.daemon = True
            p.start()
        for p in Processes:
            p.join()
    except KeyboardInterrupt:
        for p in Processes:
            p.terminate()
        print ("Kill all looping!!")