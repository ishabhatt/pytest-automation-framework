import yaml
import os

def load_config(env="default"):
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)
    return cfg.get(env, cfg["default"])
