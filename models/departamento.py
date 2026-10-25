from models.Empleado import empleado

# atributos clave id_departamento, nombre, gerente, presupuesto
class Departamento:
    def __init__(self, id_departamento: int, nombre: str, gerente: str | None, presupuesto: int):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.gerente = gerente
        self.presupuesto = presupuesto

    @property
    def id_departamento(self) -> int:
        return self._id_departamento

    @id_departamento.setter
    def id_departamento(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El ID del departamento debe ser un número entero mayor a 0.")
        self._id_departamento = value

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser un texto.")
        value = value.strip()
        if len(value) < 3:
            raise ValueError("El nombre debe ser al menos 3 caracteres.")
        self._nombre = value

    @property
    def gerente(self):
        return self._gerente

    @gerente.setter
    def gerente(self, value):
        if value is None or value == "":
            self._gerente = None
            return

        if not isinstance(value, str):
            raise ValueError("El gerente debe ser texto o vacío.")

        value = value.strip()
        if len(value) < 3:
            raise ValueError("El RUT del gerente debe tener al menos 3 caracteres.")
        self._gerente = value

    @property
    def presupuesto(self) -> int:
        return self._presupuesto

    @presupuesto.setter
    def presupuesto(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El presupuesto debe ser un número entero mayor a 0.")
        self._presupuesto = value

    def __repr__(self):
        return f"Departamento(id_departamento='{self.id_departamento}', nombre='{self.nombre}', gerente='{self.gerente}', presupuesto={self.presupuesto})"