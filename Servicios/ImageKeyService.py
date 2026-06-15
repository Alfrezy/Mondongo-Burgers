import os
import hashlib

class ImageKeyService:
    @staticmethod
    def get_key_from_image(image_path: str) -> bytes:
        """
        Lee los bytes crudos de la imagen (ej: Key.jpg) y genera un 
        hash SHA-256 estandarizado de 32 bytes para usar con AES.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"No se encontró la imagen llave en la ruta: {image_path}")
            
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()
            
        # Retorna el hash crudo de 32 bytes generado a partir de la imagen
        return hashlib.sha256(image_bytes).digest()