import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (900, 700)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    # Draw an ellipse
    #                                    x   y   w     h    outline only size
    pygame.draw.ellipse(screen, GREEN, [50, 50, 200, 100])
    pygame.draw.ellipse(screen, GREEN, [250, 50, 200, 100], 8)

    # Draw a rectangle                x    y   w    h     outline only size
    pygame.draw.rect(screen, RED, [450, 50, 150, 100])
    pygame.draw.rect(screen, RED, [650, 50, 150, 100], 8)

    # TO DO: Make a list for a Polygon
    polygonPoints = [[200,100], [300,240], [80,400], [70, 400], [20,500]]
    #Draw a Polygon           color tuple (r,g,b)
    pygame.draw.polygon(screen, (90,90,90), polygonPoints)

    # Draw a bunch of arcs 
    pi = 3.1414
    pygame.draw.arc(screen, RED, [300, 300,200, 200], 0, pi/2, 8)
    pygame.draw.arc(screen, GREEN, [300,300, 200,200], pi/2, pi,8)
    pygame.draw.arc(screen, BLACK, [300,300,200,200], pi, 3*pi/2, 8)
    pygame.draw.arc(screen, (0,0,255), [300,300,200,200], 3*pi/2, 2*pi,8)

    #  Draw a line                 start point  stop point  line width
    pygame.draw.line(screen, BLACK, [50,650],   [450,650],   7)
    # --- Go ahead and update the screen with what we've drawn.

    # Draw a circle
    pygame.draw.circle(screen, (40,170, 30),[550,450], 60)

    # Write some text
    #                         name        size  bold  italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    #  Make the text image 
    text = font.render("My Text Here", True, BLACK)
    # Put the text on the screen at location [450,500]
    screen.blit(text, [450, 500])

    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
