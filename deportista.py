class Deportista():

    def __init__(self, años, deporte="Futbol"):
        self._deporte = deporte
        self._añosPracticando = años


    
    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._añosPracticando

    def setDeporte(self, x):
        self._deporte = x

    def setAñosPracticando(self,x):
        self._añosPracticando = x