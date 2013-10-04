# This python module is meant to be used along with the corresponding ipython notebook/blog post
# Visit www.caffeinateddata.com to find it.
from math import pi
class Stellar:
	"""
	Creates a planetary object for our solar-system
	"""
	def __init__(self, name, radius = None, location_from_sun = None):
		self.name = name
		self.radius = radius
		self.location_from_sun = location_from_sun

	def volume(self):
		"""
		Take the radius of a stellar obect and returns a volume
		"""
		if self.radius:
			return (4/3)*pi*self.radius**3
		else:
			return 'radius is not defined for this object'

class Asteroid(Stellar):
    """
    Creates an asteroid object, a subclass of Stellar
    """
    def __init__(self, name, a_axis, b_axis, c_axis):
        Stellar.__init__(self, name)
        self.a_axis = a_axis
        self.b_axis = b_axis
        self.c_axis = c_axis
    def volume(self):
        volume = (4/3)*pi*self.a_axis*self.b_axis*self.c_axis
        return volume
    

class Planet(Stellar):
    """
    Creates a planet class
    """
    def __init__(self, name, radius, location_from_sun, hospitable):
        Stellar.__init__(self, name, radius, location_from_sun)
        self.hospitable = hospitable
class Star(Stellar):
    """
    Creates a star class
    """
    def __init__(self, name, radius, classification, hospitable = False):
        Stellar.__init__(self, name, radius, location_from_sun = 0)
        self.classification = classification
        self.hospitable = hospitable 



class Recursive:
    """
    Creates a planetary object for our solar-system
    """
    def __init__(self):
        self.name = self