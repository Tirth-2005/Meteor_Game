import os

SCREENSIZE= (956, 560)

FONTPATH = os.path.join(os.getcwd(), 'Meteor/resources/font/simkai.ttf')

IMAGEPATHS = {
    'asteroid': os.path.join(os.getcwd(), 'Meteor/resources/images/asteroid.png'),
    'bg_big': os.path.join(os.getcwd(), 'Meteor/resources/images/bg_big.png'),
    'bullet': os.path.join(os.getcwd(), 'Meteor/resources/images/bullet.png'),
    'seamless_space': os.path.join(os.getcwd(), 'Meteor/resources/images/seamless_space.png'),
    'ship': os.path.join(os.getcwd(), 'Meteor/resources/images/ship.png'),
    'ship_exploded': os.path.join(os.getcwd(), 'Meteor/resources/images/ship_exploded.png'),
    'space3': os.path.join(os.getcwd(), 'Meteor/resources/images/space3.jpg')
}

SOUNDPATHS = {
    'boom': os.path.join(os.getcwd(), 'Meteor/resources/sounds/boom.wav'),
    'Cool Space Music': os.path.join(os.getcwd(), 'Meteor/resources/sounds/Cool Space Music.mp3'),
    'shot': os.path.join(os.getcwd(), 'Meteor/resources/sounds/shot.ogg')
}

FPS = 60