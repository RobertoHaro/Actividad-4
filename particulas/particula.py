class Particle:
    def __init__(self, destinyX=0<=500, destinyY=0<=500, speed=0, red=0<=255, green=0<=255, blue=0<=255):

        self.__destinyX = destinyX
        self.__destinyY = destinyY
        self.__speed = speed
        self.__red = red
        self.__green = green
        self.__blue = blue
    
    def __str__(self):
        return(
            '\nDestino X: ' + str(self.__destinyX) + '\n' +
            'Destino Y: ' + str(self.__destinyY) + '\n' +
            'Velocidad: ' + str(self.__speed) + '\n' +
            'Rojo: ' + str(self.__red) + '\n' +
            'Verde: ' + str(self.__green) + '\n' +
            'Azul: ' + str(self.__blue) + '\n'
        )