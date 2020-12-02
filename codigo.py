
import random
import time
import pygame
pygame.init()
relogio = pygame.time.Clock()
pygame.display.set_caption("Alfabetizando")

icon = pygame.image.load("assets/icon.jpg")
pygame.display.set_icon(icon)
largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
background = pygame.image.load("assets/sky.png")
lapis = pygame.image.load("assets/lapis.png")
lapisLargura = 260
lapisPosicaoX = 360
lapisPosicaoY = 470
lapisMovimento = 0
lapisVelocidade = 10
missel = pygame.image.load("assets/missile.png")
misselLargura = 50
misselAltura = 250
misselPosicaoX = 360
misselPosicaoY = 10 - misselAltura
misselMovimento = 0
velocidadeMissel = 5
pygame.mixer.music.load('assets/ironsound.mp3')
pygame.mixer.music.play(-1)
misselSound = pygame.mixer.Sound("assets/missile.wav")
misselSound.set_volume(0.1)
pygame.mixer.Sound.play(misselSound)
pygame.mixer.music.set_volume(0.1)
explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
explosaoSound.set_volume(0.2)

def escrevendoPlacar(contador):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios: "+str(contador), True, (255, 255, 255))
    display.blit(texto, (10, 10))
def dead():
    pygame.mixer.Sound.play(explosaoSound)
    pygame.mixer.music.stop()
    font = pygame.font.SysFont(None, 150)
    texto = font.render("Você Morreu!", True, (0, 0, 0))
    display.blit(texto, (100, 200))
    pygame.display.update()
    time.sleep(5)
contador = 0
while True:
    # Trabalhar com Background
    display.fill((255, 255, 255))
    display.blit(background, (0, 0))
    #              devolve uma lista de eventos da tela []
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                lapisMovimento = lapisVelocidade * -1
            elif evento.key == pygame.K_RIGHT:
                lapisMovimento = lapisVelocidade
        if evento.type == pygame.KEYUP:
            lapisMovimento = 0
    lapisPosicaoX = lapisPosicaoX + lapisMovimento
    if lapisPosicaoX < 0:
        lapisPosicaoX = 0
    elif lapisPosicaoX > largura - lapisLargura:
        lapisPosicaoX = largura - lapisLargura
    display.blit(lapis, (lapisPosicaoX, lapisPosicaoY))
    misselPosicaoY = misselPosicaoY + velocidadeMissel
    escrevendoPlacar(contador)
    # controlando o míssel novo
    if misselPosicaoY > altura:
        misselPosicaoY = 10 - misselAltura
        velocidadeMissel = velocidadeMissel + 1
        pygame.mixer.Sound.play(misselSound)
        misselPosicaoX = random.randrange(0, largura)
        contador += 1  # contator = contator + 1
    display.blit(missel, (misselPosicaoX, misselPosicaoY))
    # Verificando Colisões
    if lapisPosicaoY < misselPosicaoY + misselAltura:
        if lapisPosicaoX < misselPosicaoX and lapisPosicaoX + lapisLargura > misselPosicaoX or misselPosicaoX+misselLargura > lapisPosicaoX and misselPosicaoX+misselLargura < lapisPosicaoX+lapisLargura:
            dead()
            velocidadeMissel = 5
            misselPosicaoY = 0 - misselAltura
            contador = 0
    pygame.display.update()
    relogio.tick(60)
print("Volte Sempre....")
