"""
Convert PNG icon to ICO format for Windows executable
"""
from PIL import Image

# Open the PNG icon
img = Image.open('assets/icon.png')

# Convert to RGBA if not already
img = img.convert('RGBA')

# Save as ICO with multiple sizes (16x16, 32x32, 48x48, 64x64, 128x128, 256x256)
# Windows will use the appropriate size based on display context
img.save('assets/icon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])

print("✅ Successfully converted icon.png to icon.ico")
print("   Location: assets/icon.ico")
