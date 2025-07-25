from vectors import Ponto, Vetor

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
