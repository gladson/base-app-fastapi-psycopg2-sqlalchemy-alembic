import hashlib


class GPass:
    @staticmethod
    def get_password_hash(password: str) -> str:
        """
        Retorna o hash MD5 da senha fornecida.

        Parameters:
            password (str): A senha a ser criptografada.

        Returns:
            str: O hash MD5 da senha.
        """
        # Converte a senha para bytes
        password_bytes = password.encode("utf-8")

        # Calcula o hash MD5 da senha
        password_hash = hashlib.md5(password_bytes).hexdigest()

        return password_hash

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verifica se a senha fornecida corresponde ao hash da senha.

        Parameters:
            plain_password (str): A senha em texto simples.
            hashed_password (str): O hash da senha.

        Returns:
            bool: True se a senha corresponder ao hash, False caso contrário.
        """
        # Gera o hash MD5 da senha fornecida
        plain_password_hash = GPass.get_password_hash(plain_password)

        # Compara os hashes
        return plain_password_hash == hashed_password


# Exemplo de uso:
# password = "minha_senha_secreta"
# hashed_password = GPass.get_password_hash(password)
# print("Hash MD5 da senha:", hashed_password)

# # Verificar senha
# plain_password = "minha_senha_secreta"
# if GPass.verify_password(plain_password, hashed_password):
#     print("Senha correta!")
# else:
#     print("Senha incorreta!")
