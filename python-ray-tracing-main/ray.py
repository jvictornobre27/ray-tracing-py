from vectors import Ponto, Vetor

<<<<<<< HEAD

class Ray:
    """Class Representing a Ray in 3D Space
    Args:
        origin, direction
    """

    def __init__(self, origin: "Ponto", direction: "Vetor"):
        """Initialize the Ray"""
=======
class Ray:
#representa os raios da camera tem funções para pegar pontos ao longo do raio, somar/subtrair/multiplicar/dividir raios

    def __init__(self, origin: "Ponto", direction: "Vetor"):
        #inicia com o ponto da origem dele e para onde ele vai
>>>>>>> 3690121782a231f6b125acf1cab2be1414203b90
        self.origin = origin
        self.direction = direction

    def __str__(self):
<<<<<<< HEAD
        """Return the string representation of the Ray"""
        return f"Ray({self.origin}, {self.direction})"

    def __repr__(self):
        """Return the string representation of the Ray"""
        return self.__str__()

    def get_point(self, t: float) -> "Ponto":
        """Return the point at t distance from the origin"""
        return self.origin + (self.direction.__mul_escalar__(t))

    def __add__(self, other: "Ray") -> "Ray":
        """Return the sum of two rays"""
=======
        return f"Ray({self.origin}, {self.direction})"
#para imprimir o raio de forma legível no terminal
    def __repr__(self):
        return self.__str__()
    
    def get_point(self, t: float) -> "Ponto": #serve para pegar um ponto que está a uma distância t do ponto de origem do raio, seguindo sua direção
        return self.origin + (self.direction.__mul_escalar__(t))

    def __add__(self, other: "Ray") -> "Ray": #soma dois raios somando origem com origem e direção com direção
>>>>>>> 3690121782a231f6b125acf1cab2be1414203b90
        return Ray(
            self.origin.__add__(other.origin), self.direction.__add__(other.direction)
        )

    def __sub__(self, other: "Ray") -> "Ray":
<<<<<<< HEAD
        """Return the subtraction of two rays"""
=======
>>>>>>> 3690121782a231f6b125acf1cab2be1414203b90
        return Ray(
            self.origin.__sub__(other.origin), self.direction.__sub__(other.direction)
        )

<<<<<<< HEAD
    def __mul__(self, other: float) -> "Ray":
        """Return the multiplication of a ray by a scalar"""
        return Ray(self.origin.__mul__(other), self.direction.__mul__(other))

    def __truediv__(self, other: float) -> "Ray":
        """Return the division of a ray by a scalar"""
=======
    def __mul__(self, other: float) -> "Ray": #mult origem e direção por um escalar (escalonar)
        return Ray(self.origin.__mul__(other), self.direction.__mul__(other))

    def __truediv__(self, other: float) -> "Ray": #divide origem e direção por um escalar other
>>>>>>> 3690121782a231f6b125acf1cab2be1414203b90
        return Ray(self.origin.__truediv__(other), self.direction.__truediv__(other))
