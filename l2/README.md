# Lista 2 ✏️

## 👆 Zadanie 0 (przykład w wykładu)

Producent czekolady produkuje 2 rodzaje czekolad: mleczną i luksusową.

Zysk: 1 tablicza mlecznej (M) kosztuje 1 zł, a 1 tabliczna luksusowej (L) kosztuje 6 zł. Dzienne możliwości produkcji to 400 tabliczek. Dzienny popyt to 200 tabliczek mlecznej, 300 tabliczek luksusowej.

Jaki jest optymalny poziom produkcji, maksymalizacja zysku.

## 👆 Zadanie 1 

Pewne przedsiębiorstwo otnicze musi podjąć decyzję o zakupie paliwa do samolotów odrzutowych, mając do wyboru trzech dostawców. Samoloty tankują paliwo regularnie na czterech lotniskach, które obsługują.

Firmy paliwowe poinformowały, że mogą dostarczyć następujące ilości paliwa w nadchodzącym miesiącu; Firma 1 - 275 000 galonów, Firma 2 - 550 000 galonów i Frima 3 - 660 000 galonów. Niezbędne ilości paliwa do odrzutowców na poszczególnych lotniskach są odpwiednio równe: na lotnisku 1 - 110 000 galonów, na lotnisku 2 - 220 000 galonów, na lotniksu 3 - 330 000 galonów i na lotniusku 4 - 440 000 galonów. Koszt galonu paliwa z uwzględnieniem kosztów transportu dostarczonego przez poszczególnych dostawców kształtuję się na każdym lotnisku następująco:

|   	|   Firma 1	|   Firma 2	|   Firma 3	|
|---	|---	|---	|---	|
|   Lotnisko 1	|   10	|   7 	|   8	|
|   Lotnisko 2	|   10	|   11	|   14	|
|   Lotnisko 3	|   9	|   12	|   4	|
|   Lotnisko 4	|   11	|   13	|   9	|

Wyznacz plan zakupu i dostaw paliwa na lotniska, który minimalizuje koszty.

Czy wszystkie firmy dostarczają paliwo?

Czy możliwości dostaw paliwa przez firmy są wyczerpane?

## Rozwiązanie zadania 1

Zadanie zostało maksymalnie sparametryzowane. W pliku w pierwszej linijce podajemy ilość lotnisk i ilość firm dostraczających paliwo, oddzielone średnikiem. W kolejnej linijce podajemy również po średniku ile są w stanie dostawcy dostarczyć paliwa w danym miesiącu. Następnej linijce podajemy zapotrzebowanie na każdym z lotnisk. Potem podajemy w len(lotniskach), len(firmy) koszty transportu jedengo galonu paliwa. Przykadowy plik, z rozwiązaniem tego zadania z powyżej opisanymi danymi znajduję się w pliku ```model.txt```

Funckja minimalizująca i warunki ograniczające dla danych z zadania to:

$$ \begin{aligned}
\min\quad 
& 10 x_{A1,C1} + 7 x_{A1,C2} + 8 x_{A1,C3} + \\ 
& 10 x_{A2,C1} + 11 x_{A2,C2} + 14 x_{A2,C3} + \\
& 9 x_{A3,C1} + 12 x_{A3,C2} + 4 x_{A3,C3} + \\
& 11 x_{A4,C1} + 13 x_{A4,C2} + 9 x_{A4,C3}\\
\text{Subject to} \quad & x_{A1,C1} + x_{A1,C2} + x_{A1,C3} = 110000.0\\
 & x_{A2,C1} + x_{A2,C2} + x_{A2,C3} = 220000.0\\
 & x_{A3,C1} + x_{A3,C2} + x_{A3,C3} = 330000.0\\
 & x_{A4,C1} + x_{A4,C2} + x_{A4,C3} = 440000.0\\
 & x_{BIN,C1} + x_{BIN,C2} + x_{BIN,C3} = 385000.0\\
 & x_{A1,C1} + x_{A2,C1} + x_{A3,C1} + x_{A4,C1} + x_{BIN,C1} = 275000.0\\
 & x_{A1,C2} + x_{A2,C2} + x_{A3,C2} + x_{A4,C2} + x_{BIN,C2} = 550000.0\\
 & x_{A1,C3} + x_{A2,C3} + x_{A3,C3} + x_{A4,C3} + x_{BIN,C3} = 660000.0\\
 & \sum_{(A, C) : A \in \{A1, A2, A3, A4, BIN\}, C \in \{ C1, C2, C3\}}{x_{A,C}} \geq 0.0\end{aligned} \\
$$

 Plan zakupowy dostaw paliwa na lotniska, który minimalizuje koszty, przestawiłem w tabeli poniżej.

 |   Lotnisko \ Firma	|   Firma 1	|   Firma 2	|   Firma 3	|
|---	|---	|---	|---	|
|   Lotnisko 1	|   0	|   110000.0 	|   0	|
|   Lotnisko 2	|   165000	|   55000.0	|   0	|
|   Lotnisko 3	|   0	|   0	|   330000.0	|
|   Lotnisko 4	|   110000.0	|   0	|   330000.0	|


## ✌️ Zadanie 2

Dana jest sieć połączeń między `n` miastami reprezentowana za pomocą skierowanego grafu G = (N, A) gdzie N jest zbiorem miast (wierzchołków), |N| = n jest zbiorem połączeń między miastami (łuków), |A| = m. Dla każdego połączenia z miasta `i` do miasta `j` $(i, j) \in A$ dane są koszty przejazdu $c_{ij}$ oraz czas przejazdu $t_{ij}$ (im mniejszy koszt, tym dłuższy czas przejazdu). Dane są również dwa miasta $i^*, j^* \in N$

Celem jest znalezienie połączenia (ścieżki) między zadanymi dwoma miastami, którego całkowity koszt jest najmniejszy i całkowity czas przejazdu nie przekracza z góry zdanego czsu przejazdu T.

Funckja minimalizująca i warunki ograniczające dla danych z zadania to:

$$ \begin{aligned}
\min\quad & x_{City 1,City 2} + 2 x_{City 1,City 4} + x_{City 2,City 3} + 5 x_{City 2,City 4} + 3 x_{City 4,City 5} + 5 x_{City 5,City 3}\\
\text{Subject to} \quad & x_{City 1,City 2} + x_{City 1,City 4} = 1.0\\
 & -x_{City 1,City 2} + x_{City 2,City 3} + x_{City 2,City 4} = 0.0\\
 & -x_{City 2,City 3} - x_{City 5,City 3} = -1.0\\
 & -x_{City 1,City 4} - x_{City 2,City 4} + x_{City 4,City 5} = 0.0\\
 & x_{City 5,City 3} - x_{City 4,City 5} = 0.0\\
 & 10 x_{City 1,City 2} + 11 x_{City 2,City 3} + 8 x_{City 5,City 3} + 2 x_{City 1,City 4} + 8 x_{City 2,City 4} + 4 x_{City 4,City 5} \leq 20.0\\
 
& \sum_{City_i,City_j : i, j \in \{ 1,2,3,4,5\}}{x_{City_i,City_j}} \geq 0.0 \\
& \sum_{City_i,City_j : i, j \in \{ 1,2,3,4,5\}}{x_{City_i,City_j}} \leq 1.0 \\
& \sum_{City_i,City_j : i, j \in \{ 1,2,3,4,5\}}{x_{City_i,City_j}} \in \mathbb{Z} \\
\end{aligned} $$

Plan przejścia z wierzchołka 1 do wierzchołka 3 o najmnijesyzm koszcie i całkowity czas przejazdu nie przekracza zadanego czasu przejazdu T = 20. 

|   	|   1	|   2	|   3	|   4	|   5	|
|---	|---	|---	|---	|---	|---	|
|   1	|   0	|   0	|   0	|   1	|   0	|
|   2	|   0	|   0	|   0	|   0	|   0	|
|   3	|   0	|   0	|   0	|   0	|   0	|
|   4	|   0	|   0	|   0	|   0	|   1	|
|   5	|   0	|   0	|   1	|   0	|   0	|

Pliki wejściowy z danymi to: `graph.txt` oraz `graph2.txt`

### Przykład 

![alt text for screen readers](/l2/png/2.png)

Jak widzimy na załączonym przykładzie, najkrótsza ścieżka w tym grafie z pominięciem czasu to 1 -> 2 -> 3. Jedank gdy nałożymy ograniczenie na czas (W tym przykładzie wynosi 20), to najktrótsza ścieżka różni się od pierwotnej, i wygląda następująco 1 -> 4 -> 5 -> 3.

## 🤟 Zadanie 3

Policja w małym miasteczku posiada w swoim zasięgu trzy dzielnnice oznaczone jako $p_1, p_2, p_3$. Każda dzielnica ma przypisaną pewną liczbę radiowozów wyposażonych w radiotelefony i sprzęt pierwszej pomocy. Policja pracuje w systemie trzyzmianowym. W tabelki poniżej podanę są minimalne i maksymalne liczby radiowozów dla każdej zmiany i dzielnicy odziellone znkaiem "/"

|   	|   z1	|   z2	|   z3	|
|---	|---	|---	|---	|
|   p1	|   2/3	|   4/7	|   3/5	|
|   p2	|   3/5	|   6/7	|   5/10	|
|   p3	|   5/8	|   7/12	|   6/10	|

Ponadto aktualne przepisy wymuszają, że dla zmiany 1,2,3 powinno być dostępnych odpowiednio, co najmniej 10, 20, 18 radiowozów. Ponadto dzielnice $p_1, p_2, p_3$ powinny mieć przypisane, odpowiednio co najmniej 10, 20, 13 radiowozów. Polica chce wyznaczyć przydział radiowozów spełniający powyższe wymagania  i minimalizując ich całkowitą liczbę. Sformułuj ten problem jako problem cyrkulacji.

Powyższy model prezentuje się następująco:

$$ \begin{aligned}
\min\quad & x_{District 1,Shift 1} + x_{District 1,Shift 2} + x_{District 1,Shift 3} + \\
& x_{District 2,Shift 1} + x_{District 2,Shift 2} + x_{District 2,Shift 3} + \\
& x_{District 3,Shift 1} + x_{District 3,Shift 2} + x_{District 3,Shift 3} \\
\text{Subject to} \quad & x_{District 1,Shift 1} \geq 2.0\\
 & x_{District 1,Shift 2} \geq 4.0\\
 & x_{District 1,Shift 3} \geq 3.0\\
 & x_{District 2,Shift 1} \geq 3.0\\
 & x_{District 2,Shift 2} \geq 6.0\\
 & x_{District 2,Shift 3} \geq 5.0\\
 & x_{District 3,Shift 1} \geq 5.0\\
 & x_{District 3,Shift 2} \geq 7.0\\
 & x_{District 3,Shift 3} \geq 6.0\\
 & x_{District 1,Shift 1} + x_{District 2,Shift 1} + x_{District 3,Shift 1} \geq 10.0\\
 & x_{District 1,Shift 2} + x_{District 2,Shift 2} + x_{District 3,Shift 2} \geq 20.0\\
 & x_{District 1,Shift 3} + x_{District 2,Shift 3} + x_{District 3,Shift 3} \geq 18.0\\
 & x_{District 1,Shift 1} + x_{District 1,Shift 2} + x_{District 1,Shift 3} \geq 10.0\\
 & x_{District 2,Shift 1} + x_{District 2,Shift 2} + x_{District 2,Shift 3} \geq 20.0\\
 & x_{District 3,Shift 1} + x_{District 3,Shift 2} + x_{District 3,Shift 3} \geq 13.0\\
 & x_{District 1,Shift 1} \leq 3.0\\
 & x_{District 1,Shift 2} \leq 7.0\\
 & x_{District 1,Shift 3} \leq 5.0\\
 & x_{District 2,Shift 1} \leq 5.0\\
 & x_{District 2,Shift 2} \leq 7.0\\
 & x_{District 2,Shift 3} \leq 10.0\\
 & x_{District 3,Shift 1} \leq 8.0\\
 & x_{District 3,Shift 2} \leq 12.0\\
 & x_{District 3,Shift 3} \leq 10.0\\
& \sum_{(d, s) : d, s \in \{1,2,3\} }{x_{d,s}} \geq 0.0 \\
& \sum_{(d, s) : d, s \in \{1,2,3\} }{x_{d,s}} \in \mathbb{Z} \\ 
\end{aligned} $$

Plan przydziału radiowozów dla każdej ze stref dl akażdej zmiany przedstawiony zosatł w tabelki poniżej.

|   	|   z1	|   z2	|   z3	|
|---	|---	|---	|---	|
|   p1	|   2	|   6	|   3	|
|   p2	|   3	|   7	|   10	|
|   p3	|   5	|   7	|   6	|

Plik wejściowy z danymi to `polizei.txt`

## 🖖 Zadanie 4

Pewna firma przeładunkowo posaida teren, na którym składuje kontenery z cennym ładunkiem. Teren podzielony jest na m x n kwadratów. Konterenty składowane są w wybranych kwadratach. Zakłada się, że kwadrat może być zajmowany przez co najwyżej jeden kontener. Frima musi rozmieścić kamery, żeby monitorować kontenery. Każda kamera może obserwować k kwadratów na lewo, k kwadratów na prawo, k kwadratów w góregę i k kwadratów w dół. Kamera nie może być umieszczona w kwadracie zajmowanym przez kontener.

Zaplanuj rozmieszczenie kamer w kwadratch tak, aby każdy kontener był monitorowany przez conajmniej jedną kamerę oraz liczba kamer była minimalna

$$ \begin{aligned}
\min\quad & x_{1,1} + x_{1,2} + x_{1,3} + x_{1,4} + x_{1,5} + x_{2,1} + x_{2,2} + x_{2,3} + x_{2,4} + x_{2,5} + x_{3,1} + x_{3,2} + x_{3,3} + x_{3,4} + x_{3,5} + x_{4,1} + x_{4,2} + x_{4,3} + x_{4,4} + x_{4,5} + x_{5,1} + x_{5,2} + x_{5,3} + x_{5,4} + x_{5,5} + x_{6,1} + x_{6,2} + x_{6,3} + x_{6,4} + x_{6,5}\\
\text{Subject to} \quad & x_{2,1} + x_{3,1} + x_{2,2} + 2 x_{3,2} + x_{4,2} + x_{1,3} + 2 x_{2,3} + 3 x_{3,3} + x_{4,3} + x_{3,4} + x_{1,5} + x_{2,5} + 2 x_{3,5} + x_{4,5} \geq 3.0\\
 & x_{1,1} + x_{2,1} + x_{3,1} + 14 x_{1,2} + x_{2,2} + x_{3,2} + x_{1,3} + x_{2,3} + x_{3,3} + x_{1,4} + x_{2,4} + x_{3,4} \geq 1.0\\
 & x_{1,2} + x_{2,2} + x_{3,2} + x_{4,2} + x_{1,3} + x_{2,3} + x_{3,3} + x_{4,3} + x_{1,4} + 10 x_{2,4} + x_{3,4} + x_{4,4} + x_{1,5} + x_{2,5} + x_{3,5} + x_{4,5} \geq 1.0\\
 & x_{1,2} + x_{2,2} + x_{3,2} + x_{1,3} + x_{2,3} + x_{3,3} + 14 x_{1,4} + x_{2,4} + x_{3,4} + x_{1,5} + x_{2,5} + x_{3,5} \geq 1.0\\
& \sum_{i,j : i \in \{ 1,...,n\} j \in \{ 1,...,m\} }{x_{i,j}} \geq 0.0 \\ 
& \sum_{i,j : i \in \{ 1,...,n\} j \in \{ 1,...,m\} }{x_{i,j}} \leq 1.0 \\ 
& \sum_{i,j : i \in \{ 1,...,n\} j \in \{ 1,...,m\} }{x_{i,j}} \in \mathbb{Z} \\
\end{aligned} $$

Plan rozkładu kamer

|   n\m	|   1	|   2	|   3	|   4	|   5	|
|---	|---	|---	|---	|---	|---	|
|   1	|   0	|   0	|   0	|   0	|   0	|
|   2	|   0	|   0	|   0	|   0	|   0	|
|   3	|   0	|   0	|   1	|   0	|   0	|
|   4	|   0	|   0	|   0	|   0	|   0	|
|   5	|   0	|   0	|   0	|   0	|   0	|
|   6	|   0	|   0	|   0	|   0	|   0	|

Plik wejściowy z danymi to `company.txt`