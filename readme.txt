W pliku beatbox.py znajduje siê g³ówny program do tworzenia w³asnych kompozycji.
Aby stworzyæ swoj¹ w³asn¹ piosenkê musisz mieæ folder z plikami song.txt, 
track01.txt, ..., tracknm.txt, plik defs.txt oraz sample o nazwach sample01, ..., samplenm.
Folder z potrzebnymi plikami mo¿e byæ równie¿ "spakowany", czyli w formacie zip. 

Aby uruchomiæ program na podstawie katalogu nale¿y uruchomiæ nastêpuj¹c¹ komendê:
./beatbox.py nazwa_katalogu/
Natomiast aby uruchomiæ program dla spakowanego pliku:
./beatbox.py nazwa_pliku.zip

Program beatbox.py korzysta z dwóch modu³ów:
Modul1.py oraz Modul2.py.

W Module1 znajduj¹ siê funkcje:
reading - odczytuje s³ownik z pliku tekstowego,
lista_trackow - tworzy listê tracków na podstawie pliku song.txt,
lista_sampli - tworzy listê sampli i nutek na podstawie listy trackow.

W Module2 znajduj¹ siê:
s³ownik nuty,
tworz_nute - funkcja tworz¹ca falê sinusoidaln¹,
tworz_piosenke - funkcja tworzy wektor definiuj¹cy utwór,
zapisz - funkcja, która zapisuje wektor numeryczny do formatu .wav.