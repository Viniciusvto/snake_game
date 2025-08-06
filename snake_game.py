# configurações iniciais

import pygame # Biblioteca para criar jgos

import random # Para numeros aleatorios (posicao da comida)

pygame.init() #iniciei todos os modolos da biblioteca

pygame.display.set_caption("Jogo Snake Python") # Defini o titulo da janela

largura, altura = 1200, 800 # dimensoes da janela

tela = pygame.display.set_mode((largura, altura)) # Criei a janela do jogo

relogio = pygame.time.Clock() # Controlo a velocidade do jogo por meio do relogio (como?)

# cores RGB, Defino as cores que vou usar

preta = (0, 0, 0)

branca = (255, 255, 255)

vermelha = (255, 0, 0)

verde = (0, 255, 0)

# parametros da cobrinha

tamanho_quadrado = 20 # tamanho de cada segmento da cobra/comida

velocidade_jogo = 15 # velocidade da atualizacao do jogo(fps)

def gerar_comida(): #gera as coordenadas em x e y (explicar melhor)

    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
#desenhei a comida sendo verde
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
#desenha cada segmento da cobra sendo um pontinho branco
    for pixel in pixels:

        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
#crio o texto com a pontuacao atual e defino o tamanho e a cor
    fonte = pygame.font.SysFont("Helvetica", 35)

    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)

    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
# funcao para controlar a direcao com base na tecla
    if tecla == pygame.K_DOWN: #seta pra baixo

        velocidade_x = 0

        velocidade_y = tamanho_quadrado

    elif tecla == pygame.K_UP: # seta pra cima

        velocidade_x = 0

        velocidade_y = -tamanho_quadrado

    elif tecla == pygame.K_RIGHT: #seta pra direita

        velocidade_x = tamanho_quadrado

        velocidade_y = 0

    elif tecla == pygame.K_LEFT: #seta pra esquerda

        velocidade_x = -tamanho_quadrado

        velocidade_y = 0

    return velocidade_x, velocidade_y

def rodar_jogo():
    #funcao principal do jogo
    fim_jogo = False

    x = largura / 2 #posicao inicial da cobra em x

    y = altura / 2 #posicao inicial da cobra em y

    velocidade_x = 0 # parado em x

    velocidade_y = 0 #inicia parado em y tmb

    tamanho_cobra = 1 # tamanho inicial 1 so pixel

    pixels = [] #armazena o tamanho dela

    comida_x, comida_y = gerar_comida() #gera a primeira comida

    while not fim_jogo:

        tela.fill(preta) #limpa a tela com a cor preta

        for evento in pygame.event.get(): #verifica eventos (tecla, mouse)

            if evento.type == pygame.QUIT: # se clicar x fecha

                fim_jogo = True
            elif evento.type == pygame.KEYDOWN: # se precionar uma telcla

                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # desenhar_comida

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualizar a posicao da cobra

        if x < 0 or x >= largura or y < 0 or y >= altura: # se bateu na parede

            fim_jogo = True

        x += velocidade_x # atualiza posicao em x

        y += velocidade_y #atualiza posicao em y

        # atualiza o corpo da cobra

        pixels.append([x, y]) #Adiciona nova posicao

        if len(pixels) > tamanho_cobra: # remove segmentos extras

            del pixels[0]

        # se a cobrinha bateu no proprio corpo

        for pixel in pixels[:-1]:

            if pixel == [x, y]:

                fim_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels) # desenha a cobra e a pontuacao


        desenhar_pontuacao(tamanho_cobra - 1) #pontuacao = tamanho-1

        # atualizacao da tela

        pygame.display.update()

        # criar uma nova comida

        if x == comida_x and y == comida_y: #verifica se a cobra comeu

            tamanho_cobra += 1 #aumenta a cobra em u tamanho

            comida_x, comida_y = gerar_comida() #gera outra comida

        relogio.tick(velocidade_jogo) #controlei a velocidade por aqui

rodar_jogo()