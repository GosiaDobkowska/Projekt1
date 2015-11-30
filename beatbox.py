
import sys

total = len(sys.argv)
cmdargs = str(sys.argv)

if len(sys.argv) != 2:
    print('Nie podano wszystkich argumentow!')
    sys.exit(1)

import Modul1 as m1
import Modul2 as m2

import zipfile
if zipfile.is_zipfile('./'+sys.argv[1]):
    with zipfile.ZipFile('./'+sys.argv[1], "r") as z:
        z.extractall('/tmp/')
    
    tempo = m1.reading('/tmp/'+sys.argv[1][0:len(sys.argv[1])-4]+'/defs.txt')
    bpm = tempo.get("bpm")
    lt = m1.lista_trackow('/tmp/'+sys.argv[1][0:len(sys.argv[1])-4]+'/song.txt', '/tmp/'+sys.argv[1][0:len(sys.argv[1])-4]+'/')
    ls = m1.lista_sampli(lt)
    p = m2.tworz_piosenke(bpm, ls, '/tmp/'+sys.argv[1][0:len(sys.argv[1])-4]+'/' )
    
    m2.zapisz(p, sys.argv[1][0:len(sys.argv[1])-4])

else:   
    tempo = m1.reading('./'+sys.argv[1]+'defs.txt')
    bpm = tempo.get("bpm")
    lt = m1.lista_trackow('./'+sys.argv[1]+'song.txt', './'+sys.argv[1])
    ls = m1.lista_sampli(lt)
    p = m2.tworz_piosenke(bpm, ls, './'+sys.argv[1]+'/')
    m2.zapisz(p, sys.argv[1][0:len(sys.argv[1])-1])
