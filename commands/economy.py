from disnake.ext import commands
import disnake
import json
import os 
import random

os.chdir('commands')

class EconomyCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    

    #!BALANCE
    @commands.slash_command(name='bal', description='💳 View your balance')
    async def economy(self, ctx: disnake.ApplicationCommandInteraction):

        user = ctx.author
        users = await get_bank_data()

        await open_account(user)

        wallet_amt = users[str(user.id)]["Wallet"]

        balembed = disnake.Embed(title=f"{user.name}'s balance.") 
        balembed.add_field(name="Wallet Balance",value = f"🪙 {wallet_amt} coins")
        balembed.set_thumbnail(url=user.avatar)

        await ctx.send(embed=balembed)
    
    #!WORK
    @commands.slash_command(name='work', description='⚙️ Work')
    async def work(self, ctx: disnake.ApplicationCommandInteraction):

        user = ctx.author
        users = await get_bank_data()
        
        await open_account(user)

        earnings = random.randrange(100)

        workembed = disnake.Embed(title=f"Work") 
        workembed.add_field(name="Working...",value = f"{user.name} went work and won 🪙 {earnings} coins")
        workembed.set_thumbnail(url=user.avatar)
        await ctx.send(embed=workembed)

        users[str(user.id)]["Wallet"] += earnings

        with open("bank.json", 'w') as f:
            json.dump(users, f)


    #!PROFILE 
    @commands.slash_command(name='profile', description='📖 View you profile')
    async def profile(self, ctx: disnake.ApplicationCommandInteraction):

        user = ctx.author
        users = await get_bank_data()

        await open_account(user)

        wallet_amt = users[str(user.id)]["Wallet"]

        profileembed = disnake.Embed(title=f'{ctx.user.name} profile')
        profileembed.add_field(name='Info', value=f'Name : {user.name} \nId : {user.id}', inline=False)
        profileembed.add_field(name='Ecomomy', value=f'{user.name} have 🪙 {wallet_amt} coins')
        profileembed.set_thumbnail(url=f'{user.avatar}')
        await ctx.send(embed=profileembed)


#!OPEN ACCOUNT
async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Wallet"] = 500

    with open("bank.json", 'w') as f:
        json.dump(users, f)
    return True

#!GET BANK DATA
async def get_bank_data():
    with open("bank.json", 'r') as f:
        users = json.load(f)
    return users



def setup(bot: commands.Bot):
    bot.add_cog(EconomyCommand(bot))