# Mr ProAL
# Indonesia Teror Family
#decompiled by Mr ProAL
import os, sys
print ('\x1b[1;32mGeus aya ID Jeung Password nya?')       
print ('\x1b[1;32mMangga Login ')
import os, sys

def wa():
    os.system('xdg-open https://wa.me/628558883118?text=%20Assalamualaikum%20Mr%20ProAL%20Yang%20gans%20,%20Boleh%20minta%20ID+PASS%20Sc%20Sms%20Gratis?')


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if sandi == '161616' and user == 'Mr.ProALGans':
    print ('ente geus Login')
    sys.exit
else:
    print ('Mampus Login GAGAL, Mangga hubungi ADMIN')
    wa()
    restart()
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')
	
from requests import Session
import re, sys
s = Session()

try:
	print("\n\n * SMS Gratis by Mr ProAL - Indonesia Teror Family\n * Gunakan kode negara elu bred(ex: 628xxxxx)\n")
	no = int(input(" Nomor ente : "))
	msg = input(" Pesannye bro : ")
except:
	print("\n\t* Cek nomer and pesan lu bred! *")
	sys.exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
    'Referer': 'http://sms.payuterus.biz/alpha/'
}

bypass = s.get("http://sms.payuterus.biz/alpha/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypass)[0]
jml = re.findall(r'<span>(.*?) = </span>', bypass)[0]
captcha = eval(jml.replace("x", "*").replace(":", "/"))

data = {
	'nohp':no,
	'pesan':msg,
	'captcha':captcha,
	'key':key	
}

send = s.post("http://sms.payuterus.biz/alpha/send.php", headers=headers, data=data).text

if 'SMS Gratis Telah Dikirim' in send:
	print(f"\n  [ Anjay Pengiriman sukses ]\n  [ {no} : {msg} ]\n")
elif 'MAAF....!' in send:
	print("\n  [ Mohon tunggu 15 menit untuk mengirim pesan yg sama ]\n")
else:
	print("\n  [ Pengiriman gagal ]\n")
