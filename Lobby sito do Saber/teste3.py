import pygame
from dialogos import*
    #Coloca um if
    # se a resp estiver certa ele puxa outra def
    #Se estiver certo, puxa a def de pergunta

pygame.init()

# Constantes
WIDTH = 1280
HEIGHT = 720
WHITE = (255, 255, 255)

# Inicialização da tela e relógio
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sitio do Saber')
relogio = pygame.time.Clock()

# Fontes
dial = pygame.font.Font('fontes/TitanOne-Regular.ttf', 35)
dialm1 = pygame.font.Font('fontes/TitanOne-Regular.ttf', 31)
dialm2 = pygame.font.Font('fontes/TitanOne-Regular.ttf', 28)

# Funções de diálogo
def render_dialogos():
    return [
        dial.render('Olá, seja bem vinde ao Sitio do Saber!!!', 1, 'black'),
        dial.render('onde tudo acontece de forma educativa.', 1, 'black'),
        dialm2.render('O que acha de fazermos atividades por aqui?', 1, 'black'),
        dial.render('Vamos para a primeira fase!!!', 1, 'black'),
        dial.render('Esta é a sala de aula do sitio onde', 1, 'black'),
        dialm2.render('vamos ter a primeira atividade do dia na lousa', 1, 'black'),
        dialm2.render('Primeiro vamos dividir as maçãs para os cavalos',1,'black'),
        dialm2.render('temos 4 maças e 2 cavalos, quantas maçãs cada',1,'black'),
        dialm2.render('um comerá ?' ,1, 'black'),
        dialm1.render('temos 4 maças e 2 cavalos, quantas maçãs cada',1,'black'),
        dialm1.render('um comerá ?' ,1, 'black')
    ]

def get_dialogo_rects():
    return [
        dialogos[0].get_rect(topleft=(50, 530)),
        dialogos[1].get_rect(topleft=(50, 610)),
        dialogos[2].get_rect(topleft=(55, 530)),
        dialogos[3].get_rect(topleft=(130, 610)),
        dialogos[4].get_rect(topleft=(100, 530)),
        dialogos[5].get_rect(topleft=(80, 610)),
        dialogos[6].get_rect(topleft=(60, 530)),
        dialogos[7].get_rect(topleft=(60, 590)),
        dialogos[8].get_rect(topleft=(60, 620)),
        dialogos[9].get_rect(topleft=(60, 590)),
        dialogos[10].get_rect(topleft=(60, 620))
    ]

# Carregar imagens
def load_images():
    return {
        'cn': pygame.image.load('imagens/cenario2.png').convert(),
        'cno': pygame.image.load('imagens/cenario_opaco (1).png').convert(),
        'sl': pygame.image.load('imagens/saladaula.png').convert(),
        'ls': pygame.image.load('imagens/lousa.png').convert(),
        'cavalo': pygame.image.load('imagens/cavalo_sticker.png').convert_alpha(),
        'maca': pygame.image.load('imagens/maca_sticker.png').convert_alpha(),
        'prof': pygame.image.load('imagens/professora.png').convert_alpha()
    }

# Escalar imagens da professora
def scale_prof_images(images):
    images['prof_m'] = pygame.transform.scale(images['prof'], (400, 400))
    images['prof_M'] = pygame.transform.scale(images['prof'], (450, 450))
    images['prof'] = images['prof_m']
    return images

# Inicialização de variáveis
def initialize_variables():
    return {
        'pos_prof': (850, 290),
        'prof_rect': images['prof'].get_rect(topleft=(850, 290)),
        'cavalo_rect': images['cavalo'].get_rect(topleft=(570, 200)),
        'cavalo_rect2': images['cavalo'].get_rect(topleft=(360, 330)),
        'maca_rect': images['maca'].get_rect(topleft=(90, 300)),
        'maca_rect2': images['maca'].get_rect(topleft=(190, 250)),
        'maca_rect3': images['maca'].get_rect(topleft=(440, 100)),
        'maca_rect4': images['maca'].get_rect(topleft=(310, 190)),
        'bl': pygame.Rect(50, 520, 750, 150),
        'contador': 3,
        'erro': False,
        'rt': False,
        'cenario': images['cn'],
        'rodando': True,
        'tam_alt': (150, 0)
    }

# Funções para desenhar elementos
def draw_professora(tela, images, variables):
    tela.blit(images['prof'], variables['prof_rect'])

def draw_cenario(tela, images, variables):
    tela.blit(variables['cenario'], (0, 0))

def draw_elements(tela, images, variables):
    if variables['contador'] == 0 or variables['contador'] == -1:
        pygame.draw.line(tela, 'white', (70, 500), (800, 100), 15)
        tela.blit(images['cavalo'], variables['cavalo_rect'])
        tela.blit(images['cavalo'], variables['cavalo_rect2'])
        tela.blit(images['maca'], variables['maca_rect'])
        tela.blit(images['maca'], variables['maca_rect2'])
        tela.blit(images['maca'], variables['maca_rect3'])
        tela.blit(images['maca'], variables['maca_rect4'])
        if variables['contador'] == -1:
            draw_alternativas(tela, variables)
#
def draw_alternativas(tela, variables):
            pygame.draw.rect(tela, 'white', variables['bl'])
            #Alternativa 001
            alt_a = dial.render('1', 1, 'black')
            palt_a = (1033,83)
            
            alta_rect = alt_a.get_rect(center = palt_a)
            pygame.draw.rect(tela,'white',alta_rect.inflate(variables['tam_alt']))
            tela.blit(alt_a, alta_rect)
            pygame.draw.rect(tela,'Black',alta_rect.inflate(variables['tam_alt']),6)
            
            #Alternativa 002
            alt_b = dial.render('2', 1, 'black')
            palt_b = (1033,133)
            
            altb_rect = alt_b.get_rect(center = palt_b)
            pygame.draw.rect(tela,'white',altb_rect.inflate(variables['tam_alt']))
            tela.blit(alt_b, altb_rect)
            pygame.draw.rect(tela,'Black',altb_rect.inflate(variables['tam_alt']),6)

            #Alternativa 003
            alt_c = dial.render('3', 1, 'black')
            palt_c = (1033,183)
            
            altc_rect = alt_c.get_rect(center = palt_c)
            pygame.draw.rect(tela,'white',altc_rect.inflate(variables['tam_alt']))
            tela.blit(alt_c, altc_rect)
            pygame.draw.rect(tela,'Black',altc_rect.inflate(variables['tam_alt']),6)

            #Alternativa 004
            alt_d = dial.render('4', 1, 'black')
            palt_d = (1033,233)
            
            altd_rect = alt_d.get_rect(center = palt_d)
            pygame.draw.rect(tela,'white',altd_rect.inflate(variables['tam_alt']))
            tela.blit(alt_d, altd_rect)
            pygame.draw.rect(tela,'Black',altd_rect.inflate(variables['tam_alt']),6)
            
            '''if pygame.mouse.get_pressed()[0] == 1:
             pos_mouse = pygame.mouse.get_pos()
            if variables['alta_rect'].collidepoint(pos_mouse):
                pass
            
            res = True

            if altb_rect.collidepoint(pos_mouse):
                if res:
                    print('Acertou')
                    res = False
            elif alta_rect.collidepoint(pos_mouse):
                if res:
                    print('Errou')
                    res = False
            elif altc_rect.collidepoint(pos_mouse):
                if res:
                    print('Errou')
                    res = False
            elif altd_rect.collidepoint(pos_mouse):
                if res:
                    print('Errou')
                    res = False
            else:
                res = True'''

                
def colid_alt(tela, variables):
    pass

def draw_dialogo(tela, variables):
    pygame.draw.rect(tela, WHITE, variables['bl'])
    if variables['contador'] == 3:
        tela.blit(dialogos[0], dialogo_rects[0])
        tela.blit(dialogos[1], dialogo_rects[1])
    elif variables['contador'] == 2:
        tela.blit(dialogos[2], dialogo_rects[2])
        tela.blit(dialogos[3], dialogo_rects[3])
    elif variables['contador'] == 1:
        variables['cenario'] = images['sl']
        tela.blit(dialogos[4], dialogo_rects[4])
        tela.blit(dialogos[5], dialogo_rects[5])
    elif variables['contador'] == 0:
        variables['cenario'] = images['ls']
        tela.blit(dialogos[6], dialogo_rects[6])
        tela.blit(dialogos[7], dialogo_rects[7])
        tela.blit(dialogos[8], dialogo_rects[8])
    elif variables['contador'] == -1:
        tela.blit(dialogos[9], dialogo_rects[9])
        tela.blit(dialogos[10], dialogo_rects[10])

# Função principal do jogo
def game_loop():
    while variables['rodando']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                variables['rodando'] = False
            if variables['prof_rect'].collidepoint(pygame.mouse.get_pos()):
                images['prof'] = images['prof_M']
                variables['rt'] = True
                if variables['cenario'] != images['sl'] and variables['cenario'] != images['ls']:
                    variables['cenario'] = images['cno']
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] == 1:
                        variables['contador'] -= 1
            else:
                images['prof'] = images['prof_m']
                if variables['contador'] > 1:
                    variables['cenario'] = images['cn']
                if variables['contador'] <= 1:
                    variables['cenario'] = images['sl']
                if variables['contador'] <= 0:
                    variables['cenario'] = images['ls']
                variables['rt'] = False
                    


        draw_cenario(tela, images, variables)
        draw_professora(tela, images, variables)
        draw_elements(tela, images, variables)
        if variables['rt']:
            draw_dialogo(tela, variables)

        pygame.display.update()
        relogio.tick(60)

# Inicializações e chamadas de função
dialogos = render_dialogos()
dialogo_rects = get_dialogo_rects()
images = scale_prof_images(load_images())
variables = initialize_variables()

game_loop()
pygame.quit()