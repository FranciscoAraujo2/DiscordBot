from disnake.ext import commands
import disnake

class ClearCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #!CLEAR
    @commands.slash_command(name='clear', description='💬 Clear messages')
    async def clear(self, ctx: disnake.ApplicationCommandInteraction , amount: int):
        if ctx.permissions.manage_messages :
            clearembed = disnake.Embed(title="FireSecurity clear", description=f"{ctx.author} cleaned {amount} messages")
            await ctx.channel.purge(limit=amount)
            await ctx.send(embed=clearembed)
        else :
            clearembederror = disnake.Embed(title="Error", description=f"{ctx.author} You are not admin on this server")
            await ctx.send(embed=clearembederror)

    #!BAN
    @commands.slash_command(name='ban', description='🚀 Ban users')
    async def ban(self, ctx: disnake.ApplicationCommandInteraction , user: disnake.Member, *, reason):
        if ctx.permissions.ban_members :
            await ctx.guild.ban(user, reason=reason)
            banembed = disnake.Embed(name=f"{user} has been successfully baned", description=f'Guild : {ctx.guild} \n Reason : {ctx.guild}')
            await ctx.send(embed=banembed)
        else :
            banembederror = disnake.Embed(title="Error", description=f"{ctx.author} You are not admin on this server")
            await ctx.send(embed=banembederror)
            
    #!KICK
    @commands.slash_command(name='kick', description='🚀 Kick user')
    async def kick(self, ctx: disnake.ApplicationCommandInteraction, user: disnake.Member, *, reason):
        if ctx.permissions.kick_members:
            await ctx.guild.kick(user, reason=reason)
            kickembed = disnake.Embed(name=f"{user} has been successfully kicked", description=f'Guild : {ctx.guild} \n Reason : {ctx.guild}')
            await ctx.send(embed=kickembed)
        else:
            kickembederror = disnake.Embed(title='Error', description=f'{ctx.author} you are not admin on this server')
            await ctx.send(embed=kickembederror)  


    #!LOCK
    @commands.slash_command(name='lock', description='🔒 lock channel')
    async def lock(self, ctx: disnake.ApplicationCommandInteraction, channel : disnake.TextChannel=None):
        if ctx.permissions.manage_channels:
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.send(f'{ctx.channel} locked.')
        else:
            lockembederror = disnake.Embed(title='Error', description=f'{ctx.author} you are not admin on this server')
            await ctx.send(embed=lockembederror)

    #!UNLOCK    
    @commands.slash_command(name='unlock', description='🔓 unlock channel')
    async def unlock(self, ctx: disnake.ApplicationCommandInteraction, channel : disnake.TextChannel=None):
        if ctx.permissions.manage_channels:
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.send(f'{ctx.channel} unlocked.')
        else:
            lockembederror = disnake.Embed(title='Error', description=f'{ctx.author} you are not admin on this server')
            await ctx.send(embed=lockembederror)

def setup(bot: commands.Bot):
    bot.add_cog(ClearCommand(bot))