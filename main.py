from App import App
from Book import Book
from Patron import Patron

if __name__ == '__main__':

  app = App()

  books = [
    ("Introduction to Quantum Mechanics", "David J. Griffiths", "978-1-107-17986-8"),
    ("Quantum Computation and Quantum Information", "Michael Nielsen & Isaac Chuang", "978-1-107-00217-3"),
    ("Structure and Interpretation of Computer Programs", "Abelson, Sussman & Sussman", "0-262-51087-1"),
    ("Core Python Programming", "Wesley J. Chun", "0-13-226993-7"),
    ("Compilers: Principles, Techniques, and Tools", "Aho, Lam, Sethi & Ullman", "0-201-10088-6"),
    ("Clean Code", "Robert C. Martin", "978-0132350884"),
    ("Introduction to Algorithms", "Cormen, Leiserson, Rivest & Stein", "978-0262033848"),
    ("Artificial Intelligence: A Modern Approach", "Russell & Norvig", "978-0134610993"),
    ("Database System Concepts", "Silberschatz, Korth & Sudarshan", "978-0078022159"),
    ("Operating System Concepts", "Silberschatz, Galvin & Gagne", "978-1118063330"),
    ("Computer Systems: A Programmer’s Perspective", "Randal E. Bryant", "978-9332573901"),
  ]

  patrons = [
    ("Tony Stark", "P001"),
    ("Nikola Tesla", "P002"),
    ("Albert Einstein", "P003"),
    ("Alan Turing", "P004"),
    ("Richard Feynman", "P005"),
    ("Elon Musk", "P006"),
    ("Steve Jobs", "P007"),
  ]

  for title, author, isbn in books:
    app.library.add_book(Book(title, author, isbn))

  for name, patron_id in patrons:
    app.library.add_patron(Patron(name, patron_id))

  app.library.checkout("978-0262033848", "P001")
  app.library.checkout("0-13-226993-7", "P007")
  app.refresh_all()
  app.run()

  # الحمدلله
