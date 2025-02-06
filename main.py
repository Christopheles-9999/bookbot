def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() # defines 'file_contents' as f: with read() function
    print(file_contents) # outputs the contents of the .txt as console 
    

def count():
    with open("books/frankenstein.txt") as f: 
            # captures the book as a reference
        book_contents = f.read()
        words = book_contents.split()
    
    total = len(words)
        # prints the numbers of words based on the split


def text():

    with open("books/frankenstein.txt") as pages:
        book_string = pages.read()
        
        lower_string = book_string.lower()

    captures = {}

    for char in lower_string:
        if char in captures:
            captures[char] += 1
                # counts the occurences of a value if already present
        else:
            captures[char] = 1
                # enters the 1st value when occures
    
    print(captures)
text()