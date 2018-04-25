========================================================
Aleksander Puchalski - MongoDB Python Driver app
========================================================

Opis
-------

Dwa skrypty Pythonowe do agregacji ocen w recenzjach książek Amazon Kindle

Wymagnia
----------
- MongoDB uruchomione na domyślnych ustawieniach
- Python 2.7 z pakietem pymongo

Przygotowanie
---------------
Pobranie i wypakowanie paczki danych z Kaggle (plik ``kindle_reviews.json`` należy umieścić w folderze ``data``)

Nadanie praw do uruchomienia skryptów:
``chmod +x bin/*``

Uruchomić plik ``import.sh`` z folderu ``bin`` w celu zaimportowania danych:
``./import.sh``

W celu usunięcia dodanej kolekcji z bazy:
``python reset.py``

Średnia ocen danej pozycji
---------------------------
Skrypt ``aggregateScore.py`` pozwala na obliczenie średniej ocen ze wszystkich recenzji danej książki

``python aggregateScore.py``

Skrypt poprosi nas o ID książki (np. ``B000F83SZQ``) i zwróci nam średnią ocen z recenzji zawartych w bazie.

Pomocność recenzji użytkownika
-------------------------------
Kindle Store posiada system oceny recenzji użytkowników. Pozwala ocenić, czy dana recenzja była przydatna bądź nie. Skrypt ``scoreUseful.py`` zwraca nam ocenę przydatności recenzji danego użytkownika.

``python scoreUseful.py``

Skrypt poprosi o podanie ID użytkownika (np. ``A1F6404F1VG29J``) i zwróci nam procentową ocenę przydatności jego recenzji (liczba ocen pozytywnych podzielona przez ilość wszystkich ocen)


Czasy importów
---------------
Ilość rekordów: ``982619``


|                                                    | 
|----------------------------------------------------| 
| type,write_concern,user,sys,elapsed                | 
| standalone,"W:3, j:false",43.54,2.15,0:16.26       | 
| standalone,"W:3, j:false",43.59,2.12,0:16.16       | 
| standalone,"W:3, j:false",43.53,2.18,0:16.19       | 
| standalone,"W:3, j:false",43.53,2.26,0:16.38       | 
| standalone,"W:3, j:false",43.56,2.28,0:16.21       | 
| ,,l,,                                              | 
| local replica,"w: 1, j: false",43.00,2.13,0:22.40  | 
| local replica,"w: 1, j: false",42.53,2.07,0:21.01  | 
| local replica,"w: 1, j: false",42.43,2.12,0:21.50  | 
| local replica,"w: 1, j: false",42.53,2.07,0:21.01  | 
| local replica,"w: 1, j: false",42.44,1.98,0:21.05  | 
| ,,,,                                               | 
| local replica,"w: 1, j: true",42.43,2.27,0:23.20   | 
| local replica,"w: 1, j: true",42.54,2.01,0:21.23   | 
| local replica,"w: 1, j: true",42.67,1.95,0:21.30   | 
| local replica,"w: 1, j: true",42.47,2.30,0:22.33   | 
| local replica,"w: 1, j: true",42.83,2.06,0:21.79   | 
| ,,,,                                               | 
| local replica,"W: 2, j: false",42.43,2.12,0:21.50  | 
| local replica,"W: 2, j: false",42.50,2.06,0:21.22  | 
| local replica,"W: 2, j: false",42.47,2.30,0:22.33  | 
| local replica,"W: 2, j: false",42.83,2.06,0:21.79  | 
| local replica,"W: 2, j: false",43.54,2.15,0:16.26  | 
| ,,,,                                               | 
| local replica,"W: 2, j: true",42.83,2.06,0:21.79   | 
| local replica,"W: 2, j: true",42.54,2.01,0:21.23   | 
| local replica,"W: 2, j: true",42.43,2.12,0:21.50   | 
| local replica,"W: 2, j: true",42.53,2.07,0:21.01   | 
| local replica,"W: 2, j: true",42.44,1.98,0:21.05   | 
| ,,,,                                               | 
| local replica,"W:3, j:false",42.31,2.19,0:21.25    | 
| local replica,"W:3, j:false",42.50,2.03,0:22.60    | 
| local replica,"W:3, j:false",42.47,2.30,0:22.33    | 
| local replica,"W:3, j:false",43.53,2.18,0:16.19    | 
| local replica,"W:3, j:false",43.54,2.15,0:16.26    | 
| ,,,,                                               | 
| ,,,,                                               | 
| remote replica,"W:3, j:false",61.32,3.44,0:38.65   | 
| remote replica,"W:3, j:false",61.74,3.28,0:37.16   | 
| remote replica,"W:3, j:false",61.59,3.41,0:36.34   | 
| remote replica,"W:3, j:false",61.56,3.45,0:35.77   | 
| remote replica,"W:3, j:false",61.57,3.30,0:38.07   | 
| ,,,,                                               | 
| remote replica,"w: 1, j: false",60.92,3.24,0:36.01 | 
| remote replica,"w: 1, j: false",58.52,3.23,0:34.72 | 
| remote replica,"w: 1, j: false",61.40,3.32,0:35.58 | 
| remote replica,"w: 1, j: false",61.57,3.30,0:38.07 | 
| remote replica,"w: 1, j: false",61.32,3.44,0:38.65 | 
| ,,,,                                               | 
| remote replica,"w: 1, j: true",61.67,3.33,0:36.79  | 
| remote replica,"w: 1, j: true",61.57,3.30,0:38.07  | 
| remote replica,"w: 1, j: true",54.26,3.07,0:38.54  | 
| remote replica,"w: 1, j: true",61.56,3.45,0:35.77  | 
| remote replica,"w: 1, j: true",61.32,3.44,0:38.65  | 
| ,,,,                                               | 
| remote replica,"W: 2, j: false",61.38,3.32,0:36.07 | 
| remote replica,"W: 2, j: false",61.56,3.45,0:35.77 | 
| remote replica,"W: 2, j: false",61.62,3.47,0:35.69 | 
| remote replica,"W: 2, j: false",61.57,3.30,0:38.07 | 
| remote replica,"W: 2, j: false",61.32,3.44,0:38.65 | 
| ,,,,                                               | 
| remote replica,"W: 2, j: true",61.67,3.33,0:36.79  | 
| remote replica,"W: 2, j: true",61.32,3.44,0:38.65  | 
| remote replica,"W: 2, j: true",61.62,3.47,0:35.69  | 
| remote replica,"W: 2, j: true",61.56,3.45,0:35.77  | 
| remote replica,"W: 2, j: true",61.57,3.30,0:38.07  | 



Git sizer output
-------------------
Processing blobs: 10                        
Processing trees: 12                        
Processing commits: 9                        
Matching commits to trees: 9                        
Processing annotated tags: 0                        
Processing references: 2                        
| Name                         | Value     | Level of concern               |
| ---------------------------- | --------- | ------------------------------ |
| Overall repository size      |           |                                |
| * Commits                    |           |                                |
|   * Count                    |     9     |                                |
|   * Total size               |  2.29 KiB |                                |
| * Trees                      |           |                                |
|   * Count                    |    12     |                                |
|   * Total size               |  1021 B   |                                |
|   * Total tree entries       |    28     |                                |
| * Blobs                      |           |                                |
|   * Count                    |    10     |                                |
|   * Total size               |  11.5 KiB |                                |
| * Annotated tags             |           |                                |
|   * Count                    |     0     |                                |
| * References                 |           |                                |
|   * Count                    |     2     |                                |
|                              |           |                                |
| Biggest objects              |           |                                |
| * Commits                    |           |                                |
|   * Maximum size         [1] |   283 B   |                                |
|   * Maximum parents      [2] |     1     |                                |
| * Trees                      |           |                                |
|   * Maximum entries      [3] |     4     |                                |
| * Blobs                      |           |                                |
|   * Maximum size         [4] |  5.30 KiB |                                |
|                              |           |                                |
| History structure            |           |                                |
| * Maximum history depth      |     9     |                                |
| * Maximum tag depth          |     0     |                                |
|                              |           |                                |
| Biggest checkouts            |           |                                |
| * Number of directories  [5] |     3     |                                |
| * Maximum path depth     [5] |     2     |                                |
| * Maximum path length    [5] |    21 B   |                                |
| * Number of files        [5] |     6     |                                |
| * Total size of files    [5] |  6.44 KiB |                                |
| * Number of symlinks         |     0     |                                |
| * Number of submodules       |     0     |                                |

[1]  197f8890cb2129df534e4b32bcf5fc15a299bc21
[2]  bddfce471b6294a0c14c290cf84e0c50afebc20c (refs/heads/master)
[3]  13104e91737f1959e94972ed4f8dbb43da4dd2b4 (refs/heads/master:bin)
[4]  80715ca46028f07cdc39710f38b8179876fee304 (refs/heads/master:README.md)
[5]  05c0815ec155f76b8d13337ee87e8ba22d06474e (refs/heads/master^{tree})

