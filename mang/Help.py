import pygame
import random

from pygame import mixer

##########
Vastusekoht = 80
Vastusetäidetud = []
Vastuseri = []
Vastuserinev = []
Valitud_vastus = ""
kvastus= []
tuup = "Title"
Milline = 0
lase_lahti = True
#########
#VALEMID
pyth_lause = "Kirjuta pythagorase teoreem, kus c on hüpotenuus."
pyth_valem =["c )square", "=","a )square","+", "b )square"]
pyth_vastused = [["2a+b2", "a2+b2", "2b+a2", "b2+a2"],["2c", "c2"]]

summaruudu_lause = "Kirjuta summaruudu/vaheruudu valem:"
summaruudu_valem = ["(", "a", "±", "b",") )square","=", "a )square", "±", "2ab","+","b )square"]
summaruudu_vastused =[["(a±b)2","(b±a)2","a(±b)2","b(±a)2"], ["2b±2ab+a2","b2±2ab+a2","2a±2ab+b2", "a2±2ab+b2", "±2ab+a2+b2", "±2ab+b2+a2"]]

ruutudevahe_lause ="Kirjuta ruutude vahe valem, kus lahutatakse b a-st"
ruutudevahe_valem = ["a )square", "-", "b )square", "=", "(", "a", "+", "b", ")", "(","a","-","b", ")"]
ruutudevahe_vastused =[["2a-b2", "a2-b2"],["(a-b)(a+b)","a(-b)(a+b)","(a-b)a(+b)","a(-b)a(+b)","(a+b)(a-b)","a(+b)(a-b)","(a+b)a(-b)","a(+b)a(-b)"]]

ringS_lause = "Kirjuta ringi pindala valem"
ringS_valem = ["S", "=", "π", "r ) square"]
ringS_vastused = [["S"],["πr2", "2rπ", "r2π"]]
VALEMID =[[pyth_lause, pyth_valem, pyth_vastused],[summaruudu_lause, summaruudu_valem,summaruudu_vastused],[ruutudevahe_lause,ruutudevahe_valem,ruutudevahe_vastused],[ringS_lause, ringS_valem, ringS_vastused]]
########

mixer.init()
mixer.music.load("Music.wav")
mixer.music.set_volume(0.7)
mixer.music.play(-1)
#######
pygame.init()

ekraani_pind = pygame.display.set_mode((1200,800))
pygame.display.set_caption("ÕpiPähe")
ekraani_pind.fill( (30,75,150) )

font_sort = pygame.font.SysFont("Arial", 25)

kontrollyV =150
kontrollxV =75
pilt2 = pygame.image.load("Out_line.png").convert()
kontrollV = pilt2.get_rect()
uus_pilt = pygame.transform.scale(pilt2,( 10* kontrollV.width, kontrollV.height))
kontrollV = uus_pilt.get_rect()
kontrollV.y = kontrollyV
kontrollV.x =kontrollxV

ekraani_pind.blit(uus_pilt, (kontrollxV, kontrollyV))   

kontrollx = 950
kontrolly = 350
pilt1 = pygame.image.load("Check.png")

kontroll = pilt1.get_rect()
pilt1 = pygame.transform.scale(pilt1,( kontroll.width/3, kontroll.height/3))
kontroll = pilt1.get_rect()
kontroll.x = kontrollx
kontroll.y = kontrolly
ekraani_pind.blit(pilt1, (kontrollx, kontrolly))

clearx = 950
cleary = 550
clear = pygame.image.load("Clear.png")
cleark = clear.get_rect()
clear = pygame.transform.scale(clear,( cleark.width/3, cleark.height/3))
cleark = clear.get_rect()
ekraani_pind.blit(clear, (clearx, cleary))
cleark.y =cleary
cleark.x =clearx
########################################

bg = pygame.image.load("Ruudustik.png")
bgk = bg.get_rect()
bg =pygame.transform.scale(bg,(bgk.width*1.5, bgk.height*1.5))
ekraani_pind.blit(bg,(0,0))

tbg = pygame.image.load("tbackground.png")
tbgk = tbg.get_rect()
tbg =pygame.transform.scale(tbg,(bgk.width*1.5, bgk.height*1.5))
ekraani_pind.blit(tbg,(0,0))

startbutx =600-150
startbuty = 400-100
startbut = pygame.image.load("Out_line.png")
kstartbut = startbut.get_rect()
startbut = pygame.transform.scale(startbut,( kstartbut.width*3, kstartbut.height*2))
kstartbut =startbut.get_rect()
kstartbut.x =startbutx
kstartbut.y =startbuty
ekraani_pind.blit(startbut, (startbutx, startbuty))

font_sortA = pygame.font.SysFont("Arial", 75)

tekstit = font_sortA.render("START", False, (0,0,0))

done = False
clock = pygame.time.Clock()





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
        elif tekst == "(" or tekst == ")":
            self.tekst = tekst
            self.font = pygame.font.SysFont("Arial", 45)
            self.eriline = True
        else:
            self.font = pygame.font.SysFont("Arial", 45)
            self.tekst = tekst
            self.eriline = False
        self.pilt = self.font.render(self.tekst, False, ( 0,0,0))
        self.id =id
        
        
key_list = pygame.sprite.Group()

def lisa_valem(class1, ulessanne_nimi, lisamiseks_valem, oige_vastus):
    x_areas = 25
    y_areas = 350
    increase = 0
    uus_valem = []
    for i in lisamiseks_valem:
            x = i.split(" )")
            for j in x:
                uus_valem +=[j]
    random.shuffle(uus_valem)
    for k in uus_valem:
        class1.add(Key(x_areas+increase, y_areas, k ,len(key_list) + 1))
        if (x_areas + increase) >= 550:
            y_areas += 105
            increase = 0
        else:
            increase+=105
    return ulessanne_nimi, oige_vastus

Milline = random.randint(0,(len(VALEMID)-1))
ulesanne, kontroll_vastused = lisa_valem(key_list, VALEMID[Milline][0] , VALEMID[Milline][1], VALEMID[Milline][2])
VALEMID.pop(Milline)
teksti_pilt = font_sort.render(ulesanne, False, (0,0,0))

while not done:
    if tuup == "Title":
        ekraani_pind.blit(tbg,(0,0))
        ekraani_pind.blit(startbut, (startbutx, startbuty))
        ekraani_pind.blit(tekstit, (500, 350))
        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if kstartbut.collidepoint(pos):
                    tuup = "mang"
    elif tuup == "mang":
        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.type == pygame.quit:
                    done = True
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y =pos[1]
                if event.button == 1:
                    for key in key_list:
                        if key.rect.collidepoint(pos):
                            if lase_lahti == True:
                                lase_lahti = False
                                blokkh= mixer.Sound("Blokk.wav")
                                blokkh.set_volume(0.7)
                                blokkh.play()
                            key.clicked = True
                        
                            
                                
                                
            if event.type == pygame.MOUSEBUTTONUP:
        
                lase_lahti = True
                pos = pygame.mouse.get_pos()
                if event.type == pygame.quit:
                    done = True
                if kontroll.collidepoint(pos):
                    for i in Vastusetäidetud:
                        for key in key_list:
                            if i == key.id:
                                Valitud_vastus += key.tekst
                    try:
                        kvastus = Valitud_vastus.split("=")
                        if len(kontroll_vastused) ==2:
                            if (kvastus[0] in kontroll_vastused[0] and kvastus[1] in kontroll_vastused[1]) or (kvastus[1] in kontroll_vastused[0] and kvastus[0] in kontroll_vastused[1]):
                                oigeh= mixer.Sound("Correct_ans.wav")
                                oigeh.set_volume(0.7)
                                oigeh.play()
                                del key_list
                                key_list = pygame.sprite.Group()
                                if len(VALEMID)== 0:
                                   pass
                                else:
                                   Milline = random.randint(0,(len(VALEMID)-1))
                                   ulesanne, kontroll_vastused = lisa_valem(key_list, VALEMID[Milline][0] , VALEMID[Milline][1], VALEMID[Milline][2])
                                   VALEMID.pop(Milline)
                                   teksti_pilt = font_sort.render(ulesanne, False, (0,0,0))
                            else:
                                flh= mixer.Sound("Wrong_ans.wav")
                                flh.set_volume(0.15)
                                flh.play()
                    except:
                        flh= mixer.Sound("Wrong_ans.wav")
                        flh.set_volume(0.15)
                        flh.play()
                    Valitud_vastus = ""
                    kvastus = []

                    
                    
                    
                    
                for key in key_list:
                    if pygame.Rect.colliderect(kontrollV, key.rect):
                        if key.id not in Vastusetäidetud and key.eriline == False:
                            Vastuseri += [key.id]
                            Vastusetäidetud +=[key.id]
                        elif key.id not in Vastusetäidetud:
                            Vastusetäidetud +=[key.id]
                            Vastuserinev +=[key.id] 
                        key.spot = True
                        key.rect.y = kontrollyV
                        if key.eriline == False:
                            key.rect.x = Vastusekoht + (Vastuseri.index(key.id))*105
                        else:
                             key.rect.x = Vastusekoht + (max(0, Vastusetäidetud.index(key.id) -Vastuserinev.index(key.id)-1))*105
                    else:
                        if key.id in Vastusetäidetud:
                            Vastusetäidetud.remove(key.id)
                        if key.id in Vastuseri:
                            Vastuseri.remove(key.id)
                        if key.id in Vastuserinev:
                            Vastuserinev.remove(key.id)

                        key.spot = False
                        
                    key.clicked = False
                    if key.spot == False:
                           key.rect.y = key.originaly
                           key.rect.x = key.originalx
                           
                if cleark.collidepoint(pos):
                    Vastusetäidetud = []
                    Vastuseri  = []
                    for key in key_list:
                        key.spot = False
                        key.rect.y = key.originaly
                        key.rect.x = key.originalx


        for key in key_list:
            if key.clicked == True:
                pos = pygame.mouse.get_pos()
                key.rect.x = pos[0]-(key.rect.width/2)
                key.rect.y =pos[1]-(key.rect.height/2)
        

        
        
        ekraani_pind.blit(bg,(0,0))          
        ekraani_pind.blit(pilt1, (kontrollx, kontrolly))
        ekraani_pind.blit(uus_pilt, (kontrollxV, kontrollyV))   
        key_list.draw(ekraani_pind)
        ekraani_pind.blit(clear, (clearx, cleary))
        ekraani_pind.blit(teksti_pilt, (25, 25))
        for key in key_list:
            if key.eriline == True and key.tekst == "2":
                ekraani_pind.blit(key.pilt,(key.rect.x + key.rect.width // 2 + 20 ,key.rect.y + key.rect.height // 2 - 25))
            elif  key.eriline == True and key.tekst == "(":
                ekraani_pind.blit(key.pilt,(key.rect.x + key.rect.width // 2 - 25 ,key.rect.y + key.rect.height // 2 - 15))
            elif  key.eriline == True and key.tekst == ")":
                ekraani_pind.blit(key.pilt,(key.rect.x + key.rect.width // 2 + 15 ,key.rect.y + key.rect.height // 2 - 15))
            else:
                ekraani_pind.blit(key.pilt,(key.rect.x + key.rect.width // 2 - 5 ,key.rect.y + key.rect.height // 2 - 15))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
