import redis
import json
from common.utils import load_config

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def init_config():
    cfg = load_config()
    r.set("sys_config", json.dumps(cfg))

def get_config():
    return json.loads(r.get("sys_config"))