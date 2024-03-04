import pygame

pygame.init()

#Setup game window
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fraction Game")

#create sprite character
player_image = pygame.Surface((50,50))
player_image.fill((255,0,0))
player_rect = player_image.get_rect()

#Set Initial Coordinates/Position
player_rect.centerx = WIDTH / 2
player_rect.centery = HEIGHT / 2

#Create Target Character
target_image = pygame.Surface((50,50))
target_image.fill((0, 255, 0))
target_rect = target_image.get_rect()

#Set Initial Coordinates/Position
target_rect.centerx = 100
target_rect.centery = 100

#Score Counter
score = 0

#Function to move the players based on arrow keys
def move_player(keys):
  if keys[pygame.K_UP]:
    player_rect.centery -=10
  elif keys[pygame.K_DOWN]:
    player_rect.centery +=10
  elif keys[pygame.K_LEFT]:
    player_rect.centery -=10
  elif keys[pygame.K_RIGHT]:
    player_rect.centery +=10


#Draw the Elements on the screen
def draw():
  screen.fill((0, 0,0))
  screen.blit(player_image, player_rect)
  screen.blit(target_image, target_rect)
  font = pygame.font.Font(None, 30)
  text = font.render("Score: " + str(score), True, (0, 0, 0))
  screen.blit(text, (10, 10))

#Main game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running


#Exit 
pygame.quit()