from os import getenv

class Config(object):
      API_HASH = getenv("c0da9c346d2c45dbc7ec49a05da9b2b6")
      API_ID = int(getenv("API_ID", 13675555))
      AS_COPY = True if getenv("AS_COPY", True) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "6680969743:AAHpx2FWxrJDDBZTasyyUk05h7a0zG6aeMc")
      CHANNEL = list(x for x in getenv("1824390877", "").replace("\n", " ").split(' '))
