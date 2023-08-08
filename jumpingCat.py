import pygame
import sys
from time import sleep


pygame.init()
pygame.display.set_caption('JUMPING CAT')
MAX_WIDTH = 800
MAX_HEIGHT = 400
myFont = pygame.font.SysFont("impact", 40, False, False)
btnFont = pygame.font.SysFont("impact", 30, False, False)
startFont = pygame.font.SysFont("impact", 60, False, False) #bauhaus93
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

def startPage():
    while True:
        screen.fill('mintcream')
        startTitle = startFont.render("JUMPING CAT", True, 'orchid')
        titleRect = startTitle.get_rect()
        titleRect.centerx = MAX_WIDTH / 2
        titleRect.centery = MAX_HEIGHT / 4
        screen.blit(startTitle, titleRect)
        kkamang = pygame.image.load('resources/kkamang.png')
        kkamang = pygame.transform.scale(kkamang, (120, 110))
        kkamang.set_colorkey((0, 0, 255))
        banjjok = pygame.image.load('resources/banjjok2.png')
        banjjok = pygame.transform.scale(banjjok, (40, 40))
        banjjok.set_colorkey((0, 0, 255))
        screen.blit(kkamang, (100, 30))
        screen.blit(kkamang, (580, 30))

        easyBtn = btnFont.render("EASY", True, (0, 0, 0))
        easyRect = easyBtn.get_rect(centerx = MAX_WIDTH / 2, centery = MAX_HEIGHT / 2 + 20)
        screen.blit(easyBtn, easyRect)
		
        normalBtn = btnFont.render("NORMAL", True, (0, 0, 0))
        normalRect = normalBtn.get_rect(centerx = MAX_WIDTH / 2, centery = MAX_HEIGHT / 2 + 70)
        screen.blit(normalBtn, normalRect)

        hardBtn = btnFont.render("HARD", True, (0, 0, 0))
        hardRect = hardBtn.get_rect(centerx = MAX_WIDTH / 2, centery = MAX_HEIGHT / 2 + 120)
        screen.blit(hardBtn, hardRect)

        #onmosueover menu
        if easyRect.collidepoint(pygame.mouse.get_pos()):
            easyBtn = btnFont.render("EASY", True, 'mediumpurple')	#mediumorchid
            screen.blit(easyBtn, easyRect)
            screen.blit(banjjok, (300, MAX_HEIGHT / 2))
            screen.blit(banjjok, (460, MAX_HEIGHT / 2))
        elif normalRect.collidepoint(pygame.mouse.get_pos()):
            normalBtn = btnFont.render("NORMAL", True, 'mediumpurple')
            screen.blit(normalBtn, normalRect)
            screen.blit(banjjok, (280, MAX_HEIGHT / 2 + 50))
            screen.blit(banjjok, (480, MAX_HEIGHT / 2 + 50))
        elif hardRect.collidepoint(pygame.mouse.get_pos()):
            hardBtn = btnFont.render("HARD", True, 'mediumpurple')
            screen.blit(hardBtn, hardRect)
            screen.blit(banjjok, (300, MAX_HEIGHT / 2 + 100))
            screen.blit(banjjok, (460, MAX_HEIGHT / 2 + 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easyRect.collidepoint(event.pos):
                    print("easy")
                    return 15
                elif normalRect.collidepoint(event.pos):
                    print("normal")
                    return 30
                elif hardRect.collidepoint(event.pos):
                    print("hard")
                    return 90
		
        pygame.display.update()

def finalPage(scr):
    finalScore = "YOUR FINAL SCORE : " + str(scr)
    exitTitle = myFont.render(finalScore, True, 'turquoise')
    rect = exitTitle.get_rect(centerx = MAX_WIDTH / 2, centery = MAX_HEIGHT / 2)
    screen.blit(exitTitle, rect)
    pygame.display.update()

def failedPage():
    exitTitle = myFont.render("YOU FAILED", True, 'turquoise')
    rect = exitTitle.get_rect(centerx = MAX_WIDTH / 2, centery = MAX_HEIGHT / 3)
    screen.blit(exitTitle, rect)
    pygame.display.update()

def main():
    # set fps
    fps = pygame.time.Clock()
    close = 1
    
    # cat
    imgcat1 = pygame.image.load('resources/cat1.png')
    imgcat2 = pygame.image.load('resources/cat2.png')
    imgcat1.set_colorkey((255, 255, 255))
    imgcat2.set_colorkey((255, 255, 255))
    cat_height = imgcat1.get_size()[1]
    cat_bottom = MAX_HEIGHT - cat_height
    cat_x = 50
    cat_y = cat_bottom
    jump_top = 200
    leg_swap = True
    is_bottom = True
    is_go_up = False
 
    # tree
    imgTree = pygame.image.load('resources/tree.png')
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

    # score
    score = 0
	
    #life
    life = 3
    life1 = pygame.image.load('resources/life_1.png')
    life2 = pygame.image.load('resources/life_2.png')
    life3 = pygame.image.load('resources/life_3.png')
    life1.set_colorkey((255, 255, 255))
    life2.set_colorkey((255, 255, 255))
    life3.set_colorkey((255, 255, 255))
	
    #background
    background = pygame.image.load('resources/sun2.png')	#sun background
    background2 = pygame.image.load('resources/cloud.png')	#cloud background
	
    difficulty = startPage()
    print(difficulty)

    while close:
        screen.blit(background, (0, 0))
 
        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:			# End the game(ESC key event)
                    finalPage(score)
                    pygame.display.update()
                    pygame.time.delay(3000)
                    pygame.quit()
                    sys.exit()
                if is_bottom:
                    is_go_up = True
                    is_bottom = False

        # cat move
        if is_go_up:
            cat_y -= 10.0
        elif not is_go_up and not is_bottom:
            cat_y += 10.0
 
        # cat top and bottom check
        if is_go_up and cat_y <= jump_top:
            is_go_up = False
 
        if not is_bottom and cat_y >= cat_bottom:
            is_bottom = True
            cat_y = cat_bottom
 
        # tree move
        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = MAX_WIDTH
 
        # draw tree
        screen.blit(imgTree, (tree_x, tree_y))
 
        # draw cat
        if leg_swap:
            screen.blit(imgcat1, (cat_x, cat_y))
            leg_swap = False
        else:
            screen.blit(imgcat2, (cat_x, cat_y))
            leg_swap = True

		# count score
        if tree_x < 9:
            if cat_y > (tree_y - 100):
                score -= 1
                life -= 1
                print(score)
            else:
                score += 1
                print(score)

		
		# show score
        printScore = "SCORE  " + str(score)
        text_title = myFont.render(printScore, True, 'violet')
        screen.blit(text_title, [630, 10])

		#life
        screen.blit(life1, (450, 15))
        screen.blit(life2, (500, 15))
        screen.blit(life3, (550, 15))
		
		#exit
        if life == 2:
            life1.set_alpha(0)
        elif life == 1:
            life2.set_alpha(0)
        elif life == 0:
            close -= 1
            pygame.time.delay(200)
            screen.blit(background2, (0, 0))
            failedPage()
            finalPage(score)
            pygame.time.delay(3000)

        # update
        pygame.display.update()
        fps.tick(difficulty)
 
 
if __name__ == '__main__':
    main()