class Book:
  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.is_checked_out = False
    self.checked_out_date = None
    self.checked_out_by = None

  def __repr__(self):
    return f"{self.title} by {self.author}"