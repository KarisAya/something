from PIL import Image
from io import BytesIO
from pathlib import Path
from pyzbar import pyzbar
import qrcode
import qrcode.image.svg


def decode_qr_code(image_path: str) -> bytes | None:
    # 使用 PIL 打开图像
    image = Image.open(image_path)
    # 使用 pyzbar 解码二维码
    decoded_objects = pyzbar.decode(image)
    if decoded_objects:
        return decoded_objects[0].data


data = decode_qr_code("qrcode_1676538742221.jpg")
assert data is not None

qr = qrcode.QRCode(border=2)
qr.add_data(data)

qr.make(fit=True)
# 生成 SVG 格式的二维码
image = BytesIO()
qr.make_image(image_factory=qrcode.image.svg.SvgImage).save(image)
# 保存为 SVG 文件
Path("qrcode.svg").write_bytes(image.getvalue())
