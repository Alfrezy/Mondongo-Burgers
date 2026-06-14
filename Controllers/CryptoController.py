import os
import base64
from flask import Blueprint, Response
from .ImageKeyService import ImageKeyService
from .CryptoService import CryptoService

# Definimos un Blueprint para organizar la ruta en la app
test_crypto_bp = Blueprint('test_crypto', __name__)

@test_crypto_bp.route('/TestCrypto')
def index():
    try:
        # 1. Construir la ruta dinámica hacia la imagen de Reze
        # Modifica la ruta relativa si la carpeta de llaves cambia de lugar
        base_dir = os.getcwd()
        image_path = os.path.join(base_dir, "SegurityKey", "Key.jpg")
        
        # 2. Obtener los bytes de la llave
        key_bytes = ImageKeyService.get_key_from_image(image_path)
        
        # Convertir visualmente a Base64 para mostrar en pantalla
        key_base64_visual = base64.b64encode(key_bytes).decode('utf-8')
        
        # 3. Datos de prueba
        password_de_prueba = "OsirisGod123"
        
        # 4. Flujo completo
        encrypted = CryptoService.encrypt(password_de_prueba, key_bytes)
        decrypted = CryptoService.decrypt(encrypted, key_bytes)
        
        # 5. Respuesta como texto plano limpio idéntica al original
        output = (
            f"=== MONDONGO BURGERS CRYPTO TEST (PYTHON) ===\n\n"
            f"LLAVE DERIVADA DE LA IMAGEN (Base64):\n{key_base64_visual}\n\n"
            f"TEXTO ORIGINAL:\n{password_de_prueba}\n\n"
            f"TEXTO ENCRIPTADO (AES-256 + IV):\n{encrypted}\n\n"
            f"TEXTO DESENCRIPTADO:\n{decrypted}"
        )
        return Response(output, mimetype='text/plain')
        
    except Exception as e:
        return Response(f"❌ ERROR EN EL TEST: {str(e)}", mimetype='text/plain')