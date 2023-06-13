from dataclasses import dataclass, field
import io
import base64
import PIL.Image as Image


@dataclass(order=True)
class Imagem:
    id: int = field(default=0)
    imagem: bytearray = field(default=None)
    url: str = field(default="")
    altura: int = field(default=0)
    largura: int = field(default=0)

    def image_bytearray_to_encode64(self):
        return base64.b64encode(io.BytesIO(self.imagem).getvalue()).decode()

    def return_image_format(self):
        return Image.open(io.BytesIO(self.imagem)).format.lower()
