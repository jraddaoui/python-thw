ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "There should be 10 items in that list."

stuff = ten_things.split(' ') # convert string to list by whitespaces
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] # second one
print stuff[-1] # last one
print stuff.pop() # extract the last one
print ' '.join(stuff) # concatenate with whitespace
print '#'.join(stuff[3:5]) # concatenate only some items
