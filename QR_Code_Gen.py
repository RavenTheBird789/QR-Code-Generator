# QR Code Generator

def blue(text: str) -> str:
    """Returns the given text in blue color for terminal output."""
    return f"\033[94m{text}\033[0m"

def red(text: str) -> str:
    """Returns the given text in red color for terminal output."""
    return f"\033[91m{text}\033[0m"

def bold(text: str) -> str:
    """Returns the given text in bold for terminal output."""
    return f"\033[1m{text}\033[0m"

# Global Variables
equalSign = "="
emptySpace = " "

# Trademark Decorator
def trademark(QR_func):
    def wrapper():
        print(blue(equalSign * 20))
        print(blue(bold(f"{emptySpace}QR Code Generator")))
        print(blue(equalSign * 20))
        print(red("By: RavenTheBird789"))
        print(blue(equalSign * 20))
        QR_func()
    return wrapper

@trademark
def QR_Code():
    # Include QR code python library
    import qrcode

    # Create a QR code object with a larger size and higher error correction
    qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

    # Define the data to be encoded in the QR code
    data = input(blue("What would you like to turn into a QR code?: "))

    # Add the data to the QR code object
    qr.add_data(data)

    # Make the QR code
    qr.make(fit=True)

    # Create an image from the QR code with a yellow fill color and red background
    img = qr.make_image(fill_color="yellow", back_color="red")

    # Save the QR code image
    img.save("qr_code.png")
    print(blue("QR code saved as qr_code.png"))
QR_Code();
