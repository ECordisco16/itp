FINAL PROJECT LINK: https://ecordisco16.github.io/


First I wanted to get used to using this software/ code so I researched examples of how to insert images into the code and certain shapes I may want to add. (https://editor.p5js.org/claesjohnson/sketches/f0huO1Y4h)  (https://www.google.com/search?q=how+to+add+images+to+p5js&oq=how+to+add+photo+to+p5&gs_lcrp=EgZjaHJvbWUqCAgBEAAYFhgeMgYIABBFGDkyCAgBEAAYFhgeMggIAhAAGBYYHjIICAMQABgWGB4yDQgEEAAYhgMYgAQYigUyDQgFEAAYhgMYgAQYigUyDQgGEAAYhgMYgAQYigUyDQgHEAAYhgMYgAQYigXSAQkxMDQ5OWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:21864d3e,vid:friYx8xdLOE,st:0)
  Some of the commands I needed to use were not showing up, such as a spot to add the image that I wanted to call to in my code. I realized I had to make an account in order to add images.
- My first set of code was adding the main image into p5.js:
let AK

function preload (){
  AK = createImg('AKCover.png')
}

function setup() {
  createCanvas(400, 400);
}

function draw(){
  background(220);
  AK.position(0,0)
  AK.size(400,400)
}
- Adding my second image, but having trouble getting the two images to overlap.
  - Spent so much time going back and forth between way to add multiple overlapping images. I tried "load image", "Create image", using a "background image". It kept loading one image but not the other until one day it just randomly loaded. I did not question it..
- New code for multiple images is:


let img1, img2, img3;

function preload(){
  img1 = loadImage('AK1.jpeg');
  img2 = loadImage('AK2.jpeg');
  //img3 = loadImage('AK3.png');

}

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

image(img1, 0, 0, width, height);
//image(img2, 100, 100, width, height);
  img2.resize(220, 220);
  image(img2, 250, 250);

- Decided to write code for individual elements and then add them all together in the end.
- Added music to the main piece of code which includes the cover photos
let song;

function setup() {
song = loadSound('PlayersAudio.wav');
createCanvas(400, 400);

}

function mousePressed() {
if (song.isPlaying()) {

  song.stop();

} else {
  song.play();

}
}

- For the pulsing circle I looked at a couple other p5.js examples to understand which variables I need to add to get movement from the cirlce.
  ("https://editor.p5js.org/dansakamoto/sketches/ryu0YwxYm") This one was more complicated than what I was going for, but I used a lot of the same varibles.

- For the little flower symbol I took a lot from what we did on the midterm. I knew I needed to add many elipses but didn't want to call each one like when we did the tiling. I used the command "for (let i = 0; i < 10; i ++)" to add elipses, and I used the command "rotate" to spread them out.
  - At first I was putting in random numbers for the rotate command but after looking at this examplege ("https://p5js.org/reference/#/p5/TWO_PI") I tried out PI/numbers and got even distribution.

- Reasraching a lot of different examples to try and replicate a cube with an image inside of it. Looking at a lot of them and getting familiar with the functions: Translate, WEBGL, Rotate, Frame count ect.
  - First code that I used a part of was this: (https://editor.p5js.org/nc2516/sketches/jUfOSXA5B) I added on to it using some of this (https://editor.p5js.org/littlescience/sketches/bK7TfIdR5) And then had to alter it a lot and was able to simplify it. Getting much more comfortable uploading the images I need and calling them as variables in my function.
  - When I added the rotating cube from its own are of code to the rest of my image, everything was altered. "WEBGL" changed the orgins of the canvas. I tried to figure out how to move the cube, but felt it was easier to move the other objects around.
    - Cannot find the pulsing circle, and cannot move the flower. Will have to adress that.
      - OK the X Y axis is all messed up bow because I had to alter the canvas to "createCanvas(400, 400, WEBGL);" in order to add the 3D cube. Messed with the coordinates and was able to bring the circle back in.

  - In its own seperate code I made all these cute flowers using "function setup() {
  createCanvas(400, 400);
}

function draw() {

  ellipse(120,100,30,30);
  ellipse(100,115,30,30);
  ellipse(100,83,30,30);
  ellipse(80,100,30,30);
  fill(255, 230, 51);
  fill (225, random(225), random(225));
  ellipse(100,100,22,22);


}" But when I try to add it on top of the image in my main piece of code its not showing up. I wonder if this is similar to the circle- like the X Y axis being all weird, or if its hidden under the image now. Going to play around with the "draw" function + defining the variables.
  - Tried but just couldn't get the flower to place on top of the backround image.
  - Instead added letter objects and more circles. May add one more shape.
