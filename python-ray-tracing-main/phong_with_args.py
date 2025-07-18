import numpy as np
from entidades import Esfera, Plane, Mesh
from vectors import Ponto

"""
Fórmula que queremos satisfazer
I = I_a * k_a + sum_lights( I_l * [ k_d * (N · L) + k_s * (R · V)^n ] )
"""

#vai servir p limitar um valor entre mínimo e máximo, como garantir que a luz não passe de 255 nem seja negativa
def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))

#calcula a cor no ponto onde o raio bateu
def phong(entidade, luzes, ponto_intersec, camera_position):
    
    Ia = np.array([50, 50, 50])  #intensidade da luz ambiente (claridade) -> I_a na fórmula

    #vetor da superfície até a câmera (de onde estamos olhando)
    V = np.array([
        camera_position.x - ponto_intersec.x,
        camera_position.y - ponto_intersec.y,
        camera_position.z - ponto_intersec.z,
    ])
    V = V / np.linalg.norm(V)  #normaliza V 

    #Agora precisamos do vetor normal N no ponto onde o raio bateu
    N = None

    if isinstance(entidade, Esfera):
        #P/ uma esfera, a normal é radial (vai do centro -> ponto de intersecção)
        N = np.array(entidade.__get_normal_vector_to_intersection_point__(ponto_intersec))

    elif isinstance(entidade, Plane):
        #P/ 1 plano, a normal é constante
        N = np.array([
            entidade.normal.x,
            entidade.normal.y,
            entidade.normal.z,
        ])

    elif isinstance(entidade, Mesh):
        #P/ uma malha, pode ter uma normal calculada no ponto
        if entidade.normal_to_intersection_point is not None:
            N = np.array([
                entidade.normal_to_intersection_point.x,
                entidade.normal_to_intersection_point.y,
                entidade.normal_to_intersection_point.z,
            ])
        else:
            N = None

    #vemos se tem normal e normalizamos (sempre queremos vetores unitários)
    if N is not None and np.linalg.norm(N) != 0:
        N = N / np.linalg.norm(N)
    else:
        # Se não tem normal válida, retorna cor preta
        return [0, 0, 0]

    #iluminação começa zerada (isso será o somatório la que chamamos de sum_lights)
    i_sum = np.array([0.0, 0.0, 0.0])
    entidade.color = np.array(entidade.color)  

    #para cada luz no cenário vamos somar sua contribuição
    for luz in luzes:
        luz.I = np.array(luz.I)  # I_l na fórmula (intensidade da luz pontual)

        #vetor da superfície até a luz
        L = np.array([
            luz.x - ponto_intersec.x,
            luz.y - ponto_intersec.y,
            luz.z - ponto_intersec.z,
        ])
        L = L / np.linalg.norm(L)  # normaliza L

        # R = vetor de reflexão (espelho)
        R = 2 * N * (N.dot(L)) - L

        # N.L mede o quão de frente está para a luz
        N_dot_L = clamp(0, N.dot(L), 1) #(N · L) faz parte da difusa

        # R.V mede o brilho espelhado na direção da câmera
        R_dot_V = clamp(0, R.dot(V), 1) # (R · V) faz parte da especular

        #-----Componente difusa-----
        # I_difusa = I_l * k_d * (N · L)
        I_difusa = luz.I * entidade.color * entidade.k_difuso * N_dot_L

        #-----Componente especular-----
        # I_especular = I_l * k_s * (R · V)^n
        I_especular = luz.I * entidade.k_especular * (R_dot_V**entidade.n_rugosidade)

        #Soma essas contribuições para essa luz
        i_sum += I_difusa + I_especular # sum_lights

    #Agora somamos a luz ambiente (independe de luzes pontuais)
    # I_a * k_a (luz ambiente)
    cor = (Ia * entidade.k_ambiental) + i_sum

    cor_final = [min(255, max(0, int(i))) for i in cor] #garantia que cada canal RGB fique entre 0 e 255 (sem estouro)

    return cor_final
