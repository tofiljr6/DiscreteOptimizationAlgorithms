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

Funkcja minimalizującą dla danych z zadania to: 10 x[A1,C1] + 7 x[A1,C2] + 8 x[A1,C3] + 10 x[A2,C1] + 11 x[A2,C2] + 14 x[A2,C3] + 9 x[A3,C1] + 12 x[A3,C2] + 4 x[A3,C3] + 11 x[A4,C1] + 13 x[A4,C2] + 9 x[A4,C3]

Warunki (Subject to) z pominięciem warunków banalncyh tj. większych od zera:

x[A1,C1] + x[A1,C2] + x[A1,C3] = 110000.0
 x[A2,C1] + x[A2,C2] + x[A2,C3] = 220000.0
 x[A3,C1] + x[A3,C2] + x[A3,C3] = 330000.0
 x[A4,C1] + x[A4,C2] + x[A4,C3] = 440000.0
 x[BIN,C1] + x[BIN,C2] + x[BIN,C3] = 385000.0
 x[A1,C1] + x[A2,C1] + x[A3,C1] + x[A4,C1] + x[BIN,C1] = 275000.0
 x[A1,C2] + x[A2,C2] + x[A3,C2] + x[A4,C2] + x[BIN,C2] = 550000.0
 x[A1,C3] + x[A2,C3] + x[A3,C3] + x[A4,C3] + x[BIN,C3] = 660000.0

 Plan zakupowy dostaw paliwa na lotniska, który minimalizuje koszty, przestawiłem w tabeli poniżej.

 |   Lotnisko \ Firma	|   Firma 1	|   Firma 2	|   Firma 3	|
|---	|---	|---	|---	|
|   Lotnisko 1	|   0	|   110000.0 	|   0	|
|   Lotnisko 2	|   165000	|   55000.0	|   0	|
|   Lotnisko 3	|   0	|   0	|   330000.0	|
|   Lotnisko 4	|   110000.0	|   0	|   330000.0	|