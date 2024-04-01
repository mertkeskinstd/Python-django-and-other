import qrcode

def url_to_qrcode(url, output_path):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the URL data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to the specified output path
    img.save(output_path)

if __name__ == "__main__":
    # Example usage
    website_url = "https://docs.google.com/presentation/d/1wODo2WboDaY3oetMb4M3-ot0PckWShIJ/edit?usp=sharing&ouid=103037143124182505812&rtpof=true&sd=true"
    output_qr_code_path = "C:\\Users\\tahak\\Desktop\\Yeni klasör (4)\\output_qr_code.png"

    url_to_qrcode(website_url, output_qr_code_path)

