from datetime import datetime

class Library:
  def __init__(self):
    self.books = {}
    self.patrons = {}

  def add_book(self, book):
    if book.isbn not in self.books:
      self.books[book.isbn] = book
      return True
    return False

  def remove_book(self, isbn):
    if isbn in self.books and not self.books[isbn].is_checked_out:
      del self.books[isbn]
      return True
    return False

  def add_patron(self, patron):
    if patron.patron_id not in self.patrons:
      self.patrons[patron.patron_id] = patron
      return True
    return False

  def remove_patron(self, patron_id):
    if patron_id in self.patrons and not self.patrons[patron_id].borrowed_books:
      del self.patrons[patron_id]
      return True
    return False

  def checkout(self, isbn, patron_id):
    if isbn in self.books and patron_id in self.patrons:
      book = self.books[isbn]
      patron = self.patrons[patron_id]
      if not book.is_checked_out:
        book.is_checked_out = True
        book.checked_out_date = datetime.now().strftime("%Y-%m-%d")
        book.checked_out_by = patron_id
        patron.borrowed_books.append(isbn)
        return True
    return False

  def checkin(self, isbn):
    if isbn in self.books and self.books[isbn].is_checked_out:
      book = self.books[isbn]
      patron = self.patrons[book.checked_out_by]
      patron.borrowed_books.remove(isbn)
      book.is_checked_out = False
      book.checked_out_date = None
      book.checked_out_by = None
      return True
    return False
