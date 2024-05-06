import os

API_KEY: str = os.getenv("API_KEY")
PRICE_GTE: float = os.getenv("PRICE_GTE", 68000.0)
PRICE_LTE: float = os.getenv("PRICE_LTE", 62500.0)
ALERT_TIMES: int = os.getenv("ALERT_TIMES", 100)