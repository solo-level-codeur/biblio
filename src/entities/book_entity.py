"""from entite_author import author"""
class BookEntity:
    def __init__(self, id=None, isbn=None, title=None, author=None, published_date=None, 
                 creation_date=None, book_format=None, editor=None, genre=None, added_by=None):   
 
        self.id = id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.published_date = published_date
        self.creation_date = creation_date
        self.book_format = book_format
        self.editor = editor
        self.genre = genre
        self.added_by = added_by

    def __str__(self):
        return (f"BookEntity(id={self.id}, isbn={self.isbn}, title={self.title}, "
                f"author={self.author}, published_date={self.published_date}, "
                f"creation_date={self.creation_date}, book_format={self.book_format}, "
                f"editor={self.editor}, genre={self.genre}, added_by={self.added_by})")
