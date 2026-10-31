import networkx as nx
import matplotlib.pyplot as plt
import random
from typing import Optional

BIJELA = 1
CRNA = 0

class Stablo:
    def __init__(self, boja: bool, evaluacija: Optional[float] = None):
        self.boja = boja
        self.evaluacija = evaluacija
        self.djeca: list['Stablo'] = []

    def dodaj_dijete(self, dijete: 'Stablo'):
        self.djeca.append(dijete)

    def daj_boju(self):
        return self.boja
    
    def daj_evaluaciju(self):
        return self.evaluacija

    def postavi_evaluaciju(self, eval):
        self.evaluacija = eval
    def je_list(self):
        return len(self.djeca) == 0


def staticka_evaluacija(pozicija: Stablo):
    #U svrhu primjera dajemo samo random vrijednost
    return random.uniform(-10, 10)



def minimax(pozicija: Stablo, dubina: int, bojaIgraca: bool):
    najbolje_dijete = None
    if dubina == 0 or pozicija.je_list():
        if pozicija.evaluacija is None:
            pozicija.evaluacija = staticka_evaluacija(pozicija)
        return pozicija.evaluacija, None

    if bojaIgraca == BIJELA:
        najbolja_evaluacija = float('-inf')
        for dijete in pozicija.djeca:
            vrijednost, _ = minimax(dijete, dubina-1, CRNA)
            if vrijednost > najbolja_evaluacija:
                najbolja_evaluacija = vrijednost
                najbolje_dijete = dijete
        
    if bojaIgraca == CRNA:
        najbolja_evaluacija = float('inf')
        for dijete in pozicija.djeca:
            vrijednost, _ = minimax(dijete, dubina-1, BIJELA)
            if vrijednost < najbolja_evaluacija:
                najbolja_evaluacija = vrijednost
                najbolje_dijete = dijete


    pozicija.evaluacija = najbolja_evaluacija   

    return najbolja_evaluacija, najbolje_dijete







# Dio koda  između --- za vizualizaciju grafova je napravio AI.
# ----------------------------------------------------------

def izgradi_graf(cvor: Stablo, graf: nx.DiGraph, parent_id=None, counter=None):
    """Rekurzivno dodaje čvorove i bridove u NetworkX graf."""
    if counter is None:
        counter = [0]
    
    current_id = counter[0]
    counter[0] += 1

    # Oznaka koja se ispisuje unutar čvora
    naziv_boje = "BIJELI" if cvor.boja == BIJELA else "CRNI"
    labela = f"{cvor.evaluacija:+.0f}"
    
    # Boja kružića na slici
    boja_kruga = "#e0e0e0" if cvor.boja == BIJELA else "#404040"
    boja_teksta = "black" if cvor.boja == BIJELA else "white"

    graf.add_node(current_id, label=labela, color=boja_kruga, text_color=boja_teksta)

    if parent_id is not None:
        graf.add_edge(parent_id, current_id)

    for dijete in cvor.djeca:
        izgradi_graf(dijete, graf, current_id, counter)


def hijerarhijski_raspored(graf, root_id=0, width=1.0, vert_gap=0.2, xcenter=0.5):
    """Računa (x, y) koordinate tako da čvorovi izgledaju kao pravo stablo odozgo prema dolje."""
    pos = {root_id: (xcenter, 1.0)}
    
    def _postavi(cvor_id, lijevo, desno, vert_pos):
        djeca = list(graf.successors(cvor_id))
        if not djeca:
            return
        dx = (desno - lijevo) / len(djeca)
        next_x = lijevo + dx / 2
        for dijete in djeca:
            pos[dijete] = (next_x, vert_pos)
            _postavi(dijete, next_x - dx / 2, next_x + dx / 2, vert_pos - vert_gap)
            next_x += dx

    _postavi(root_id, 0.0, width, 1.0 - vert_gap)
    return pos


def nacrtaj_stablo(korijen: Stablo):
    graf = nx.DiGraph()
    izgradi_graf(korijen, graf)

    pos = hijerarhijski_raspored(graf, root_id=0)

    # Izdvajanje vizualnih svojstava
    boje_cvorova = [graf.nodes[n]['color'] for n in graf.nodes]
    labele = {n: graf.nodes[n]['label'] for n in graf.nodes}

    plt.figure(figsize=(8, 6))
    
    # Crtanje bridova (strelica prema dolje)
    nx.draw_networkx_edges(graf, pos, arrows=True, arrowsize=15, edge_color="gray")
    
    # Crtanje kružića
    nx.draw_networkx_nodes(graf, pos, node_color=boje_cvorova, node_size=2800, edgecolors="black")

    # Crtanje teksta u čvorovima
    for node, (x, y) in pos.items():
        plt.text(x, y, labele[node], 
                 fontsize=15, 
                 ha='center', 
                 va='center', 
                 color=graf.nodes[node]['text_color'], 
                 weight='bold')

    plt.title("Prikaz stabla poteza", fontsize=14)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

# -------------------------------------------------------------------------

def generiraj_random_stablo(korijen: Stablo, dubina: int, min_djece: int = 1, max_djece: int = 3):
    if dubina <= 0:
        return

    broj_djece = random.randint(min_djece, max_djece)

    for i in range(broj_djece):
        dijete = Stablo(boja= not korijen.boja)
        korijen.dodaj_dijete(dijete)
        generiraj_random_stablo(dijete, dubina-1, min_djece, max_djece)


if __name__ == "__main__":


    korijen1 = Stablo(boja=BIJELA)
    dubina = 2
    generiraj_random_stablo(korijen1, dubina = dubina, min_djece = 2, max_djece = 3)

    optimalna_vrijednost, odabrani_potez = minimax(korijen1, dubina = dubina, bojaIgraca = BIJELA)

    nacrtaj_stablo(korijen1)



    korijen = Stablo(boja=BIJELA)

    potez1 = Stablo(boja=CRNA)
    potez2 = Stablo(boja=CRNA)
    korijen.dodaj_dijete(potez1)
    korijen.dodaj_dijete(potez2)


    potez1.dodaj_dijete(Stablo(boja=BIJELA, evaluacija = -2) )
    potez1.dodaj_dijete(Stablo(boja=BIJELA, evaluacija = 8))
    
    potez2.dodaj_dijete(Stablo(boja=BIJELA, evaluacija = -1))
    potez2.dodaj_dijete(Stablo(boja=BIJELA, evaluacija = 2))
    potez2.dodaj_dijete(Stablo(boja=BIJELA, evaluacija = 4))

    optim2, _ = minimax(korijen, dubina = 2, bojaIgraca = BIJELA)
    
    nacrtaj_stablo(korijen)