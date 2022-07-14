# DiscordBot
🤖・Discord Bot

# Disnake 
* pip install disnake <br>
* https://docs.disnake.dev/en/latest/

# About

| Systems | Description |
| --- | --- |
| Economy | Now you can work with the bot |
| Moderation | Protect your server with our system |
| Fun | Have fun with your friends |

# Cogs

```py
extensions = []
directory = 'cogs'
for file in os.listdir(directory):
    if file.endswith('.py'):
        extensions.append(f'{directory}.{file[:-3]}')

for extension in extensions:
    bot.load_extension(extension)
    print(f'{extension} loaded!')
```

#Exemple command

```py 

class PingCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #!PING
    @commands.slash_command(name='ping', description='ping')
    async def ping(self, ctx: disnake.ApplicationCommandInteraction):
        await ctx.send("pong!")
    
def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))

```
