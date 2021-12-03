import os
import importlib

# by default use local
ENV_ROLE = os.getenv('ENV_ROLE', 'local')

env_settings = importlib.import_module(f'cars_api.settings.{ENV_ROLE}')

globals().update(vars(env_settings))