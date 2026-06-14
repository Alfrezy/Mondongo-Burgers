import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

class CryptoService:
    @staticmethod
    def encrypt(plain_text: str, key_bytes: bytes) -> str:
        """Encripta texto plano usando AES-256 en modo CBC con un IV aleatorio."""
        # Generar un Vector de Inicialización (IV) de 16 bytes
        import os
        iv = os.urandom(16)
        
        # Preparar los datos con relleno PKCS7 para que su longitud sea múltiplo del bloque de AES
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text.encode('utf-8')) + padder.finalize()
        
        # Configurar y ejecutar el cifrado AES
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))
        encryptor = cipher.encryptor()
        encrypted_bytes = encryptor.update(padded_data) + encryptor.finalize()
        
        # Unir IV + Datos cifrados y codificar en Base64 para que sea un string transportable
        return base64.b64encode(iv + encrypted_bytes).decode('utf-8')

    @staticmethod
    def decrypt(cipher_text: str, key_bytes: bytes) -> str:
        """Desencripta un string en Base64 usando la clave AES de la imagen."""
        full_cipher = base64.b64decode(cipher_text.encode('utf-8'))
        
        # Extraer el IV y el cuerpo cifrado
        iv = full_cipher[:16]
        actual_cipher = full_cipher[16:]
        
        # Configurar y ejecutar el descifrado
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(actual_cipher) + decryptor.finalize()
        
        # Remover el relleno PKCS7 para recuperar el texto original
        unpadder = padding.PKCS7(128).unpadder()
        plain_bytes = unpadder.update(decrypted_padded) + unpadder.finalize()
        
        return plain_bytes.decode('utf-8')