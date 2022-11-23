class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre  = nombre
        self.apellido = apellido
        self.edad = edad
    def crece(self, years):
        self.edad += years

person = Persona('jhon', 'Calderon', 19)
print(person.edad)
person.crece(20)
print(person.edad)