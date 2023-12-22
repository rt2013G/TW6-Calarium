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
      - [Three.js](#three.js)
      - [Flask](#flask)
  - [Workflow](#workflow)
  - [What I learned](#what-i-learned)
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

### Three.js
I used Three.js to add a three-dimensional background. I added a simple moon and some stars, some of which
move when moving the mouse on the page. I didn't tinker with Three.js enough to uncover its full potential but
overall I think it looks nice enough.

### PWA
A Progressive Web App is a web application that can be installed on mobile like a native application.
In order to achieve this, I have to add a _manifest.json_ file and a _sw.js_ file in my project.
The _sw_ or _service worker_ is a thread that runs in the background and caches content, so that the app is able
to work even without a connection.

### Flask
The backend of the web application uses Python with the microframework _Flask_.\
I first created a _virtual environment_, then installed flask with ```pip install flask```
and added the files _.flaskenv_, _.env_ and _config.py_ to store configuration and environment variables.
I also installed the extension ```pip install flask_wtf``` to handle forms.
To manage databases easily, I'm also using ```pip install flask-sqlalchemy``` and ```pip install flask-migrate```.
During development, I'm working with a SQLite database as it easier to manage, but I'll be migrating to another
DBMS when the application is closer to being completed.\
To initialize a database with flask migrate, I used the flask sub-command ```flask db init```. 
```flask db migrate``` provides us with the migration script, then ```flask db upgrade``` applies the changes to 
the database. Meanwhile, to implement the login/logout/user functionalities I also added ```pip install flask-login```.


## What I learned
- Working on this project alone was a massive undertaking, it made me truly understand the phrase
"two is megl che one", although for a real-world application two might not be enough anyway.
- I'm not quite sure yet, but working on the presentation (figma, scss, etc...) before the logic (flask, the database)
might have been a mistake, at least that's how I felt when I started building the flask application.
- I spent more time researching and setting up the project than actually working on it, but that's probably fair because
this was the first time I ever worked on a complete web application or a more-than-a-few-files project. 
Now that I have a basic grasp of the technologies needed, time requirements, folder structure and what the setup 
looks like, getting started on another project will definitely be much easier.


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
- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) - A great course that helped me a lot with Flask