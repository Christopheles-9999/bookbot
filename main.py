book_path = "books/frankenstein.txt"
"""
print(f"the book path ~> alias [book_path]")
print(f"{book_path}")
print(f"     ")
"""

def main():
    with open(book_path) as f:
        file_contents = f.read() # defines 'file_contents' as f: with read() function
    # print(file_contents)
        # outputs the contents of the .txt as console 
    
    return file_contents 

the_book = main()
"""
print(f"the full book ~> alias [the_book]")
print(f"{the_book[:73]}")
print(f"     ")
"""


def count():
    with open(book_path) as f: 
            # captures the book as a reference
        book_contents = f.read()
        words = book_contents.split()
    
    cnt_total = len(words)
        # prints the numbers of words based on the split
    
    return cnt_total

word_total = count()
"""
print(f"the word count ~> alias [word_total]")
print(f"{word_total}")
print(f"     ")
"""


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
    
    # print(captures)

    return captures

digit = text()
"""
print(f"the char count ~> alias [digit]")
print(f"{digit}")
print(f"     ")
"""


def organize():
    char_list = []
        # empty list
    
    for char, count in digit.items():
        # refers to the defined prev fnc output    
            # char & count capture for the pairings within the dictionary that are undefined  
        
        if char.isalpha():
            # checks the 1st value to see what type it is

            char_dict = {
                "char": char,
                "num": count
            }
                # compiles the detected values into a grouping
        
        if char.isalnum():
            char_dict = {
                "char": char,
                "num": count
            }

        if char.isascii():
            char_dict = {
                "char": char,
                "num": count
            }
        
        char_list.append(char_dict)
                # takes the grouping and adds it to the list in order of occurance
    
        # Sort the list (see the hint about sorting in the readme)
    return char_list


# NEST GROUP 001 vvv
def sort_on(dict):
    return dict["num"]

the_sorted = organize()

the_sorted.sort(reverse=True, key=sort_on)
# NEST GROUP 001 ^^^

"""
print(f"the word total ~> alias [the_sorted]")
print(f"{the_sorted}")
print(f"     ")
"""


def the_full_sandwich():
    print(f"--- Begin report of {book_path}.txt")
    print(f"     ")
    print(f"{word_total} words found in the document")
    print(f"     ")
    
    for char_dict in the_sorted:
        if char_dict['char'].isalpha():
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    
    print(f"--- End report ---")

the_full_sandwich()

# print(f"{the_sorted[:20]}")




    
