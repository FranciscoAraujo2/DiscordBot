from disnake.ext import commands
import disnake

class PingCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #!PING
    @commands.slash_command(name='ping', description='📡 View my ping')
    async def ping(self, ctx: disnake.ApplicationCommandInteraction):
        pingembed = disnake.Embed(title="FireSecurity ping", description=f"🏓 Pong! \n 📡 My Ping : {round(self.bot.latency * 1000)}ms", color=disnake.Colour(0XFF0000))
        await ctx.send(embed=pingembed)
    
    #!HELP
    @commands.slash_command(name='help', description='📌 View my commands')
    async def help(self, ctx: disnake.ApplicationCommandInteraction):
        homehelpembed = disnake.Embed(title=f'Help', description=f'My prefix : ``/``', color=disnake.Colour(0XFF6F00))
        homehelpembed.add_field(name='Comon', value='```⌛️ Ping | 😀 Profile \n❓ Help```')
        homehelpembed.add_field(name='Ecomomy', value='```⚙️ Work | 💳 Bal```', inline=False)
        homehelpembed.add_field(name='Mod', value='```💬 Clear \n✈️ Kick | 🚀 Ban \n🔒 Lock | 🔓 Unlock```', inline=False)
        homehelpembed.set_thumbnail(url=f'{ctx.user.avatar}')
        await ctx.send(embed=homehelpembed)




def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))