from abc import ABC, abstractmethod

# Subject interface (abstract class)
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# RealSubject class
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image from {self.filename}")

    def display(self):
        print(f"Displaying image {self.filename}")

# Proxy class
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Client code
if __name__ == "__main__":
    # Using the RealImage directly
    real_image = RealImage("example.jpg")
    real_image.display()

    print("\n")

    # Using the ProxyImage
    proxy_image = ProxyImage("example.jpg")

    # The real image is loaded only when display is called on the proxy
    proxy_image.display()

    # The real image is not loaded again when display is called again
    proxy_image.display()
