def solicitar_opcion():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        opcion = input()
        if opcion.isdecimal():
            return int(opcion)
        print('Por favor, introduzca un número del 1 al 3')


def solicitar_puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        puntuacion = input()
        if puntuacion.isdecimal():
            puntuacion = int(puntuacion)
            if 1 <= puntuacion <= 5:
                return puntuacion
        print('Por favor, introduzca un valor entre 1 y 5')


def ingresar_puntuacion_y_comentario():
    puntuacion = solicitar_puntuacion()
    print('Por favor, introduzca un comentario')
    comentario = input()
    post = f'Puntuación: {puntuacion} | Comentario: {comentario}'
    
    with open("data.txt", 'a') as file_pc:
        file_pc.write(f'{post}\n')
    print('Comentario guardado exitosamente.')


def comprobar_resultados():
    try:
        with open("data.txt", 'r') as read_file:
            contenido = read_file.read()
            if contenido:
                print('Resultados hasta la fecha:')
                print(contenido)
            else:
                print('No hay resultados registrados aún.')
    except FileNotFoundError:
        print('No hay resultados registrados aún.')


def main():
    while True:
        opcion = solicitar_opcion()
        if opcion == 1:
            ingresar_puntuacion_y_comentario()
        elif opcion == 2:
            comprobar_resultados()
        elif opcion == 3:
            print('Finalizando...')
            break
        else:
            print('Por favor, introduzca un número del 1 al 3')


main()
