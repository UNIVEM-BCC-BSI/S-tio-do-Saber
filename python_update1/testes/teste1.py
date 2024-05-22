import pygame
from dialogos import*

pygame.init()

x = 1280
y = 720
#setando tela

tela = pygame.display.set_mode((x,y))
pygame.display.set_caption('sitio do saber')
#pygame.image.load()
#pygame.display.set_icon()
#cores

branco = (255, 255, 255)
#imagens e objetos

dial = pygame.font.Font('fontes/TitanOne-Regular.ttf', 35)
dialm = pygame.font.Font('fontes/TitanOne-Regular.ttf', 31)

dialogo = dial.render('Olá, seja bem vinde ao Sitio do Saber!!!', 1, 'black')
dialogo2 = dial.render('onde tudo acontece de forma educativa.', 1, 'black')
dialogo3 = dialm.render('Oque acha de fazermos atividades por aqui?', 1, 'black')
dialogo4 = dial.render('vamos para a primeira fase !!!', 1, 'black')

dialogo_rect = dialogo.get_rect(topleft = (50, 530))
dialogo_rect2 = dialogo.get_rect(topleft = (50,610)) 
dialogo_rect3 = dialogo.get_rect(topleft = (55, 530))
dialogo_rect4 = dialogo.get_rect(topleft = (130, 610))

cn = pygame.image.load('imagens/cenario2.png').convert()
cno = pygame.image.load('imagens/cenario_opaco (1).png').convert()
cenario = cn

prof = pygame.image.load('imagens/professora.png').convert_alpha()
prof_m = pygame.transform.scale(prof, (400, 400))
prof_M = pygame.transform.scale(prof, (450, 450))
prof = prof_m
pos_prof= (850, 290)
prof_rect = prof.get_rect(topleft = pos_prof)

bl = pygame.Rect(50, 520, 750, 150)

contador = 3
rt = False
#loop
rodando = True

while rodando:
    tela.blit(cn, (0, 0))
    tela.blit(prof, prof_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if prof_rect.collidepoint(pygame.mouse.get_pos()):
            prof = prof_M
            cenario = cno

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]==1:
                        rt = True
                        contador -= 1
        else:
             prof = prof_m
             cenario = cn
             rt = False
    print(contador)

#colocando na tela
    tela.blit(cenario, (0, 0))
    tela.blit(prof, prof_rect)
    if rt:
        if contador == 2:
            pygame.draw.rect(tela, branco, bl)
            tela.blit(dialogo, dialogo_rect)
            tela.blit(dialogo2, dialogo_rect2)
        if contador == 1:
            pygame.draw.rect(tela, branco, bl)
            tela.blit(dialogo3, dialogo_rect3)
            tela.blit(dialogo4, dialogo_rect4)
        if contador == 0:
            pygame.draw.rect(tela, branco, bl)
    pygame.display.update()