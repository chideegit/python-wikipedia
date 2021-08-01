import wikipedia # pip install wikipedia

search_word = input("Enter a word: ") # Enter a word you want to search for
result =  wikipedia.summary(search_word) # Search happens here!

print(result) # The result gets printed to the screen here
