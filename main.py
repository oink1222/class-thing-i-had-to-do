import pygame
import random
from pygame.locals import *
import extras
pygame.init()
ballamound = 10

screen_info = pygame.display.Info()
screen_divider = 2
size = (width, height) = (screen_info.current_w / screen_divider, screen_info.current_h / screen_divider)

screen = pygame.display.set_mode(size)

color = (26, 255, 255)
clock = pygame.time.Clock()


class Ball():
    def __init__(self,image,x,y,scale):
        self.image = image
        self.x = x
        self.y = y
        self.scale = scale
        self.ball_image = pygame.image.load(self.image)
        self.ball_image = pygame.transform.smoothscale(self.ball_image, (self.scale,self.scale))
        self.ball_rect = self.ball_image.get_rect()
        self.ball_rect_center = (width // 2, height // 2)
        self.speed = pygame.math.Vector2(5,5)
        self.speed.rotate_ip(random.randint(0,360))

    def draw_ball(self):
        screen.blit(self.ball_image, self.ball_rect)

    def move_ball (self):
        screen_info = pygame.display.Info()
        self.ball_rect.move_ip(self.speed)
        

        # checks left and right ball
        if self.ball_rect.left < 0 or self.ball_rect.right > (screen_info.current_w):
            self.speed[0] *= -1
            self.ball_rect.move_ip(self.speed[0], 0)
        if self.ball_rect.top < 0 or self.ball_rect.bottom > (screen_info.current_h):
            self.speed[1] *= -1
            self.ball_rect.move_ip(0, self.speed[1])

    def initball(self):
        self.move_ball()
        self.draw_ball()


balls = []
# ball_image = pygame.image.load("ball.png")
# ball_image = pygame.transform.smoothscale(ball_image, (30,30))
# ball_rect = ball_image.get_rect()
# ball_rect_center = (width // 2, height // 2)
for i in range(ballamound):
    balls.append(Ball("ball.png",0,0,random.randint(20/(screen_divider/2),60/(screen_divider/2))))

def main():
    mousepos = (pygame.mouse.get_pos())
    running = True
    while running:
        clock.tick(60)
        screen.fill(color)
        for j in range(ballamound):
            curball = balls[j]
            curball.initball()

        pygame.display.set_caption(f'balls FPS: {round(clock.get_fps())}')
        
        pygame.display.flip()

        for event in pygame.event.get(): 
            # Check for QUIT event     
            if event.type == pygame.MOUSEBUTTONDOWN:
                balls.append(Ball("ball.png",mousepos[0],mousepos[1],random.randint(20/(screen_divider/2),60/(screen_divider/2))))
            if event.type == pygame.QUIT: 
                running = False

if __name__ == '__main__' :
    main()