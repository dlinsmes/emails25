file = "demo text.txt"

#r is for reading the file (as opposed to writing)
fileContents = open(file, "r")

emails = []

for line in fileContents:
    #append everything in the line starting at index 2
    #bc index 0 is the classification number
    #and index 1 is a space
    emails.append(line[2:])
    print(line)

print("iteration 2")
for line in fileContents:
    print(line)

#seek() resets the cursor for a file if you need to
#go through it again
fileContents.seek(0)
print("iteration 3")
for line in fileContents:
    print(line)

#iterate through each email
for email in emails:
    print(email)

#save each word in email 0 to wordlist
wordList = emails[0].split()
for word in wordList:
    print(word)

#create a dictionary - like a list but a string
#can be used as an index ("key")