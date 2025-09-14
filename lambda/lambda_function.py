# lambda_function.py
import os
import time

from secrets_cache import get_secret, get_param


def handler(_event, _context):
    # Example usage
    secret_name = os.getenv('TEST_SECRET_NAME')
    param_name = os.getenv('TEST_PARAM_NAME')

    start = time.perf_counter()
    secret = get_secret(secret_name)
    elapsed_secret = time.perf_counter() - start
    print(f'Fetched secret in {round(elapsed_secret * 1000):.0f} ms')

    start = time.perf_counter()
    param = get_param(param_name)
    elapsed_param = time.perf_counter() - start
    print(f"Fetched parameter in {round(elapsed_param * 1000):.0f} ms")

    return {
        "secret": secret,
        "param": param,
        "timings": {
            "secret": elapsed_secret,
            "param": elapsed_param,
        }
    }
