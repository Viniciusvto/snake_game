🐍 Jogo Snake em Python com Pygame

📌 Descrição do Projeto
Desenvolvido em Python com a biblioteca Pygame. O objetivo é movimentar a cobra pela tela, coletar a comida que aparece aleatoriamente e evitar colisões com as paredes e com o próprio corpo.

🎮 Funcionalidades Principais
Movimentação da cobra com as setas do teclado.

Geração aleatória da comida em posições válidas da tela.

A cada comida consumida:

A cobra cresce em tamanho.

A pontuação é aumentada.

O jogo termina quando:

A cobra bate na parede.

A cobra colide com seu próprio corpo.

A pontuação atual é exibida em tempo real no canto superior da tela.

🧠 Conceitos e Técnicas Utilizadas
Pygame para manipulação da interface gráfica, eventos e atualização de tela.

Controle de frames por segundo (FPS) com pygame.time.Clock(), definindo a velocidade do jogo.

Eventos de teclado com pygame.KEYDOWN para detectar a direção do movimento.

Sistema de colisão:

Cobra com comida (para crescer).

Cobra com paredes (fim de jogo).

Cobra com ela mesma (fim de jogo).

Renderização em tela com pygame.draw.rect() para desenhar a cobra e a comida.

Lógica de crescimento da cobra, baseada em uma lista de posições (pixels).

Fonte e renderização de texto com pygame.font.SysFont() para exibir a pontuação.


🖥️ Requisitos
Python 3.8 ou superior
Biblioteca Pygame
Instale com:

![snake_game](https://github.com/user-attachments/assets/07990cbd-0e90-4159-abf2-9503c5bc36b9)
