import discord
from discord.ext import commands

class Welcome(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):

        server = self.client.get_guild(785708055509336084)
        welcome_channel = server.get_channel(785708055509336088)

        embed = discord.Embed(
            description = f"Welcome, {member.mention}, to **The Cheese Kingdom**!",
            color = 0xfff700
        )

        embed.set_author(name = member.name, icon_url = member.avatar_url)
        embed.set_footer(text = f"Semper Stare Fortis! | #{server.member_count}")

        await welcome_channel.send(embed = embed)

    @commands.command()
    async def test(self, ctx, member : discord.Member):

        server = self.client.get_guild(785708055509336084)
        welcome_channel = server.get_channel(785708055509336088)

        embed = discord.Embed(
            description = f"Welcome, {member.mention}, to **The Cheese Kingdom**!",
            color = 0xfff700
        )

        embed.set_author(name = member.name, icon_url = member.avatar_url)
        embed.set_footer(text = f"Semper Stare Fortis! | #{server.member_count}")

        await welcome_channel.send(embed = embed)

def setup(client):
    client.add_cog(Welcome(client))