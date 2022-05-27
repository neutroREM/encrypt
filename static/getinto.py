from flask import Flask, redirect
#elementos html
pswCodigo = Element('codigo')
btnIngreso = Element('ingreso')

def metodoLog(*args):
    #elementos
    intentos = 0
    codigo = pswCodigo.element.value
    code = 'gato'

    #logica para ingresar
    if(code != codigo or code == " "):
        print('Codigo incorrecto')
        intentos += 1
    elif intentos == 4:
        btnIngreso.element.disable
    else:
        return redirect('code.html')

btnIngreso.element.onclick = metodoLog    
    