from vectors import Ponto, Vetor
from entidades import Esfera, Mesh, Plane
from camera import Camera
from ray_casting import RayCasting
from transformation import Transformacao
import numpy as np


def main():

    p0 = Ponto(10, 0, 0)
    p1 = Ponto(0, 10, 0)
    p2 = Ponto(-10, 0, 0)
    p3 = Ponto(0, -10, 0)
    p4 = Ponto(0, 0, 10)

    v1 = p1 - p0
    v2 = p4 - p0
    normal1 = v1.__cross__(v2).__normalize__()

    v3 = p2 - p1
    v4 = p4 - p1
    normal2 = v3.__cross__(v4).__normalize__()

    v5 = p3 - p2
    v6 = p4 - p2
    normal3 = v5.__cross__(v6).__normalize__()

    v7 = p0 - p3
    v8 = p4 - p3
    normal4 = v7.__cross__(v8).__normalize__()

 
    esfera_red = Esfera( #azul
        center=Ponto(0, 0, 3),
        radius=1,
        color=(0, 0, 1),
        k_difuso=1,
        k_ambiental=1,
        k_especular=1,
        n_rugosidade=10,
    )

    esfera_green = Esfera(
        center=Ponto(3, 0, 0),
        radius=1,
        color=(0, 1, 0),
        k_difuso=0.1,
        k_ambiental=1,
        k_especular=0.1,
        n_rugosidade=10,
    )

    esfera_blue = Esfera(
        center=Ponto(0, 3, 0), #anda pra dir esq (+ esq)|cima e baixo (+ cima)|zoom perto/longe (+ perto) 
        radius=1,
        color=(1, 0, 0),
        k_difuso=0.1,
        k_ambiental=0.1,
        k_especular=1,
        n_rugosidade=10,
    )

    esfera_orange = Esfera(
        center=Ponto(-1, 0, 0), #anda pra dir esq (+ esq)|cima e baixo (+ cima)|zoom perto/longe (+ perto) 
        radius=1,
        color=(0, 0.5, 1),
        k_difuso=1,
        k_ambiental=0.1,
        k_especular=0.1,
        n_rugosidade=10,
    )
    """
    esfera_metalica = Esfera(
        center=Ponto(-3, 0, 0),
        radius=1,
        color=(0.8, 0.8, 0.8), #Cinza
        k_difuso=0.6,
        k_especular=0.95,
        k_ambiental=0.2,
        n_rugosidade=50,
    )

    esfera_fosca = Esfera(
        center=Ponto(0, 3, 0),
        radius=1,
        color=(0.7, 0.2, 0.2), #azul
        k_difuso=0.9,
        k_especular=0.05,
        k_ambiental=0.1,
        n_rugosidade=10,
    )

    esfera_iluminada = Esfera(
        center=Ponto(3, 0, 0),
        radius=1,
        color=(0.2, 0.8, 0.2), #verde
        k_difuso=0.2,
        k_especular=0.1,
        k_ambiental=0.9,
        n_rugosidade=10,
    )

    esfera_plastica = Esfera(
        center=Ponto(0, 0, 1),
        radius=1,
        color=(0.1, 0.3, 0.9), #vermelha
        k_difuso=0.8,
        k_especular=0.8,
        k_ambiental=0.4,
        n_rugosidade=20,
    )
    """

    ray_casting = RayCasting(hres=500, vres=500)

    mesh = Mesh(
        triangle_quantity=1,
        vertices_quantity=5,
        vertices=[p0, p1, p4],
        triangle_normals=[normal1, normal2, normal3, normal4],
        color=(0, 0, 255),
        triangle_tuple_vertices=[(0, 1, 2)],
        vertex_normals=[],
        k_difuso=0.7,
        k_especular=0.7,
        k_ambiental=0.1,
        k_reflexao=0.0,
        k_transmissao=0.0,
        n_rugosidade=2.0,
    )

    camera = Camera(
        target=Ponto(0, 0, 0),
        position=Ponto(0, 0, 10),
        up=Vetor(0, 1, 0),
    )

    entidades = [esfera_red, esfera_blue, esfera_green, esfera_orange]
    #entidades = [esfera_metalica, esfera_fosca, esfera_iluminada, esfera_plastica]


    ray_casting.__generate_image__(entidades,1, camera)


main()


"""
#Entrega 2 - Malha de triangulos e transformações
def main():

    ray_casting = RayCasting(hres=500, vres=500)
    
    plano = Plane(
         point=Ponto(0, 3, 0),
         normal=Vetor(0, 1, 0),
         color=(255, 0, 0),
     )

    esfera = Esfera(
        center=Ponto(2, 0, 0),
        radius=4,
        color=(0, 128, 0),
    )

#""
    p0 = Ponto(5, 0, 0) #A
    p1 = Ponto(0, 5, 0) #B
    p2 = Ponto(-5, 0, 0) #C
    p3 = Ponto(0, -5, 0) #D
    p4 = Ponto(0, 0, 5) #E

    v1 = p1.__sub__(p0) #B-A
    v2 = p4.__sub__(p0) #E-A
    normal1 = v1.__cross__(v2).__normalize__()

    v3 = p2.__sub__(p1)  #C-B
    v4 = p4.__sub__(p1) #E-B
    normal2 = v3.__cross__(v4).__normalize__()

    v5 = p3.__sub__(p2) #D-C
    v6 = p4.__sub__(p2) #E-C
    normal3 = v5.__cross__(v6).__normalize__()

    v7 = p0.__sub__(p3) #A-D
    v8 = p4.__sub__(p3) #E-D
    normal4 = v7.__cross__(v8).__normalize__()

    mesh = Mesh(
        triangle_quantity=4,
        vertices_quantity=5,
        vertices=[p0, p1, p2, p3, p4],
        triangle_normals=[normal1, normal2, normal3, normal4],
        color=(0, 25, 0),
        triangle_tuple_vertices=[(0, 1, 4), (1, 2, 4), (2, 3, 4), (0, 3, 4)], #Basicamente (A,B,E) (B,C,E) (C,D,E) (A,D,E)
        vertex_normals=[],
    )
#""
#""
    p0a = Ponto(2, 0, 0)
    p1a = Ponto(-2, 2, 0)
    p2a = Ponto(-2, -2, 0)


    v1a = p1a.__sub__(p0a)
    v2a = p2a.__sub__(p0a)
    normala = v1a.__cross__(v2a).__normalize__()

    mesh = Mesh(
        triangle_quantity=1,
        vertices_quantity=3,
        vertices=[p0a, p1a, p2a],
        triangle_normals=[normala],
        color=(0, 255, 255),
        triangle_tuple_vertices=[(0, 1, 2)],
        vertex_normals=[],
    )
#""
    #esfera = Transformacao.translate_sphere(esfera, 10, 0, 0)

    camera = Camera(
        target=Ponto(0, 0, 0),
        #position=Ponto(0, 0, 10), #Camera 1
        position=Ponto(0, 10, 2), #Camera 3
        up=Vetor(0, -1, 0)
    )

    entidades = [mesh]

    ray_casting.__generate_image__(entidades, 1, camera)


main()
"""

#------------------------------------------------------------------------

""" 
#Entrega 1 - Interseção plano/esfera

    camera = Camera(
        target=Ponto(5, 0, 0),
        position=Ponto(0, 5, 0),
        up=Vetor(0, 1, 0),
        hres=300,
        vres=300
    )

    #normal_plano = (Ponto(4, 0, 0) - camera.position).__normalize__()
    normal_plano = Vetor(0, 1, 0)

    #point_plano = Ponto(7, 0, 0)
    point_plano = Ponto(0, 0, 0)

    plano = Plane(
        point=point_plano,
        normal=normal_plano,
        color=(255, 0, 0),
    )

    esfera = Esfera(center=Ponto(4, 0, 0), radius=1, color=(0, 0, 100))
    esfera2 = Esfera(center=Ponto(6, 0, 0), radius=1, color=(0, 200, 0))

    entidades = [esfera, esfera2, plano]

    raycaster = RayCasting(hres=camera.hres, vres=camera.vres)
    raycaster.__generate_image__(entidades, distancia=1, camera=camera)

main()
"""