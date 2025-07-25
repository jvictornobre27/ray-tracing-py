import numpy as np
from phong_with_args import refract
from vectors import Ponto, Vetor
from entidades import Mesh, Esfera, Plane
from camera import Camera
from ray_casting import RayCasting


def main():


    esfera_azul_nao = Esfera(
        center=Ponto(2, 0, 0),
        radius=1,
        color=(1, 1, 0),
        k_difuso=0.8,
        k_ambiental=0.4,
        k_especular=0.8,
        n_rugosidade=1.0,
        k_reflexao=0.6,
        k_refracao=1.0,
        indice_refracao=0.3,
    )

    esfera_azul = Esfera(
        center=Ponto(2, 0, 3),
        radius=1,
        color=(0, 0, 1),
        k_difuso=0.8,
        k_ambiental=0.5,
        k_especular=0.6,
        n_rugosidade=1,
        k_reflexao=0.7,
        k_refracao=0.3,
        indice_refracao=1.0,
    )
    
    # Pontos do retângulo no plano inferior (Y = -3)
    A = Ponto(5, -3, -5)
    B = Ponto(0, -3, -5)
    C = Ponto(0, -3, 5)
    D = Ponto(5, -3, 5)
    #--
    E = Ponto(0,3,5)
    F = Ponto(0,3,-5)
    G = Ponto(5,3,-5)
    H = Ponto(5,3,5)

    # Normais para os dois triângulos da malha
    normal1 = (B - A).__cross__(C - A).__normalize__()
    normal2 = (C - A).__cross__(D - A).__normalize__()

    # Criando malha a partir de 2 triângulos
    mesh_quad = Mesh(
        triangle_quantity=2,
        vertices_quantity=4,
        vertices=[A, B, C, D],
        triangle_normals=[normal1, normal2],
        color=(0.4, 0.7, 1.0),  # Azul claro
        triangle_tuple_vertices=[(0, 1, 2), (0, 2, 3)],
        vertex_normals=[],
        k_difuso=0.7,
        k_ambiental=0.4,
        k_especular=0.6,
        n_rugosidade=8.0,
        k_reflexao=0.3,
        k_refracao=0,
        indice_refracao=0,
    )

    # ---- Mesh 2: formada pelos pontos E, H, D, C (plano direito vertical)
    normal3 = (H - E).__cross__(D - E).__normalize__()
    normal4 = (D - E).__cross__(C - E).__normalize__()

    mesh_rdir = Mesh(
        triangle_quantity=2,
        vertices_quantity=4,
        vertices=[E, H, D, C],
        triangle_normals=[normal3, normal4],
        color=(1.0, 0.7, 0.4),  # Laranja claro
        triangle_tuple_vertices=[(0, 1, 2), (0, 2, 3)],
        vertex_normals=[],
        k_difuso=0.7,
        k_ambiental=0.4,
        k_especular=0.6,
        n_rugosidade=8.0,
        k_reflexao=0.3,
        k_refracao=0,
        indice_refracao=0,
    )

    # ---- Mesh 3: formada pelos pontos G, F, A, B (plano esquerdo vertical)
    normal5 = (F - G).__cross__(A - G).__normalize__()
    normal6 = (A - G).__cross__(B - G).__normalize__()

    mesh_esq = Mesh(
        triangle_quantity=2,
        vertices_quantity=4,
        vertices=[G, F, A, B],
        triangle_normals=[normal5, normal6],
        color=(0.4, 1.0, 0.7),  # Verde claro
        triangle_tuple_vertices=[(0, 1, 2), (0, 2, 3)],
        vertex_normals=[],
        k_difuso=0.7,
        k_ambiental=0.4,
        k_especular=0.6,
        n_rugosidade=8.0,
        k_reflexao=0.3,
        k_refracao=0,
        indice_refracao=0,
    )


    ray_casting = RayCasting(hres=500, vres=500)

    camera = Camera(
        target=Ponto(10, 0, 0),
        position=Ponto(-10, 0, 0),
        up=Vetor(0, 1, 0),
    )

    entidades = [esfera_azul_nao, esfera_azul, mesh_quad, mesh_esq, mesh_rdir]

    ray_casting.__generate_image__(entidades, 1, camera)

    # result = refract(np.array([0.707107, -0.707107]), np.array([0, 1]), 9, 10)


main()
 