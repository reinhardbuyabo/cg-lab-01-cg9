import cairo
import math

# Set up the canvas
WIDTH, HEIGHT = 400, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set a white background
context.set_source_rgb(1, 1, 1)  # RGB for white background
context.paint()

# Set line width for all shapes
context.set_line_width(1.5)

# Draw house base using lines (outline with blue)
context.set_source_rgb(0, 0, 1)  # Blue color for house outline
# Move to the start point of the house (bottom left)
context.move_to(100, 300)
context.line_to(100, 200)  # Left side
context.line_to(75, 200)
context.line_to(75, 150)
context.line_to(325, 150)
context.line_to(325, 200)
context.line_to(300, 200)
context.line_to(300, 300)  # Right side
context.line_to(100, 300)  # Bottom side (close the rectangle)
context.stroke()

# Draw dome roof (semi-circle with blue outline)
context.arc(200, 150, 80, math.pi, 2 * math.pi)  # x, y, radius, start_angle, end_angle
context.stroke()

# Draw door (rectangle with green outline)
context.set_source_rgb(0, 1, 0)  # Green color for door outline
context.rectangle(175, 220, 50, 80)
context.stroke()


context.set_source_rgb(0, 0, 1)
context.arc(210, 275, 3, 0, 2 * math.pi)  
context.fill()


context.set_source_rgb(0, 1, 0)  # Green color for window outlines
context.move_to(120, 190)  # Top-left of left window (moved up)
context.line_to(120, 240)  # Left side (increased height)
context.line_to(160, 240)  # Bottom side
context.line_to(160, 190)  # Right side
context.line_to(120, 190)  # Top side (closing the window)
# Right window
context.move_to(240, 190)  # Top-left of right window (moved up)
context.line_to(240, 240)  # Left side (increased height)
context.line_to(280, 240)  # Bottom side
context.line_to(280, 190)  # Right side
context.line_to(240, 190)  # Top side (closing the window)
context.stroke()

context.set_source_rgb(0, 0, 1)
# Draw cross panes for left window
context.move_to(120, 215)
context.line_to(160, 215)  # Horizontal line
context.move_to(140, 190)
context.line_to(140, 240)  # Vertical line
context.stroke()

# Draw cross panes for right window
context.move_to(240, 215)
context.line_to(280, 215)  # Horizontal line
context.move_to(260, 190)
context.line_to(260, 240)  # Vertical line
context.stroke()

# Draw crescent moon
# Outer moon (yellow circle
context.set_source_rgb(1, 0.85, 0)  # Yellow color for the outer crescent
context.arc(300, 50, 30, 0, 2 * math.pi)  # Outer moon (centered on 300,100)
context.fill_preserve()

context.set_source_rgb(0, 0, 1)  # Blue outline for crescent moon
context.stroke()

# Inner moon (white circle shifted to the right)
context.set_source_rgb(1, 1, 1)  # White color to carve the crescent
context.arc(310, 50, 30, 0, 2 * math.pi)  # Inner moon, shifted right to create crescent
context.fill()

# Save the result to a file
surface.write_to_png("2d_house.png")

print("Drawing completed!")