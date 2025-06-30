import cv2 as cv
import numpy as np
from vectors import Ponto, Vetor #OK


def scale_rgb(color: tuple) -> tuple:
    return tuple(rgb / 255 for rgb in color)


class Ray:
#representa os raios da camera tem funções para pegar pontos ao longo do raio, somar/subtrair/multiplicar/dividir raios

    def __init__(self, origin: "Ponto", direction: "Vetor"):
        #inicia com o ponto da origem dele e para onde ele vai
        self.origin = origin
        self.direction = direction

    def __str__(self):
        return f"Ray({self.origin}, {self.direction})"
#para imprimir o raio de forma legível no terminal
    def __repr__(self):
        return self.__str__()
    


    def get_point(self, t: float) -> "Ponto": #serve para pegar um ponto que está a uma distância t do ponto de origem do raio, seguindo sua direção
        return self.origin + (self.direction.__mul_escalar__(t))

    def __add__(self, other: "Ray") -> "Ray": #soma dois raios somando origem com origem e direção com direção
        return Ray(
            self.origin.__add__(other.origin), self.direction.__add__(other.direction)
        )

    def __sub__(self, other: "Ray") -> "Ray":
        return Ray(
            self.origin.__sub__(other.origin), self.direction.__sub__(other.direction)
        )

    def __mul__(self, other: float) -> "Ray": #mult origem e direção por um escalar (escalonar)
        return Ray(self.origin.__mul__(other), self.direction.__mul__(other))

    def __truediv__(self, other: float) -> "Ray": #divide origem e direção por um escalar other
        return Ray(self.origin.__truediv__(other), self.direction.__truediv__(other))


class Camera:
    """Class Representing a Camera in 3D Space
        w vetor que aponta da câmera para o alvo (target).
        v é ortogonal a w e aponta para a direita (right).
        u é ortogonal a w e v e aponta para cima (up).
    """

    def __init__(
        self,
        target: "Ponto",
        position: "Ponto",
        up: "Vetor",
        vres: int = 300,
        hres: int = 300,
    ):
        #inicializando a camera
        self.position = position
        self.target = target
        self.up = up

        self.w: "Vetor" = self.target.__sub__(self.position)
        self.v: "Vetor" = self.up.__cross__(self.w)

        self.w = self.w.__normalize__()
        self.v = self.v.__normalize__()

        #self.u: "Vetor" = self.w.__cross__(self.v)
        self.u: "Vetor" = self.w.__cross__(self.v).__mul_escalar__(-1) #corrigir camera para parecer com orientação do geogebra
        self.u = self.u.__normalize__()

        self.target_distance = self.position.__distance__(self.target)

        self.vres = vres
        self.hres = hres

    def __intersect__( #vai disparar um raio e ver com qual objeto ele colide primeiro (mais próximo da câmera). Ele retorna a cor do objeto atingido
        self, ray: "Ray", targets: list
    ) -> list[bool, list[int, int, int]]:

        smallest_distance = float("inf")
        color = [100, 100, 100] #tudo começa cinza

        for target in targets: #itera sobre tudo que tem na tela
            intersection = target.__intersect_line__(ray.origin, ray.direction) #usa o método de interseção do objeto dos planos passando o raio. Se houver interseção, será retornado um ponto 

            if intersection: #se sim cria um vetor com o ponto de interseção e pega sua distancia
                distance_vetor = Vetor(
                    intersection[0], intersection[1], intersection[2]
                )

                distance = ray.origin.__distance__(distance_vetor) #se for a menor distancia atualiza a cor
                if distance < smallest_distance:
                    smallest_distance = distance
                    color = target.color

        return color

