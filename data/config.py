#from environs import Env

# environs kutubxonasidan foydalanish
#env = Env()
#env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
#BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
#ADMINS = env.list("ADMINS")  # adminlar ro'yxati
#IP = env.str("ip")  # Xosting ip manzili
#CHANNEL = ["-1001502729082", "-1001621599346"]
import os
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot toekn
ADMINS = list(os.environ.get("ADMINS")) # adminlar ro'yxati
IP = str(os.environ.get("ip"))
PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN"))
CHANNEL = ["-1001502729082", "-1001621599346"]
