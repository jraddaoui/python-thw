my_name = 'Radda'
my_age = 33
my_height = 1.80
my_weight = 82
my_eyes = 'Brown'
my_teeth = 'Yellow'
my_hair = 'Brown'

print "I am %s." % my_name
print "I'm %.2f metres tall." % my_height
print "I'm %d kilograms heavy." % my_weight
print "Actually that's too heavy."
print "I have %s eyes and %s hair." % (my_eyes, my_hair)
print "My teeth are usually %s depending on the coffee." % my_teeth
print "If I add %d, %.2f, and %d I get %.2f." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

# Extra

print "I'm %.2f metres tall, the same as %.2f inches." % (
    my_height, my_height * 39.37)
print "I'm %d kilograms heavy, the same as %.1f pounds" % (
    my_weight, my_weight * 2.2)
