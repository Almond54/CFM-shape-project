# shape_creator

Functionality to model 3D shapes and create new objects from existing ones

## Tutorial

In this section, we will show the general use of shape_creator

The idea of shape_creator is to model 3D shapes allowing for easier algebraic manipuluation of them.
### Creating a cube
First we're going to import the module and create a basic cuboid

```python
import shape_creator
Example_Cuboid = shape_creator.cuboid(2, 4, 6)
```

This is a cuboid with width 2, height 4, and depth 6.

### Calcuating parameters of 3D objects

We can use shape_creator to calculate some additional parameters for this cuboid

```python
Example_Cuboid.calcuate_surface_area()
```

This will return the following:

```python
88
```
We can also do the same for a volume on a 3D shape by the following
```python
Example_Cuboid.volume
```

This returns to us

```python
48
```
### Showing the faces on our cuboid
We can also show the faces of our cuboid

```python
Example_Faces_Cuboid = Example_Cuboid.Show_Faces()
```

This will return an array of faces that are in our cuboid:

```python
['0 A rectangle with sides [2, 4, 2, 4]',
 '1 A rectangle with sides [2, 4, 2, 4]',
 '2 A rectangle with sides [6, 4, 6, 4]',
 '3 A rectangle with sides [6, 4, 6, 4]',
 '4 A rectangle with sides [2, 6, 2, 6]',
 '5 A rectangle with sides [2, 6, 2, 6]']
```
### Creating a new 3D object 
Now let's make a new shape, a pyramid this time

```python
Example_Pyramid = shape_creator.rectangluar_based_pyramid(2, 6, 4)
```

This is a rectangle based pyramid with height 6 and a 2x4 rectangular base

We will  now put these two shapes together to create a new shape and add them together.

First, we will choose which face we want to be added together on each shape

to do this, we will first show faces to find our index, then use the select_face command

```python   
Example_Rectangle.Show_Faces()
Example_Rectangle.select_face(1)
Example_Pyramid.Show_faces()
Example_Pyramid.select_face(1)
```

We need the selected faces to be the same for (e.g. it is of the same 2D shape and has the same dimensions) this command, as they are here

let us now add them using the add method to create the new object

```python
NewObject = Example_Rectangle + Example_Pyramid
```

We now have our new object, and we can perform calculations on it such as show_faces and calculate_surface_area


## How
### How to create a shape

To create a shape, you simply use the command 

```python 
example_shape = shape_creator.(insert shape type here)()
```

where (insert shape type here) is the shape you wish to create, for example 

```python 
example_shape = shape_creator.cone
``` 

would create a cone

A list of shapes is as follows:

Sphere, Cuboid, Cone, Cylinder, Rectangular based pyramid, Circle, Circular sector, Quadrilateral (Rectangle is a subclass), Triangle

Now you can use this to perform other functions

### How to show faces

To show faces, you first take your created shape from before, then use the following command:
```python
example_shape.Show_Faces()
```

(where example_shape is a 3d shape)
which will return an array of shape objects which make up the faces of example_shape

### How to combine shapes
We will take our previous shapes and add them together

First, we will choose which face we want to be added together on each shape

to do this, we will first show faces to find our index, then use the select_face command

```python   
Example_Rectangle.Show_Faces()
Example_Rectangle.select_face(1)
Example_Pyramid.Show_faces()
Example_Pyramid.select_face(1)
```

We need the selected faces to be the same for this command, which is true here

let us now add them using the add method to create the new object

```python
NewObject = Example_Rectangle + Example_Pyramid
```

We now have our new object, and we can perform calculations on it such as show_faces and calculate_surface_area

## Explanations

### Uses of modelling 3D shapes in this way

shape_creator is a streamlined way to create compound objects through python. It allows for accurate calculations to be done about these shapes
that would otherwise be difficult and time-consuming to do by hand. Imagine combining a cylinder with a cone on each end. Calculating the surface
area of this object would be a difficult task for an average developer to do by hand. Shape_creator makes this simple for them to do, along with having
other functionality such as showing faces with parameters.

We hope that shape_creator would be able to help simulate optimizations to shapes aswell. For example, you could use shape_creator to measure how changing parameters for shapes can affect the way a shape acts mathematically. For example, disciplines such as engineering and architechture would be able to use this in order to 
measure the most efficient uses of materials to lower costs. 

It does this by modeling all the sides of a 3D shape as list of 2D shapes with area proptries and comparing these faces to add 3D shapes together 

### Optimisations used in the code

There are many ways in which the code is optimised. The main one is the way in which surface area is calculated. Instead of using long formulas for each
shape, it is an inherited function which sums the area of the faces of a 3D shape. Each shape's faces are created in its init method, and the area of any 2D shapes are created in their init methods. This way, the formulas are simplified and the calculate_surface_area() method is less likely to cause lag through more difficult calculations.

We also use Bretshneider's formula to calculate the area of a quadrilateral. This formula is as follows:

```python
s = (sum(self.sides) / 2)
return sym.sqrt((s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]) * (s - self.sides[3]) - math.prod(self.sides) * (sym.cos(self.angles[0] + self.angles[2]) ** 2))
```

This allows the code to not require multiple different formulas for different quadrilateral areas, and makes it much easier to add new quadrilaterals to the library
in later updates.

## References

https://mathworld.wolfram.com/BretschneidersFormula.html - Explanation of Bretshneider's formula


### List of functionality - shapes included

#### 3D
Sphere, Cuboid, Cone, Cylinder, Rectangular based pyramid

#### 2D
Circle, Circular sector, Quadrilateral (Rectangle is a subclass, room for expansion), Triangle

### List of functionality - functions of shapes
3D shapes - Calculate_Surface_Area, Show Faces, add (contains auxilliary functions such as compare_faces and create_new_object))

