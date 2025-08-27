class Patron:
  def __init__(self, name, patron_id):
    self.name = name
    self.patron_id = patron_id
    self.borrowed_books = []

  def __str__(self):
    return self.name