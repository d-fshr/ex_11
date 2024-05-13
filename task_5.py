import pygame
import random

class Molecule:

    molecules = []

    def __init__(self, x, y, radius, color):
        
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dist_x = random.uniform(-0.15, 0.15)
        self.dist_y = random.uniform(-0.15, 0.15)

        Molecule.molecules.append(self)

    def draw_mol(self):

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move_mol(self, w, h):

        self.x += self.dist_x
        self.y += self.dist_y

        if self.x <= 0 or self.x >= w:
            self.dist_x = -self.dist_x
        if self.y <= 0 or self.y >= h:
            self.dist_y = -self.dist_y


        for mol in Molecule.molecules:

            if self != mol:
                distance = ((self.x - mol.x ) ** 2 + (self.y - mol.y) ** 2) ** 0.5

                if distance <= self.radius + mol.radius:
                    self.dist_x = -self.dist_x
                    self.dist_y = -self.dist_y
                    mol.dist_x = -mol.dist_x
                    mol.dist_y = -mol.dist_y


screen = pygame.display.set_mode((600, 500))

mol_1 = Molecule(400, 400, 15, 'blue')
mol_2 = Molecule(10, 400, 20, 'red')
mol_3 = Molecule(400, 10, 15, 'green')
mol_4 = Molecule(250, 250, 20, 'black')
mol_4 = Molecule(100, 100, 25, 'grey')

flag = True
while flag:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    screen.fill('white')

    for molecule in Molecule.molecules:
        molecule.move_mol(600, 500)

    for molecule in Molecule.molecules:
        molecule.draw_mol()

    pygame.display.update()
