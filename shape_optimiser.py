import sympy as sym
import math
x,y,z,r,A,V,C,D = sym.symbols('x, y, z, r, A, V,C,D')

class shape_3d:
    def __init__(self, faces = [], volume = V):
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
        self.volume = volume
        self.faces = faces
        self.selected_face = None
    def Show_Faces(self):
        """
        This function will display the faces on a given 3d shape
        """
        Faces = []
        for index,x in enumerate(self.faces):
            if x.shape_name == "Circle":
                Faces.append(index+ " with " + x.shape_name + "and radius " + str(x.radius))
            else:
                Faces.append(str(index) + " " + x.shape_name + " with sides: " + str(x.sides) + "And angles:" + str(x.angles))
        return(Faces)
    def __add__(self, other):
        """
        Boogie Method on adding different 3d shapes to each other
        """
        side_one = self.selected_face
        side_two = other.selected_face
        if compare_faces(side_one,side_two) == True:
            return self.create_new_object(other)
        else:
            return self
    def select_face(self, index):
        """
        This method allows you to choose your the face you are performing addition on
        """
        try: self.selected_face = self.faces[index]
        except IndexError: pass
    def create_new_object(self, other):
        """
        This is the algorithm to format the new shape being created so it can be added
        it is not meant to be run normally
        """
        face_list_one = self.faces
        face_list_two = other.faces
        face_list_one.remove(self.selected_face)
        print(face_list_one)
        face_list_two.remove(other.selected_face)
        combined_face_list = face_list_one + face_list_two
        total_volume = self.volume + other.volume
        return shape_3d(faces=combined_face_list, volume= total_volume)
    def calcuate_surface_area(self):
        """
        Just returns the sum of all the areas of the 2d shapes in the faces list
        """
        return sum(face.area for face in self.faces)

class shape_2d:
    """
    basic skeleton for a 2d shape 
    """
    def __init__(self, placeability = False):
        self.placeability = placeability


class circle(shape_2d):
    """
    This class represents a given circle
    """
    def __init__(self, radius = r, placeability = True):
        self.radius = radius
        self.circumference = 2*radius*sym.pi
        self.placeability = placeability
        self.area = sym.pi * (r ** 2)
        self.shape_name = "Circle"


    
    def __dir__(self):
        """
        Overrided so comparing two different shapes 
        """
        return [self.radius]

class quadrilateral(shape_2d):
    """
    This class represents the common object of a quadrilatrial 
    """
    def __init__(self, placeability=True, angles = [sym.pi / 2, sym.pi / 2 , sym.pi / 2, sym.pi / 2], sides = [1 ,1 ,1 ,1]):
        self.angles = angles
        self.sides = sides
        self.perimeter = sum(sides)
        self.area = self.calculate_area()
        super().__init__(placeability= placeability)
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
        self.sides = [self.base, self.height , self.base, self.height]
        self.area = math.prod(self.sides)
        if self.base == self.height:
            self.shape_name = "square"
        else:
            self.shape_name = "rectangle"
    def __dir__(self):
        return [self.sides]




class cylinder(shape_3d):

    def __init__(self, height=y, radius = r):
        """
        This class inherits from the 3d shape class, with added properties su
        """
        super().__init__()
        self.height = height
        self.radius = radius
        self.top = sym.pi * self.radius ** 2
        self.volume = self.radius ** 2 * sym.pi * self.height
        self.curved_surface = 2 * sym.pi * self.height * self.radius ** 2
        self.faces = [rectangle(base = sym.pi * 2 * self.radius, height = self.height)] + [circle(radius = radius, circumference = self.radius * 2 * sym.pi, placeability=True) for x in range (2)]
    def calculate_surface_area(self):
        self.surface_area = 2 * self.top + self.curved_surface
        return self.surface_area

test = cylinder(height= 50, radius= 4)

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
                 
class sphere(shape_3d):
    def __init__(self,radius=r):
        """
        Inherits from the 3d shape class, creates a spherical object
        """
        super().__init__()
        self.radius = radius
        self.volume = (4/3)*sym.pi*self.radius**3
        self.circumference = 2*sym.pi*self.radius
        self.diameter = 2*self.radius
    def calculate_surface_area(self): 
        return 4*sym.pi*self.radius**2
    def Show_Faces(self):
        return"Sphere does not have faces"

#testsphere = sphere(radius=3)
#print(testsphere.calculate_surface_area())

"""
Harry can add a choosen side attriubte to the 3d shape class and next week we will need a meeting. I would like Callum and Niko to start working on the readme documentation
"""

def compare_faces(face_one, face_two):
    if dir(face_one) == dir(face_two):
        return True
    else:
        return False
class triangle(shape_2d):
    def __init__(self, placeability=True, angles = [sym.pi / 3, sym.pi / 3, sym.pi / 3], sides = [1, 1, 1]):
        super().__init__(placeability)
        self.angles = angles
        self.sides = sides
        self.area = 0.5 * sides[0] * sides[1] * sym.cos(angles[2])

class square_based_pyramid(shape_3d):

    def __init__(self, width=x, height=y, depth = z):
        self.width = width
        self.height = height
        self.depth = depth
        self.volume = self.width ** 2 * self.height / 3
        self.faces = [rectangle(width = width, height= height)]
    def calculate_surface_area(self):
        self.surface_area  = (2 * (sym.sqrt(3)) + self.width * 2)
        return self.surface_area
   
class cone(shape_3d):
    def __init__(self, radius=r, height=y):
        super().__init__()
        self.faces = []
        self.radius = radius
        self.height = height
        self.volume = (1/3) * sym.pi * self.height * (self.readius ** 2)
    def calculate_surface_area(self):
        self.surface_area = (sym.pi * self.radius ** 2) + (sym.pi * self.radius * (sym.sqrt((self.radius ** 2) + (self.height ** 2))))