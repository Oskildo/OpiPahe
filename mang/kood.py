import pygame
import random

pygame.init()

ekraani_pind = pygame.display.set_mode((1200,800))
pygame.display.set_caption("ÕpiPähe")
ekraani_pind.fill( (30,75,150) )

font_sort = pygame.font.SysFont("Arial", 25)
# -----------------
class Key(pygame.sprite.Sprite):
     def __init__(self, xpos, ypos, tekst, id):
        super(Key, self).__init__()
        self.image = pygame.image.load("Out_line.png").convert()
        self.clicked = False
        self.spot = False
        self.rect = self.image.get_rect()
        self.rect.width = round(self.rect.width*0.8)
        self.rect.height = round(self.rect.height*1.2)
        self.rect.y = ypos
        self.rect.x = xpos
        self.originaly = ypos
        self.originalx = xpos
        if tekst == "square":
            self.tekst = "2"
            self.font = pygame.font.SysFont("Arial", 25)
            self.eriline = True
        else:
            self.font = pygame.font.SysFont("Arial", 45)
            self.tekst = tekst
            self.eriline = False
        self.pilt = self.font.render(self.tekst, False, (255,255,255))
        self.id =id
#______________________________     
class Answer(pygame.sprite.Sprite):
     def __init__(self, xpos, ypos, tekst, rida, id):
         super(Answer, self).__init__()
         self.image = pygame.image.load("In_line.png").convert()
         self.filled = 0
         self.rect = self.image.get_rect()
         self.rect.y = ypos
         self.rect.x = xpos
         self.tekst = ""
         self.rida = rida
         self.id =id
# ----------------

done = False
clock = pygame.time.Clock()

pilt1 = pygame.image.load("Check.png")
kontroll = pilt1.get_rect()
kontrollx =1050
kontrolly = 250
kontroll.x =kontrollx
kontroll.y = kontrolly
ekraani_pind.blit(pilt1, (kontrollx, kontrolly))
#DDDDDDDDDD
key_list = pygame.sprite.Group()
answer_list = pygame.sprite.Group()
#FFFFFFFFFFFF



def lisa_valem(class1, class2, ulessanne_nimi, lisamiseks_valem, oige_vastus):
    x_areas = 25
    y_areas = 350
    increase = 0
    uus_valem = []
    mitmes = 0

    for i in lisamiseks_valem:
        x = i.split(" )")
        if len(x) >= 2:
            if x[1] == "square":
                class1.add(Answer(x_areas + increase, 100, x[0]+"2" , mitmes, len(answer_list) + 1))
        else:
            class1.add(Answer(x_areas + increase, 100, i , mitmes, len(answer_list) + 1))
        increase+= 105
        mitmes += 1
    increase = 0
    for i in lisamiseks_valem:
            x = i.split(" )")
            for j in x:
                uus_valem +=[j]
    random.shuffle(uus_valem)
    for k in uus_valem:
        class2.add(Key(x_areas+increase, y_areas, k ,len(key_list) + 1))
        if (x_areas + increase) >= 550:
            y_areas += 105
            increase = 0
        else:
            increase+=105
    return ulessanne_nimi, oige_vastus

pyth_valem =["c )square", "=","a )square","+", "b )square"]
pyth_vastused = [['c2', '=', 'a2', '+', 'b2'], ['c2', '=', 'b2', '+', 'a2'], ['a2', '+', 'b2', '=', 'c2'], ['b2', '+', 'a2', '=', 'c2']]

summaruudu_valem = ["(", "a", "+", "b",") )square","=", "a )square", "+", "2ab","+","b )square"]
summaruudu_vastused = [["(", "a", "+", "b",")2","=", "a2", "+", "2ab","+","b2"], ["(", "b", "+", "a",")2","=", "b2", "+", "2ab","+","a2"], ["b2", "+", "2ab","+","a2","=", "(", "b", "+", "a",")2"], ["a2", "+", "2ab","+","b2","=", "(", "a", "+", "b",")2"]]
kontroll_vastused =[]


ulesanne, kontroll_vastused = lisa_valem(answer_list, key_list, "Kirjuta pythagorase teoreem, kus c on hüpotenuus." , pyth_valem, pyth_vastused)

teksti_pilt = font_sort.render(ulesanne, False, (255,255,255))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done = True
#-----------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y =pos[1]
            if event.button == 1:
                for key in key_list:
                    if key.rect.collidepoint(pos):
                        key.clicked = True
#                 if kontroll.collidepoint(pos):
#                     for cols in range(len(collisions)):
#                         answer = collisions[voti[cols]][0]
#                         key = voti[cols]
#                         if pygame.Rect.colliderect(answer.rect,key.rect) and key.eriline == False:
#                             answer.tekst = key.tekst
#                     for cols in range(len(collisions)):
#                         answer = collisions[voti[cols]][0]
#                         key = voti[cols]
#                         if key.eriline == True and pygame.Rect.colliderect(answer.rect,key.rect):
#                             answer.tekst += key.tekst
#                     kontrollima = []
#                     for s in range(len(collisions)):
#                         kontrollima += ["g"]
#                     for cols in range(len(collisions)):
#                         answer = collisions[voti[cols]][0]
#                         key = voti[cols]
#                         if key.eriline == False:
#                             try:
#                                 kontrollima[answer.rida] = answer.tekst
#                             except:
#                                 pass
#                     while "g" in kontrollima:
#                         if "g" in kontrollima:
#                             kontrollima.remove("g")
#                     if kontrollima in kontroll_vastused and kontroll_vastused != summaruudu_vastused:
#                         del key_list
#                         del answer_list
#                         key_list = pygame.sprite.Group()
#                         answer_list = pygame.sprite.Group()
#                         ulesanne, kontroll_vastused = lisa_valem(answer_list, key_list, "Summa ruudu valem on", summaruudu_valem, summaruudu_vastused)
#                         teksti_pilt = font_sort.render(ulesanne, False, (255,255,255))
#                     elif kontrollima in kontroll_vastused:
#                         del key_list
#                         del answer_list
#                         key_list = pygame.sprite.Group()
#                         answer_list = pygame.sprite.Group()
#                         teksti_pilt = font_sort.render("TUBLI TÖÖ", False, (255,255,255))
#                     else:
#                         pass
#                     oige_vastus = []
                    
######################
        
        if event.type == pygame.MOUSEBUTTONUP:
            for key in key_list:
                key.clicked = False
                if key.spot == False:
                   key.rect.y = key.originaly
                   key.rect.x = key.originalx                  
#     collisions = pygame.sprite.groupcollide(key_list, answer_list, False, False, collided = None)
#     voti = list(collisions)
#     val_list = list(collisions.values())
#     if len(collisions) == 0:
#         for keys in key_list:
#             keys.spot = False
#     for keys in key_list:
#         if keys not in voti and keys.spot == True:
#             keys.spot = False
#             drag_id = 0
#     for answers in answer_list:
#         if answers not in val_list and answers.tekst != "":
#             answers.tekst = ""
#             drag_id = 0
#     for cols in range(len(collisions)):
#         answer = collisions[voti[cols]][0]
#         key = voti[cols]
#         print( collisions[voti[cols]][0])
#         if pygame.Rect.colliderect(answer.rect,key.rect) and key.spot == False:
#             answer.tekst = key.tekst
#             key.spot = True
#             key.rect.x = answer.rect.x
#             key.rect.y = answer.rect.y
#         elif pygame.Rect.colliderect(answer.rect,key.rect) and key.eriline ==  False:
#             answer.tekst = key.tekst
#             key.rect.x = answer.rect.x
#             key.rect.y = answer.rect.y
#         if pygame.Rect.colliderect(answer.rect,key.rect) and key.eriline  == True:
#             key.rect.x = answer.rect.x
#             key.rect.y = answer.rect.y

    for key in key_list:
        if key.clicked == True:
            pos = pygame.mouse.get_pos()
            key.rect.x = pos[0]-(key.rect.width/2)
            key.rect.y =pos[1]-(key.rect.height/2)
    ekraani_pind.fill( (30,75,150) )           
    ekraani_pind.blit(pilt1, (kontrollx, kontrolly))
    answer_list.draw(ekraani_pind)
    key_list.draw(ekraani_pind)
    for key in key_list:
        if key.eriline == True:
            ekraani_pind.blit(key.pilt,(key.rect.x + key.rect.width // 2 + 20 ,key.rect.y + key.rect.height // 2 - 25))
        else:
            ekraani_pind.blit(key.pilt,(key.rect.x + key.rect.width // 2 - 5 ,key.rect.y + key.rect.height // 2 - 15))
    ekraani_pind.blit(teksti_pilt, (25, 25))
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
