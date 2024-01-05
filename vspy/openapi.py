import logging
import pathlib

from fastapi.openapi.utils import get_openapi

from vspy.app import app


def main():
    # Generate and print the OpenAPI schema
    openapi_schema = get_openapi(title="verbose-sniffle-py", version="1.0.0", routes=app.routes)
    pathlib.Path("openapi.json").open("wt").write(str(openapi_schema))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logging.exception(err)
