#Author HolyofMouse -- generate qr-code in image

import segno
from segno import helpers
import pathlib

path_to_dir='~/Pictures/QR'


class Qr_code():

    
# qr-code from text
    def create_word_in_qr(self):
        name_file = input("Write name file and extension(jpg, png, pdf, svg, eps): ")
        text = segno.make_qr(input("Write your text: "))
        full_file_path=pathlib.Path(path_to_dir).expanduser() / name_file
        text.save(str(full_file_path), scale=5)

# qr-code from url addres in Browser
    def create_url_in_qr(self):
        url_input = input("Write name file and extension(jpg, png, pdf, svg, eps): ")
        ulr_txt = segno.make_qr(input("Write URL address: "))
        full_file_path=pathlib.Path(path_to_dir).expanduser() / url_input
        ulr_txt.save(str(full_file_path), scale=5)

# qr-code from wifi configuration        
    def create_wifi_in_qr(self):
        wifi_conf = helpers.make_wifi(ssid='Virus_Baza', password=None, security=None, hidden=False)
        wifi_conf.save('wifi_conf.png', scale=5)


qrcode = Qr_code()
qrcode.create_wifi_in_qr()
