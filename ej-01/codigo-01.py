class Matriz(): # interfaz
    def __init__(self, elementos: list):
        self.elementos = elementos
    
    def transponer(self):
        pass 

    def imprimir(self):
        pass


class Transpuesta(Matriz):
    def __init__(self, elementos: list):
        super().__init__(elementos)
    
    def transponer(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))])
    # usamos una funcion lambda en lugar de un bucle for
    #   para optimizar el tiempo de ejecucion y el espacio de memoria
    # crar una funcion recursiva cuando estemos tratando con grandes cantidades de datos 


class Imprimir():
    def __init__(self, matriz: Matriz):
       self.matriz = matriz
    
    def imprimir(self):
        for fila in self.matriz.elementos:
            print(fila)


# hacer clase lanzador para lanzar el main
class Lanzador(Imprimir, Transpuesta):
    # crear metodo que llame a la funcion transpuesta y funcion imprimir y lo recoja con un input y un oputput

    def __init__(self):
        self.elementos = []
        self.cantidad_filas = int(input('Ingrese la cantidad de filas: '))
        self.cantidad_columnas = int(input('Ingrese la cantidad de columnas: '))
        self.crear_matriz()
        super().__init__(self.elementos)
    
    def crear_matriz(self):
        for i in range(self.cantidad_filas):
            fila = []
            for j in range(self.cantidad_columnas):
                fila.append(int(input(f'Ingrese el elemento ({i+1},{j+1}): ')))
            self.elementos.append(fila)
    
    def lanzar(self):
        print('La matriz transpuesta es: ')
        self.imprimir()
        self.transponer().imprimir()


# crear clase Main que llame a la funcion lanzar
class Main():
    def __init__(self):
        self.lanzador = Lanzador()
        self.lanzador.lanzar()



# CODIGO EJECUTABLE ----------------------------------------------------------------
if __name__ == '__main__':
    Main()
