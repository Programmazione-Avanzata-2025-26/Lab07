# Lab 07 - Soluzione (Epoche Ordinate usando la classe `Epoca`)

> **💡 NOTA:** 
>  In questa soluzione viene definita la classe `Epoca` il cui costruttore richiede una stringa (ad esempio 
> "II secolo a.C.", "XV secolo", ecc. come lette dal database) che successivamente usa per inizializzarsi i campi 
> `secolo` e `locuzione`.
> 
> All'interno della classe viene definito il metodo `__lt()__` che definisce la relazione di `<`
> tra due epoche. Tutto questo permette poi, in `model.py`, di ordinare la lista di epoche semplicemente eseguendo
> un'istruzione di questo tipo: `sorted(lista_epoche)`

#### Argomenti

- Utilizzo pacchetto `Flet` di Python (suggerita v0.28.3)
- Utilizzo Pattern MVC
- Utilizzo dei Package
- Utilizzo di mysql-connector-python (suggerita v9.5.0)
- Utilizzo del Pattern DAO

---
> **❗ ATTENZIONE:** 
>  Ricordare di effettuare il **fork** del repository principale, quindi clonare su PyCharm il **repository personale** 
> (https://github.com/my-github-username/Lab07) e non quello principale.
> 
> In caso di dubbi consultare la guida caricata nel lab02: 
> https://github.com/Programmazione-Avanzata-2025-26/Lab02/blob/main/Guida.pdf
> 

## Setup del Database tramite **DBeaver**
1. **Avvio e creazione connessione**
   1. Una volta attivato **XAMPP** (se non già fatto, vedere il setup e attivazione nel repository del lab6), 
   aprire **DBeaver**.
   2. Cliccare sull’icona `Database → Nuova Connessione` (icona a forma di plug, in alto a sinistra).
   3. Nella finestra che si apre, selezionare ` MySQL` dall'elenco dei database supportati e cliccare `Avanti`.
   ![nuova_connessione.png](img/nuova_connessione.png)
2. **Configurazione della connessione**
   1. Inserire i seguenti parametri:
      - **Host**: localhost
      - **Port**: 3306 (porta predefinita di MySQL)
      - **Database**: lasciare vuoto se si vuole creare una nuova connessione generale (si consiglia di lasciarla vuota). 
      - **Username**: root 
      - **Password**: (nessuna, se non impostata in XAMPP)
   ![configurazione_connessione.png](img/configurazione_connessione.png)
   2. Cliccare su `Tenta di Stabilire una Connessione` per verificare che **DBeaver** riesca a collegarsi correttamente 
   al server MySQL. Se la connessione è riuscita, comparirà il messaggio `Conncted`.
   3. Premere infine `Fine`. 
3. **Creazione del database**
   1. Una volta connessi, nel pannello di sinistra `Navigatore Database`, cliccare col tasto destro su 
   `localhost → Create → Database...`
   ![creare_database.png](img/creare_database.png)
   2. Assegnare il nome `musei_torino`, e confermare con `OK`. 
4. **Importazione del database**
   1. Espandere il nodo del database `musei_torino`.
   2. Cliccare col tasto destro su di esso → `Strumenti` → `Execute Script`
   ![importare_database.png](img/importare_database.png)
   3. Selezionare il file `musei_torino.sql` fornito nel progetto.
   4. Cliccare su `Inizia` per eseguire tutte le istruzioni SQL contenute nel file. 
   5. Al termine, compariranno le tabelle (museo, artefatto) nel pannello di navigazione. 
5. **Verifica del contenuto**
   1. Espandere le tabelle per visualizzare la struttura.
   2. Per verificare i dati, cliccare con il tasto destro su una tabella (ad esempio `museo`) → `Vedi Dati`. 
   3. I dati pre-caricati saranno visibili in forma tabellare. 
6. **(Facoltativo): esportazione o query di prova**
   1. È possibile scrivere manualmente una query SQL in una nuova scheda (tasto destro sul database, quindi 
   `SQL Editor → New Script/SQL Script`) per verificare che tutto funzioni:
   `SELECT * FROM museo;`
   2. Se i dati vengono visualizzati, il database è pronto per essere utilizzato dalla tua applicazione Python tramite 
   `mysql-connector-python`. 

---

##  Gestione Museale
Implementare un’applicazione per la gestione di un sistema museale. L’applicazione deve consentire di: 
- Visualizzare gli artefatti presenti in tutti i musei 
- Visualizzare gli artefatti presenti in uno specifico museo 
- Visualizzare gli artefatti di una specifica epoca 
- Visualizzare gli artefatti in uno specifico museo di una specifica epoca 

Fare uso del pattern MVC, utilizzando i pacchetti `flet` e `mysql-connector-python`. Interagire con il database tramite 
l’uso pattern DAO, come spiegato a lezione. 

### Implementazione
Realizzare un’interfaccia grafica con `flet` simile a quella mostrata in figura. 
![layout.png](img/layout.png)

La proposta di interfaccia include:
- Titolo pagina (“Lab07”) – già fatto ✅
- Pulsante per cambiare tema (default dark mode) utilizzando `Switch` – già fatto ✅ 
- **Sezione 1**: Intestazione Gestione Museale - già fatto ✅
  - Un controllo `Text` con testo "Musei di Torino".
- **Sezione 2**: Filtraggio - TODO 📝
  - Un controllo `Dropdown` per selezionare un museo tra tutti quelli presenti nel database. 
  - Un controllo `Dropdown` per selezionare un’epoca tra tutte quelle a cui appartengono gli artefatti presenti nel 
  database. 
- **Sezione 3**: Lista Artefatti Filtrata - TODO 📝
  - Un controllo `ElevatedButton` “Mostra Artefatti” per mostrare tutti gli artefatti che soddisfano i criteri di 
  filtraggio specificati sopra. 
  - Un contenitore `ListView` da popolare con gli artefatti che vengono letti dal database (in base al tipo di 
  filtraggio indicato). Se nessun artefatto soddisfa i criteri di filtraggio indicati, il sistema risponderà con 
  un alert.

### NOTA BENE
- Per popolare il menu a tendina tramite DropDown, occorre aggiungere alla sua lista `options` oggetti di 
tipo `ft.dropdown.Option`. 
Ad esempio: 
    ```code
    self._view.elemento_dropdown.options.append(ft.dropdown.Option("Scelta 1"))`
    ```
- Per risolvere l’esercizio è necessario filtrare gli artefatti in base alle scelte effettuate dall’utente. 
- Ogni menu a tendina deve includere anche l’opzione “Nessun filtro”, che indica che il relativo filtro 
(ad esempio per nome del museo o per epoca) non è attivo. Ciò si può gestire in due modi: 
  1. Direttamente con una query SQL che tiene conto dei filtri opzionali.
  2. In Python, filtrando i dati dopo averli letti dal database. 

  **Nel primo caso (i)**, è possibile utilizzare la funzione `SQL COALESCE()`, che restituisce il primo valore non nullo tra 
  quelli passati come argomento. In questo modo, la query risulta valida sia quando l’utente seleziona un filtro, 
  sia quando sceglie “Nessun filtro”.
  
  Ad esempio: 

     ```code
     WHERE epoca = COALESCE(%s, epoca)`
     ```
  Se l’utente sceglie una opzione del dropdown, l’opzione viene usata per filtrare la lista di artefatti; se invece 
  l’utente seleziona in uno specifico dropdown “nessun filtro”, il campo viene confrontato con se stesso e la condizione 
  risulta sempre vera.  

  **Nel secondo caso (ii)** si possono leggere da SQL tutti gli artefatti, e poi applicare i filtri in Python. 
- Viene lasciata la libertà di utilizzare o meno l'**ORM** (Object Relational Mapping) spiegato a lezione, mediante, 
ad esempio, una identity map, oppure considerando che gli oggetti del DTO tengano traccia delle relazioni. 

---

## Materiale Fornito
Il repository del lab07 è organizzato con la struttura ad albero mostrata di seguito e contiene tutto il necessario per 
svolgere il laboratorio:

```code
Lab07/
├── database/
│   ├── __init__.py
|   ├── artefatto_DAO.py (DA MODIFICARE)
|   ├── connector.cnf
│   ├── DB_connect.py
│   └── museo_DAO.py (DA MODIFICARE)
│
├── model/
│   ├── __init__.py
│   ├── artefatto_DTO.py
│   ├── model.py (DA MODIFICARE)
│   └── museo_DTO.py
│
├── UI/
│   ├── __init__.py
│   ├── alert.py
│   ├── controller.py (DA MODIFICARE)
│   └── view.py (DA MODIFICARE)
│
├── musei_torino.sql (DA IMPORTARE)
├── main.py (DA ESEGUIRE)
└── requirements.txt
 ```