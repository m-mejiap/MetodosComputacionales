#Task: Your task is to determine the relationship between the given point and the vector. Direction of the vector is important! To determine if the point is to the left or to the right, you should imagine yourself standing at the beginning of the vector and looking at the end of the vector.

def point_vs_vector(point, vector):
    m = (vector[1][1]-vector[0][1])/(vector[1][0]-vector[0][0])    #Determina la pendiente de la recta que pasa por el vector.
    if( point[1] == round(m*(point[0]-vector[0][0])) + (vector[0][1]) ):    #Determina si el punto dado está sobre la recta usando la ecuación de la recta.
        return 0
    elif( vector[1][1]-vector[0][1] > 0 and point[1] > (m*(point[0]-vector[0][0])) + (vector[0][1])):    #Evalúa la dirección del vector y determina si el vector va hacia "arriba" (la flecha apunta al eje y positivo). Evalúa si el punto está "encima" de la recta.
        if (m>0):    #Si la pendiente de la recta es positiva, el punto está a la izquierda.
            return -1
        if (m<0):    #Si la pendiente de la recta es negativa, el punto está a la derecha.
            return 1
    elif( vector[1][1]-vector[0][1] > 0 and point[1] < (m*(point[0]-vector[0][0])) + (vector[0][1])):    #Evalúa la dirección del vector y determina si el vector va hacia "arriba" (la flecha apunta al eje y positivo). Evalúa si el punto está "debajo" de la recta.
        if (m>0):    #Si la pendiente de la recta es positiva, el punto está a la derecha.
            return 1
        if (m<0):     #Si la pendiente de la recta es negativa, el punto está a la izquierda.
            return -1
    elif( vector[1][1]-vector[0][1] < 0 and point[1] < (m*(point[0]-vector[0][0])) + (vector[0][1])):    #Evalúa la dirección del vector y determina si el vector va hacia "abajo" (la flecha apunta al eje y negativo). Evalúa si el punto está "debajo" de la recta.
        if (m>0):    #Si la pendiente de la recta es positiva, el punto está a la izquierda.
            return -1
        if (m<0):    #Si la pendiente de la recta es negativa, el punto está a la derecha.
            return 1
    elif( vector[1][1]-vector[0][1] < 0 and point[1] > (m*(point[0]-vector[0][0])) + (vector[0][1])):    #Evalúa la dirección del vector y determina si el vector va hacia "abajo" (la flecha apunta al eje y negativo). Evalúa si el punto está "encima" de la recta.
        if (m>0):    #Si la pendiente de la recta es positiva, el punto está a la derecha.
            return 1
        if (m<0):     #Si la pendiente de la recta es negativa, el punto está a la izquierda.
            return -1