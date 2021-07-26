# Import requests
import requests as req
import random

# Fetch JSON from https://poetrydb.org/title
r = req.get('https://poetrydb.org/title')

# Parse request body into a Object
poems = r.json()

# Get the array with name 'titles' from poems object.
titles = poems['titles']

# Choose a random title from titles array.
title = titles[random.randint(0, len(titles) - 1)]

# Fetch JSON From https://poetrydb.org/title/{title}
re = req.get('https://poetrydb.org/title/' + title)

# Parse request body into a Object
poem = re.json()[0]

# Get author of the poem
author = poem['author']

# Get title of the poem
title = poem['title']

# Get the array of lines in poem and join all the lines with a new line character
text = '\n'.join(poem['lines'])

# Print out the poem
print('Author: ' + author)
print('Title: ' + title)
print('Poem: ' + "\n" + text)