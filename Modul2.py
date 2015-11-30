
nuty = {
    "--": "0",
    "F-2": "-28",
    "F#2": "-27",
    "G-2": "-26",
    "G#2": "-25",
    "A-2": "-24",
    "A#2": "-23",
    "B-2":"-22",
    "C-3": "-21",
    "C#3": "-20",
    "D-3": "-19",
    "D#3": "-18",
    "E-3": "-17",
    "F-3": "-16",
    "F#3": "-15",
    "G-3": "-14",
    "G#3": "-13",
    "A-3":"-12",
    "A#3":"-11",
    "B-3":"-10",
    "C-4": "-9",
    "C#4": "-8",
    "D-4": "-7",
    "D#4": "-6",
    "E-4": "-5",
    "F-4": "-4",
    "F#4": "-3",
    "G-4": "-2",
    "G#4": "-1",
    "A-4": "0",
    "A#4": "1",
    "B-4": "2",
    "C-5": "3",
    "C#5": "4",
    "D-5": "5",
    "D#5": "6",
    "E-5": "7",
    "F-5": "8",
    "F#5":"9",
    "G-5":"10",
    "G#5":"11",
    "A-5": "12",
    "A#5": "13",
    "B-5": "14",
    "C-6": "15",
    "C#6": "16",
    "D-6": "17",
    "D#6": "18",
    "E-6": "19",
    "F-6": "20",
    "F#6":"21",
    "G-6":"22",
    "G#6":"23"
    
}


def tworz_nute(nuta, bpm):
    import numpy as np
    if nuta=="--": 
        f = 0
        n = 0
    else: 
        f=440
        n = nuty[nuta] 
    fs=44100
    t = np.linspace(0, 60/bpm, 60/bpm*fs)
    z = 1.0594545454545454**int(n)
    y = np.sin(2*np.pi*f*t*z+0.1)
    return y
    
    
import scipy.signal
import scipy.io.wavfile
import numpy as np
def tworz_piosenke(bmp, lista_sampli2, sciezka):
    """
    Tworzy piosenkę na podstawie listy sampli i bpm.
    """
    piosenka=np.zeros(44100*(60/bmp)*len(lista_sampli2)/4)
    a = 44100*(60/bmp)
    for i in range(0, np.int(len(lista_sampli2)/4)):   
        if lista_sampli2[4*i] in nuty:
            y = tworz_nute(lista_sampli2[4*i], bmp)
        else:  
            fs1, y = scipy.io.wavfile.read(sciezka+'sample'+lista_sampli2[4*i]+'.wav')
            y = np.mean(y, axis=1)/32767
        if len(piosenka[i*a:])>len(y):
            y=np.append(y, np.zeros(len(piosenka[i*a:])-len(y)))
        if len(piosenka[i*a:])<len(y):
            y=y[0:len(piosenka[i*a:])]
        piosenka[i*a:]=piosenka[i*a:]+0.5*y
        if lista_sampli2[4*i+1] in nuty:
            y1=tworz_nute(lista_sampli2[4*i+1], bmp)
        else: 
            fs1, y1 = scipy.io.wavfile.read(sciezka+'sample'+lista_sampli2[4*i+1]+'.wav') 
            y1 = np.mean(y1, axis=1)/32767
        if len(piosenka[i*a:])>len(y1):
            y1=np.append(y1, np.zeros(len(piosenka[i*a:])-len(y1)))
        if len(piosenka[i*a:])<len(y1):
            y1=y1[0:len(piosenka[i*a:])]
        piosenka[i*a:]=piosenka[i*a:]+0.25*y1
        if lista_sampli2[4*i+2] in nuty:
            y2=tworz_nute(lista_sampli2[4*i+2], bmp)
        else: 
            fs2, y2 = scipy.io.wavfile.read(sciezka+'sample'+lista_sampli2[4*i+2]+'.wav') 
            y2 = np.mean(y2, axis=1)/32767
        if len(piosenka[i*a:])>len(y2):
            y2=np.append(y2, np.zeros(len(piosenka[i*a:])-len(y2)))
        if len(piosenka[i*a:])<len(y2):
            y2=y2[0:len(piosenka[i*a:])]
        piosenka[i*a:]=piosenka[i*a:]+0.125*y2
        
        if lista_sampli2[4*i+3] in nuty:
            y3=tworz_nute(lista_sampli2[4*i+3], bmp)
        else: 
            fs3, y3 = scipy.io.wavfile.read(sciezka+'sample'+lista_sampli2[4*i+3]+'.wav')
            y3 = np.mean(y3, axis=1)/32767
        if len(piosenka[i*a:])>len(y3):
            y3=np.append(y3, np.zeros(len(piosenka[i*a:])-len(y3)))
        if len(piosenka[i*a:])<len(y3):
            y3=y3[0:len(piosenka[i*a:])]
        piosenka[i*a:]=piosenka[i*a:]+0.125*y3
    return piosenka
    

    
    
def zapisz(piosenka, tytul):
    """
    Zapisuje wektor jako piosenkę.
    """
    import scipy.signal
    import scipy.io.wavfile
    import numpy as np
    scipy.io.wavfile.write('./'+tytul+'.wav',44100, np.int16(piosenka/max(np.abs(piosenka))*32767))
  
  

