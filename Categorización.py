import unittest

def crear_tarea(fecha, hora, titulo, descripcion, categoria):
  """Crea una tarea en el calendario."""
  # Implementar la lógica para crear una tarea

def obtener_tareas(fecha_inicio, fecha_fin, categoria):
  """Obtiene las tareas para un rango de fechas y una categoría específica."""
  # Implementar la lógica para obtener las tareas

def editar_tarea(id_tarea, fecha, hora, titulo, descripcion, categoria):
  """Edita una tarea existente en el calendario."""
  # Implementar la lógica para editar una tarea

def eliminar_tarea(id_tarea):
  """Elimina una tarea del calendario."""
  # Implementar la lógica para eliminar una tarea

class TestCategorizacionTareas(unittest.TestCase):

  def test_crear_tarea(self):
    """Prueba la creación de una tarea."""
    fecha = "2024-02-18"
    hora = "10:00"
    titulo = "Tarea importante"
    descripcion = "Descripción de la tarea importante"
    categoria = "Trabajo"

    tarea = crear_tarea(fecha, hora, titulo, descripcion, categoria)

    # Verificaciones
    self.assertEqual(tarea["fecha"], fecha)
    self.assertEqual(tarea["hora"], hora)
    self.assertEqual(tarea["titulo"], titulo)
    self.assertEqual(tarea["descripcion"], descripcion)
    self.assertEqual(tarea["categoria"], categoria)

  def test_obtener_tareas(self):
    """Prueba la obtención de tareas para un rango de fechas y una categoría."""
    fecha_inicio = "2024-02-18"
    fecha_fin = "2024-02-18"
    categoria = "Trabajo"

    tareas = obtener_tareas(fecha_inicio, fecha_fin, categoria)

    # Verificaciones
    self.assertEqual(len(tareas), 1)
    self.assertEqual(tareas[0]["fecha"], fecha_inicio)
    self.assertEqual(tareas[0]["categoria"], categoria)

  def test_editar_tarea(self):
    """Prueba la edición de una tarea existente."""
    id_tarea = 1
    fecha = "2024-02-19"
    hora = "11:00"
    titulo = "Nueva tarea importante"
    descripcion = "Nueva descripción de la tarea importante"
    categoria = "Personal"

    editar_tarea(id_tarea, fecha, hora, titulo, descripcion, categoria)

    # Verificación
    tareas = obtener_tareas("2024-02-19", "2024-02-19", categoria)
    self.assertEqual(tareas[0]["titulo"], titulo)
    self.assertEqual(tareas[0]["descripcion"], descripcion)
    self.assertEqual(tareas[0]["categoria"], categoria)

  def test_eliminar_tarea(self):
    """Prueba la eliminación de una tarea."""
    id_tarea = 1

    eliminar_tarea(id_tarea)

    # Verificación
    tareas = obtener_tareas("2024-02-19", "2024-02-19", "Personal")
    self.assertEqual(len(tareas), 0)

if __name__ == "__main__":
  unittest.main()
