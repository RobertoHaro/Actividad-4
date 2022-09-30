from .particula import Particle

class ListP:
    def __init__(self):
        self.__particles = []

    def add_end(self, Particle:Particle):
        self.__particles.append(Particle)

    def add_beg(self, Particle:Particle):
        self.__particles.insert(0,Particle)
    
    def show(self):
        for particle in self.__particles:
            print(particle)

    def __str__(self):
        #return str(self.__particles[0])
        return "".join(
            str(particle) for particle in self.__particles
        )
