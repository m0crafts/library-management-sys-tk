# library-management-sys-tk

A minimal and clean desktop application for managing library books and patrons built with Python and Tkinter.

## Features

- **Book Management**: Add, remove, and track books in your library
- **Patron Management**: Manage library members and their information  
- **Check Out/In System**: Handle book borrowing and returns
- **Real-time Status**: View current availability and checkout information
- **Clean Interface**: Modern, minimal design with intuitive navigation

## Screenshots

The application features a tabbed interface with three main sections:
- Books tab for managing the library collection
- Patrons tab for member management
- Transactions tab for checkout and return operations

## Requirements

- Python 3.6 or higher
- tkinter (included with Python)

## Dependencies

  - `qrcode` - For generating QR codes
  - `pillow` - Image processing library (required by qrcode)

## Usage

### Managing Books
- Navigate to the Books tab
- Add new books by entering title, author, and ISBN
- Remove books using their ISBN (only if not currently checked out)
- View all books with their current status

### Managing Patrons
- Use the Patrons tab to add new library members
- Enter patron name and unique ID
- Remove patrons only if they have no outstanding books

### Book Transactions
- Check out books by entering the book's ISBN and patron ID
- Return books by entering the ISBN in the check-in section
- All transactions are tracked with dates

## Sample Data

The application loads with sample books and patrons for immediate testing:
- Classic literature titles from various authors
- Sample patron accounts
- Two pre-existing checkouts to demonstrate the system

## Technical Details

- Built with Python's native tkinter library
- Object-oriented design with separate classes for Book, Patron, and Library
- In-memory data storage (data resets on application restart)
- Clean separation between business logic and UI components

## License

MIT License - feel free to use, modify, and distribute as needed.

## Contributing

This is a simple educational project. Feel free to fork and enhance with additional features like data persistence, search functionality, or reporting capabilities.
