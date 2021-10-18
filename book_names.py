def name_find(text, names):
    """Find the first occurrence of a character in a book.
    s
    text: The full text of a book. Should be a list of strings,
          each string representing a line of text in the book.
    names: A list of characer names to search for.

    Returns a (name, line) tuple where "name" is the earliest-
    occurring character name, and "line" is the line number
    they were first mentioned."""

    # Enumerate each line in the book. Within the body of the loop,
    # i will be an automatically incremented counter, and line will
    # be each line of text.
    for i, line in enumerate(text):

        # Search the line of text for each of our names
        for name in names:
            # If we find a name, we're done - return it with the
            # current line number.
            if name in line:
                return (name, i + 1)
    return


if __name__ == "__main__":
    infile = open("jane_eyre.txt")

    text = []

    # Separate the book by lines of text
    for line in infile:
        text.append(line)

    name, line_num = name_find(text, ["Jane", "Sarah", "John", "Eliza"])

    print(name + " found on line " + str(line_num))