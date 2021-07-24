# importing module
import os
import eel
import bitly_api

current_directory = os.getcwd()

eel.init(current_directory)

# shorten the url
@eel.expose
def short_url(url):
    api_key = "21686817178bbaa98d5caf0a3df732340448f7ce"
    conn = bitly_api.Connection(access_token=api_key)
    shorten_url = conn.shorten(url)
    return shorten_url.get('url')


eel.start("index.html", size=(896, 389))
