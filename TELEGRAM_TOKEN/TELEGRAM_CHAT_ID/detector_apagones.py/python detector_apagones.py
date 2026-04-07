import requests
import time
from datetime import datetime

# =============== CONFIGURA ESTO ===============
TELEGRAM_TOKEN = "TU_TOKEN_AQUI"
TELEGRAM_CHAT_ID = "TU_CHAT_ID_AQUI"
WHATSAPP_API = "https://api.callmebot.com/whatsapp.php"  # gratis
WHATSAPP_PHONE = "521234567890"   # tu número con código de país, sin +
# ==============================================

def mandar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": mensaje})

def mandar_whatsapp(mensaje):
    url = f"{WHATSAPP_API}?phone={WHATSAPP_PHONE}&text={mensaje}&apikey=tuapikey"
    requests.get(url)

def detectar_apagon():
    try:
        r = requests.get("https://downdetector.com.mx/status/cfe/", timeout=10)
        texto = r.text.lower()
        
        if "apagón" in texto or "sin luz" in texto or "reportes" in texto:
            hora = datetime.now().strftime("%H:%M")
            msg = f"⚡ Apagón en Mexicali - {hora}"
            
            mandar_telegram(msg)
            mandar_whatsapp(msg)
            print(f"{hora} → Alerta enviada a Telegram y WhatsApp")
            return True
    except:
        pass
    return False

print("Detector de apagones CFE Mexicali iniciado...")
print("Revisa cada 3 minutos. Presiona Ctrl+C para parar.")

while True:
    detectar_apagon()
    time.sleep(180)  # 3 minutos
