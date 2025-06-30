from vectors import Ponto #OK

class Esfera: #Representa uma esfera 3D

    def __init__(self, center, radius, color): #definição da esfera e seus parametros
        self.center = center 
        self.radius = radius 
        self.color = color 

                    #centro da esf, origem, direção
    def __intersect_line__(self, line_point, line_vector): #determina se um raio interceptou a esfera, e retorna o ponto de interseção mais próximo da câmera ou seja resolve a equação do 2º grau: a·t² + b·t + c = 0

        a = sum(i * j for i, j in zip(line_vector, line_vector)) #produto escalar do vetor com ele mesmo: |v|² = v·v = x² + y² + z²

        b = 2 * sum( #b é o dobro do produto escalar entre o vetor direção do raio e o vetor que vai do centro da esfera até a origem do raio
            i * j
            for i, j in zip(
                line_vector, (p - c for p, c in zip(line_point, self.center))
            )
        )

        #diferença entre o quadrado da distância do ponto inicial ao centro da esfera e o quadrado do raio. Indica se o ponto está dentro (-), na superfície (0) ou fora (+) da esfera.
        c = sum((p - c) ** 2 for p, c in zip(line_point, self.center)) - self.radius**2

        discriminant = b**2 - 4 * a * c #delta que indica se a eq quadrática tem solução real, ou seja se o raio intersecta a esfera.

        if discriminant <= 0: #se delta = 0 não há interseção
            return None
        
        #se delta > 0 ent calculamos as possiveis soluções
        t1 = (-b + discriminant**0.5) / (2 * a)
        t2 = (-b - discriminant**0.5) / (2 * a)

        #retorna o ponto de interseção mais próximo na frente da câmera
        if 0 < t1 < t2:
            return tuple(p + t1 * v for p, v in zip(line_point, line_vector))
        if 0 < t2 < t1:
            return tuple(p + t2 * v for p, v in zip(line_point, line_vector))

        return None


class Plane: #representa um plano 3D

    def __init__(self, point, normal, color): #um ponto qualquer pertencente ao plano | vetor perpendicular ao plano | cor do plano 
        self.point = point
        self.normal = normal
        self.color = color

    def __intersect_line__(self, line_point, line_vector): #calcula o ponto de interseção entre uma linha (definida por um ponto e um vetor direção) e o plano

        d = tuple(p - lp for p, lp in zip(self.point, line_point)) #vetor d que vai do ponto da linha até o ponto do plano 

        denominator = sum(n * lv for n, lv in zip(self.normal, line_vector)) #prod escalar entre o vetor normal do plano e o vetor direção da linha 

        if denominator == 0: #produto escalar zero a linha é paralela ao plano e não há interseção
            return None
            #return (False, None)
        
        t = sum(n * dp for n, dp in zip(self.normal, d)) / denominator #calcula o "quanto andar" (parâmetro t) para alcançar o plano ao longo do vetor da linha

        return tuple(lp + t * lv for lp, lv in zip(line_point, line_vector)) #achar as coordenadas exatas do ponto de interseção

#--------------------------------SEGUNDA ENTREGA ADICIONAIS--------------------------------------------------------------------------

class Mesh: #representa uma malha

    def __init__(
        self,
        triangle_quantity: int,
        vertices_quantity: int,
        vertices: list[Ponto],
        triangle_tuple_vertices: list[tuple[int, int, int]],
        triangle_normals: list,
        vertex_normals: list,
        color,
    ):
        self.triangle_quantity = triangle_quantity
        self.vertices_quantity = vertices_quantity
        self.vertices = vertices
        self.triangle_tuple_vertices = triangle_tuple_vertices #lista de tuplas com índices de vértices que formam os triângulos
        self.triangle_normals = triangle_normals #uma normal (vetor perpendicular) para cada triângulo
        self.vertex_normals = vertex_normals

        self.color = color

    def __point_in_triangle__(self, point, triangle_vertices): #Verifica se um ponto esta dentro de um triangulo usando coord baricentrica

        #Cria vetores entre os vértices do triângulo.
        v0 = triangle_vertices[2].__sub__(triangle_vertices[0]) 
        v1 = triangle_vertices[1].__sub__(triangle_vertices[0])
        v2 = point.__sub__(triangle_vertices[0])

        d00 = v0.__mul__(v0)
        d01 = v0.__mul__(v1)
        d11 = v1.__mul__(v1)
        d20 = v2.__mul__(v0)
        d21 = v2.__mul__(v1)

        denom = d00 * d11 - d01 * d01

        v = (d11 * d20 - d01 * d21) / denom
        w = (d00 * d21 - d01 * d20) / denom
        u = 1.0 - v - w

        return (v >= 0) and (w >= 0) and (u >= 0)

    def __intersect_line__(self, line_point, line_vector): #Calcula a interseção de o ponto de interseção entre a malha e uma linha
        for index, triangle in enumerate(self.triangle_tuple_vertices):
            triangle_vertices = [self.vertices[i] for i in triangle]
            triangle_normal = self.triangle_normals[index]
            plane = Plane(triangle_vertices[0], triangle_normal, self.color)
            intersection_point = plane.__intersect_line__(line_point, line_vector)
            if intersection_point is not None:
                intersection_point = Ponto(
                    intersection_point[0], intersection_point[1], intersection_point[2]
                )
                if self.__point_in_triangle__(intersection_point, triangle_vertices):
                    return (
                        intersection_point.x,
                        intersection_point.y,
                        intersection_point.z,
                    )
        return None

