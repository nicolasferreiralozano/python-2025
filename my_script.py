import logging
from datetime import datetime, timezone

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def load_cert(pem_cert: bytes) -> x509.Certificate:
    """Load and validate an x509 certificate from PEM-encoded bytes.
    Args:
        pem_cert: PEM-encoded certificate bytes

    Returns:
        x509.Certificate: The loaded certificate object

    Raises:
        ValueError: If pem_cert is None
    """
    if pem_cert is None:
        logging.error("pem_cert is None")
        raise ValueError("pem_cert cannot be None")
    else:
        cert: x509.Certificate = x509.load_pem_x509_certificate(pem_cert, default_backend())
        expiry_time = cert.not_valid_after_utc
        current_time = datetime.now(timezone.utc)
        if current_time > expiry_time:
            logging.warning(f"Certificate has expired (expired at {expiry_time}, current time is {current_time})")
        else:
            logging.info(f"Certificate is valid until {expiry_time}")

if __name__ == "__main__":
    logging.info("Starting certificate validation")
    load_cert(None)
