books = ["Harry Potter", "Matilda", "The Jungle Book", "Charlotte's Web", "Wonder"]

print(len(books))
print(books[0])
print(books[-1])
print(books[:3])

books.append("Diary of a Wimpy Kid")
books.remove("The Jungle Book")
books.sort()
books.reverse()

librarian = {
    "name": "Ms. Priya",
    "section": "Children's Books",
    "experience": 5
}

print(librarian["name"])
librarian["experience"] = 6
librarian["email"] = "priya@schoollibrary.com"
librarian.pop("section")

book_ids = [101, 102, 103, 104, 105]
book_names = ["Matilda", "Wonder", "Harry Potter", "Charlotte's Web", "Diary of a Wimpy Kid"]
book_directory = dict(zip(book_ids, book_names))

print("Available Books:", books)
print("Librarian Details:", librarian)
print("Book ID Directory:", book_directory)

