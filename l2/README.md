# Lista 2 鉁忥笍

## 馃憜 Zadanie 0 (przyk艂ad w wyk艂adu)

Producent czekolady produkuje 2 rodzaje czekolad: mleczn膮 i luksusow膮.

Zysk: 1 tablicza mlecznej (M) kosztuje 1 z艂, a 1 tabliczna luksusowej (L) kosztuje 6 z艂. Dzienne mo偶liwo艣ci produkcji to 400 tabliczek. Dzienny popyt to 200 tabliczek mlecznej, 300 tabliczek luksusowej.

Jaki jest optymalny poziom produkcji, maksymalizacja zysku.

## 馃憜 Zadanie 1 

Pewne przedsi臋biorstwo otnicze musi podj膮膰 decyzj臋 o zakupie paliwa do samolot贸w odrzutowych, maj膮c do wyboru trzech dostawc贸w. Samoloty tankuj膮 paliwo regularnie na czterech lotniskach, kt贸re obs艂uguj膮.

Firmy paliwowe poinformowa艂y, 偶e mog膮 dostarczy膰 nast臋puj膮ce ilo艣ci paliwa w nadchodz膮cym miesi膮cu; Firma 1 - 275 000 galon贸w, Firma 2 - 550 000 galon贸w i Frima 3 - 660 000 galon贸w. Niezb臋dne ilo艣ci paliwa do odrzutowc贸w na poszczeg贸lnych lotniskach s膮 odpwiednio r贸wne: na lotnisku 1 - 110 000 galon贸w, na lotnisku 2 - 220 000 galon贸w, na lotniksu 3 - 330 000 galon贸w i na lotniusku 4 - 440 000 galon贸w. Koszt galonu paliwa z uwzgl臋dnieniem koszt贸w transportu dostarczonego przez poszczeg贸lnych dostawc贸w kszta艂tuj臋 si臋 na ka偶dym lotnisku nast臋puj膮co:

|   	|   Firma 1	|   Firma 2	|   Firma 3	|
|---	|---	|---	|---	|
|   Lotnisko 1	|   10	|   7 	|   8	|
|   Lotnisko 2	|   10	|   11	|   14	|
|   Lotnisko 3	|   9	|   12	|   4	|
|   Lotnisko 4	|   11	|   13	|   9	|

Wyznacz plan zakupu i dostaw paliwa na lotniska, kt贸ry minimalizuje koszty.

Czy wszystkie firmy dostarczaj膮 paliwo?

Czy mo偶liwo艣ci dostaw paliwa przez firmy s膮 wyczerpane?

## Rozwi膮zanie zadania 1

Zadanie zosta艂o maksymalnie sparametryzowane. W pliku w pierwszej linijce podajemy ilo艣膰 lotnisk i ilo艣膰 firm dostraczaj膮cych paliwo, oddzielone 艣rednikiem. W kolejnej linijce podajemy r贸wnie偶 po 艣redniku ile s膮 w stanie dostawcy dostarczy膰 paliwa w danym miesi膮cu. Nast臋pnej linijce podajemy zapotrzebowanie na ka偶dym z lotnisk. Potem podajemy w len(lotniskach), len(firmy) koszty transportu jedengo galonu paliwa. Przykadowy plik, z rozwi膮zaniem tego zadania z powy偶ej opisanymi danymi znajduj臋 si臋 w pliku ```model.txt```

Funckja minimalizuj膮ca i warunki ograniczaj膮ce dla danych z zadania to:

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

 Plan zakupowy dostaw paliwa na lotniska, kt贸ry minimalizuje koszty, przestawi艂em w tabeli poni偶ej.

 |   Lotnisko \ Firma	|   Firma 1	|   Firma 2	|   Firma 3	|
|---	|---	|---	|---	|
|   Lotnisko 1	|   0	|   110000.0 	|   0	|
|   Lotnisko 2	|   165000	|   55000.0	|   0	|
|   Lotnisko 3	|   0	|   0	|   330000.0	|
|   Lotnisko 4	|   110000.0	|   0	|   330000.0	|


## 鉁岋笍 Zadanie 2

Dana jest sie膰 po艂膮cze艅 mi臋dzy `n` miastami reprezentowana za pomoc膮 skierowanego grafu G = (N, A) gdzie N jest zbiorem miast (wierzcho艂k贸w), |N| = n jest zbiorem po艂膮cze艅 mi臋dzy miastami (艂uk贸w), |A| = m. Dla ka偶dego po艂膮czenia z miasta `i` do miasta `j` $(i, j) \in A$ dane s膮 koszty przejazdu $c_{ij}$ oraz czas przejazdu $t_{ij}$ (im mniejszy koszt, tym d艂u偶szy czas przejazdu). Dane s膮 r贸wnie偶 dwa miasta $i^*, j^* \in N$

Celem jest znalezienie po艂膮czenia (艣cie偶ki) mi臋dzy zadanymi dwoma miastami, kt贸rego ca艂kowity koszt jest najmniejszy i ca艂kowity czas przejazdu nie przekracza z g贸ry zdanego czsu przejazdu T.

Funckja minimalizuj膮ca i warunki ograniczaj膮ce dla danych z zadania to:

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

Plan przej艣cia z wierzcho艂ka 1 do wierzcho艂ka 3 o najmnijesyzm koszcie i ca艂kowity czas przejazdu nie przekracza zadanego czasu przejazdu T = 20. 

|   	|   1	|   2	|   3	|   4	|   5	|
|---	|---	|---	|---	|---	|---	|
|   1	|   0	|   0	|   0	|   1	|   0	|
|   2	|   0	|   0	|   0	|   0	|   0	|
|   3	|   0	|   0	|   0	|   0	|   0	|
|   4	|   0	|   0	|   0	|   0	|   1	|
|   5	|   0	|   0	|   1	|   0	|   0	|

Pliki wej艣ciowy z danymi to: `graph.txt` oraz `graph2.txt`

### Przyk艂ad 

![alt text for screen readers](/l2/png/2.png)

Jak widzimy na za艂膮czonym przyk艂adzie, najkr贸tsza 艣cie偶ka w tym grafie z pomini臋ciem czasu to 1 -> 2 -> 3. Jedank gdy na艂o偶ymy ograniczenie na czas (W tym przyk艂adzie wynosi 20), to najktr贸tsza 艣cie偶ka r贸偶ni si臋 od pierwotnej, i wygl膮da nast臋puj膮co 1 -> 4 -> 5 -> 3.

## 馃 Zadanie 3

Policja w ma艂ym miasteczku posiada w swoim zasi臋gu trzy dzielnnice oznaczone jako $p_1, p_2, p_3$. Ka偶da dzielnica ma przypisan膮 pewn膮 liczb臋 radiowoz贸w wyposa偶onych w radiotelefony i sprz臋t pierwszej pomocy. Policja pracuje w systemie trzyzmianowym. W tabelki poni偶ej podan臋 s膮 minimalne i maksymalne liczby radiowoz贸w dla ka偶dej zmiany i dzielnicy odziellone znkaiem "/"

|   	|   z1	|   z2	|   z3	|
|---	|---	|---	|---	|
|   p1	|   2/3	|   4/7	|   3/5	|
|   p2	|   3/5	|   6/7	|   5/10	|
|   p3	|   5/8	|   7/12	|   6/10	|

Ponadto aktualne przepisy wymuszaj膮, 偶e dla zmiany 1,2,3 powinno by膰 dost臋pnych odpowiednio, co najmniej 10, 20, 18 radiowoz贸w. Ponadto dzielnice $p_1, p_2, p_3$ powinny mie膰 przypisane, odpowiednio co najmniej 10, 20, 13 radiowoz贸w. Polica chce wyznaczy膰 przydzia艂 radiowoz贸w spe艂niaj膮cy powy偶sze wymagania  i minimalizuj膮c ich ca艂kowit膮 liczb臋. Sformu艂uj ten problem jako problem cyrkulacji.

Powy偶szy model prezentuje si臋 nast臋puj膮co:

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

Plan przydzia艂u radiowoz贸w dla ka偶dej ze stref dl aka偶dej zmiany przedstawiony zosat艂 w tabelki poni偶ej.

|   	|   z1	|   z2	|   z3	|
|---	|---	|---	|---	|
|   p1	|   2	|   6	|   3	|
|   p2	|   3	|   7	|   10	|
|   p3	|   5	|   7	|   6	|

Plik wej艣ciowy z danymi to `polizei.txt`

## 馃枛 Zadanie 4

Pewna firma prze艂adunkowo posaida teren, na kt贸rym sk艂aduje kontenery z cennym 艂adunkiem. Teren podzielony jest na m x n kwadrat贸w. Konterenty sk艂adowane s膮 w wybranych kwadratach. Zak艂ada si臋, 偶e kwadrat mo偶e by膰 zajmowany przez co najwy偶ej jeden kontener. Frima musi rozmie艣ci膰 kamery, 偶eby monitorowa膰 kontenery. Ka偶da kamera mo偶e obserwowa膰 k kwadrat贸w na lewo, k kwadrat贸w na prawo, k kwadrat贸w w g贸reg臋 i k kwadrat贸w w d贸艂. Kamera nie mo偶e by膰 umieszczona w kwadracie zajmowanym przez kontener.

Zaplanuj rozmieszczenie kamer w kwadratch tak, aby ka偶dy kontener by艂 monitorowany przez conajmniej jedn膮 kamer臋 oraz liczba kamer by艂a minimalna

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

Plan rozk艂adu kamer

|   n\m	|   1	|   2	|   3	|   4	|   5	|
|---	|---	|---	|---	|---	|---	|
|   1	|   0	|   0	|   0	|   0	|   0	|
|   2	|   0	|   0	|   0	|   0	|   0	|
|   3	|   0	|   0	|   1	|   0	|   0	|
|   4	|   0	|   0	|   0	|   0	|   0	|
|   5	|   0	|   0	|   0	|   0	|   0	|
|   6	|   0	|   0	|   0	|   0	|   0	|

Plik wej艣ciowy z danymi to `company.txt`