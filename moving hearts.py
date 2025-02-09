import turtle
import time

def draw_heart(t, size, color):
    """Draws a heart with the given size and color."""
    t.fillcolor(color)
    t.begin_fill()
    t.left(50)
    t.forward(size)
    t.circle(size / 2, 180)
    t.right(100)
    t.circle(size / 2, 180)
    t.forward(size)
    t.end_fill()
    t.setheading(0)  # Reset orientation

def move_heart(t, x, y):
    """Moves the turtle to a new position."""
    t.penup()
    t.goto(x, y)
    t.pendown()

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Moving Hearts")
screen.tracer(0)  # Turn off animation for smoother updates

# Turtle setup
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.hideturtle()

# Define pastel colors
pastel_colors = ["#FFB6C1", "#FFDAB9", "#FFFACD", "#E0FFFF", "#DDA0DD"]

# Create moving hearts
hearts = []
size = 100
y_positions = [-200, -150, -100, -50, 0]  # Starting positions for hearts

# Initialize hearts
for i, color in enumerate(pastel_colors):
    heart = turtle.Turtle()
    heart.speed(0)
    heart.hideturtle()
    heart.color(color)
    heart.penup()
    heart.goto(0, y_positions[i])
    hearts.append((heart, size, color))
    size -= 20

# Animation loop
while True:
    for heart, size, color in hearts:
        heart.clear()  # Clear previous heart
        draw_heart(heart, size, color)
        x, y = heart.position()
        heart.goto(x, y + 5)  # Move the heart up

        # Reset position if it moves off the screen
        if y > 300:
            heart.goto(0, -300)

    screen.update()  # Update the screen
    time.sleep(0.05)  # Pause for a short time
