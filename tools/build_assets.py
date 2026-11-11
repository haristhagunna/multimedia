from PIL import Image, ImageDraw, ImageFont
import glob
bold = next(iter(glob.glob("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")), None)
reg = next(iter(glob.glob("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")), None)
W, H = 1200, 630
im = Image.new("RGB", (W, H)); d = ImageDraw.Draw(im)
for y in range(H):  # indigo -> violet gradient
    t = y / H; d.line([(0, y), (W, y)], fill=(int(49 + 60 * t), int(46 + 10 * t), int(129 + 50 * t)))
import math
for i in range(60):  # waveform motif
    x = 80 + i * 18; h = 20 + 50 * abs(math.sin(i / 4.5)) * (0.4 + 0.6 * abs(math.cos(i / 11)))
    d.rounded_rectangle([x, 500 - h, x + 9, 500 + h * 0.0 + 0], radius=4, fill=(255, 255, 255, 70) if False else (170, 175, 245))
F = lambda p, s: ImageFont.truetype(p, s)
d.text((80, 110), "BCA429CO", font=F(bold, 34), fill=(190, 195, 255))
d.text((80, 170), "Multimedia and", font=F(bold, 88), fill="white")
d.text((80, 270), "Application", font=F(bold, 88), fill="white")
d.text((80, 375), "Notes · Class slides · Labs · Mock exams", font=F(reg, 34), fill=(225, 228, 255))
d.text((80, 565), "Er. Harish Thagunna", font=F(bold, 30), fill="white")
im.save("docs/assets/og-image.png", optimize=True)
fav = Image.new("RGBA", (128, 128), (0, 0, 0, 0)); fd = ImageDraw.Draw(fav)
fd.rounded_rectangle([0, 0, 127, 127], radius=28, fill=(79, 70, 229))
for i, h in enumerate([30, 60, 90, 50, 74, 36]):
    fd.rounded_rectangle([14 + i * 18, 64 - h / 2, 24 + i * 18, 64 + h / 2], radius=5, fill="white")
fav.resize((64, 64), Image.LANCZOS).save("docs/assets/favicon.png")
print("assets ok")
