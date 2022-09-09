# A 'Crossy' type, simple game.

import pygame

# size of the screen
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# colors with RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Clock used to update game events and frames
clock = pygame.time.Clock()

class Game:
    # Typical rate of 60, equivalent to FPS
    tickRate = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # create the window of specified size in white to display the game
        self.gameScreen = pygame.display.set_mode((width, height))
        # set the game window color to white
        self.gameScreen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def runGameLoop(self):
        gameOver = False

        # Main game loop, used to update all gameplay such as movement, checks and graphics.
        # Runs until gameOver = True
        while not gameOver:
            # A loop to get all of the events occuring at any given time
            # Events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():
                # If we have a quit type event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    gameOver = True
                print(event)

            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.tickRate)

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        objectImage = pygame.image.load(image_path)
        # scale the image up
        self.image = pygame.transform.scale(objectImage, (width, height))

        self.x_pos = x
        self.y_pos = y

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

pygame.init()

newGame = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
newGame.runGameLoop()

# Quit pygame and the program
pygame.quit()
quit()


# # load the player image from the file directory
# playerImage = pygame.image.load('images/player.png')
# # scale the image up
# playerImage = pygame.transform.scale(playerImage, (50, 50))

# pygame.draw.rect(gameScreen, BLACK_COLOR, [350, 350, 100, 100])
# pygame.draw.circle(gameScreen, BLACK_COLOR, (400, 300), 50)

# Display the player image on the screen
# gameScreen.blit(playerImage, (375, 375))