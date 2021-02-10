import discord
from discord.ext import commands

class Help(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("Bot is ready")

	@commands.group(invoke_without_command = True)
	async def help(self, ctx):
		em = discord.Embed(title = "Help", description= "Use .help <command> for extended information on a command.", color = ctx.author.color)
		em.add_field(name="Moderation", value="kick, Ban, Unban, Mute, Unmute, Add Role, Remove Role")
		em.add_field(name="Fun", value="Ping, Hello, Yeet, Say")
		await ctx.send(embed=em)

	#### moderation commands ####
	@help.command()
	async def kick(self, ctx):
		em = discord.Embed(title="Kick", description="Kicks a member from the guild", color=ctx.author.color)
		em.add_field(name="**Syntax**", value = ".kick <member> [reason]")
		await ctx.send(embed=em)

	@help.command()
	async def ban(self, ctx):
		em = discord.Embed(title="Ban", description="Bans a member from the guild", color=ctx.author.color)
		em.add_field(name="**Syntax**", value = ".ban <member> [reason]")
		await ctx.send(embed=em)

	@help.command()
	async def unban(self, ctx):
		em = discord.Embed(title="Unban", description="Unbans a member from the guild", color=ctx.author.color)
		em.add_field(name="**Syntax**", value = ".unban <member> [reason]")
		await ctx.send(embed=em)

	@help.command()
	async def mute(self, ctx):
		em = discord.Embed(title="Mute", description="Mutes mentioned user from the guild", color=ctx.author.color)
		em.add_field(name="**Syntax**", value = ".mute <member>")
		await ctx.send(embed=em)

	@help.command()
	async def unmute(self, ctx):
		em = discord.Embed(title="Unmute", description="Unmutes a muted member from the guild", color=ctx.author.color)
		em.add_field(name="**Syntax**", value = ".unmute <member>")
		await ctx.send(embed=em)

	@help.command()
	async def addrole(self, ctx):
		em = discord.Embed(title="Add Role", description="Adds given role to mentioned member", color=ctx.author.color)
		em.add_field(name="**Syntax**", value = ".addrole [Role name] <member>")
		await ctx.send(embed=em)

	@help.command()
	async def removerole(self, ctx):
		em = discord.Embed(title="Remove Role", description="Removes given role from mentioned member", color=ctx.author.color)
		em.add_field(name="**Syntax**", value = ".removerole [Role name] <member>")
		await ctx.send(embed=em)

	#### fun commands ####
	@help.command()
	async def ping(self, ctx):
		em = discord.Embed(title="Ping", description="Shows Bot's latency to Discord's API.", color=ctx.author.color)
		em.add_field(name="**Syntax**", value = ".ping")
		await ctx.send(embed=em)

	@help.command()
	async def hello(self, ctx):
		em = discord.Embed(title="Hello", description="Says Hello back to you", color=ctx.author.color)
		em.add_field(name="**Syntax**", value = ".hello")
		await ctx.send(embed=em)
	
	@help.command()
	async def yeet(self, ctx):
		em = discord.Embed(title="Yeet", description="Yeet the Child", color=ctx.author.color)
		em.add_field(name="**Syntax**", value = ".yeet")
		await ctx.send(embed=em)
	@help.command()
	async def say(self, ctx):
		em = discord.Embed(title="Say", description="Enter text you want bot to say\n*it also deletes your old message*", color=ctx.author.color)
		em.add_field(name="**Syntax**", value = ".say [text]")
		await ctx.send(embed=em)


def setup(client):
	client.add_cog(Help(client))