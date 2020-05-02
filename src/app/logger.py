from logging.config import dictConfig

def configurar_logging():
    logging_configuracion = dict(
        version=1,
        disable_existing_loggers=False,
        formatters={
            "default": {"format": "%(levelname)s en %(module)s: %(message)s"},
        },
        handlers={
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            }
        },
        root={"handlers": ["console"], "level": "DEBUG"},
    )
    dictConfig(logging_configuracion)
