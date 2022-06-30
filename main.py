import disnake
from disnake.ext import commands

token = ""

bot = commands.InteractionBot()
game = disnake.Game("👋 Hi")

@bot.event
async def on_ready():
    print("The bot is ready!")
    await bot.change_presence(status=disnake.Status.idle, activity=game)
   
bot.run(token)
