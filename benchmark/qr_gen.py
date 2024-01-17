import qrcode

github_url = 'https://github.com/Secreez/DS_Pitch_Project'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(github_url)
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="transparent")

img.save("repo_qrcode.png")