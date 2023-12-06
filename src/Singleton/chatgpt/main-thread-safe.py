import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

def create_singleton():
    singleton = Singleton()
    print(f"Singleton instance created in thread {threading.current_thread().name}: {singleton}")

def main():
    # Creating instances of Singleton in multiple threads
    thread1 = threading.Thread(target=create_singleton, name="Thread 1")
    thread2 = threading.Thread(target=create_singleton, name="Thread 2")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
