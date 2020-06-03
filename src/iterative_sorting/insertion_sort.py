def simple_insert(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j - 1]
            j -= 1
    return arr

#sorting books

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    def __str__(self):
        return f'{self.title} by {self.author} in {self.genre}'
    
books = [Book('AAA', 'asdft', 'b'),Book('ABB','sgdfdg','a'),Book('ABC', 'sdfsdf', 'c'),Book('BAA', 'sdfgsdf','aa')]

def book_insert(book):
    for i in range(1, len(book)):
        temp = book[i]
        j = i
        # while we're not at front of list and these two should be swapped
        while j > 0 and temp.genre < book[j - 1].genre:
            book[j] = book[j - 1]
            j -= 1
        book[j] = temp
    return book
books = book_insert(books)
print([book.genre for book in books])