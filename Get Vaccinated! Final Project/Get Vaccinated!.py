import pygame
import random
import os
import time
pygame.font.init()
WIDTH, HEIGHT = 900, 900
HAPPY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Get Vaccinatted!")


Virus_Bacterium1 = pygame.image.load(os.path.join("Properties", "Covid1.png"))
Virus_Bacterium1_trans = pygame.transform.scale(Virus_Bacterium1, (80, 80))

Virus_Bacterium2 = pygame.image.load(os.path.join("Properties", "Covid2.png"))
Virus_Bacterium2_trans = pygame.transform.scale(Virus_Bacterium2, (80, 80))

Virus_Bacterium3 = pygame.image.load(os.path.join("Properties", "Covid3.png"))
Virus_Bacterium3_trans = pygame.transform.scale(Virus_Bacterium3, (80, 80))

Vaccine_Vial = pygame.image.load(os.path.join("Properties", "Vaccineshot_Vial.png"))
Vaccine_shot_vial = pygame.transform.scale(Vaccine_Vial, (150, 150))


Covid_Germ1 = pygame.image.load(os.path.join("Properties", "Germ1.png"))
Covid_Germ1_trans = pygame.transform.scale(Covid_Germ1, (80, 80))

Covid_Germ2 = pygame.image.load(os.path.join("Properties", "Germ2.png"))
Covid_Germ2_trans = pygame.transform.scale(Covid_Germ2, (80, 80))

Covid_Germ3 = pygame.image.load(os.path.join("Properties", "Germ3.png"))
Covid_Germ3_trans = pygame.transform.scale(Covid_Germ3, (50, 50))

Vaccine_Liquid = pygame.image.load(os.path.join("Properties", "VaccineGel.png"))
Vaccine_Liquid_trans = pygame.transform.scale(Vaccine_Liquid, (1, 1))

Background_Environment = pygame.transform.scale(
    pygame.image.load(os.path.join("Properties", "Hospital_Background.png")), (WIDTH, HEIGHT))



class Vaccine:  

    WAITTIME = 15

    def __init__(self, a, b, health=100):
        self.a = a
        self.b = b
        self.health = health
        self.virus_img = None
        self.germ_img = None
        self.germs = []
        self.wait_time_interval = 0

    def draw(self, window):
        window.blit(Vaccine_shot_vial, (self.a, self.b))
        for germ in self.germs:
            germ.draw(window)

    def move_germs(self, vel, obj):
        self.waittime()
        for germ in self.germs:
            germ.move(vel)
            if germ.off_screen(HEIGHT):
                self.germs.remove(germ)
            elif germ.collision(obj):
                obj.health -= 10
                

    def move(self, vel):
        self.b += vel


    def waittime(self):
        if self.wait_time_interval >= self.WAITTIME:
            self.wait_time_interval = 0
        elif self.wait_time_interval > 0:
            self.wait_time_interval += 1

    def shoot(self):
        if self.wait_time_interval == 0:
            germ = Germ(self.a, self.b, self.germ_img)
            self.germs.append(germ)
            self.wait_time_interval = 1

    def get_width(self):
        return self.virus_img.get_width()

    def get_height(self):
        return self.virus_img.get_height()


class Germ:  

    def __init__(self, a, b, img):
        self.a = a
        self.b = b
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.a, self.b))

    def move(self, vel):
        self.b += vel

    def off_screen(self, height):
        return not (self.b <= height and self.b >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Virus1:  
    WAITTIME = 30

    def __init__(self, a, b, health=100):
        self.a = a
        self.b = b
        self.health = health
        self.virus_img = None
        self.germ_img = None
        self.germs = []
        self.wait_time_interval = 0

    def draw(self, window):
        window.blit(Covid_Germ1_trans, (self.a, self.b))
        for germ in self.germs:
            germ.draw(window)

    def move_germs(self, vel, obj):
        self.waittime()
        for germ in self.germs:
            germ.move(vel)
            if germ.off_screen(HEIGHT):
                self.germs.remove(germ)
            elif germ.collision(obj):
                obj.health -= 10
                



    def waittime(self):
        if self.wait_time_interval >= self.WAITTIME:
            self.wait_time_interval = 0
        elif self.wait_time_interval > 0:
            self.wait_time_interval += 1

    def shoot(self):
        if self.wait_time_interval == 0:
            germ = Germ(self.a, self.b, self.germ_img)
            self.germs.append(germ)
            self.wait_time_interval = 1

    def get_width(self):
        return self.virus_img.get_width()

    def get_height(self):
        return self.virus_img.get_height()


class Virus2:  

    WAITTIME = 30

    def __init__(self, a, b, health=100):
        self.a = a
        self.b = b
        self.health = health
        self.virus_img = None
        self.germ_img = None
        self.germs = []
        self.wait_time_interval = 0

    def draw(self, window):
        window.blit(Covid_Germ2_trans, (self.a, self.b))
        for germ in self.germs:
            germ.draw(window)
    def move_germs(self, vel, obj ):
        self.waittime()
        for germ in self.germs:
            germ.move(vel)
            if germ.off_screen(HEIGHT):
                self.germs.remove(germ)
            elif germ.collision(obj):
                obj.health -= 10
                

    def waittime(self):
        if self.wait_time_interval >= self.WAITTIME:
            self.wait_time_interval = 0
        elif self.wait_time_interval > 0:
            self.wait_time_interval += 1

   

    def shoot(self):
        if self.wait_time_interval == 0:
            germ = Germ(self.a, self.b, self.germ_img)
            self.germs.append(germ)
            self.wait_time_interval = 1

    def get_width(self):
        return self.virus_img.get_width()

    def get_height(self):
        return self.virus_img.get_height()


class Virus3:  

    WAITTIME = 30

    def __init__(self, a, b, health=100):
        self.a = a
        self.b = b
        self.health = health
        self.virus_img = None
        self.germ_img = None
        self.germs = []
        self.wait_time_interval = 0

    def draw(self, window):
        window.blit(Covid_Germ3_trans, (self.a, self.b))
        for germ in self.germs:
            germ.draw(window)

    def move_germs(self, vel, obj):
        self.waittime()
        for germ in self.germs:
            germ.move(vel)
            if germ.off_screen(HEIGHT):
                self.germs.remove(germ)
            elif germ.collision(obj):
                obj.health -= 10
                

    def shoot(self):
        if self.wait_time_interval == 0:
            germ = Germ(self.a, self.b, self.germ_img)
            self.germs.append(germ)
            self.wait_time_interval = 1

    def waittime(self):
        if self.wait_time_interval >= self.WAITTIME:
            self.wait_time_interval = 0
        elif self.wait_time_interval > 0:
            self.wait_time_interval += 1

    def get_width(self):
        return self.virus_img.get_width()

    def get_height(self):
        return self.virus_img.get_height()


class User(Vaccine):  

    def __init__(self, a, b, health=100):
        super().__init__(a, b, health)
        self.virus_img = Vaccine_Vial
        self.germ_img = Vaccine_Liquid
        self.mask = pygame.mask.from_surface(self.virus_img)
        self.max_health = health

    
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def move_germs(self, vel, objs):
        self.waittime()
        for germ in self.germs:
            germ.move(vel)
            if germ.off_screen(HEIGHT):
                self.germs.remove(germ)
            else:
                for obj in objs:
                    if germ.collision(obj):
                        objs.remove(obj)
                        

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                        (self.a, self.b + self.virus_img.get_height() + 10, self.virus_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.a, self.b + self.virus_img.get_height() + 10, self.virus_img.get_width() * (self.health / self.max_health),
        10))


class Opponent1(Virus1):  

    def __init__(self, a, b, health=100):
        super().__init__(a, b, health)
        self.virus_img = Virus_Bacterium1_trans
        self.germ_img = Covid_Germ1_trans
        self.mask = pygame.mask.from_surface(self.virus_img)
        self.max_health = health

    def move(self, vel):
        self.b += vel

    def move_germs(self, vel, objs):
        self.waittime()
        for germ in self.germs:
            germ.move(vel)
            if germ.off_screen(HEIGHT):
                self.germs.remove(germ)
            else:
                for obj in objs:
                    if germ.collision(obj):
                        objs.remove(obj)


class Opponent2(Virus2):  

    def __init__(self, a, b, health=100):
        super().__init__(a, b, health)
        self.virus_img = Virus_Bacterium2_trans
        self.germ_img = Covid_Germ2_trans
        self.mask = pygame.mask.from_surface(self.virus_img)
        self.max_health = health

    def move(self, vel):
        self.b += vel

    def move_germs(self, vel, objs):
        self.waittime()
        for germ in self.germs:
            germ.move(vel)
            if germ.off_screen(HEIGHT):
                self.germs.remove(germ)
            else:
                for obj in objs:
                    if germ.collision(obj):
                        objs.remove(obj)
                        


class Opponent3(Virus3):  

    def __init__(self, a, b, health=100):
        super().__init__(a, b, health)
        self.virus_img = Virus_Bacterium3_trans
        self.germ_img = Covid_Germ3_trans
        self.mask = pygame.mask.from_surface(self.virus_img)
        self.max_health = health

    def move(self, vel):
        self.b += vel

    def move_germs(self, vel, objs):
        self.waittime()
        for germ in self.germs:
            germ.move(vel)
            if germ.off_screen(HEIGHT):
                self.germs.remove(germ)
            else:
                for obj in objs:
                    if germ.collision(obj):
                        objs.remove(obj)
                        


def collide(obj1, obj2):
    offset_a = obj2.a - obj1.a
    offset_b = obj2.b - obj1.b
    return obj1.mask.overlap(obj2.mask, (offset_a, offset_b)) != None


def main():
    run = True
    FPS = 60
    level = 1
    lives = 30
    main_font = pygame.font.SysFont("Italic", 40)
    lost_font = pygame.font.SysFont("Italic", 40)
    clock = pygame.time.Clock()
    lost = False
    lost_count = 0
    user = User(300, 650)
    user_vel = 9
    germ_vel = 23
    opponents = []
    wave_length = 1
    opponent1_vel = 1
    opponent2_vel = 1
    opponent3_vel = 1

    def element_display():

        HAPPY.blit(Background_Environment, (0, 0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (200, 0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (0, 0, 200))
        HAPPY.blit(level_label, (10, 10))
        HAPPY.blit(lives_label, (WIDTH - lives_label.get_width() - 10, 10))

        for opponent1 in opponents:
            opponent1.draw(HAPPY)

        for opponent2 in opponents:
            opponent2.draw(HAPPY)

        for opponent3 in opponents:
            opponent3.draw(HAPPY)

        user.draw(HAPPY)

        if lost:
            lost_label = lost_font.render("Sorry, You Lost :(", 1, (255, 0, 0))
            HAPPY.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)

        element_display()

        if lives <= 0 or user.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 5:
                run = False
            else:
                continue

        if len(opponents) == 0:
            level += 1
            wave_length += 3
            for i in range(wave_length):
                opponent1 = Opponent1(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                                      random.choice(["brown", "blue", "pink"]))
                opponent2 = Opponent2(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                                      random.choice(["brown", "blue", "pink"]))
                opponent3 = Opponent3(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                                      random.choice(["brown", "blue", "pink"]))

                opponents.append(opponent1)
                opponents.append(opponent2)
                opponents.append(opponent3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and user.a - user_vel > 0:
            user.a -= user_vel
        if keys[pygame.K_RIGHT] and user.a + user_vel + user.get_width()  < 1100:
            user.a += user_vel
        if keys[pygame.K_UP] and user.b - user_vel > 0:
            user.b -= user_vel
        if keys[pygame.K_DOWN] and user.b + user_vel + user.get_height()  < HEIGHT:
            user.b += user_vel
        if keys[pygame.K_SPACE]:
            user.shoot()

        for opponent1 in opponents[:]:
            opponent1.move(opponent1_vel)
            opponent1.move_germs(germ_vel, user)
            if opponent1.b + opponent1.get_height() > HEIGHT:
                lives -= 1
                opponents.remove(opponent1)


        for opponent2 in opponents[:]:
            opponent2.move(opponent2_vel)
            opponent2.move_germs(germ_vel, user)
            if opponent2.b + opponent2.get_height() > HEIGHT:
                lives -= 1
                opponents.remove(opponent2)

        for opponent3 in opponents[:]:
            opponent3.move(opponent3_vel)
            opponent3.move_germs(germ_vel, user)
            if opponent3.b + opponent3.get_height() > HEIGHT:
                lives -= 1
                opponents.remove(opponent3)

        user.move_germs(-germ_vel, opponents)

        pygame.display.update()

def main_menu():
    title_font = pygame.font.SysFont("italic", 40)
    run = True
    while run:
        HAPPY.blit(Background_Environment, (0,0))
        title_label = title_font.render("Click to begin the game!", 1, (0,0,255))
        HAPPY.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

main_menu()



main()

