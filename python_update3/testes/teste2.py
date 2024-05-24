import pygame
from dialogos import*

pygame.init()

x = 1280
y = 720

# Setando tela
tela = pygame.display.set_mode((x, y))
pygame.display.set_caption('Sitio do Saber')
relogio = pygame.time.Clock()

# Cores
branco = (255, 255, 255)

# Imagens e objetos
dial = pygame.font.Font('fontes/TitanOne-Regular.ttf', 35)
dialm1 = pygame.font.Font('fontes/TitanOne-Regular.ttf', 31)
dialm2 = pygame.font.Font('fontes/TitanOne-Regular.ttf', 28)

dialogo = dial.render('Olá, seja bem vinde ao Sitio do Saber!!!', 1, 'black')
dialogo2 = dial.render('onde tudo acontece de forma educativa.', 1, 'black')
dialogo3 = dialm2.render('O que acha de fazermos atividades por aqui?', 1, 'black')
dialogo4 = dial.render('Vamos para a primeira fase!!!', 1, 'black')
dialogo5 = dial.render('Esta é a sala de aula do sitio onde', 1, 'black')
dialogo6 = dialm2.render('vamos ter a primeira atividade do dia na lousa', 1, 'black')
dialogo7 = dialm2.render('Primeiro vamos dividir as maçãs para os cavalos',1,'black')
dialogo8 = dialm2.render('temos 4 maças e 2 cavalos, quantas maçãs cada',1,'black')
dialogo9 = dialm2.render('um comerá ?' ,1, 'black')
dialogo10 = dialm1.render('temos 4 maças e 2 cavalos, quantas maçãs cada',1,'black')
dialogo11 = dialm1.render('um comerá ?' ,1, 'black')

dialogo_rect = dialogo.get_rect(topleft=(50, 530))
dialogo_rect2 = dialogo.get_rect(topleft=(50, 610))
dialogo_rect3 = dialogo.get_rect(topleft=(55, 530))
dialogo_rect4 = dialogo.get_rect(topleft=(130, 610))
dialogo_rect5 = dialogo.get_rect(topleft=(100, 530))
dialogo_rect6 = dialogo.get_rect(topleft=(80, 610))
dialogo_rect7 = dialogo.get_rect(topleft=(60, 530))
dialogo_rect8 = dialogo.get_rect(topleft=(60, 590))
dialogo_rect9 = dialogo.get_rect(topleft=(60, 620))
dialogo_rect10 = dialogo.get_rect(topleft=(60, 590))
dialogo_rect11 = dialogo.get_rect(topleft=(60, 620))

cn = pygame.image.load('imagens/cenario2.png').convert()
cno = pygame.image.load('imagens/cenario_opaco (1).png').convert()
sl = pygame.image.load('imagens/saladaula.png').convert()
ls = pygame.image.load('imagens/lousa.png').convert()
cavalo = pygame.image.load('imagens/cavalo_sticker.png').convert_alpha()
maca = pygame.image.load('imagens/maca_sticker.png').convert_alpha()
prof = pygame.image.load('imagens/professora.png').convert_alpha()

prof_m = pygame.transform.scale(prof, (400, 400))
prof_M = pygame.transform.scale(prof, (450, 450))
prof = prof_m
pos_prof = (850, 290)
prof_rect = prof.get_rect(topleft=pos_prof)
cavalo_rect = cavalo.get_rect(topleft = (570, 200))
cavalo_rect2 = cavalo.get_rect(topleft = (360, 330))
maca_rect = maca.get_rect(topleft = (90, 300))
maca_rect2 = maca.get_rect(topleft = (190, 250))
maca_rect3 = maca.get_rect(topleft = (440, 100))
maca_rect4 = maca.get_rect(topleft = (310, 190))

bl = pygame.Rect(50, 520, 750, 150)

contador = 0
rt = False
# Loop
rodando = True

tam_alt = (150, 0)

while rodando:
    tela.blit(cn, (0, 0))
    tela.blit(prof, prof_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if prof_rect.collidepoint(pygame.mouse.get_pos()):
            prof = prof_M
            rt = True
            if cenario != sl and cenario != ls:
                cenario = cno

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == 1:
                    contador -= 1
        else:
            prof = prof_m
            if contador > 1:
                cenario = cn
            if contador <= 1:
                cenario = sl
            if contador <= 0:
                cenario = ls
                
            rt = False
    
    #print(contador)
    print(pygame.mouse.get_pos())

    # Colocando na tela
    tela.blit(cenario, (0, 0))
    tela.blit(prof, prof_rect)
    if contador == 0 or contador == -1:
        pygame.draw.line(tela, 'white', (70, 500), (800, 100), 15)
        tela.blit(cavalo, cavalo_rect)
        tela.blit(cavalo, cavalo_rect2)
        tela.blit(maca, maca_rect)
        tela.blit(maca, maca_rect2)
        tela.blit(maca, maca_rect3)
        tela.blit(maca, maca_rect4)
        if contador == -1:

            tela.blit(dialogo10, dialogo_rect10)
            tela.blit(dialogo11, dialogo_rect11)
            pygame.draw.rect(tela, branco, bl)
            #Alternativa 001
            alt_a = dial.render('1', 1, 'black')
            palt_a = (1033,83)
            
            alta_rect = alt_a.get_rect(center = palt_a)
            pygame.draw.rect(tela,'white',alta_rect.inflate(tam_alt))
            tela.blit(alt_a, alta_rect)
            pygame.draw.rect(tela,'Black',alta_rect.inflate(tam_alt),6)
            
            #Alternativa 002
            alt_b = dial.render('2', 1, 'black')
            palt_b = (1033,133)
            
            altb_rect = alt_b.get_rect(center = palt_b)
            pygame.draw.rect(tela,'white',altb_rect.inflate(tam_alt))
            tela.blit(alt_b, altb_rect)
            pygame.draw.rect(tela,'Black',altb_rect.inflate(tam_alt),6)

            #Alternativa 003
            alt_c = dial.render('3', 1, 'black')
            palt_c = (1033,183)
            
            altc_rect = alt_c.get_rect(center = palt_c)
            pygame.draw.rect(tela,'white',altc_rect.inflate(tam_alt))
            tela.blit(alt_c, altc_rect)
            pygame.draw.rect(tela,'Black',altc_rect.inflate(tam_alt),6)

            #Alternativa 004
            alt_d = dial.render('4', 1, 'black')
            palt_d = (1033,233)
            
            altd_rect = alt_d.get_rect(center = palt_d)
            pygame.draw.rect(tela,'white',altd_rect.inflate(tam_alt))
            tela.blit(alt_d, altd_rect)
            pygame.draw.rect(tela,'Black',altd_rect.inflate(tam_alt),6)

    if rt:
        pygame.draw.rect(tela, branco, bl)
        if contador == 3:
            tela.blit(dialogo, dialogo_rect)
            tela.blit(dialogo2, dialogo_rect2)
        elif contador == 2:
            tela.blit(dialogo3, dialogo_rect3)
            tela.blit(dialogo4, dialogo_rect4)
        elif contador == 1:
            cenario = sl
            tela.blit(dialogo5, dialogo_rect5)
            tela.blit(dialogo6, dialogo_rect6)
        elif contador == 0:
            cenario = ls
            tela.blit(dialogo7, dialogo_rect7)
            tela.blit(dialogo8, dialogo_rect8)
            tela.blit(dialogo9, dialogo_rect9)
        elif contador == -1:
            tela.blit(dialogo10, dialogo_rect10)
            tela.blit(dialogo11, dialogo_rect11)
            
            
            
            

            

    pygame.display.update()
    relogio.tick(60)