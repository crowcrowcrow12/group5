import pygame as pg
import os


# Initialize pygame mixer
pg.mixer.init()

# Define the correct path for the audio files
audio_path = os.path.join(os.path.dirname(__file__), 'audio')

# Load all sound effects
pad_hit = pg.mixer.Sound(os.path.join(audio_path, 'pad_hit.ogg'))
brick_breaking = pg.mixer.Sound(os.path.join(audio_path, 'brick_breaking.ogg'))
dropping_ball = pg.mixer.Sound(os.path.join(audio_path, 'dropping_ball.ogg'))
game_end = pg.mixer.Sound(os.path.join(audio_path, 'game_end_.ogg'))
win_game = pg.mixer.Sound(os.path.join(audio_path, 'win_game.ogg'))

# Screen dimensions
WIDTH = 550
HEIGHT = 600

BG_COLOR = "black"

# Text color
color = "white"


# Paddle settings
paddle_x = 200
paddle_y = 550
paddle_width = 100
paddle_height = 20


# Ball settings
ball_x = 250
ball_y = 540
ball_x_speed = 2
ball_y_speed = 2
ball_radius = 8


# Text settings
text_x = 300


# Bricks settings
brick_width = 45
brick_height = 20