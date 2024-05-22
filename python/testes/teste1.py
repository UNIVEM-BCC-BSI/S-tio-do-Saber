import pygame

pygame.init()

x = 1280
y = 720
#setando tela
tela = pygame.display.set_mode((x,y))
pygame.display.set_caption('sitio do saber')
#cores
branco = (255, 255, 255)
#imagens e objetos
dial = pygame.font.Font('fontes/TitanOne-Regular.ttf', 35)
dialogo = dial.render('Olá, seja bem vinde ao Sitio do Saber!!!', 1, 'black')
dialogo_rect = dialogo.get_rect(topleft = (50, 520))
cn = pygame.image.load('imagens/cenario2.png').convert()
prof = pygame.image.load('imagens/professora.png').convert_alpha()
prof_m = pygame.transform.scale(prof, (400, 400))
prof_M = pygame.transform.scale(prof, (450, 450))
prof = prof_m
pos_prof= (850, 290)
prof_rect = prof.get_rect(topleft = pos_prof)
bl = pygame.Rect(50, 520, 750, 150)
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]==1:
                        rt = True
        else:
             prof = prof_m
             rt = False


#colocando na tela
    tela.blit(cn, (0, 0))
    tela.blit(prof, prof_rect)
    if rt:
         
         pygame.draw.rect(tela, branco, bl)
         tela.blit(dialogo, dialogo_rect)

    pygame.display.update()