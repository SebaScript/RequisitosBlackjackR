class Carta:

    def __init__(self, pinta: str, valor: str):
        self.pinta = pinta
        self.valor = valor
        self.tapada: bool = True


class Mano:

    def __init__(self, cartas: tuple[Carta]):
        self.cartas: list[Carta] = []
        self.cartas.extend(cartas)

    def es_blackjack() -> bool:
        pass

class Baraja:

    PINTAS: str = ("\u2764\uFE0F", "\u2663\uFE0F", "\u2666\uFE0F", "\u2660\uFE0F")
    VALORES: str = ("A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self):
        self.cartas: list[Carta] = []
        for pinta in Baraja.PINTAS:
            for valor in Baraja.VALORES:
                self.cartas.append(Carta(pinta, valor))

    def revolver(self):
        pass

    def repartir_carta(self) -> Carta:
        pass

class Jugador:

    PLANTARSE: True
    PEDIR_CARTA: False

    def __init__(self, nombre: str, fichas:int):
        self.nombre: str = nombre
        self.fichas: int = fichas
        self.mano: Mano = None

    def inicializar_mano(self, cartas: tuple[Carta]):
        self.mano = Mano(cartas)

    def decision(self) -> bool:
        self.plantarse:bool = Jugador.PLANTARSE
        self.pedir: bool = Jugador.PEDIR_CARTA

    def calcular_valor_mano(self, decision, mano):
        self.decision: bool = decision

    def repartir_carta_jugador(self,baraja) -> Carta:
        self.mano = Mano.append(0)



class Casa:

    def __init__(self):
        self.mano: Mano = None

    def inicializar_mano(self, cartas: tuple[Carta]):
        self.mano = Mano(cartas)

    def destapar_carta(self, mano):
        self.mano.tapada = False

    def repartir_carta_casa(self, baraja) -> Carta:
        self.mano = Mano.append(0)

    def valor_mano_casa(self, mano) -> bool:
        pass


class Blackjack:

    FICHAS_INICIALES: int = 100

    def __init__(self):
        self.apuesta_actual: int = 0
        self.baraja: Baraja = Baraja()
        self.jugador: Jugador = None
        self.cupier: Casa = None

    def registrar_jugador(self, nombre):
        self.jugador = Jugador(nombre, Blackjack.FICHAS_INICIALES)

    def iniciar_juego(self, apuesta: int):
        self.apuesta_actual = apuesta

    def es_blackjack(self, mano) -> bool:
        pass

    def es_empate(selfself,mano) -> bool:
        pass

    def calcular_fichas(self, apuesta):
        pass


