import sys
 
# Create a dictionary to map words to counts
wordcount = dict()
 
# Get input from stdin
for line in sys.stdin:
    #Remove spaces from beginning and end of the line
    line = line.strip()
 
    # parse the input from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue
 
    try:
        wordcount[word] = wordcount[word]+count
    except:
        wordcount[word] = count
 
# Write the tuples to stdout
# Currently tuples are unsorted
for word in wordcount.keys():
    print('%s\t%s'% ( word, wordcount[word] ))