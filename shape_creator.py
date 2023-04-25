import sympy as sym
import math
import copy
a,x,y,z,r,A,V,C,D = sym.symbols('a,x, y, z, r, A, V,C,D')

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
            Faces.append(str(index) + " " + repr(x))
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
        face_list_one = copy.copy(self.faces)
        face_list_two = copy.copy(other.faces)
        face_list_one.remove(self.selected_face)
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
    This class represents a given circle only requires radius
    """
    def __init__(self, radius = r, placeability = True):
        self.radius = radius
        self.circumference = 2*radius*sym.pi
        self.placeability = placeability
        self.area = sym.pi * (radius ** 2)
        self.shape_name = "Circle"

    def __repr__(self):
        return "A " + self.shape_name + " with radius " + str(self.radius)
    
    def __eq__(self, other):
        """
        Overrided so comparing two different cirlces 
        """
        if type(self) == type(other):
            return self.radius == other.radius
        else:
            return False
    def __mul__(self, other):
        """
        Could be expanded a new function for creating a sector of circle
        """
        return circular_sector(self.radius, other, self.placeability)

class circular_sector(shape_2d):
    """
    Class for a circular segment requires an angle and a radius
    """
    def __init__(self, radius=r, angle=a, placeability = True):
        super().__init__(placeability)
        self.radius = radius
        self.perimiter = radius * angle + 2 * radius
        self.angle = angle
        self.area = (angle / (2*sym.pi)) * sym.pi * self.radius ** 2
    def __repr__(self):
        return "A circular sector with radius " + str(self.radius) + " and angle " + str(self.angle)
    def __eq__(self, other):
        """
        allows us to compare two different sectors
        """
        if type(self) == type(other):
            return self.radius == other.radius and self.angle == other.angle
        else:
            return False
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
        super().__init__(placeability)
        self.base = base
        self.height = height
        self.angles = [sym.pi / 2, sym.pi / 2, sym.pi / 2, sym.pi / 2]
        self.sides = [self.base, self.height , self.base, self.height]
        self.area = base * height
        if self.base == self.height:
            self.shape_name = "square"
        else:
            self.shape_name = "rectangle"
    def __eq__(self, other):
        if type(self) == type(other):
            return self.sides == other.sides
        else:
            return False
    def __repr__(self):
        return "A " + self.shape_name + " with sides " + str(self.sides)



class cylinder(shape_3d):

    def __init__(self, height=y, radius = r):
        """
        This class inherits from the 3d shape class, with added properties 
        """
        super().__init__()
        self.height = height
        self.radius = radius
        self.top = sym.pi * self.radius ** 2
        self.volume = self.radius ** 2 * sym.pi * self.height
        self.curved_surface = 2 * sym.pi * self.height * self.radius ** 2
        self.faces = [rectangle(base = sym.pi * 2 * self.radius, height = self.height)] + [circle(radius = radius, placeability=True) for x in range (2)]
    def calculate_surface_area(self):
        self.surface_area = 2 * self.top + self.curved_surface
        return self.surface_area

class cuboid(shape_3d):
    """
    This code is the code for creating a cubeboid object
    """
    def __init__(self, width=x, height=y, depth=z):
        """
        Passes most parameters back into 3d and then creats a list of objects for each side
        """
        super().__init__()
        self.width = width
        self.height = height
        self.depth = depth
        self.volume =   width * height * depth
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

def compare_faces(face_one, face_two):
    if face_one == face_two and (face_one.placeability and face_two.placeability):
        return True
    else:
        return False
    

class triangle(shape_2d):
    def __init__(self, angles = [sym.pi / 3, sym.pi / 3, sym.pi / 3], sides = [1, 1, 1], placeability = True):
        super().__init__(placeability)
        self.angles = angles
        self.sides = sides
        self.shape_name = "Triangle"
        self.area = 0.5 * sides[0] * sides[1] * sym.sin(angles[2])
    def __repr__(self):
        return "A " + self.shape_name + " with sides " + str(self.sides) + " and " + str(self.angles)
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.angles == other.angles and self.sides == other.sides
        else:
            return False

class rectangluar_based_pyramid(shape_3d):
    """
    class holding all the data for rectangluar_based_pyramid
    """
    def __init__(self, width=x, height=y, depth = z):
        self.width = width
        self.height = height
        self.depth = depth
        self.volume = self.width ** 2 * self.height / 3
        self.faces = [rectangle(base= width, height= depth)] + [self.get_triangle_faces(width, height, depth= depth) for x in range(2)] + [self.get_triangle_faces(width= depth, height= height, depth= width) for x in range(2)]
    def get_triangle_faces(self, width, height, depth):
        """
        we know the triangles for the retangular based pyramid will be isoleces so this function creates the triangles and returns in into a list for the faces array
        depth is the mesurement going inwards from the triangle we are calculating
        """
        slant_height = sym.sqrt((depth/2) ** 2 + height ** 2)
        pyramid_triangle = triangle([sym.pi - 2 * sym.atan(slant_height/(width/2)), sym.atan(slant_height/(width/2)), sym.atan(slant_height/(width/2))], [width ,sym.sqrt((width/2)**2 + slant_height ** 2), sym.sqrt((width/2)**2 + slant_height ** 2)])
        return pyramid_triangle
   
class cone(shape_3d):
    def __init__(self, radius=r, height=y):
        super().__init__()
        self.radius = radius
        self.height = height
        self.faces = [circle(radius=radius), circle(radius=sym.sqrt(radius ** 2 + height ** 2), placeability=False) * (2 * sym.pi * radius/sym.sqrt(radius ** 2 + height ** 2))]
        self.volume = (1/3) * sym.pi * self.height * (self.radius ** 2)


