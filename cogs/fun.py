import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.find("it's night") != -1:
            await message.channel.send(f"{message.author.mention}, I think you should sleep now")
        
        if message.content.lower().find("gg") != -1:
            if (message.author.id != self.client.user.id):
                await message.channel.send("gg")

    @commands.command(aliases=["p"])
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)} ms")

    @commands.command(aliases=["hi"])
    async def hello(self, ctx):
        await ctx.send("""██╗░░██╗██╗\n██║░░██║██║\n███████║██║\n██╔══██║██║\n██║░░██║██║\n╚═╝░░╚═╝╚═╝""")

    @commands.command()
    async def yeet(self, ctx):
        await ctx.send(""":woman_cartwheeling:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             :manual_wheelchair:     :man_golfing:""")
    
    @commands.command()
    async def say(self, ctx, *, message_to_say):
        await ctx.message.delete()
        await ctx.send(message_to_say)

def setup(client):
    client.add_cog(Fun(client))
