import os
import shutil
import qrcode

OUTPUT_FOLDER = ".png"

# Créer le dossier ou vider son contenu s'il existe déjà
if os.path.exists(OUTPUT_FOLDER):
    shutil.rmtree(OUTPUT_FOLDER)

os.makedirs(OUTPUT_FOLDER)

with open("meters.txt", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()

MAX_CHARS = 2000

chunk = []
current_size = 0
index = 1

for line in lines:
    line_size = len(line) + 1

    if current_size + line_size > MAX_CHARS:
        qr_content = "\n".join(chunk)

        img = qrcode.make(qr_content)
        img.save(os.path.join(OUTPUT_FOLDER, f"qr_{index}.png"))

        print(
            f"Generated qr_{index}.png "
            f"({len(chunk)} lines, {len(qr_content)} chars)"
        )

        index += 1
        chunk = []
        current_size = 0

    chunk.append(line)
    current_size += line_size

if chunk:
    qr_content = "\n".join(chunk)

    img = qrcode.make(qr_content)
    img.save(os.path.join(OUTPUT_FOLDER, f"qr_{index}.png"))

    print(
        f"Generated qr_{index}.png "
        f"({len(chunk)} lines, {len(qr_content)} chars)"
    )

print(f"\n{index} QR code(s) generated in folder: {OUTPUT_FOLDER}")