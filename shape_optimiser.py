
import sympy as sym
import math
x,y,z,r,A,V,C,D = sym.symbols('x, y, z, r, A, V,C,D')

class shape_3d:
    def __init__(self, surface_area = A, volume = V, width = x, height = y, depth = z):
        """
        The initialiser function for 3d shapes. Just a skeleton containing the shapes properties as follows:
            > Surface area
            > Volume
            > Width
            > Height
            > Depth
            > Faces (Will be defined by other functions)
        The class is just used to inherit from other 3d shapes 
        """
        self.surface_area = surface_area
        self.volume = volume
        self.width = width
        self.height = height
        self.depth = depth
        self.faces = []
    def Show_Faces(self):
        """
        This function will display the faces on a given 3d shape
        """
        for x in self.faces:
            print(x.shape_name + "with area:" + x.area)
            if x.shape_name == "Circle":
                pass
            else:
                print("And angles:" + x.angles)

class shape_2d:
    """
    basic skeleton for a 2d shape 
    """
    def __init__(self, area = A, base = x, height = y, placeability = False):
        self.area = area
        self.base = base
        self.height = height
        self.placeability = placeability

class circle(shape_2d):
    """
    This class represents a given circle
    """
    def __init__(self, radius = r, circumference = c, placeability = True):
        self.radius = r
        self.circumference = C
        self.placeability = True
        self.area = sym.pi * (r ** 2)
        self.shape_name = "Circle"

class quadrilateral(shape_2d):
    """
    This class represents the common object of a quadrilatrial 
    """
    def __init__(self, base=x, height=y, placeability=True, angles = [sym.pi / 2, sym.pi / 2 , sym.pi / 2, sym.pi / 2], sides = [1 ,1 ,1 ,1]):
        self.angles = angles
        self.sides = sides
        self.area = self.calculate_area()
        super().__init__(base= base,height= height, placeability= placeability)
    def calculate_area(self):
        """
        This uses Bretshneider's formula
        """
        s = (sum(self.sides) / 2)
        return sym.sqrt((s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]) * (s - self.sides[3]) - math.prod(self.sides) * (sym.cos(self.angles[0] + self.angles[2]) ** 2))

class rectangle(quadrilateral):
    """
    Class that creates a rectangle shape
    """
    def __init__(self, base=x, height=y, placeability=True):
        super().__init__(base, height, placeability)
        angles = [sym.pi / 2, sym.pi / 2, sym.pi / 2, sym.pi / 2]
        print(self.base)
        self.sides = [self.base, self.height , self.base, self.height]
        print(self.sides)
        self.area = math.prod(self.sides)
        self.shape_name = "rectangle"




class cylinder(shape_3d):

    def __init__(self, surface_area=A, volume=V, width=x, height=y, depth=z, radius = r):
        """
        This class inherits from the 3d shape class, with added properties su
        """
        super().__init__(surface_area, volume, width, height, depth)
        self.radius = radius
        self.top = sym.pi * self.radius ** 2
        self.curved_surface = 2 * sym.pi * self.height * self.radius ** 2
        self.faces = [rectangle(base = sym.pi * 2 * self.radius, height = self.height)] + [circle(radius = radius, circumference = self.radius * 2 * sym.pi, placeability=True) for x in range (2)]
    def calculate_surface_area(self):
        self.surface_area = 2 * self.top + self.curved_surface
        return self.surface_area


test = cylinder(height= 50, radius= 4)

print(test.calculate_surface_area())

wickked = shape_3d(surface_area=5)


class cuboid(shape_3d):
    """
    This code is the code for creating a cubeboid object
    """
    def __init__(self, surface_area=A, volume=V, width=x, height=y, depth=z):
        """
        Passes most parameters back into 3d and then creats a list of objects for each side
        """
        super().__init__(surface_area, volume, width, height, depth)
        self.faces = [rectangle(base= width, height= height) for x in range(2)] + [rectangle(base=depth, height= height) for x in range(2)] + [rectangle(base=width, height=depth) for x in range(2)]
    def caculate_surface_area(self):
        """
        Returns the sum of all the areas of the 2d shapes
        """
        return sum(self.faces)

testcube = cuboid()
print(testcube.faces)
testcube.Show_Faces()
                           
class sphere(shape_3d):
    def __init__(self,radius=r,surface_area=A,volume=V,circumference=C,diameter=D):
        """
        Inherits from the 3d shape class, creates a spherical object
        """
        super().__init__(radius = r,surface_area,volume,circumference,diameter)
        self.radius = radius
        self.surface_area = 4*sym.pi*self.radius**2
        self.volume = (4/3)*sym.pi*self.radius**3
        self.circumference = 2*sym.pi*self.radius
        self.diameter = 2*self.radius
    def calculate_surface_area(self):
        surface_area = 4*sym.pi*self.radius**2
        return self.surface_area

testsphere = sphere(radius=3)
print(testsphere.calculate_surface_area())

"""
Harry can add a choosen side attriubte to the 3d shape class and next week we will need a meeting. I would like Callum and Niko to start working on the readme documentation
"""
