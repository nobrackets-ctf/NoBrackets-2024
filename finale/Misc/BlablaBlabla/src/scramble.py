from PIL import Image
import random

def scramble_image(image_path, output_path, grid_size=10):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Calculate size of each piece
    piece_width = width // grid_size
    piece_height = height // grid_size
    
    # Extract pieces and store in a list
    pieces = []
    for i in range(grid_size):
        for j in range(grid_size):
            box = (j * piece_width, i * piece_height, (j + 1) * piece_width, (i + 1) * piece_height)
            piece = img.crop(box)
            pieces.append(piece)
    
    # Shuffle the pieces
    random.shuffle(pieces)
    
    # Create a new blank image to paste the scrambled pieces
    scrambled_img = Image.new('RGB', (width, height))
    
    # Paste each piece back into the scrambled image
    index = 0
    for i in range(grid_size):
        for j in range(grid_size):
            scrambled_img.paste(pieces[index], (j * piece_width, i * piece_height))
            index += 1
    
    # Save the scrambled image
    scrambled_img.save(output_path)
    print(f"Scrambled image saved to {output_path}")

# Example usage
scramble_image('pole_excellence_cyber_logo.jpeg', 'pec_scrambled_image.jpg')

