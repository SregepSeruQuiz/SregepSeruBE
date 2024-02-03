import dotenv
import environ

dotenv.load_dotenv()


@environ.config(prefix="")  # type: ignore
class Config:
    """
    config utama
    """
    db: str = environ.var()
    secret: str = environ.var()
    forgot: str = environ.var()
    server: str = environ.var()


cfg: Config = environ.to_config(Config)

