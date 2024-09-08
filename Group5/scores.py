import pygame as pg

class ScoreBoard:
    def __init__(self, x, color, screen):
        self.screen = screen
        self.color = color
        self.x = x
        self.score = 0
        self.high_score = 0
        self.lives = 5  # Changed from trials to lives
        self.font = pg.font.SysFont("calibri", 20)

    def show_scores(self):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, self.color)
        lives_text = self.font.render(f"Lives: {self.lives}", True, self.color)  # Changed from trials to lives
        # Calculate the width of each text to position them horizontally with a consistent gap
        screen_width = self.screen.get_width()

        # Define some spacing between each text block
        spacing = 20
             # Get the width of each text block
        score_text_width = score_text.get_width()
        high_score_text_width = high_score_text.get_width()
        lives_text_width = lives_text.get_width()

        # Calculate starting positions based on the screen width and spacing
        score_x = screen_width - (score_text_width + high_score_text_width + lives_text_width + 2 * spacing + 10)
        high_score_x = score_x + score_text_width + spacing
        lives_x = high_score_x + high_score_text_width + spacing

    # Blit the text onto the screen
        self.screen.blit(score_text, (score_x, 10))
        self.screen.blit(high_score_text, (high_score_x, 10))
        self.screen.blit(lives_text, (lives_x, 10))
    def is_game_over(self):
        if self.lives <= 0:  # Changed from trials to lives
            return True
        return False

    def game_over(self):
        game_over_color = 'red'
        game_over_font = pg.font.SysFont("calibri", 30)
        game_over_text = game_over_font.render(f"Game Over! Click '0' to restart.", True, game_over_color)
        game_over_rect = game_over_text.get_rect(topright=(50, 300))
        self.screen.blit(game_over_text, (50, 300))
        self.record_high_score()

    def success(self):
        game_success_color = 'green'
        game_success_font = pg.font.SysFont("calibri", 30)
        game_success_text = game_success_font.render(f"You won! Click '0' to restart.", True, game_success_color)
        game_success_rect = game_success_text.get_rect(topleft=(50, 300))
        self.screen.blit(game_success_text, (50, 300))
        self.record_high_score()

    def set_high_score(self):
        try:
            with open("records.txt", mode="r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            with open("records.txt", mode="w") as data:
                data.write("0")
                score = 0
        else:
            score = lines[0]

        self.high_score = int(score)

    def record_high_score(self):
        if self.score > self.high_score:
            with open("records.txt", mode="w") as file:
                file.write(f"{self.score}")
