import numpy as np

#elementos html
txtTexto = Element('texto')
btnEncriptar = Element('codific')
listCodigos = Element('lista_mensajes')

#metodo para encriptar
def encrypt(*args):
    #elementos
    texto = txtTexto.element.value
    crifrado = [] 
    abc = {' ':0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'ñ':15, 'o':16, 'p':17, 'q':18, 'r':19, 's':20, 't':21, 'u':22, 'v':23, 'w':24, 'x':25, 'y':26, 'z':27}
    matriz = np.array([[1, 2, 1], [0, -1, 3], [2, 1, 0]])

    #logica para encriptar
    limit = 3
    for i in texto:
        for k, v in abc.items():
            if (i == k):
                i = v
                crifrado.append(i)
    datosOr = [crifrado[n:n + limit] for n in range(0 , len(crifrado), limit)]
        
    #rellenar arreglos sin tercia
    for h in range(len(datosOr)):
        if  len(datosOr[h]) < 2:
            datosOr[h].append(0)
            datosOr[h].append(0)
        elif len(datosOr[h]) < 3:
            datosOr[h].append(0) 
    for n in datosOr:
        resultado = np.dot(n, matriz)
        grupoMensajes = create("li", classes="grupo_mensajes")
        grupoMensajes.element.innerText = resultado 
        listCodigos.element.appendChild(grupoMensajes.element)
    
    puntos = "----------------------------------------"
    separacionG = create("li", classes="separacion")
    separacionG.element.innerText = puntos
    listCodigos.element.appendChild(separacionG.element)


    txtTexto.clear()

btnEncriptar.element.onclick = encrypt