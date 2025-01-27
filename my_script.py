from datetime import datetime, timezone
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def load_cert(pem_cert: bytes):
    """This explains how the function works, path "\\\\?\\C:\\hello\\do".
    Is a path "\\\\?\\"
    """
    if pem_cert is None:
        print("pem_cert is None")
    else:
        cert: x509.Certificate = x509.load_pem_x509_certificate(pem_cert, default_backend())
        if datetime.now(timezone.utc) > cert.not_valid_after:
            print("hello")
        else:
            print("goodbye")

if __name__ == "__main__":
    print("hello world!")
    load_cert(None)
