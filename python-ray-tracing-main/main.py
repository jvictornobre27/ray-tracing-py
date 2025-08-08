import numpy as np
import math
from phong_with_args import refract
from vectors import Ponto, Vetor
from entidades import Mesh, Esfera, Plane
from camera import Camera
from ray_casting import RayCasting
from toro import Toro

def main():

    camera = Camera(
        target=Ponto(1, 0, 0),
        position=Ponto(-2, 2, 0.7),
        up=Vetor(0, 0, 1),
    )

    toro = Toro(centro_y = 0, 
                centro_z = 0, 
                R = 0.7, 
                r = 0.4, 
                cor = (0.5, 0, 0.5)
            )
    
    malha_toro = toro.triangulate(1.0)
    entidades = [malha_toro]

    ray_casting = RayCasting(hres = 500, vres = 500)

    ray_casting.__generate_image__(entidades, 1, camera)

main() 