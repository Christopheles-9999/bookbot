frankenstein = open("books/frankenstein.txt")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() # defines 'file_contents' as f: with read() function
    print(file_contents) # outputs the contents of the .txt as console 

def count():
    with frankenstein as book: 
            # captures the book as a reference
        book_contents = book.read()
        words = book_contents.split()
    
    total = len(words)

    print(total)
count()