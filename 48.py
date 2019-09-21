# Mr ProAL
# Indonesia Teror Family
from requests import Session
import re, sys
s = Session()
try:
	print("\n\n \033[91m      ┌┬┐┌─┐ ┌─┐┌─┐┌─┐ ┌─┐┬\n      │││|   ├─┘|  | | ├─┤│  \n      ┴ ┴┴   ┴  ┴  └─┘ ┴ ┴┴─┘\n   From Indonesia Teror Family\n")
	print("\n\n \033[92m * SMS Gratis by Mr ProAL - Indonesia Teror Family\n * Gunakan kode negara elu bred(ex: 628xxxxx)\n")
	no = int(input(" Nomor target : "))
	msg = input(" Pesannye bro : ")
except:
	print("\n\t* ada kesalahan! cek nomornya bred! *")
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
	print("\n  [Santuy tunggu 15 menit untuk mengirim pesan yg sama ]\n")
else:
	print("\n  [ mampus Pengiriman gagal ]\n")
