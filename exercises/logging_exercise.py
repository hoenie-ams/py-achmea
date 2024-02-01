from loguru import logger
import secrets

logger.warning("Program is for demo purposes only")


def main():
    """Run program to email a secret token"""
    token = generate_token()
    email_token(token)


def generate_token():
    """Return a token for password reset"""
    token = secrets.token_hex()
    return token


def email_token(token):
    """Email the token"""
    body = f"The token to reset your password: {token}"
    logger.debug(body)


if __name__ == "__main__":
    main()
