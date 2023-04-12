import sympy as sym
import math
x,y,z,r,A,V,C,D = sym.symbols('x, y, z, r, A, V,C,D')

class shape_3d:
    def __init__(self, faces = [], volume = V, width = x, height = y, depth = z):
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
        self.width = width
        self.height = height
        self.depth = depth
        self.faces = faces
        self.selected_face = None
    def Show_Faces(self):
        """
        This function will display the faces on a given 3d shape
        """
        Faces = []
        for index,x in enumerate(self.faces):
            if x.shape_name == "Circle":
                Faces.append(index+ " with " + x.shape_name + "and radius" + str(x.radius))
            else:
                Faces.append(x.shape_name + " with sides: " + str(x.sides) + "And angles:" + str(x.angles))
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
    def choose_face(self, index):
        """
        This method allows you to choose your the face you are performing addition on
        """
        try: self.selected_face = self.faces[index]
        except IndexError: pass
    def create_new_object(self, other):
        """
        This is the algorithm to format the new shape being created so it can be added
        """
        face_list_one = self.faces
        face_list_two = other.faces
        face_list_one.remove(self.selected_face)
        face_list_two.remove(other.selected_face)
        combined_face_list = face_list_one + face_list_two
        total_volume = self.volume + other.volume
        return shape_3d(faces=combined_face_list, volume= total_volume)
    def calcuate_surface_area(self):
        """
        Just returns the sum of all the areas of the 2d shapes in the faces list
        """
        return sum(self.faces)

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
    def __init__(self, radius = r, circumference = C, placeability = True):
        self.radius = r
        self.circumference = C
        self.placeability = True
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
        self.sides = [self.base, self.height , self.base, self.height]
        self.area = math.prod(self.sides)
        if self.base == self.height:
            self.shape_name = "square"
        else:
            self.shape_name = "rectangle"
    def __dir__(self):
        return [self.sides]




class cylinder(shape_3d):

    def __init__(self, surface_area=A, width=x, height=y, depth=z, radius = r):
        """
        This class inherits from the 3d shape class, with added properties su
        """
        super().__init__(surface_area, width, height, depth)
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
    def caculate_surface_area(self):
        """
        Returns the sum of all the areas of the 2d shapes
        """
        return sum(self.faces)

testcube = cuboid()
testcube.Show_Faces()                    
class sphere(shape_3d):
    def __init__(self,radius=r):
        """
        Inherits from the 3d shape class, creates a spherical object
        """
        self.radius = radius
        self.surface_area = 4*sym.pi*self.radius**2
        self.volume = (4/3)*sym.pi*self.radius**3
        self.circumference = 2*sym.pi*self.radius
        self.diameter = 2*self.radius
        super().__init__(radius=r, SA=4*sym.pi*self.radius**2, V=(4/3)*sym.pi*self.radius**3, C=2*sym.pi*self.radius, D=2*self.radius)
    def calculate_surface_area(self):
        surface_area = 4*sym.pi*self.radius**2
        return self.surface_area
    def Show_Faces(self):
        print("Sphere does not have faces")

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