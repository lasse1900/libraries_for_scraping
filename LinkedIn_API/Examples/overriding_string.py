class Book():

    favourites = []

    def __init__(self, title, pages) -> None:
        self.title = title
        self.pages = pages

    def is_long(self):
        if self.pages > 100:
            return True
        return False
    
    # Overriding
    def __str__(self) -> str:
        return f"{self.title} is {self.pages} pages long"
    
book = Book("Are you my friend", 72)
book2 = Book("Th4e long way home", 72)

Book.favourites.append(book)
Book.favourites.append(book2)

for b in Book.favourites:
    print(b)

