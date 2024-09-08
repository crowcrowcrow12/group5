import random
import pygame as pg

class Bricks:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width  # Adjust this value for larger brick width
        self.height = height  # Adjust this value for larger brick height
        self.colors = ['navy', 'white', 'light blue']  # Color pattern for rows
        self.bricks = []
        self.brick_colors = []
        self.set_values()

    def set_values(self):
        y_values = [int(y) for y in range(100, 200, 25)]  # Adjust vertical spacing if needed
        x_values = [int(x) for x in range(10, 550, 52)]  # Adjust horizontal spacing if needed
        y_index = 0
        self.loop(x_values, y_values, y_index)

    def loop(self, x_values, y_values, y_index):
        for n in x_values:
            # Check if it is the last position in the x_values list.
            if n == x_values[-1]:
                # Check if all the positions in the y_values has been occupied
                if y_index < len(y_values) - 1:
                    y_index += 1
                    # Run the method again if there are still vacant positions.
                    self.loop(x_values, y_values, y_index)
            else:
                x = n
                y = y_values[y_index]
                brick = pg.Rect(x, y, self.width, self.height)
                self.bricks.append(brick)
                # Set color based on row index
                row_color_index = y_index % len(self.colors)
                self.brick_colors.append(self.colors[row_color_index])

    def show_bricks(self):
        for loop in range(len(self.bricks)):
            brick = self.bricks[loop]
            color = self.brick_colors[loop]
            pg.draw.rect(self.screen, color, brick)
