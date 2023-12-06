import functions_framework
import bcrypt
import os
from supabase import Client, create_client
import time

cache = {}


def authorize_api_key(api_key):
    res = {
        "authorized": False,
    }
    try:
        key_id = api_key.split("+")[0] 
        secret = api_key.lstrip(key_id)
        secret = secret.lstrip("+")
        url:str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        supabase: Client = create_client(url, key)
        response = supabase.table("api_keys").select("*").eq("id", key_id).single().execute()
        hashed_secret = response.data["key"]
        if bcrypt.checkpw(secret.encode(), hashed_secret.encode()):
            res["team_id"] = response.data["team_id"]
            res["supabase"] = supabase
            res["authorized"] = True
            res["system_id"] = response.data["system_id"]
            return res
    except Exception as e:
        return res
    return res

def authorize_jwt(jwt):
    res = {
        "authorized": False,
    }
    try:
        url:str = os.environ.get("SUPABASE_URL")
        supabase: Client = create_client(url, jwt)
        team = supabase.table("teams").select("*").single().execute()
        res["team_id"] = team.data["id"]
        res["supabase"] = supabase
        if team.data["pickgpt_online"]:
            res["authorized"] = True
        else:
            res["authorized"] = False
        return res
    except Exception as e:
        return res
    return res


def get_cached(api_key, authorization_func=authorize_api_key):
    now = time.time()
    cached = None
    if api_key in cache:
        cached = cache[api_key]
        if (now - cached["timeadded"]) > 60*60:
            cached = None
    if cached is None:
        authorization = authorization_func(api_key)
        authorization["timeadded"] = now
        if authorization["authorized"]:
            cache[api_key] = authorization
        cached = authorization
    return cached

@functions_framework.http
def pickgpt(request: functions_framework.flask.Request):
    jwt = request.headers.get("Authorization")
    if jwt is not None:
        jwt = jwt.lstrip("Bearer ")
        authorization = get_cached(jwt, authorization_func=authorize_jwt)
    else:
        api_key = request.headers.get("X-API-KEY")
        if api_key is None:
            return ("API Key not provided", 401)
        authorization = get_cached(api_key)

    if authorization["authorized"] is False:
        return ("Key not authorized", 401)
    if request.method == "POST":
        try:
            print("CALLING PICKGPT WOHOOOOOOOOOOOOOOOOO")
            return  ("worked", 200)
        except Exception as e:
            return (f"Error getting token", 500)
    else:
        return ("Method not allowed", 405)