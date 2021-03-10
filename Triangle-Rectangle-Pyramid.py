### All Rights Reserved ###

#Copyright (c) ${Triangle-Rectangle-Pyramid.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def cube_perimeter(self):
        return self.length * 12

    def volume(self):
        face_area = super().area()
        return face_area * self.length


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height


class Pyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height

        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):  # SquarePyramid
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area

    def area_3(self):
        perimeter = super().perimeter()
        triangle_area = super().tri_area()
        return 0.5 * perimeter * self.slant_height + triangle_area

    def volume(self):
        base_area = super().area()
        return 1 / 3 * base_area * self.slant_height


a = Rectangle(2, 5)
print('Rectangle Area: ', a.area())
print("Rectangle Perimeter: ", a.perimeter())
print("#############")

b = Square(5)
print('Square Area:', b.area())
print("Square Perimeter: ", b.perimeter())
print("##################")

c = Cube(3)
print("Cube Surface Area: ", c.surface_area())
print("Cube Volume: ", c.volume())
print("Cube Edge Perimeter: ", c.cube_perimeter())
print("##################")

d = Triangle(5, 10)
print("Triangle Area: ", d.tri_area())
print("##################")

e = Pyramid(5, 10)
print("Pyramid Area : ", e.area())
# OR
print("Pyramid Area 2: ", e.area_2())
# OR
print("Pyramid Area 3: ", e.area_3())

print("Pyramid Volume: ", e.volume())
print("##################")

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.