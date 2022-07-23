import pygame
import os

class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.loadImages


    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        pass

    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if (not fileName.endswith(".png")):
                continue
            image = pygame.Image.load(r"images/" + fileName)
            image = pygame.transform.scale(image, pieceSize)
            self.images[fileName.split(".")[0]] = image
