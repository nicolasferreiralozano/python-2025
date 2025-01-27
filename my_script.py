import logging
from datetime import datetime, timezone

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def load_cert(pem_cert: bytes):
    """This explains how the function works, path "\\?\C:\hello\do".
    Is a path "\\?\"
    """
    if pem_cert is None:
        logging.error("pem_cert is None")
        raise ValueError("pem_cert cannot be None")
    else:
        cert: x509.Certificate = x509.load_pem_x509_certificate(pem_cert, default_backend())
        if datetime.now(timezone.utc) > cert.not_valid_after:
            logging.warning("Certificate has expired")
        else:
            logging.info("Certificate is valid")

if __name__ == "__main__":
    logging.info("Starting certificate validation")
    load_cert(None)
