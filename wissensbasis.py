#!/usr/bin/python3

# Define a simple class for logical expressions
class AtomareFormel:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Negation:
    def __init__(self, ausdruck):
        self.ausdruck = ausdruck

    def __repr__(self):
        return f"¬{self.ausdruck}"


class Konjunktion:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return f"({' ∧ '.join(map(str, self.args))})"


class Disjunktion:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return f"({' ∨ '.join(map(str, self.args))})"


class Implikation:
    def __init__(self, voraussetzung, folge):
        self.voraussetzung = voraussetzung
        self.folge = folge

    def __repr__(self):
        return f"({self.voraussetzung} → {self.folge})"


# Function to create a propositional logic knowledge base
def erstelle_wissensbasis():
    # Erstellen atomare Formeln
    N = AtomareFormel("N")  # Nomen
    I = AtomareFormel("I")  # International
    S = AtomareFormel("S")  # Sprache

    #Aufgabe1

    # Das ist die Liste der Regeln, wie ein Regelwerk wie die Verkehrssituation aussehen könnte.
    F = AtomareFormel ("F") # Fußgänger
    H = AtomareFormel ("H") # Hupe
    A = AtomareFormel ("A") # Anhalten
    R = AtomareFormel ("R") # AmpelRot
    W = AtomareFormel ("W") # Weiterfahren





    # Definieren Sie Ihre logischen Regeln (Formeln)
    # Aufgabe2
    # Hier werden die Regeln definiert, die die Beziehungen zwischen den atomaren Formeln beschreiben.

    wissensbasis = [
        Implikation(F, H),
        Implikation(H, A),
        Implikation (R, A),
        Implikation (Konjunktion(Negation(F), Negation(R)), W) # zwei Argumente und verknüpft; Annahme dass A und B passiert
    ]

    return wissensbasis


# Function to apply Modus Ponens
# Das ist die eigentliche Schlussfolgerngslogik, die dei Regeln der Wissensbasis anwendet, um die bekannten Fakten anzuwenden.
# Die while Schleife sorgt dafür, dass alle möglichen Schlussfolgerungen gezogen werden, bis keine neuen Fakten mehr abgeleitet werden können.

def wende_modus_ponens_an(wb, bekannte_fakten):
    abgeleitete_fakten = set(str(fact) for fact in bekannte_fakten)  # Store string representations of facts
    geaendert = True
    while geaendert:
        geaendert = False
        for regel in wb:
            if isinstance(regel, Implikation) and str(regel.voraussetzung) in abgeleitete_fakten:
                if str(regel.folge) not in abgeleitete_fakten:
                    print(f"Modus Ponens ausgeführt: {regel.voraussetzung} → {regel.folge}")
                    abgeleitete_fakten.add(str(regel.folge))
                    geaendert = True
    return abgeleitete_fakten