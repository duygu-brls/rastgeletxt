from random import randint as rastgeleSayi
import os
from datetime import datetime
dosyaAdres = "C:\\TEST\\"
if (not os.path.exists(dosyaAdres)):
    os.mkdir(dosyaAdres)

dosyaAdres = dosyaAdres + "rastgele.txt"
dosya = open(dosyaAdres, "w+")

dosya.write( "\t"+ "Zaman" + "\t"+ "\t"+ "   "+"OlaySırası" + "\t" + "   " +"RastgeleSayı" + "\n")
sayi_adedi=0
for i in range(10):
    sayi_adedi+=1
    zaman = datetime.now()
    dosya.write(str(zaman.strftime("%Y.%m.%d %H:%M:%S")) + "\t" + "\t" + str(sayi_adedi) + "\t" + "\t" + str(rastgeleSayi(1, 100)) + "\n")
dosya.close()
