#Author HolyofMouse -- generate qr-code in image

def printing():
    print("┌────────────────────────────────┐ ")
    print("│                                │ ")
    print("│ QQQQQ  RRRRRR                  │ ")
    print("│QQ   QQ RR  RR  pp pp   yy   yy │ ")
    print("│QQ   QQ RRRRRR  ppp  pp yy   yy │ ")
    print("│QQ  QQ  RR  RR  pppppp   yyyyyy │ ")
    print("│QQQQ Q  RR   RR pp           yy │ ")
    print("│                pp       yyyyy  │ ")
    print("└────────────────────────────────┘ ")

        
printing()

import segno
from segno import helpers
import pathlib

path_to_dir='~/Pictures/QR/'


class Qr_code():

# qr-code from text
    def create_word_in_qr(self):
        name_file = input("Write name file and extension(png, pdf, svg, eps): ")
        text = segno.make_qr(input("Write your text: "))
        full_file_path=pathlib.Path(path_to_dir).expanduser() / name_file
        text.save(str(full_file_path), scale=5)

# qr-code from url addres in Browser
    def create_url_in_qr(self):
        url_input = input("Write name file and extension(png, pdf, svg, eps): ")
        ulr_txt = segno.make_qr(input("Write URL address: "))
        full_file_path=pathlib.Path(path_to_dir).expanduser() / url_input
        ulr_txt.save(str(full_file_path), scale=5)

# qr-code from wifi configuration        
    def create_wifi_in_qr(self):
        wifi_conf = helpers.make_wifi(ssid='Virus_Baza', password=None, security=None, hidden=False)
        wifi_conf_name = input("Write name file and extension(png, pdf, svg, eps): ")
        full_file_path=pathlib.Path(path_to_dir).expanduser() / wifi_conf_name 
        wifi_conf.save(str(full_file_path), scale=5)



# Start class
qrcode = Qr_code()
choice_qr = str(input("choice param(wifi, word, url): "))

# choice param
def case_choice(choice_qr):
    match choice_qr:
        case "word":
            qrcode.create_word_in_qr()
        case "wifi":
            qrcode.create_wifi_in_qr()
        case "url":
            qrcode.create_url_in_qr()
        case _:
            return "your write wrong param"
# input validation
if choice_qr == "word":
    print(case_choice("word"))
elif choice_qr == "wifi":
    print(case_choice("wifi"))
elif choice_qr == "url":
    print(case_choice("url"))



