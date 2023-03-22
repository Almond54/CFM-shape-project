import sympy as sym
import shape_optimiser

def testsphere():
    """
    This function will test the sphere's surface area function and the show faces function
    Expected Outcomes: 16pi, and "Sphere does not have faces" 
    """
    TestObject = shape_optimiser.sphere(radius=2)
    assert(TestObject.calculate_surface_area(), 16*sym.pi)
    assert(TestObject.Show_Faces(), "Sphere does not have faces")

def testcuboid():
    """
    This function will test the cuboid's surface area and show faces functions
    Expected outcomes: 52, and showing six rectangle faces with areas 6, 8, and 12 (two of each)
    """
    TestObject = shape_optimiser.cuboid(52, 24, 2, 3, 4)
    assert(TestObject.caculate_surface_area(), 52)
    TestObject.Show_Faces()

def testcylinder():
    """
    This function will test the sphere's surface area and show faces functions
    Expected outcomes: 24pi, two circles and a rectangle"""
    TestObject = shape_optimiser.cylinder(24*sym.pi, 16*sym.pi, 2, 4, 2, 2)
    assert(TestObject.calculate_surface_area(), 24*sym.pi)
    TestObject.Show_Faces()

def testrectangle():
    """
    this function will test the rectangle's calculate area fucntion, and what it's shape name will be
    Expected outcome: 16 and square, 18 and rectangle"""
    TestSquare = shape_optimiser.rectangle(4, 4, True)
    assert(TestSquare.calculate_area(), 16), f""
    assert(TestSquare.shape_name, "square")
    testrectangle = shape_optimiser.rectangle(3, 6, True)
    assert(testrectangle.calculate_area(), 18)
    assert(testrectangle.shape_name, "rectangle")


testcuboid()
