import pygame, random, time
 
size = 456                      # Size of window/dice
spsz = size//10                 # size of spots
m = int(size/2)                 # mid-point of dice (or die?)
l=t=int(size/4)                 # location of left and top spots
r=b=size-l                      # location of right and bottom spots
rolling = 16                    # times that dice rolls before stopping
diecol = (28, 9, 98)          # die colour
spotcol = (137, 221, 10)           # spot colour
 
d = pygame.display.set_mode((size, size))
d.fill(diecol)
pygame.display.set_caption("Dice Simulator")
 
for i in range(rolling):            # roll the die...
    n=random.randint(1,6)                   # random number between 1 & 6
    d.fill(diecol)                          # clear previous spots
    if n % 2 == 1:
        pygame.draw.circle(d,spotcol,(m,m),spsz)  # middle spot
    if n==2 or n==3 or n==4 or n==5 or n==6:
        pygame.draw.circle(d,spotcol,(l,b),spsz)  # left bottom
        pygame.draw.circle(d,spotcol,(r,t),spsz)  # right top
    if n==4 or n==5 or n==6:
        pygame.draw.circle(d,spotcol,(l,t),spsz)  # left top
        pygame.draw.circle(d,spotcol,(r,b),spsz)  # right bottom
    if n==6:
        pygame.draw.circle(d,spotcol,(m,b),spsz)  # middle bottom
        pygame.draw.circle(d,spotcol,(m,t),spsz)  # middle top
     
    pygame.display.flip()
    time.sleep(0.5)