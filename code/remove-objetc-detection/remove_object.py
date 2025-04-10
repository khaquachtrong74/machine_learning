from rembg import remove
from PIL import Image
input_path='./b.jpg'
output_path='./b.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
