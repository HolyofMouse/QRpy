#Author HolyofMouse -- generate qr-code in image

import segno
import pathlib

path_to_dir='~/Pictures/QR'


class Qr_code():

    

    def create_word_in_qr(self, text):
        self.text = text
        name_file = input("Write name file and extension(jpg, png, pdf, svg, eps): ")
        text = segno.make_qr(input())
        full_file_path=pathlib.Path(path_to_dir).expanduser() / name_file
        text.save(str(full_file_path), scale=5)

qrcode = Qr_code()
qrcode.create_word_in_qr('hello world')
