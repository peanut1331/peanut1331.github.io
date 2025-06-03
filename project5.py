'''
Jaiden Duke
Project Variation #1
'''

"""
Improvements from Original:
1. STRUCTURE: Broke down draw_scene() into smaller functions:
   - draw_house() with components (base, roof, door, windows)
   - draw_sun()
   - draw_cloud() (reusable for multiple clouds)

2. REUSABILITY: Created generalized draw_cloud() function that:
   - Uses parameters for position/size
   - Draws multiple circles in one call
   - Replaced hardcoded cloud drawing

3. SCENE ENHANCEMENT: Added more clouds (total 6) to demonstrate:
   - How refactored code enables easy expansion
   - Reuse of draw_cloud() with different positions

4. CODE QUALITY:
   - Eliminated duplicate drawing code
   - Improved readability"""


import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen

def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()

def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()

def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    original_heading = t.heading()
    
    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)
    
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_scene(t):
    """Draw a colorful scene with various shapes"""
    # Set background color
    screen = t.getscreen()
    screen.bgcolor("skyblue")


# --------------------------
# Refactored Drawing Helpers
# --------------------------

def draw_house(t, x, y):
    """Draw a house with a rectangular base, triangular roof, door, and windows."""
    # House base
    jump_to(t, x, y)
    t.setheading(0)
    draw_rectangle(t, 200, 400, fill_color="red")

    # Roof
    jump_to(t, x, y)
    t.setheading(0)
    draw_triangle(t, 200, fill_color="brown")

    # Door
    jump_to(t, x + 80, y - 146)
    t.setheading(0)
    draw_rectangle(t, 50, 80, fill_color="yellow")

    # Left window
    jump_to(t, x + 30, y - 20)
    t.setheading(0)
    draw_square(t, 30, fill_color="lightblue")

    # Right window
    jump_to(t, x + 140, y - 20)
    t.setheading(0)
    draw_square(t, 30, fill_color="lightblue")


def draw_sun(t, x, y):
    """Draw the sun at a specified position"""
    jump_to(t, x, y)
    t.setheading(0)
    draw_circle(t, 40, fill_color="yellow")


def draw_cloud(t, x, y, size=1.0):
    """Draw a cloud made of multiple overlapping circles"""
    jump_to(t, x, y)
    t.pencolor("white")
    positions = [
        (0, 0), (size * 15, size * 10), (size * 30, 0),
        (size * 45, size * 5), (size * 60, 0)
    ]
    for pos_x, pos_y in positions:
        jump_to(t, x + pos_x, y + pos_y)
        draw_circle(t, size * 20, "white")


# --------------------------
# Refactored Main Scene
# --------------------------

def draw_scene(t):
    """Draw a colorful scene with house, sun, and clouds"""
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    draw_house(t, -100, -100)
    draw_sun(t, 200, 150)

    # Clouds
    draw_cloud(t, -200, 140, size=1)
    draw_cloud(t, -100, 180, size=1)
    draw_cloud(t , 150, 120, size=1)
    draw_cloud(t, -250, 100, size=1)
    draw_cloud(t, 0, 200, size=1)
    draw_cloud(t, 250, 160, size=1)


def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

if __name__ == "__main__":
    main()



