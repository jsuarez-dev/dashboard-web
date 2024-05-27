
from dotenv import load_dotenv
import os
import pandas as pd
load_dotenv()

env_var = os.getenv("DATA_SOURCE")

if env_var is None:
    raise ValueError("There is no file path in the environment variables")

if not os.path.exists(env_var):
    raise FileNotFoundError("The file does not exist")

df = pd.read_json(env_var)

print(df.head())
