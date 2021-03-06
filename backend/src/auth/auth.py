import json
from flask import request, _request_ctx_stack, abort
from functools import wraps
from flask.json import jsonify
from jose import jwt
from urllib.request import urlopen
from icecream import ic
import os

CONFIG_PATH = "../config.json"

## AuthError Exception
"""
AuthError Exception
A standardized way to communicate auth failure modes
"""


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


## Auth Header

"""
STATUS: DONE
@TODO: implement get_token_auth_header() method
    it should attempt to get the header from the request
        it should raise an AuthError if no header is present
    it should attempt to split bearer and the token
        it should raise an AuthError if the header is malformed
    return the token part of the header
"""


def load_config(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def get_token_auth_header():
    if "Authorization" not in request.headers:
        raise AuthError(
            {"code": "not_found", "description": "Bearer Token Not Found"}, 401
        )
    authString = request.headers["Authorization"]
    parts = authString.split(" ")
    if parts[0] != "Bearer" or len(parts) != 2:
        raise AuthError(
            {"code": "invalid_token", "description": "Invalid Bearer Token"},
            401,
        )

    jwtToken = parts[1]
    components = jwtToken.split(".")
    if len(components) != 3:
        raise AuthError(
            {"code": "invalid_token", "description": "Invalid Bearer Token"},
            401,
        )

    return jwtToken


"""
STATUS: DONE
@TODO: implement check_permissions(permission, payload) method
    @INPUTS
        permission: string permission (i.e. 'post:drink')
        payload: decoded jwt payload

    it should raise an AuthError if permissions are not included in the payload
        !!NOTE check your RBAC settings in Auth0
    it should raise an AuthError if the requested permission string is not in the payload permissions array
    return true otherwise
"""


def check_permissions(permission, payload):
    if "permissions" not in payload:
        raise AuthError(
            {
                "code": "invalid_token",
                "description": "Token format is invalid",
            },
            400,
        )
    if permission == "":
        return True
    if permission in payload["permissions"]:
        return True
    raise AuthError(
        {"code": "unauthorized", "description": "Permission not granted"},
        403,
    )


"""
STATUS: DONE
@TODO: implement verify_decode_jwt(token) method
    @INPUTS
        token: a json web token (string)

    it should be an Auth0 token with key id (kid)
    it should verify the token using Auth0 /.well-known/jwks.json
    it should decode the payload from the token
    it should validate the claims
    return the decoded payload

    !!NOTE urlopen has a common certificate error described here: https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
"""


def verify_decode_jwt(token):
    config = load_config(CONFIG_PATH)
    # GET THE PUBLIC KEY FROM AUTH0
    jsonurl = urlopen(
        "https://{}/.well-known/jwks.json".format(config["DOMAIN"])
    )
    jwks = json.loads(jsonurl.read())

    # GET THE DATA IN THE HEADER
    unverified_header = jwt.get_unverified_header(token)

    # CHOOSE OUR KEY
    rsa_key = {}
    if "kid" not in unverified_header:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Unable to parse authentication token",
            },
            400,
        )

    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
            break

    # Finally, verify!!!
    if rsa_key:
        try:
            # USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=config["ALGORITHMS"],
                audience=config["API_IDENTIFIER"],
                issuer="https://{}/".format(config["DOMAIN"]),
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError(
                {"code": "token_expired", "description": "Token expired."}, 401
            )

        except jwt.JWTClaimsError:
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "Incorrect claims. Please, check the audience and issuer.",
                },
                401,
            )
        except Exception:
            raise AuthError(
                {
                    "code": "invalid_header",
                    "description": "Unable to parse authentication token",
                },
                400,
            )
    raise AuthError(
        {
            "code": "invalid_header",
            "description": "Unable to find the appropriate key.",
        },
        400,
    )


"""
STATUS: DONE
@TODO: implement @requires_auth(permission) decorator method
    @INPUTS
        permission: string permission (i.e. 'post:drink')

    it should use the get_token_auth_header method to get the token
    it should use the verify_decode_jwt method to decode the jwt
    it should use the check_permissions method validate claims and check the requested permission
    return the decorator which passes the decoded payload to the decorated method
"""


def requires_auth(permission=""):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)

            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator
