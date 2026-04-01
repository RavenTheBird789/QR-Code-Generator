# QR Code Generator

# Include QR code python library
import qrcode # type: ignore

# Create a QR code object with a larger size and higher error correction
qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

# Define the data to be encoded in the QR code
data = input("What would you like to turn into a QR code?: ")

# Add the data to the QR code object
qr.add_data(data)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code with a black fill color and white background
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("qr_code.png")