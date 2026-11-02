# TicTacToe-AI-Ref_Learning

Un Tic Tac Toe (tris) giocabile contro una CPU che **impara dalle partite** grazie a una forma semplice di reinforcement learning. Ogni partita modifica i valori salvati dall'IA, che quindi gioca meglio man mano che accumuli esperienza.

L'interfaccia grafica è realizzata con **Pygame**.

## Come funziona

Il gioco usa un approccio a tabella di valori (*tabular* RL):

- **Tu giochi con la X** e fai la prima mossa. **La CPU gioca con la O**.
- Il file `AIData.json` contiene la "memoria" dell'IA. Ogni voce è identificata da un ID e contiene:
  1. una configurazione della griglia 3x3 (stato di gioco),
  2. una matrice 3x3 di valori, uno per ogni cella (quanto è "buona" quella mossa in quello stato).
- Quando tocca alla CPU, cerca nel file lo stato uguale alla griglia attuale e sceglie la cella con il **valore più alto**. Le celle con valore `0` sono considerate non valide (celle già occupate) e vengono escluse.
- Le mosse fatte dalla CPU durante la partita vengono memorizzate. A fine partita i loro valori vengono aggiornati in base al risultato:

| Risultato per la CPU | Aggiornamento del valore delle mosse giocate |
|----------------------|-----------------------------------------------|
| Vittoria             | `+0.1`                                        |
| Pareggio             | `+0.05`                                       |
| Sconfitta            | `-0.1`                                        |

- L'aggiornamento viene scritto direttamente su `AIData.json`, quindi **l'apprendimento è persistente** tra una partita e l'altra.

## Struttura del progetto

```
.
├── tictactoe.py     # Avvio del gioco: finestra Pygame, griglia, input del mouse, controllo vittoria
├── CPUVersus.py     # Logica dell'IA: scelta della mossa e aggiornamento dei valori
├── AIData.json      # Memoria dell'IA (stati di gioco e valori delle mosse)
└── .gitattributes
```

## Requisiti

- Python 3.8 o superiore
- [Pygame](https://www.pygame.org/)
- [NumPy](https://numpy.org/)

## Installazione

```bash
git clone https://github.com/Rick88999/TicTacToe-AI-Ref_Learning.git
cd TicTacToe-AI-Ref_Learning
pip install pygame numpy
```

## Utilizzo

Avvia il gioco **dalla cartella del progetto** (il file `AIData.json` viene letto con un percorso relativo):

```bash
python tictactoe.py
```

- Clicca con il mouse su una cella vuota per piazzare la tua X.
- La CPU risponde subito con la sua O.
- A fine partita (vittoria, sconfitta o pareggio) i valori dell'IA vengono aggiornati e il programma si chiude dopo un paio di secondi. Rilancialo per giocare una nuova partita.

## Note

- Ogni esecuzione corrisponde a **una sola partita**.
- Se la CPU non trova nel file lo stato di gioco corrente, non gioca nessuna mossa e lo segnala sul terminale.
- Non modificare a mano `AIData.json`, a meno che tu non voglia resettare o alterare l'apprendimento.

## Licenza

BSD 3-Clause License

## Autore

**Riccardo Tulini** — [@Rick88999](https://github.com/Rick88999)
