# Lista 1

Lista ta to bardziej powtórzenie algorytmów grafowych z poprzedniego semestru z przedmiotu Alogrytmy i Struktury Danych. Dla listy należało przeprowadzić testy, jednak nie chciało mi się powielać pracy z poprzedniego semestru. Szczegółowe dane znajdziemy w repozytorium od przedmitou AiSD.

Wszytskie zaimplementowane algorytmy napisane sa w python 3.8.2

## Zadanie 1

Celem tego zadania było przypomnienie i implemetacja algorytmow grafowych DFS i BFS. Impelmentacja algorytmu znjaduje się w plikach `BFS.py` i `DFS.py` oraz korzysta z klas pomocniczych jak `Color.py` i `Graph.py`.

Program na wejściu przyjmuje:

- D lub U - informujący czy graf jest skierowany (D) czy też nieskierowany (U)
- liczbe wierzchołków n = |v|. Przyjałem, inaczej niż w poleceniu że wierzchołki są etykietowane kolejnymi liczbami naturalnymi ze zbioru {0....n-1}.
- liczba krawędzi m = |E|
- kolejno m definicji krawędzi postaci u v. (Odzielone spacją)

### Uruchominie 

W celu uruchomienia zadania pierwszego, należy w terminalu wpisać:

```
python3 zadanie1.py -d=True/False -t=True/False -f=file.txt
```

| Parament   |  Wartości |  Opis |
|:----|:-------------|:------|
| -d |  True lub False |  Graf skierowany czy nieskierowanych|
| -f |    nazwapliku.txt   |   Nazwa pliku w której podane są krawędzie |
| -t |  True lub False |    Drukowanie w terminalu krawędzie należących do drzewa |


## Zadanie 2

Do zaimplemetowania był algorytm sortowania topologicznego dla grafów skierowanych z ewentualnym wykrywaniem istnienia skierowanego cyklu. Algorytm na wyjściu zwraca listę wierzchołków w porządku topologicznym.

### Uruchomienie

W celu uruchomienia programu należy wpisać w linii komend:

```
python3 zadanie2.py -f=nazwapliku.txt
```

Plik na wyjściu wypisuje wierzchołi w topologicznym porządku i informację czy w grafie występuję cykl.

## Zadanie 3

W tym zadaniu, należało zaimplementować algorytm, do którego na wejściu podawaliśmy graf skierowany G = (V, E) i zwracał jego rozkład na silnie spójne składowe. Algorytm działa o czasie O(|V|+|E|).

### Uruchomienie 

W linii komend wpisujemy podobnie jak w potrzenim algorytmie:

```
python3 zadanie3.py -f=nazwapliku.txt
```

Program na wyjściu wypisuje jakie krawędzie należą do pierwszej silnie spójnej składowej, co jest jednoznczne aby stwierdzić jakie wierzchołki należą do niej. Plus jeżeli do silnej składowej jest wypisany wierzchołek, oznacza że jest on sam w sobie silnie spójną składową. Nie chciało mi się bawić w preety code, to tylko kwestia printowania.

## Zadanie 4 

Zaimplentowanie efektywnego algorytmu, który dla podanego na wejściu grafu G = (V, E) (skierowanego lub nieskierowanego, nie koniecznie spójnego) zwraca informace czy graf G jest grafem dwudzielnym i jeśli tak, zwraca rozbicie V na dwa podzbiory V_0 i V_1 takie, że jeśli (u, v) \in E, o u \in V_i i v \in V_{1-i} i \in {0,1}.

### Metoda rozwiązania

Na graf naleząło pokolorować, na dwa kolory. Idą od dowolnego wierzchołka, kolorując odwiedzone wierzchołki na przemiennie (Blue & Red). Jeżeli przeszliśmy cały graf i dowolne dwa połączone wierzchołki nie są pokolorowane tym samym kolorem.

### Uruchomienie

Program uruchamiamy w podobny sposób jak dwa poprzednie. 

```
python3 zadanie4.py -f=nazwapliku.txt
```

Na wyjściu wypisuje jedną z dwóch wartości. True jeżeli graf podany w pliku wejściowym jest grafem dwudzielnym. w przeciwnym przypadku wypisuje False. Ponadto gdy jest to graf dwudzielny, wypisuje rozbicie.

## Literatura

Wszystkie algorytmy implementowałem z notatek z poprzedniego semsetru na kursie Algorytmy i Struktury Danych oraz z ksiązki "Wprowadzenie do teorii grafów - "Cormen" w wersji angielskiej.