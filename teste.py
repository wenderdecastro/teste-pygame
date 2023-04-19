import pygame

# Initialize Pygame
pygame.init()

# cria a janela
size = (400, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("gato")

# background
image = pygame.image.load("gato.png")

# tamanho da imagem
image_size = image.get_size()

# calcula o centro da imagem
center = (size[0] / 2 - image_size[0] / 2, size[1] / 2 - image_size[1] / 2)

# bota a imagem de fundo
screen.blit(image, center)
pygame.display.flip()

# icone
icon = pygame.image.load("gato.png")
pygame.display.set_icon(icon)

# Loop until the user clicks the close button
done = False
while not done:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# Quit Pygame
pygame.quit()
