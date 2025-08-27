import tkinter as tk
import webbrowser
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from Library import Library
from Book import Book
from Patron import Patron
from utils import *

class App:
  def __init__(self):
    self.library = Library()
    self.root = tk.Tk()
    self.root.title("Mo's Library Management System 􀤨")
    self.root.geometry("1200x960")
    self.root.configure(bg="#fefefe")

    qr_path = generate_qr_code()
    self.qr_photo = ImageTk.PhotoImage(Image.open(qr_path).resize((120, 120)))

    self.create_layout()

  def create_layout(self):
    main_frame = ttk.Frame(self.root)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    title_frame = ttk.Frame(main_frame)
    title_frame.pack(fill="x", pady=25)

    title_label = tk.Label(
      title_frame,
      text="Mo's Library Management System 􀤨",
      font=("Source Code Pro", 32, "bold"),
      bg="#f8f9fa",
      fg="#212529"
    )
    title_label.pack()

    self.info_icon = tk.PhotoImage(file="img/info_icon_24.png")
    info_button = tk.Button(
      title_frame,
      image=self.info_icon,
      bd=0,
      command=self.show_info,
      bg="#f8f9fa",
      highlightthickness=0
    )
    info_button.place(x=title_label.winfo_reqwidth() * 1.7, y=10)

    self.notebook = ttk.Notebook(main_frame)
    self.notebook.pack(fill="both", expand=True)

    self.create_books_tab()
    self.create_patrons_tab()
    self.create_transactions_tab()

  def show_info(self):
    popup = tk.Toplevel(self.root)
    popup.title("About Me")
    popup.geometry("450x250")
    popup.resizable(False, False)
    popup.configure(bg="#f0f2f5")

    card = tk.Frame(popup, bg="white", bd=3, relief="ridge")
    card.place(relx=0.5, rely=0.5, anchor="center", width=440, height=220)

    tk.Button(card, image=self.qr_photo, bg="white", command= lambda: webbrowser.open('https://www.linkedin.com/in/mo-edris')).place(x=20,y=50)

    info_text = "Hi! I'm Mohamed Aly.\n\nThis is my Library Management System.\n\nFeel free to explore!"
    tk.Label(
      card,
      text=info_text,
      bg="white",
      fg="#333",
      font=("Source Code Pro", 12),
      justify="left"
    ).place(x=160, y=50)

    tk.Button(
      card,
      text="Close",
      command=popup.destroy,
      bg="#4CAF50",
      fg="#333",
      bd=0,
      font=("Source Code Pro", 10),
      activebackground="#45a049",
      activeforeground="white"
    ).place(x=160, y=170, width=100, height=30)

  def create_books_tab(self):
    # TODO LATER: Change layout to display books in a grid with a picture for each book

    self.books_tab = ttk.Frame(self.notebook)
    self.notebook.add(self.books_tab, text="Books")

    table_frame = ttk.Frame(self.books_tab)
    table_frame.pack(fill="both", expand=True, pady=20)

    self.books_tree = ttk.Treeview(table_frame, columns=("Title", "Author", "ISBN", "Status", "Patron", "Date"), show="headings", height=12)

    self.books_tree.heading("Title", text="Title")
    self.books_tree.heading("Author", text="Author")
    self.books_tree.heading("ISBN", text="ISBN")
    self.books_tree.heading("Status", text="Status")
    self.books_tree.heading("Patron", text="Checked Out By")
    self.books_tree.heading("Date", text="Date")

    print(self.books_tree.column("Title", width=350, anchor="w"))
    self.books_tree.column("Author", width=220, anchor="w")
    self.books_tree.column("ISBN", width=150, anchor="center")
    self.books_tree.column("Status", width=100, anchor="center")
    self.books_tree.column("Patron", width=100, anchor="center")
    self.books_tree.column("Date", width=100, anchor="center")

    books_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.books_tree.yview)
    self.books_tree.configure(yscrollcommand=books_scroll.set)
    self.books_tree.bind("<Double-1>", self.copy_to_clipboard)

    self.books_tree.pack(side="left", fill="both", expand=True)
    books_scroll.pack(side="right", fill="y")

    controls_frame = ttk.Frame(self.books_tab)
    controls_frame.pack(fill="x", pady=20)

    add_book_frame = ttk.LabelFrame(controls_frame, text="Add Book", padding=20)
    add_book_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

    self.book_title = tk.StringVar()
    self.book_author = tk.StringVar()
    self.book_isbn = tk.StringVar()

    ttk.Label(add_book_frame, text="Title").grid(row=0, column=0, sticky="w", pady=(0, 5))
    ttk.Entry(add_book_frame, textvariable=self.book_title, width=30).grid(row=0, column=1, sticky="ew", pady=(0, 10))

    ttk.Label(add_book_frame, text="Author").grid(row=1, column=0, sticky="w", pady=(0, 5))
    ttk.Entry(add_book_frame, textvariable=self.book_author, width=30).grid(row=1, column=1, sticky="ew", pady=(0, 10))

    ttk.Label(add_book_frame, text="ISBN").grid(row=2, column=0, sticky="w", pady=(0, 5))
    ttk.Entry(add_book_frame, textvariable=self.book_isbn, width=30).grid(row=2, column=1, sticky="ew", pady=(0, 15))

    ttk.Button(add_book_frame, text="Add Book", command=self.add_book).grid(row=3, column=0, columnspan=2, pady=10)

    add_book_frame.columnconfigure(1, weight=1)

    remove_book_frame = ttk.LabelFrame(controls_frame, text="Remove Book", padding=20)
    remove_book_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

    self.remove_book_isbn = tk.StringVar()

    ttk.Label(remove_book_frame, text="ISBN").pack(pady=(0, 5))
    ttk.Entry(remove_book_frame, textvariable=self.remove_book_isbn, width=25).pack(pady=(0, 15))
    ttk.Button(remove_book_frame, text="Remove Book", command=self.remove_book).pack(pady=5)

  # I created this, so that you could double-click on any row and get the ID of the patron or the ISBN of the book without having to manually copy it for testing =) Enjoy!
  def copy_to_clipboard(self, event):
    tree = event.widget
    selected_item = tree.focus()
    if not selected_item:
      return

    values = tree.item(selected_item, "values")
    print(values)
    if not values:
      return
    text_to_copy = None
    if tree == self.books_tree:
      text_to_copy = values[2]
    elif tree == self.patrons_tree:
      text_to_copy = values[0]

    self.root.clipboard_clear()
    self.root.clipboard_append(text_to_copy)
    self.root.update()

    print(f"Copied to clipboard: {text_to_copy}")

  def create_patrons_tab(self):
    self.patrons_tab = ttk.Frame(self.notebook)
    self.notebook.add(self.patrons_tab, text="Patrons")

    table_frame = ttk.Frame(self.patrons_tab)
    table_frame.pack(fill="both", expand=True, pady=(0, 20))

    self.patrons_tree = ttk.Treeview(table_frame, columns=("ID", "Name", "Books"), show="headings", height=12)

    self.patrons_tree.heading("ID", text="ID")
    self.patrons_tree.heading("Name", text="Name")
    self.patrons_tree.heading("Books", text="Books Borrowed")

    self.patrons_tree.column("ID", width=120, anchor="center")
    self.patrons_tree.column("Name", width=300, anchor="w")
    self.patrons_tree.column("Books", width=150, anchor="center")

    patrons_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.patrons_tree.yview)
    self.patrons_tree.configure(yscrollcommand=patrons_scroll.set)
    self.patrons_tree.bind("<Double-1>", self.copy_to_clipboard)
    self.patrons_tree.pack(side="left", fill="both", expand=True)
    patrons_scroll.pack(side="right", fill="y")

    controls_frame = ttk.Frame(self.patrons_tab)
    controls_frame.pack(fill="x", pady=10)

    add_patron_frame = ttk.LabelFrame(controls_frame, text="Add Patron", padding=20)
    add_patron_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

    self.patron_name = tk.StringVar()
    self.patron_id = tk.StringVar()

    ttk.Label(add_patron_frame, text="Name").grid(row=0, column=0, sticky="w", pady=(0, 5))
    ttk.Entry(add_patron_frame, textvariable=self.patron_name, width=30).grid(row=0, column=1, sticky="ew", pady=(0, 10))

    ttk.Label(add_patron_frame, text="ID").grid(row=1, column=0, sticky="w", pady=(0, 5))
    ttk.Entry(add_patron_frame, textvariable=self.patron_id, width=30).grid(row=1, column=1, sticky="ew", pady=(0, 15))

    ttk.Button(add_patron_frame, text="Add Patron", command=self.add_patron).grid(row=2, column=0, columnspan=2, pady=5)

    add_patron_frame.columnconfigure(1, weight=1)

    remove_patron_frame = ttk.LabelFrame(controls_frame, text="Remove Patron", padding=20)
    remove_patron_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

    self.remove_patron_id = tk.StringVar()

    ttk.Label(remove_patron_frame, text="Patron ID").pack(pady=(0, 5))
    ttk.Entry(remove_patron_frame, textvariable=self.remove_patron_id, width=25).pack(pady=(0, 15))
    ttk.Button(remove_patron_frame, text="Remove Patron", command=self.remove_patron).pack(pady=5)

  def create_transactions_tab(self):
    self.transactions_tab = ttk.Frame(self.notebook)
    self.notebook.add(self.transactions_tab, text="Transactions")

    main_container = ttk.Frame(self.transactions_tab)
    main_container.pack(expand=True, fill="both", pady=100)

    checkout_frame = ttk.LabelFrame(main_container, text="Check Out Book", padding=30)
    checkout_frame.pack(side="top", expand=True, fill="none", padx=(0, 10))

    self.checkout_isbn = tk.StringVar()
    self.checkout_patron = tk.StringVar()

    ttk.Label(checkout_frame, text="Book ISBN").grid(row=0, column=0, sticky="w", pady=(0, 5))
    ttk.Entry(checkout_frame, textvariable=self.checkout_isbn, width=25).grid(row=0, column=1, sticky="ew", pady=(0, 15))

    ttk.Label(checkout_frame, text="Patron ID").grid(row=1, column=0, sticky="w", pady=(0, 5))
    ttk.Entry(checkout_frame, textvariable=self.checkout_patron, width=25).grid(row=1, column=1, sticky="ew", pady=(0, 20))

    ttk.Button(checkout_frame, text="Check Out", command=self.checkout_book).grid(row=2, column=0, columnspan=2, pady=10)

    checkout_frame.columnconfigure(1, weight=1)

    checkin_frame = ttk.LabelFrame(main_container, text="Check In Book", padding=30)
    checkin_frame.pack(side="bottom", expand=True, fill="none", padx=(0, 10))

    self.checkin_isbn = tk.StringVar()

    ttk.Label(checkin_frame, text="Book ISBN").pack(pady=(20, 5))
    ttk.Entry(checkin_frame, textvariable=self.checkin_isbn, width=25).pack(pady=(0, 20))
    ttk.Button(checkin_frame, text="Check In", command=self.checkin_book).pack(pady=10)

  def add_book(self):
    title = self.book_title.get().strip()
    author = self.book_author.get().strip()
    isbn = self.book_isbn.get().strip()

    if not all([title, author, isbn]):
      messagebox.showerror("Error", "Please fill in all fields")
      return

    if self.library.add_book(Book(title, author, isbn)):
      messagebox.showinfo("Success", "Book added successfully")
      self.book_title.set("")
      self.book_author.set("")
      self.book_isbn.set("")
      self.refresh_books()
    else:
      messagebox.showerror("Error", "Book with this ISBN already exists")

  def remove_book(self):
    isbn = self.remove_book_isbn.get().strip()
    if not isbn:
      messagebox.showerror("Error", "Please enter an ISBN")
      return

    if self.library.remove_book(isbn):
      messagebox.showinfo("Success", "Book removed successfully")
      self.remove_book_isbn.set("")
      self.refresh_books()
    else:
      messagebox.showerror("Error", "Book not found or currently checked out")

  def add_patron(self):
    name = self.patron_name.get().strip()
    patron_id = self.patron_id.get().strip()

    if not all([name, patron_id]):
      messagebox.showerror("Error", "Please fill in all fields")
      return

    if self.library.add_patron(Patron(name, patron_id)):
      messagebox.showinfo("Success", "Patron added successfully")
      self.patron_name.set("")
      self.patron_id.set("")
      self.refresh_patrons()
    else:
      messagebox.showerror("Error", "Patron with this ID already exists")

  def remove_patron(self):
    patron_id = self.remove_patron_id.get().strip()
    if not patron_id:
      messagebox.showerror("Error", "Please enter a Patron ID")
      return

    if self.library.remove_patron(patron_id):
      messagebox.showinfo("Success", "Patron removed successfully")
      self.remove_patron_id.set("")
      self.refresh_patrons()
    else:
      messagebox.showerror("Error", "Patron not found or has borrowed books")

  def checkout_book(self):
    isbn = self.checkout_isbn.get().strip()
    patron_id = self.checkout_patron.get().strip()

    if not all([isbn, patron_id]):
      messagebox.showerror("Error", "Please fill in both fields")
      return

    if self.library.checkout(isbn, patron_id):
      messagebox.showinfo("Success", "Book checked out successfully")
      self.checkout_isbn.set("")
      self.checkout_patron.set("")
      self.refresh_all()
    else:
      messagebox.showerror("Error", "Book or patron not found, or book already checked out")

  def checkin_book(self):
    isbn = self.checkin_isbn.get().strip()
    if not isbn:
      messagebox.showerror("Error", "Please enter an ISBN")
      return

    if self.library.checkin(isbn):
      messagebox.showinfo("Success", "Book checked in successfully")
      self.checkin_isbn.set("")
      self.refresh_all()
    else:
      messagebox.showerror("Error", "Book not found or currently checked out")

  def refresh_books(self):
    # That is a shitty way of doing it and inefficient at all but i will keep it for simplicity purposes =)
    for item in self.books_tree.get_children():
      self.books_tree.delete(item)

    for book in self.library.books.values():
      status = "Checked Out" if book.is_checked_out else "Available"
      patron = book.checked_out_by if book.is_checked_out else ""
      date = book.checked_out_date if book.is_checked_out else ""

      self.books_tree.insert("", "end", values=(
        book.title, book.author, book.isbn, status, patron, date
      ))

  def refresh_patrons(self):
    # Again, that is a shitty way of doing it and inefficient at all but i will keep it for simplicity purposes =)
    for item in self.patrons_tree.get_children():
      self.patrons_tree.delete(item)

    for patron in self.library.patrons.values():
      self.patrons_tree.insert("", "end", values=(
        patron.patron_id, patron.name, len(patron.borrowed_books)
      ))

  def refresh_all(self):
    self.refresh_books()
    self.refresh_patrons()

  def run(self):
    self.root.mainloop()
