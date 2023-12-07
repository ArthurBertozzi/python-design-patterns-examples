class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


def main():
    # Creating instances of Singleton
    singleton1 = Singleton()
    singleton2 = Singleton()

    # Both instances should be the same
    print(f"Is singleton1 the same as singleton2? {singleton1 is singleton2}")


if __name__ == "__main__":
    main()
