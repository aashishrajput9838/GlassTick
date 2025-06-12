from PIL import Image, ImageDraw
import os

def create_clock_icon():
    # Create a new image with a transparent background
    size = 256
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw the clock circle
    margin = 10
    draw.ellipse([margin, margin, size-margin, size-margin], 
                 fill=(0, 120, 215, 255),  # Windows 8.1 blue
                 outline=(255, 255, 255, 255),
                 width=2)
    
    # Draw clock hands
    center = size // 2
    # Hour hand
    draw.line([center, center, center, center-60], 
             fill=(255, 255, 255, 255), width=4)
    # Minute hand
    draw.line([center, center, center+80, center], 
             fill=(255, 255, 255, 255), width=4)
    
    # Save as ICO
    image.save('clock.ico', format='ICO', sizes=[(256, 256)])

if __name__ == '__main__':
    create_clock_icon() 