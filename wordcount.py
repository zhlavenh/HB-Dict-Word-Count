"""Count words in file."""

def word_count(filename):

    file_name = open(filename, "r")

    word_counts = {}
    words = []

    for line in file_name:
        line = line.splitlines(keepends=False)
        line = " ".join(line)
        lines = line.split(" ")

        words = words + lines

    file_name.close()


    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

print(word_count('twain.txt'))
    


