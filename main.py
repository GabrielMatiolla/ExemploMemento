class Memento:
    """Armazena o estado do Originador"""
    def __init__(self, estado):
        self._estado = estado

    def get_estado_salvo(self):
        return self._estado


class Originador:
    """Cria e restaura seu estado através de Mementos"""
    def __init__(self):
        self._estado = ""

    def set_estado(self, estado):
        print(f"Originador: Definindo estado para {estado}")
        self._estado = estado

    def salvar_para_memento(self):
        print("Originador: Salvando para Memento.")
        return Memento(self._estado)

    def restaurar_de_memento(self, memento):
        self._estado = memento.get_estado_salvo()
        print(f"Originador: Estado após restaurar do Memento: {self._estado}")


class Cuidador:
    """Responsável por guardar os Mementos"""
    def __init__(self, originador):
        self._originador = originador
        self._mementos = []

    def backup(self):
        print("\nCuidador: Salvando estado do Originador...")
        self._mementos.append(self._originador.salvar_para_memento())

    def undo(self):
        if not self._mementos:
            return

        memento = self._mementos.pop()
        print(f"Cuidador: Restaurando estado para: {memento.get_estado_salvo()}")
        self._originador.restaurar_de_memento(memento)


# Código cliente
if __name__ == "__main__":
    originador = Originador()
    cuidador = Cuidador(originador)

    originador.set_estado("Estado 1")
    cuidador.backup()

    originador.set_estado("Estado 2")
    cuidador.backup()

    originador.set_estado("Estado 3")
    
    print("\nClient: Agora vamos desfazer as alterações!\n")
    cuidador.undo()
    cuidador.undo()