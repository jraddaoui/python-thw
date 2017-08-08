x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r displays the raw data, adding single quotes to the string
print "I said: %r." % x

# %s displays the string value
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Concatenating with + doesn't add a space like with ,
print w + e
print w, e
