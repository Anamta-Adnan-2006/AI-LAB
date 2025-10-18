class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def viewFullDescription(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: ${self.price}")

    def addToShoppingBasket(self):
        print(f"{self.name} has been added to your shopping basket.")

    def removeFromShoppingBasket(self):
        print(f"{self.name} has been removed from your shopping basket.")
class MP3(Item):
    def __init__(self, name, description, price, artist, duration):
        super().__init__(name, description, price)
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"Playing {self.name} by {self.artist} ({self.duration} mins).")

    def download(self):
        print(f"Downloading {self.name} by {self.artist}...")

class DVD(Item):
    def __init__(self, name, description, price, certificate, duration, actors):
        super().__init__(name, description, price)
        self.certificate = certificate
        self.duration = duration
        self.actors = actors

    def viewTrailer(self):
        print(f"Viewing trailer for {self.name} featuring {self.actors}.")

class Book(Item):
    def __init__(self, name, description, price, author, numberOfPages, genre):
        super().__init__(name, description, price)
        self.author = author
        self.numberOfPages = numberOfPages
        self.genre = genre

    def previewContent(self):
        print(f"Previewing first few pages of '{self.name}' by {self.author}.")

if __name__ == "__main__":
    # MP3 Object
    mp3 = MP3("Ranjhan", "song by parampara tandon", 1.99, "song by parampara tandon", 4)
    mp3.viewFullDescription()
    mp3.play()
    mp3.download()
    mp3.addToShoppingBasket()
    print()

    dvd = DVD("me before you", "thea sharrock", 14.99, "PG-13", 148, "emilia clarke , sam clafin")
    dvd.viewFullDescription()
    dvd.viewTrailer()
    dvd.addToShoppingBasket()
    print()

    book = Book("namal ", "suspense", 9.99, "nemrah ahmed", 450, "islamic crime thiller")
    book.viewFullDescription()
    book.previewContent()
    book.addToShoppingBasket()
