import qrcode
import os

def generate_qr_code(url='https://www.linkedin.com/in/mo-edris', force=False):
  p = 'img/my_qr.png'
  if os.path.exists(p) and not force:
    print("Already exists")
    return p

  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )

  qr.add_data(url)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  img.save(p)
  return p

