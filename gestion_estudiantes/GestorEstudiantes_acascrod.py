import pandas as pd
from Estudiante_acascrod import Estudiante

archivo_estudiantes = pd.read_csv('estudiantes.csv')
archivo_notas = pd.read_csv('notas.csv')


class GestorEstudiantes:
    
    def __init__(self, archivo_estudiantes='estudiantes.csv', archivo_notas='notas.csv'):

        self.archivo_estudiantes = pd.read_csv(archivo_estudiantes)
        self.archivo_notas = pd.read_csv(archivo_notas)
        self.estudiantes = []
        print(f"Datos cargados: {len(self.archivo_estudiantes)} estudiantes, {len(self.archivo_notas)} notas")

    def registrar_estudiante(self, nombre, notas):
       
        if len(self.archivo_estudiantes) > 0:
            nuevo_id = self.archivo_estudiantes['id'].max() + 1
        else:
            nuevo_id = 1
        
        nuevo_estudiante = Estudiante(nombre, notas)
        self.estudiantes.append(nuevo_estudiante)

        nuevas_notas = pd.DataFrame({
            'id_estudiante': [nuevo_id] * len(notas),  
            'nota': notas
        })
        self.archivo_notas = pd.concat([self.archivo_notas, nuevas_notas], ignore_index=True)
        
        nuevo_registro_estudiante = pd.DataFrame({
            'id': [nuevo_id],
            'nombre': [nombre],
            'promedio': [nuevo_estudiante.calcular_promedio()],
            'estado': [nuevo_estudiante.determinar_estado()]
        })
        self.archivo_estudiantes = pd.concat([self.archivo_estudiantes, nuevo_registro_estudiante], ignore_index=True)
              
        self.archivo_estudiantes.to_csv('estudiantes.csv', index=False)
        self.archivo_notas.to_csv('notas.csv', index=False)
        
        print(f" Estudiante '{nombre}' registrado con ID {nuevo_id}")
        print(f" Promedio: {nuevo_estudiante.calcular_promedio():.2f} - Estado: {nuevo_estudiante.determinar_estado()}")
        
        return nuevo_id
    
    def eliminar_estudiante(self, nombre):
      
        estudiante = self.archivo_estudiantes[self.archivo_estudiantes['nombre'].str.lower() == nombre.lower()]
        
        if estudiante.empty:
            print(f"No se encontró estudiante con nombre '{nombre}'")
            return False
        
        id_estudiante = estudiante['id'].values[0]
        nombre_completo = estudiante['nombre'].values[0]
        
        self.archivo_notas = self.archivo_notas[self.archivo_notas['id_estudiante'] != id_estudiante]
        
        self.archivo_estudiantes = self.archivo_estudiantes[self.archivo_estudiantes['id'] != id_estudiante]
        
        self.archivo_estudiantes.to_csv('estudiantes.csv', index=False)
        self.archivo_notas.to_csv('notas.csv', index=False)
        
        print(f" Estudiante '{nombre_completo}' (ID {id_estudiante}) eliminado correctamente.")
        print(f"   - Registro eliminado de estudiantes.csv")
        print(f"   - Notas eliminadas de notas.csv")
        
        return True

    def promedio_general(self):
        if len(self.archivo_estudiantes) == 0:
            return 0
        else:
            promedio_general = self.archivo_estudiantes['promedio'].mean()
            return promedio_general
        
    def buscar_estudiante(self, nombre):
        estudiante = self.archivo_estudiantes[self.archivo_estudiantes['nombre'].str.lower() == nombre.lower()]
        if not estudiante.empty:
            return {
                "nombre": estudiante['nombre'].values[0],
                "promedio": round(float(estudiante['promedio'].values[0]), 2),
                "estado": estudiante['estado'].values[0]
            }
        else:
            print(f"No se encontró el estudiante con nombre '{nombre}'")
            return None
    def actualizar_notas(self, nombre, nuevas_notas):

        estudiante = self.archivo_estudiantes[self.archivo_estudiantes['nombre'].str.lower() == nombre.lower()]
        if estudiante.empty:
            print(f"No se encontró el estudiante con nombre '{nombre}'")
            return False
        
        id_estudiante = estudiante['id'].values[0]

        self.archivo_notas = self.archivo_notas[self.archivo_notas['id_estudiante'] != id_estudiante]
        
        notas_df = pd.DataFrame({
            'id_estudiante': [id_estudiante] * len(nuevas_notas),
            'nota': nuevas_notas
        })
        self.archivo_notas = pd.concat([self.archivo_notas, notas_df], ignore_index=True)
        
        est_actualizado = Estudiante(nombre, nuevas_notas)
        
        self.archivo_estudiantes.loc[self.archivo_estudiantes['id'] == id_estudiante, 'promedio'] = est_actualizado.calcular_promedio()
        self.archivo_estudiantes.loc[self.archivo_estudiantes['id'] == id_estudiante, 'estado'] = est_actualizado.determinar_estado()
        
        self.archivo_estudiantes.to_csv('estudiantes.csv', index=False)
        self.archivo_notas.to_csv('notas.csv', index=False)
        
        print(f" Notas del estudiante '{nombre}' actualizadas correctamente.")
        print(f" Nuevo Promedio: {est_actualizado.calcular_promedio():.2f} - Nuevo Estado: {est_actualizado.determinar_estado()}")
        
        return True
    
    def mostrar_estudiantes(self):
        for _, estudiante in self.archivo_estudiantes.iterrows():
            print(estudiante.to_dict())

    def mostrar_por_estado(self, filtro_estado):
        estudiantes_filtrados = self.archivo_estudiantes[self.archivo_estudiantes['estado'].str.lower() == filtro_estado.lower()]
        for _, estudiante in estudiantes_filtrados.iterrows():
            print(estudiante.to_dict())
    
    def contar_por_estado(self):
        conteo = self.archivo_estudiantes['estado'].value_counts()
        return conteo.to_dict()
    
    def guardar_en_csv(self):
        self.archivo_estudiantes.to_csv('estudiantes.csv', index=False)
        self.archivo_notas.to_csv('notas.csv', index=False)
        print("Datos guardados en estudiantes.csv y notas.csv")

    def cargar_desde_csv(self):
        self.archivo_estudiantes = pd.read_csv('estudiantes.csv')
        self.archivo_notas = pd.read_csv('notas.csv')
        print("Datos cargados desde estudiantes.csv y notas.csv")


if __name__ == "__main__":
    gestor = GestorEstudiantes()  
    gestor.registrar_estudiante("Juan", [7.5, 6.0, 5.5])
    gestor.registrar_estudiante("Ana", [4.0, 5.0, 3.0])
    gestor.registrar_estudiante("Luis", [8.0, 9.0, 10.0])
    print("\n=== Todos los estudiantes ===")
    gestor.mostrar_estudiantes()
    print("\n=== Buscar estudiante 'luis' ===")
    est = gestor.buscar_estudiante("luis")
    if est:
        print(est)
    print("\n=== Estudiantes Aprobados ===")
    gestor.mostrar_por_estado("Aprobado")
    print("\n=== Estudiantes Suspensos ===")
    gestor.mostrar_por_estado("Suspenso")
    print("\n=== Actualizar notas de Ana ===")
    gestor.actualizar_notas("Ana", [7.0, 8.0, 6.5, 7.0])
    print("\n=== Actualizar notas - Verificacion ===")
    print(gestor.buscar_estudiante("Ana"))  
    print("\n=== Promedio general del grupo ===")
    print(gestor.promedio_general())
    print("\n=== Conteo por estado ===")
    print(gestor.contar_por_estado())
    print("\n=== Eliminar estudiante 'Juan' ===")
    gestor.eliminar_estudiante("Juan")
    print("\n=== Lista final de estudiantes ===")
    gestor.mostrar_estudiantes()