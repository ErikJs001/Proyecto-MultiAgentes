import agentpy as ap

# Clase Carro
class Carro(ap.Agent):

    def setup(self):
        # Creamos un agente de tipo Carro

        # Definimos su posición
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    """ 
    Funciones para mover al carro en la calle
    Según Unity, nuestra calle estaría en los ejes x,z
    no nos moveríamos sobre 'y', eso significaría que se elevaría o descendería el carro
    """
    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n
    
    def move_down(self, n):
        self.z -= n

    def move_up(self, n):
        self.z += n