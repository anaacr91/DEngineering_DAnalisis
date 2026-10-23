import pandas as pd

estudiantes_listado = pd.read_csv('estudiantes.csv')
notas_estudiantes = pd.read_csv('notas.csv')

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
        self.promedio = self.calcular_promedio()
        self.estado = self.determinar_estado()

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        else:
            promedio_notas = sum(self.notas) / len(self.notas)
            return promedio_notas
        
    def determinar_estado(self):
        promedio = self.calcular_promedio()  
        estado = "Aprobado" if promedio >= 5 else "Suspenso"
        return estado
    
    def actualizar_notas(self, nueva_nota):
        self.notas = nueva_nota
        self.promedio = self.calcular_promedio()
        self.estado = self.determinar_estado()

    def to_dict(self):
            return {
                "nombre": self.nombre,
                "notas": self.notas,
                "promedio": self.calcular_promedio(),
                "estado": self.determinar_estado()
            }
        
    def __str__(self):
        return {f"Nombre: {self.nombre}, Notas: {self.notas}, Promedio: {self.promedio}, Estado: {self.estado}"}
    
    @staticmethod
    def filtrar_notas_por_id(id_estudiante, lista_filas_notas):
        if len(lista_filas_notas) == 0:
            return 0
        else:
            lista_filas_notas = pd.read_csv('notas.csv')
            return {lista_filas_notas[lista_filas_notas['id_estudiante'] == id_estudiante]['nota'].tolist()}

        

if __name__ == "__main__":
        pass