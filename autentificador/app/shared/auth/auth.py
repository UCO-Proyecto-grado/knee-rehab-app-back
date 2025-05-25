import jwt

def decode_id_token(id_token: str):
    # Decodifica el id_token sin verificar firma para simplificar
    return jwt.decode(id_token, options={"verify_signature": False})
