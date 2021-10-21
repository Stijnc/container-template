import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    BACKGROUND_COLOR = os.getenv("BACKGROUND_COLOR") or "#1d1e20"
    COLOR = os.getenv("COLOR") or "#fff"
    NAME = os.getenv("NAME") or "there"
    TEXT = os.getenv("TEXT") or ""
    IMG_URI = (
        os.getenv("IMG_URI")
        or "https://raw.githubusercontent.com/Stijnc/Stijnc/main/img/profile_round.png"
    )
