# Mehraneh 30062786
# AT2.5 - Question 2
# Create a code file that opens a text file named “news.txt” to write to it
# Writes an entire paragraph of text from a news article of your choice.
# You must close the file after you have written to it.

# Define a text variable
text = """Motoring News China-made $90k electric ute smashed.
Australia’s first electric utes are here – but at more than $90,000 a pop,
they don’t come cheap, among other issues.

May 8, 2014 · Trusted and independent source of local, national and world news.
In-depth analysis, business, sport, weather and more."""
# open to write the text in a text file. if the file doesn't exist, creat it. 
file = open("news.txt", "w")
# write the text in the file
file.write(text)
# close the file
file.close()
