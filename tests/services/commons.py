import os


def get_credentials():
    """
    Checks and returns if dependencies for running tests resolved or not

    :return: tuple(str,str)
    """
    access_token = os.getenv('FORTNOX_ACCESS_TOKEN')
    client_secret = os.getenv('FORTNOX_CLIENT_SECRET')
    if not access_token:
        raise ValueError("You must set `FORTNOX_ACCESS_TOKEN` environment variables")
    if not client_secret:
        raise ValueError("You must set `FORTNOX_CLIENT_SECRET` environment variables")
    return access_token, client_secret
