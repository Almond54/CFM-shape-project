import shape_creator
import sympy as sym
x,y,z = sym.symbols("x,y,z")

def test_circle():
    CircleTestObject = shape_creator.circle(2, True)
    assert CircleTestObject.radius == 2, "did not return radius correctly"
    
def test_rectangle():
    RectangleTestObject = shape_creator.rectangle(2, 4, True)
    assert RectangleTestObject.area == 8, "Did not calculate area correctly"
    assert RectangleTestObject.sides == [2,4,2,4], "Sides did not initialize correctly"

def test_cylinder():
    CylinderTestObject = shape_creator.cylinder(8, 2)
    CylinderTestArray = [shape_creator.rectangle(base = 4 * sym.pi, height = 8)] + [shape_creator.circle(radius = 2, placeability=True) for x in range (2)]
    assert CylinderTestObject.faces == CylinderTestArray, "Faces were not correct"

def test_sphere():
    SphereTestObject = shape_creator.sphere(2)
    assert SphereTestObject.Show_Faces() == "Sphere does not have faces", "Sphere apparently has faces?"

def test_square_pyramid():
    PyramidTestObject = shape_creator.rectangluar_based_pyramid(2,2,2)
    slant_height = sym.sqrt((2/2) ** 2 + 2 ** 2)
    assert PyramidTestObject.calcuate_surface_area() == 2 * 2 + 2*sym.sqrt((2/2) ** 2 + 2 ** 2) + 2*sym.sqrt((2/2) ** 2 + 2 ** 2), "Surface area is WRONG"
    assert PyramidTestObject.faces == [shape_creator.rectangle(base= 2, height= 2)] + [shape_creator.triangle([sym.pi - 2*sym.atan(slant_height/(2/2)), sym.atan(slant_height/(2/2)), sym.atan(slant_height/(2/2))], [2, sym.sqrt((2/2)**2 + slant_height ** 2), sym.sqrt((2/2)**2 + slant_height ** 2)]) for x in range(4)], "The expected faces of a square based priamid did not match the returned value"

def test_cone():
    ConeTestObject = shape_creator.cone(2, 2)
    assert ConeTestObject.calcuate_surface_area() == (sym.pi * 2 ** 2) + (sym.pi * 2 * (sym.sqrt((2 ** 2) + (2 ** 2)))), "Surface area is wrong"
    assert ConeTestObject.faces == [shape_creator.circle(2), shape_creator.circle(radius=sym.sqrt(2 ** 2 + 2 ** 2), placeability=False) * (2 * sym.pi * 2/sym.sqrt(2 ** 2 + 2 ** 2))], "Faces displaying wrong"

def test_dupe():
    """
    This tests for an error why trying to create a new object by adding the same object together
    """
    CubeDupeTestObject = shape_creator.cuboid()
    CubeDupeTestObject.select_face(3)
    DoubleCubeTestObject = CubeDupeTestObject + CubeDupeTestObject
    assert DoubleCubeTestObject.calcuate_surface_area() == 4 * x * y + 4 * x * z + 2 * y * z , "Error with the dupe surface area calacuation"

test_sphere()
test_circle()
test_rectangle()
test_cylinder()
test_square_pyramid()
test_cone()
test_dupe()
