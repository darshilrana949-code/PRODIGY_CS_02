from PIL import Image

def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Encrypt pixel values
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print(f"Encrypted image saved as {output_image}")


def decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Decrypt pixel values
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print(f"Decrypted image saved as {output_image}")


# Main Program
print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter your choice (1/2): ")
key = int(input("Enter encryption key (0-255): "))

if choice == "1":
    input_file = input("Enter input image path: ")
    output_file = input("Enter encrypted image name: ")
    encrypt_image(input_file, output_file, key)

elif choice == "2":
    input_file = input("Enter encrypted image path: ")
    output_file = input("Enter decrypted image name: ")
    decrypt_image(input_file, output_file, key)

else:
    print("Invalid choice!")