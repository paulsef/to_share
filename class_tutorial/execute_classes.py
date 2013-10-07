# We start off by importing the learnClasses module. This contains the class Stellar
# When  you're ready to move on, remove the docstrings (""") to see the next output
import learnClasses as lc

# initializing our fist stellar object
stellar1 = lc.Stellar(name ='Unknown_object', radius = 6371, location_from_sun = 3)
print stellar1.radius, stellar1.name, stellar1.volume()

"""
# exploring self (how philisophical)
recur = lc.Recursive()
print recur.name == recur.name.name == recur.name.name == recur.name.name.name
"""

"""
# using subclasses
ast1 = lc.Asteroid('halebop', 2, 3, 4)
print str(ast1.name) +' has volume ' + str(ast1.volume())
"""

"""
planet1 = lc.Planet(name = "Mars", radius = 6371, location_from_sun = 4, hospitable = False)
planet2 = lc.Star(name = "Sun", radius = 695500, classification = "yellow dwarf")
average_sa = (planet1.volume() + planet2.volume())/2
print 'the average volume of ' + str(planet1.name) + ' and ' + str(planet2.name) + ' is ' + str(average_sa)
"""