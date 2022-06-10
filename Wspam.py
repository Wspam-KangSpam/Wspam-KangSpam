GNU nano 6.3                              Wspam-KangSpam.py
import requests, os

url_api_Wspam_brutall = "https://aink-sanz.herokuapp.com/api/free-tutorial-spam-wa"

os.system("clear")
os.system("figlet Wspam-brutall")
print("[-] Creator : Whyu KangSpam")
print("[-] Instagram : Dwcillboyz_")
nomor = input("\n[?] Input Nomor : ")
jumlah = input("[?] Input Jumlah : ")
print()
data = {
"nomor": nomor
}
for Whyu_KangSpam in range(int(jumlah)):
        Wspam = requests.get(url_api_Wspam_brutall, params=data)
        if "Berhasil cok spamnya!!" in Wspam.text:
                print("[!] Gagal asuu")
        else:
                print("[+] Berhasil yahaha wahyuu")