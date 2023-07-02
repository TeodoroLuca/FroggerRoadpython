import pygame
import os

def caminho_arquivo(nome:str):
    caminho = os.path.dirname(os.path.realpath(__file__))
    caminhoImg = os.path.join(caminho, nome)
    return caminhoImg

# Inicialização do pygame
pygame.init()

# Configurações da janela do jogo
largura_janela = 650
altura_janela = 650
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("FROGGER ROAD")

fundo = pygame.image.load((caminho_arquivo("fundo.png")))
fundo = pygame.transform.scale(fundo,(650,650))
# Carregamento das imagens

fundo2 = pygame.image.load(caminho_arquivo("fundo2.png"))
jogador_img = pygame.image.load(caminho_arquivo("frog.png"))
carro_img = pygame.image.load(caminho_arquivo("lamborghini.png"))
carro_img2 = pygame.image.load(caminho_arquivo("porshe.png"))
carro_img3 = pygame.image.load(caminho_arquivo("policia.png"))
carro_img4= pygame.image.load(caminho_arquivo("ferrari.png"))
ciclista_img = pygame.image.load(caminho_arquivo("ciclista.png"))
ciclista2_img = pygame.image.load(caminho_arquivo("ciclista4.png"))

# Variáveis do jogador
tamanho_jogador = 50
posicao_jogador_x = largura_janela // 2 - tamanho_jogador // 2
posicao_jogador_y = altura_janela - tamanho_jogador - 10
velocidade_jogador = 5

# Lista de carros
carros = []

# Variáveis do jogo
pontuacao = 0
vidas = 3
linha_chegada = 0

# Fontes do jogo
fonte = pygame.font.Font(caminho_arquivo('against regular.ttf'), 20)
fonte_vidas = pygame.font.Font(caminho_arquivo('against regular.ttf'), 20)
fonte2 = pygame.font.Font(None, 36)

# Variáveis de estado do jogo
menu_ativo = True
jogo_iniciado = False

# Classe Carros, ciclistas
class Carro:
    def __init__(self,y,v,direcao):
        self.tamanho = 50
        self.posicao_y = y
        self.velocidade = v
        self.direcao = direcao
        if self.direcao == "direita":
            self.posicao_x = -50
        else:
            self.posicao_x = 650
    
    def mover(self):
        if self.direcao == "direita":
            self.posicao_x += self.velocidade
            if self.posicao_x > 650:
                self.posicao_x = -50
        else:
            self.posicao_x -= self.velocidade
            if self.posicao_x < -50:
                self.posicao_x = 650
    
    def desenhar(self):
        janela.blit(carro_img, (self.posicao_x, self.posicao_y, self.tamanho, self.tamanho))

class Carro2:
    def __init__(self,y,v,direcao):
        self.tamanho = 50
        self.posicao_y = y
        self.velocidade = v
        self.direcao = direcao
        if self.direcao == "direita":
            self.posicao_x = -50
        else:
            self.posicao_x = 650
    
    def mover(self):
        if self.direcao == "direita":
            self.posicao_x += self.velocidade
            if self.posicao_x > 650:
                self.posicao_x = -50
        else:
            self.posicao_x -= self.velocidade
            if self.posicao_x < -50:
                self.posicao_x = 650
    
    def desenhar(self):
        janela.blit(carro_img2, (self.posicao_x, self.posicao_y, self.tamanho, self.tamanho))

class Carro3:
    def __init__(self,y,v,direcao):
        self.tamanho = 50
        self.posicao_y = y
        self.velocidade = v
        self.direcao = direcao
        if self.direcao == "direita":
            self.posicao_x = -50
        else:
            self.posicao_x = 650
    
    def mover(self):
        if self.direcao == "direita":
            self.posicao_x += self.velocidade
            if self.posicao_x > 650:
                self.posicao_x = -50
        else:
            self.posicao_x -= self.velocidade
            if self.posicao_x < -50:
                self.posicao_x = 650
    
    def desenhar(self):
        janela.blit(carro_img3, (self.posicao_x, self.posicao_y, self.tamanho, self.tamanho))

class Carro4:
    def __init__(self,y,v,direcao):
        self.tamanho = 50
        self.posicao_y = y
        self.velocidade = v
        self.direcao = direcao
        if self.direcao == "direita":
            self.posicao_x = -50
        else:
            self.posicao_x = 650
    
    def mover(self):
        if self.direcao == "direita":
            self.posicao_x += self.velocidade
            if self.posicao_x > 650:
                self.posicao_x = -50
        else:
            self.posicao_x -= self.velocidade
            if self.posicao_x < -50:
                self.posicao_x = 650
    
    def desenhar(self):
        janela.blit(carro_img4, (self.posicao_x, self.posicao_y, self.tamanho, self.tamanho))

class Ciclista:
    def __init__(self,y,v,direcao):
        self.tamanho = 50
        self.posicao_y = y
        self.velocidade = v
        self.direcao = direcao
        if self.direcao == "direita":
            self.posicao_x = -50
        else:
            self.posicao_x = 650
    
    def mover(self):
        if self.direcao == "direita":
            self.posicao_x += self.velocidade
            if self.posicao_x > 650:
                self.posicao_x = -50
        else:
            self.posicao_x -= self.velocidade
            if self.posicao_x < -50:
                self.posicao_x = 650
    
    def desenhar(self):
        janela.blit(ciclista_img, (self.posicao_x, self.posicao_y, self.tamanho, self.tamanho))

class Ciclista2:
    def __init__(self,y,v,direcao):
        self.tamanho = 50
        self.posicao_y = y
        self.velocidade = v
        self.direcao = direcao
        if self.direcao == "direita":
            self.posicao_x = -50
        else:
            self.posicao_x = 650
    
    def mover(self):
        if self.direcao == "direita":
            self.posicao_x += self.velocidade
            if self.posicao_x > 650:
                self.posicao_x = -50
        else:
            self.posicao_x -= self.velocidade
            if self.posicao_x < -50:
                self.posicao_x = 650
    
    def desenhar(self):
        janela.blit(ciclista2_img, (self.posicao_x, self.posicao_y, self.tamanho, self.tamanho))

# Função para desenhar objetos na janela
def desenhar_objetos():
    janela.blit(fundo2, (0, 0))
    janela.blit(jogador_img, (posicao_jogador_x, posicao_jogador_y))
    for carro in carros:
        carro.desenhar()
        carro.mover()

# Função para verificar colisão
def verificar_colisao():
    jogador_rect = pygame.Rect(posicao_jogador_x, posicao_jogador_y, tamanho_jogador, tamanho_jogador)
    for carro in carros:
        carro_rect = pygame.Rect(carro.posicao_x, carro.posicao_y, carro.tamanho, carro.tamanho)
        if jogador_rect.colliderect(carro_rect):
            return True
    return False

# Função para exibir o menu inicial
def exibir_menu():
    janela.blit(fundo,(0,0))
    
    titulo_fonte = pygame.font.Font(caminho_arquivo('against regular.ttf'), 25)
    titulo_texto = titulo_fonte.render("FROGGER ROAD", fonte2, True, (238, 118, 0))
    titulo_posicao = (largura_janela // 2 - titulo_texto.get_width() // 2, altura_janela // 660)
    janela.blit(titulo_texto, titulo_posicao)
    
    opcoes_fonte = pygame.font.Font(caminho_arquivo('against regular.ttf'), 25)
    iniciar_jogo_texto = opcoes_fonte.render("1. Iniciar Jogo", fonte, True, (238, 118, 0))
    instrucoes_texto = opcoes_fonte.render("2. Instruções de Jogo", fonte,  True, (238, 118, 0))
    sair_texto = opcoes_fonte.render("3. Sair", fonte, True,(238, 118, 0))
    
    iniciar_jogo_posicao = (largura_janela // 2 - iniciar_jogo_texto.get_width() // 2, altura_janela // 2)
    instrucoes_posicao = (largura_janela // 2 - instrucoes_texto.get_width() // 2, altura_janela // 2 + 100)
    sair_posicao = (largura_janela // 2 - sair_texto.get_width() // 2, altura_janela // 2 + 200)
    
    janela.blit(iniciar_jogo_texto, iniciar_jogo_posicao)
    janela.blit(instrucoes_texto, instrucoes_posicao)
    janela.blit(sair_texto, sair_posicao)
    
    #pygame.display.update()

# Função para exibir as instruções do jogo
def exibir_instrucoes():
    janela.blit(fundo, (0, 0))
    # texto das intruções
    instrucoes_fonte = pygame.font.Font(caminho_arquivo('against regular.ttf'), 20)
    instrucoes_texto1 = instrucoes_fonte.render("Instruções de Jogo", fonte2, True, (0, 139, 0))
    instrucoes_texto2 = instrucoes_fonte.render("Use as setas para mover o jogador", fonte2, True, (238, 118, 0))
    instrucoes_texto3 = instrucoes_fonte.render("Evite colidir com os carros", fonte2, True, (0, 139, 0))
    instrucoes_texto4 = instrucoes_fonte.render("Chegue à linha de chegada 3 vezes para vencer",fonte2, True, (238, 118, 0))
    instrucoes_texto5 = instrucoes_fonte.render("Você tem 3 vidas, cuidado!",fonte2, True, (0, 139, 0))
    instrucoes_texto6 = instrucoes_fonte.render("Pressione Enter para voltar ao menu",fonte2, True, (238, 118, 0))
    #posicionamento do texto na tela

    instrucoes_posicao1 = (largura_janela // 2 - instrucoes_texto1.get_width() // 2, altura_janela // 3 + 43)
    instrucoes_posicao2 = (largura_janela // 2 - instrucoes_texto2.get_width() // 2, altura_janela // 2)
    instrucoes_posicao3 = (largura_janela // 2 - instrucoes_texto3.get_width() // 2, altura_janela // 2 + 50)
    instrucoes_posicao4 = (largura_janela // 2 - instrucoes_texto4.get_width() // 2, altura_janela // 2 + 100)
    instrucoes_posicao5 = (largura_janela // 2 - instrucoes_texto5.get_width() // 2, altura_janela // 2 + 150)
    instrucoes_posicao6 = (largura_janela // 2 - instrucoes_texto6.get_width() // 2, altura_janela // 2 + 200)
    #imprime texto no pygame escrita e suas respectivas posições
    
    janela.blit(instrucoes_texto1, instrucoes_posicao1)
    janela.blit(instrucoes_texto2, instrucoes_posicao2)
    janela.blit(instrucoes_texto3, instrucoes_posicao3)
    janela.blit(instrucoes_texto4, instrucoes_posicao4)
    janela.blit(instrucoes_texto5, instrucoes_posicao5)
    janela.blit(instrucoes_texto6, instrucoes_posicao6)

#listaY = [60,120,280,340,450,530]
# Adiciona novos carros
direcao = "direita"
direcao2 = "esquerda"
listaY = [60,115,220,255,280,340,450,530]

#Loop para a movimentação dos carros e ciclistas
for i in range(1):
    v = (2)
    v2 = (3)
    v3 = (4)
    v4 = (6)
    v5 = (7)
    novo_carro = Carro(listaY[0],v4,direcao2)
    carros.append(novo_carro)
    novo_carro = Carro4(listaY[1],v5,direcao2)
    carros.append(novo_carro)
    novo_carro = Ciclista(listaY[2],v2,direcao2)
    carros.append(novo_carro)
    novo_carro = Ciclista2(listaY[3],v,direcao)
    carros.append(novo_carro)
    novo_carro = Carro4(listaY[4],v3,direcao2)
    carros.append(novo_carro)
    novo_carro = Carro2(listaY[5],v2,direcao)
    carros.append(novo_carro)
    novo_carro = Carro3(listaY[6],v2,direcao)
    carros.append(novo_carro)
    novo_carro = Carro(listaY[7],v3,direcao2)
    carros.append(novo_carro)
info = False

# Fonte para mensagem de fim de jogo
mensagem_fonte = pygame.font.Font(caminho_arquivo('against regular.ttf'), 20)

# Loop principal do jogo
clock = pygame.time.Clock()
game_over = False
jogandinho = True
while jogandinho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogandinho = False
        
        # Eventos do teclado
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                menu_ativo = False
                jogo_iniciado = True
            elif evento.key == pygame.K_2:
                info = True
            elif evento.key == pygame.K_3:
                game_over = True
                pygame.quit()
                
            if evento.key == pygame.K_RETURN:             
                info = False
    if info:
        exibir_instrucoes()

    elif not game_over:
        if menu_ativo:
            exibir_menu()
        elif jogo_iniciado:
            # Movimentação do jogador
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT] and posicao_jogador_x > 0:
                posicao_jogador_x -= velocidade_jogador
            if teclas[pygame.K_RIGHT] and posicao_jogador_x < largura_janela - tamanho_jogador:
                posicao_jogador_x += velocidade_jogador
            if teclas[pygame.K_UP] and posicao_jogador_y > 0:
                posicao_jogador_y -= velocidade_jogador
            if teclas[pygame.K_DOWN] and posicao_jogador_y < altura_janela - tamanho_jogador:
                posicao_jogador_y += velocidade_jogador

            # Movimentação dos carros
            for carro in carros:
                carro.mover()

            # Verificação de colisão
            if verificar_colisao():
                vidas -= 1
                if vidas == 0:
                    game_over = True
                else:
                    posicao_jogador_x = largura_janela // 2 - tamanho_jogador // 2
                    posicao_jogador_y = altura_janela - tamanho_jogador - 10

            # Verificação da linha de chegada
            if posicao_jogador_y <= linha_chegada:
                pontuacao += 1
                if pontuacao >= 3:
                    game_over = True
                else:
                    posicao_jogador_x = largura_janela // 2 - tamanho_jogador // 2
                    posicao_jogador_y = altura_janela - tamanho_jogador - 10

            # Renderização do jogo
            desenhar_objetos()

            # Placar de pontuação
            pontuacao_texto = fonte.render("Chegada: " + str(pontuacao), fonte2, True, (255, 255, 255))
            pontuacao_posicao = (500, 10)
            janela.blit(pontuacao_texto, pontuacao_posicao)

            # Placar de vidas
            vidas_texto = fonte.render("Vidas: " + str(vidas), fonte2, True, (255, 255, 255))
            vidas_posicao = (10, 10)
            janela.blit(vidas_texto, vidas_posicao)

            clock.tick(60)
    if game_over:
        # Exibir mensagem de fim de jogo quando todas as vidas forem perdidas
        if vidas == 0:
            janela.blit(fundo2, (0, 0))
            mensagem_fim = mensagem_fonte.render("Game Over!!! - Deseja Jogar Novamente s/n ", fonte2, True, (255, 0, 0))
            mensagem_fim_posicao = (largura_janela // 3 - mensagem_fim.get_width() // 3, altura_janela // 4 - mensagem_fim.get_height() // 1)
            janela.blit(mensagem_fim, mensagem_fim_posicao)

            for evento in pygame.event.get():
                # Eventos do teclado
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_s:
                        vidas = 4
                        menu_ativo = True
                        jogandinho = True
                        jogo_iniciado = False
                        game_over = False
                    elif evento.key == pygame.K_n:
                        jogandinho = False
                        #pygame.quit()
            
        # Exibir mensagem de fim de jogo quando todas as chegadas forem completadas
        elif pontuacao == 3:
            janela.blit(fundo2, (0, 0))
            mensagem_fim = mensagem_fonte.render("Você Ganhou - Deseja Jogar Novamente s/n ", fonte2, True, (0, 255, 50))
            mensagem_fim_posicao = (largura_janela // 3- mensagem_fim.get_width() // 3, altura_janela // 4 - mensagem_fim.get_height() // 1)
            janela.blit(mensagem_fim, mensagem_fim_posicao)

            for evento in pygame.event.get():
                # Eventos do teclado
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_s:
                        vidas = 3
                        pontuacao = -1
                        menu_ativo = True
                        jogandinho = True
                        jogo_iniciado = False
                        game_over = False
                    elif evento.key == pygame.K_n:
                        jogandinho = False
                        pygame.quit()
                    
    pygame.display.update()
pygame.quit()    
