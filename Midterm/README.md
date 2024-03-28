**Midterm**

**Phase 1**
- I drew a person on my graph paper that consisted of a circle as the head, a triangle as the clothing, and 4 rectangles that make up the arms and legs.

**Phase 2**
- First, I used the "eye" example from class to begin my sketch. I played around with the circles that you had already provided and deleted then altered a lot of the code. I began my sketch with a circle at the top middle of the screen and used the code:
def draw():
background(204)
fill(255)
ellipse(50, 25, 30, 30)
fill(0)

- I looked on processing.com to find the rules for sketching a triangle which are: "triangle(x1, y1, x2, y2, x3, y3)"
- 	Whenever I sketch the triangle on its own it is fine, but when I try and add it to the already coded circle, the sketch goes blank.
- Added code:
def setup():
    size(100, 100)
    noStroke()
    - Added after looking at "eye" example again
- messed around with coordinates for a while and finally got an off centered fully shaded triangle.
- These are my even triangle coordinates:
  triangle(30, 80, 50, 40, 70, 80)
    fill(0)
- Added in a rectangle from one of your code examples, messed around with coordinates to match my sketch.
- Added a second rectangle for the second arm.
- Added rectangles for legs
  rect(55, 65, 2 , 30)
  rect(42, 65, 2 , 30)
- Cannot figure out how to make the fill white on arms and legs because every time I write "fill(0)" nothing happens.
  - Ok, changed the "fill (0)" to coming before the rectangle code and it worked.
  - Altered the rectangle coordinates to fit with the filled triangle and non filled arms and legs.
- I think I finished!

**Phase3**
- I added functions drawObject, size, setup, scale, push, and pop.
  - Default gave me my sketch but very small at the lower left of the screen.
- Edited the parameters so the sketch would be large and centered.
- Had to removed "background" because my objects were being hidden behind the background.

**Phase 4**
- Watched this youtube video (https://www.youtube.com/watch?v=ugYuWAQ25kA&ab_channel=JohnPark) and it made sense, but my code just doesn't seem to work. I think there is something wrong with my syntax? Every time I try to write a for loop i get the error "Maybe there's an unclosed paren or quote mark somewhere before this line?"
