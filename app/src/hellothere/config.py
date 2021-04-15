import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    BACKGROUND_COLOR = os.getenv("BACKGROUND_COLOR") or "#1d1e20"
    COLOR = os.getenv("COLOR") or "#fff"
    NAME = os.getenv("NAME") or "there"
    IMG_URI = (
        os.getenv("IMG_URI")
        or "https://raw.githubusercontent.com/Stijnc/Stijnc/main/img/profile_round.png"
    )
    GIT_REPO = (
        os.getenv("GIT_REPO") or "https://github.com/Stijnc/container-template.git"
    )
    MAINTAINER = os.getenv("MAINTAINER") or "Stijn Callebaut"
    VERSION = os.getenv("VERSION") or "0.0.1"
    RELEASE_ID = os.getenv("RELEASE_ID") or ""
    DESCRIPTION = (
        os.getenv("DESCRIPTION")
        or "sample python hello world app developed by Stijn Callebaut"
    )
