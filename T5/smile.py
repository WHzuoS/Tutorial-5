import pygame as pg

pg.init()

screensize = width, height = 400,400

black = (0,0,0)
white = (255,255,255)
brown = (139,69,19)
clock = pg.time.Clock()
seconds = 1

pg.time.set_timer(pg.USEREVENT, 1000)

display = pg.display.set_mode(screensize)
display.fill(white)

for i in range(height):
    
    if (i % 20 == 0):
        pg.draw.line(display, (220,220,220), (0,i), (400,i))
        
    for j in range(width):
        
        if (j % 20 == 0):
            pg.draw.line(display, (220,220,220), (j,0), (j,400))
    
pg.draw.circle(display, black, (200,200), 100, width = 1)
pg.draw.circle(display, brown, (240,170), 10, width = 0)
pg.draw.circle(display, brown, (160,170), 10, width = 0)

rect = (150, 220, 100, 50)
pg.draw.arc(display, black, rect, 3, 0)
pg.display.update()

# Save image
pg.image.save(display, "smile.png")

while True:
    for e in pg.event.get():  
        if e.type == pg.USEREVENT:
            seconds+=1
            if (seconds == 5):
                pg.quit()
        