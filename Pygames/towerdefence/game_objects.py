class Tower:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 100
        self.cooldown = 0

    def fire(self, enemies):
        if self.cooldown == 0:
            for enemy in enemies:
                if self.distance(enemy) <= self.range:
                    enemy.health -= 10
                    if enemy.health <= 0:
                        enemies.remove(enemy)
                    self.cooldown = 10

    
    def distance(self, enemy):
        math.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2 )


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.health = 100

    def move(self):
        self.x += self.speed
    
    def draw(self, screen):
        screen.blit(enemy_img, (self.x, self.y))
    

class Projectile:
    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.target = target 
        self.speed = 10

    def move(self):
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        dist = math.sqrt(dx**2 + dy**2)
        if dist <= self.speed:
            self.target.health -= 10
            if self.target.heath <= 0:
                enemies.remove(self.target)
            projectiles.remove(self)
        else:
            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0,0), (self.x, self.y))


    