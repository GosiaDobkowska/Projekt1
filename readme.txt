W pliku beatbox.py znajduje si� g��wny program do tworzenia w�asnych kompozycji.
Aby stworzy� swoj� w�asn� piosenk� musisz mie� folder z plikami song.txt, 
track01.txt, ..., tracknm.txt, plik defs.txt oraz sample o nazwach sample01, ..., samplenm.
Folder z potrzebnymi plikami mo�e by� r�wnie� "spakowany", czyli w formacie zip. 

Aby uruchomi� program na podstawie katalogu nale�y uruchomi� nast�puj�c� komend�:
./beatbox.py nazwa_katalogu/
Natomiast aby uruchomi� program dla spakowanego pliku:
./beatbox.py nazwa_pliku.zip

Program beatbox.py korzysta z dw�ch modu��w:
Modul1.py oraz Modul2.py.

W Module1 znajduj� si� funkcje:
reading - odczytuje s�ownik z pliku tekstowego,
lista_trackow - tworzy list� track�w na podstawie pliku song.txt,
lista_sampli - tworzy list� sampli i nutek na podstawie listy trackow.

W Module2 znajduj� si�:
s�ownik nuty,
tworz_nute - funkcja tworz�ca fal� sinusoidaln�,
tworz_piosenke - funkcja tworzy wektor definiuj�cy utw�r,
zapisz - funkcja, kt�ra zapisuje wektor numeryczny do formatu .wav.