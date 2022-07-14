import disnake
from disnake.ext import commands

token = ""

bot = commands.InteractionBot()
game = disnake.Game("👋 Hi")

@bot.event
async def on_ready():
    print("The bot is ready!")
    await bot.change_presence(status=disnake.Status.idle, activity=game)
   
extensions = []
directory = 'cogs'
for file in os.listdir(directory):
    if file.endswith('.py'):
        extensions.append(f'{directory}.{file[:-3]}')

for extension in extensions:
    bot.load_extension(extension)
    print(f'{extension} loaded!')
   
bot.run(token)
