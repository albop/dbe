# download the text from wikipedia entry for European Central bank

import wikipedia

# get the text from wikipedia
text = wikipedia.page("European Central Bank").content  # get the text from wikipedia
print(text)  # print the text 

# count the number of times the word "inflation" appears
print(text.count("inflation"))  # count the number of times the word "inflation