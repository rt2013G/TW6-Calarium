# TW6-Calarium
This is a project created for my university course of _Web Tecnologies_, with the purpose of designing and building
a web application in its entirety, including both the front end and the back end, with tools of our choice.

## Table of contents

- [Overview](#overview)
- Building the project
  - Tools used
      - [Figma](#figma)
      - [Sass](#sass)
      - [Gulp](#gulp)
      - [HTML](#html)
      - [Javascript](#javascript)
      - Three.js
      - [Flask](#flask)
  - [Workflow](#workflow)
- [Author](#author)
- [Additional resources and acknowledgements](#additional-resources-and-acknowledgements)


## Overview
_Calarium_ itself is a game I made in Unity, which features a procedurally generated planet that
the user has to survey and analyze.\
The purpose of this web application is to provide an additional layer of interactivity with the players: 
it serves as an online client where people can not only download the game but also connect with one another through
various different provided services, almost as if it were a game on its own.
![](./game.jpg)


## Workflow


### Figma
The first step is the UX/UI design.
This was my first time ever using figma or any website design tool, but I tried my best to put up a half-decent interface.
I used as reference 1366x700 for desktop and 400x700 for mobile.\
All design files and images can be found in the _design_ folder.

### Setting up the project
Having **Node** installed on the machine, run\
```npm init -y```\
```npm install sass```

### Sass
I first created a folder structure based on the **7:1 pattern**, then added some basic _.scss_ files.\
The command\
```sass --watch app/sass:app/out```\
can be used to compile Sass into CSS and tell Sass to watch 
the app/Sass folder for changes.\
I will be using this command later when setting up a **Gulp** workflow.

### Gulp
```npm install gulp-cli```\
```npm install --save-dev gulp gulp-sass browser-sync```\
Gulp is a toolkit to automate development workflow, I haven't tinkered with it much, so I'll just be using it for
auto compiling Sass files and auto updating my browser page.\
_npm_ signals some vulnerabilities with gulp's dependencies, so I had to add this to my _package.json_:
```
"overrides": {
    "glob-parent": "^6.0.2"
  }
```
and run ```npm upate```\
Now I can set up a Gulp workflow by creating a _gulpfile.js_ file, then simply run ```gulp watch``` in the command line.

### HTML
I then created the index.html file, imported the font [_Inter_](https://fonts.google.com/specimen/Inter) and styled the page using only SCSS.

### Javascript
After styling only the home page, I decided to add the first bits of Javascript to include the sound toggle button.\
To help making the website interactive, I installed _JQuery_, and then _Three.js_ to add 3D animations.
I imported them as HTML script tags, but they can also be installed with npm as follows:\
```npm install jquery```\
```npm install --save three```

### Flask
The backend of the web application uses Python with the microframework _Flask_.\
I first created a _virtual environment_, then installed flask with\
```pip install flask```


## Author
Raffaele Talente, student enrolled at University of Naples "Parthenope"


## Additional resources and acknowledgements
- [Raffaele Montella](https://github.com/raffmont) - Professor of the course
- [Acerola's epic color palette](https://acerola.gg/colors.html) - For helping me find a color scheme to use
- [Sass website](https://sass-lang.com/guide/) and [Sass guidelines](https://sass-guidelin.es/) - For everything related to Sass
- [SVG Repo](https://www.svgrepo.com/) - For the icons used
- [ArctSound](https://pixabay.com/music/main-title-sci-fi-cyberpunk-trailer-110587/) - For the music theme
- [This codepen](https://codepen.io/sosuke/pen/Pjoqqp) - For changing color of SVG icons
- [Three.js docs](https://threejs.org/docs/)
- [This video](https://www.youtube.com/watch?v=Q7AOvWpIVHU) - For the image assets
- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)