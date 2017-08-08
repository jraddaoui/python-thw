def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!\n" % boxes_of_crackers


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Extra
def total_items(a_count, b_count):
    print "You have %d total items!" % (a_count + b_count)


total_items(20, 30)
total_items(amount_of_cheese, amount_of_crackers)
total_items(10 + 20, 5 + 6)
total_items(amount_of_cheese + 100, amount_of_crackers + 1000)
