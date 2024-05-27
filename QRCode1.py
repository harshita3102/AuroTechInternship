import qrcode
import matplotlib.pyplot as plt

def generate_and_show_qr(data):
    """
    Generate a QR code for the given data and display it on the screen.
    
    :param data: The data to encode in the QR code.
    """
    try:
        print(f"Generating QR code for: {data}")
        
        # Create QR code
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code, 1 is the smallest version.
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls the error correction used for the QR Code.
            box_size=10,  # Controls how many pixels each “box” of the QR code is.
            border=4,  # Controls how many boxes thick the border should be (the default is 4).
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill='black', back_color='white')

        # Convert the image to a format suitable for displaying with matplotlib
        img = img.convert("RGB")
        plt.imshow(img)
        plt.axis('off')  # Hide the axis
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\nQR Code Generator")
        print("1. Generate QR code for a URL")
        print("2. Generate QR code for text")
        print("3. Generate QR code for other information")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            url = input("Enter the URL: ")
            generate_and_show_qr(url)
        elif choice == '2':
            text = input("Enter the text: ")
            generate_and_show_qr(text)
        elif choice == '3':
            other_data = input("Enter the information: ")
            generate_and_show_qr(other_data)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

