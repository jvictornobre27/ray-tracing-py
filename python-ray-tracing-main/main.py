from vectors import Ponto, Vetor
from entidades import Esfera, Plane
from camera import Camera


def main():
    camera = Camera(
        target=Ponto(5, 0, 0),
        position=Ponto(0, 5, 0),
        up=Vetor(0, -1, 0),
    )

    #normal_plano = (Ponto(4, 0, 0) - camera.position).__normalize__()  # normal calculada em função da posição da câmera
    normal_plano = Vetor(0, 1, 0) 

    #point_plano = Ponto(7, 0, 0)  
    point_plano = Ponto(0, 0, 0) 

    plano = Plane(
        point=point_plano,
        normal=normal_plano,
        color=(255, 0, 0),  # vermelho para destacar
    )

    esfera = Esfera(
        center=Ponto(4, 0, 0),
        radius=1,
        color=(0, 0, 100),  # azul escuro
    )

    esfera2 = Esfera(
        center=Ponto(6, 0, 0),
        radius=1,
        color=(0, 200, 0),  # verde
    )

    esfera3 = Esfera(
        center=Ponto(8, 0, 0),
        radius=0.75,
        color=(100, 0 , 0),
    )

    target = Esfera(
        center=Ponto(5, 0, 0),
        radius=0.25,
        color=(255, 255 , 255),
    )

    entidades = [esfera, esfera2,plano]  

    camera.__ray_casting__(entidades, 1)

main()