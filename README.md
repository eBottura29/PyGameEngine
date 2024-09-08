## DOCUMENTATION IS CURRENTLY INCOMPLETE

# HOW TO RUN:
1. Run terminal_interface.py
2. Follow the instructions
3. Scripts are located in the scripts folder in the main directory
# SCRIPT STRUCTURE:
  -  There are 2 default functions present when you create a script. The start() and the update() functions. The start() function is executed once when the game starts. The update() function is executed every frame.
  -  You can also see that in the beginning of the script there is a import statement for the engine.py_game_engine module. It contains lots of cool and important stuff to create your own game in PyGameEngine.
# DECORATORS:
### ```@timer```:
> Measures execution time of a function
# FUNCTIONS:
### ```clamp(value, min_value, max_value)```
> Clamps the value between the minimum and maximum values
### ```lerp(start, end, t)```
> Linear interpolation between start and end with a factor of t
### ```map_value(value, start1, stop1, start2, stop2)```
> Maps a value from one range to another
### ```draw_circle(screen, color, position, radius)```
> Shortcut that draws a circle on the screen
### ```draw_rectangle(screen, color, position, size)```
> Shortcut that draws a rectangle on the screen
### ```random_float(min_value, max_value)```
> Generates a random float between a specified range
### ```sign(value)```
> Returns the sign of a value (-1 for negative, 1 for positive, 0 for zero)
### ```rect_collision(rect1, rect2)```
> Checks for collisions between two rectangles
> Both params should be Rect objects (explained later)
### ```circle_collision(circle1, cirlce2)```
> Checks for collisions between two circles
> Both params should be Circle objects (explained later)
# CLASSES:
## ``Color(r, g, b)``
> Color object with red, green and blue params. (regular RGB from 0 to 255)
> 
> colors.BLACK = ```rgb(0,0,0)```
> 
> colors.DARK_GRAY = ```rgb(85,85,85)```
> 
> colors.LIGHT_GRAY = ```rgb(170,170,170)```
> 
> colors.WHITE = ```rgb(255,255,255)```
> 
> colors.RED = ```rgb(255,0,0)```
> 
> colors.LIME = ```rgb(0,255,0)```
> 
> colors.BLUE = ```rgb(0,0,255)```
> 
> colors.YELLOW = ```rgb(255,255,0)```
> 
> colors.PINK = ```rgb(255,0,255)```
> 
> colors.LIGHT_BLUE = ```rgb(0,255,255)```
> 
> colors.GREEN = ```rgb(0,128,0)```
> 
> colors.PURPLE = ```rgb(128,0,128)```
> 
> colors.DARK_BLUE = ```rgb(0,0,128)```
> 
> colors.ORANGE = ```rgb(255,170,0)```
> 
> colors.BROWN = ```rgb(128,60,0)```
> 
> ### ```random()```
> > Returns a random color
> ### ```blend(other, ratio=0.5)```
> > Blends two colors based on a ratio
> ### ```to_hex(prefix="#")```
> > Converts color to hexadecimal string
> ### ```to_hsl(hue_angle=True)```
> > Converts RGB to HSL (Hue, Saturation, Lightness)
> ### ```get_tup()```
> > Returns the color as a tuple (r, g, b)
## ``Vector2(x, y)``
> Vector object in 2 dimensions.
