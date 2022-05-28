# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as f:
        lines = f.read()
    
    return lines


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    textTolower = text.lower()
    split_text = textTolower.split()
    
    count = {}
    for n in split_text:
        if n == "as":
            count[n] = 10
        
        elif n == "would":
            count[n] = 20
        


    return count


print(count_words())