import RPi.GPIO as GPIO
import MFRC522
import signal
import pymysql

Host = "localhost"
User = "root"
Password = "Fokouong01"
database = "ogrenci_bilgi"
 
conn = pymysql.connect(host = Host , user = User , password = Password, db=database)
cur = conn.cursor()


continue_reading = True

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = format(i, '02X') + mystring
    return mystring

def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)

MIFAREReader = MFRC522.MFRC522()

print("Öğreci kartınız basın...")

while continue_reading:
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    if status == MIFAREReader.MI_OK:
        (status, uid) = MIFAREReader.MFRC522_SelectTagSN()
        if status == MIFAREReader.MI_OK:
            #ogrenci_kart_no = str(uidToString(uid))
            uid_str = ''.join(str(e) for e in uid)
            ogrenci_kart_no = int(uid_str)
            #print ("Card numarasi : " + " " + ogrenci_kart_numarasi)
            break
        else:
            print("Authentication error")
            


#burda aldığım bilgileri liste içersinde kaydetiyorum            
#ogrenci_bilgileri = [ogrenci_isim, ogrenci_soyismin, ogrenci_kimlik_no, ogrenci_sinif, ogrenci_kard_id]
#print("ogrenci_bilgileri : ")
#print(ogrenci_bilgileri)

#isim = input("isim girin : ")
#sinif = int(input("sinif girin : "))

query = f"INSERT INTO uid (uid_num) VALUES ('{ogrenci_kart_no}')" #SAVE DATA İN DATABASE
            
#query = f"INSERT INTO ogrenci_kayitlari (isim,soyisim,sinif,ogrenci_no,kart_no) VALUES ('{isim}','{sinif}')" #SAVE DATA İN DATABASE

#query = f"INSERT INTO ogrenci2 (isim ,sinif) SELECT isim,sinif FROM ogrenci1 WHERE sira_no ='2'" # TRANSFER DATA İN DATABASE

cur.execute(query)
print(f"{cur.rowcount} details insered")
conn.commit()
conn.close()

print("Kayitiniz Tamamlandi...")

'''
print("isim : " + " " + ogrenci_isim)
print("soyisim : " + " " + ogrenci_soyismin)
print("ogrenci no :" + " " + ogrenci_kimlik_no)
print("sinif :  " + " " + ogrenci_sinif)
print("ogrenci kard id : " + " " + ogrenci_kard_id )'''