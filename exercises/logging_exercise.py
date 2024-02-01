import logging
import secrets

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    # filename="logging_exercise.log",
    # filemode="w"
)


def main():
    """Run program to email a secret token"""
    logging.info("Start program")
    token = generate_token()
    email_token(token)
    logging.info("End program")


def generate_token():
    """Return a token for password reset"""
    logging.info("Generating token")
    token = secrets.token_hex()
    logging.debug(f"Token: {token}")
    return token


def email_token(token):
    """Email the token"""
    logging.info("Emailing the token")
    body = f"The token to reset your password: {token}"
    logging.debug(body)


if __name__ == "__main__":
    main()
