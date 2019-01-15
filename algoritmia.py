pilaDeContenedores = [1,2,3,4,5,6,7,8,9,10]

def retirarContenedor(pilaDeContenedores):
    return pilaDeContenedores.pop()

def apilarContenedor(contenedor, pilaDeContenedores):
    pilaDeContenedores.append(contenedor)
    return pilaDeContenedores

def desapilarContenedor(contenedor, pilaDeContenedores):
    pilaDeContenedoresBuffer = []
    while len(pilaDeContenedores) != 0:
        contenedor_buffer = retirarContenedor(pilaDeContenedores)
        if contenedor_buffer == contenedor:
            break
        pilaDeContenedoresBuffer.append(contenedor_buffer)
    while len(pilaDeContenedoresBuffer) != 0:
        apilarContenedor(retirarContenedor(pilaDeContenedoresBuffer), pilaDeContenedores)
    return pilaDeContenedores
