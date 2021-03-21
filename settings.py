import os


def loadEnv(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise Exception(f"Missing environment variable: {key}")
    return val


def getConfig() -> dict:
    return {
        "offersUrl": loadEnv("OFFERS_URL"),
        "senderEmail": loadEnv("GMAIL_EMAIL"),
        "senderPassword": loadEnv("GMAIL_PASSWORD"),
        "receiverEmail": loadEnv("MAIL_RECEIVER")
    }
