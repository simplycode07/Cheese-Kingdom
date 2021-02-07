import discord
import os
from discord.ext import commands, tasks

token = os.environ.get("TECH_AND_GAMING_BOT")

client = commands.Bot(command_prefix = ".")

client.remove_command("help")

@client.event
async def on_ready():
    print("Bot is ready")

##### Moderation commands (only admin and mods can use) #####
@client.command()
@commands.has_any_role("admin","mod","Owner")
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}\nReason={reason}")

@client.command()
@commands.has_any_role("admin","mod","Owner")
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for banned_entry in banned_user:
        user = banned_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return
    await ctx.send(f"{member} was not found")
    

@client.command(aliases=["purge"])
@commands.has_any_role("admin","mod","Owner")
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_any_role("admin","mod","Owner")
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}\nReason={reason}")

@client.command(aliases=['m'])
@commands.has_any_role("admin","mod","Owner")
async def mute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(785417099131486239)

    await member.add_roles(muted_role)

    await ctx.send(f"{member.mention} has been muted by {ctx.author.mention}")

@client.command()
@commands.has_any_role("admin","mod","Owner")
async def unmute(ctx, member : discord.Member):
    await member.remove_roles(ctx.guild.get_role(785417099131486239))
    await ctx.send(f"{member.mention} has been unmuted by {ctx.author.mention}")

###### Fun commands (anyone can use) #####

@client.command(aliases=["p"])
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms")

@client.command(aliases=["hi"])
async def hello(ctx):
    await ctx.send("Hello! {}".format(ctx.message.author.mention))

@client.command()
async def yeet(ctx):
    await ctx.send(""":woman_cartwheeling:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             :manual_wheelchair:     :man_golfing:""")
    


################## help commands ##################
@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description= "Use .help <command> for extended information on a command.", color = ctx.author.color)

    em.add_field(name="Moderation", value="kick, Ban, Unban, Mute, Unmute")
    em.add_field(name="Fun", value="Ping, Hello, Yeet")
    await ctx.send(embed=em)

@help.command()
async def kick(ctx):
    em = discord.Embed(title="Kick", description="Kicks a member from the guild", color=ctx.author.color)
    em.add_field(name="**Syntax**", value = ".kick <member> [reason]")
    await ctx.send(embed=em)

@help.command()
async def ban(ctx):
    em = discord.Embed(title="Ban", description="Bans a member from the guild", color=ctx.author.color)
    em.add_field(name="**Syntax**", value = ".ban <member> [reason]")
    await ctx.send(embed=em)

@help.command()
async def unban(ctx):
    em = discord.Embed(title="Unban", description="Unbans a member from the guild", color=ctx.author.color)
    em.add_field(name="**Syntax**", value = ".unban <member> [reason]")
    await ctx.send(embed=em)

@help.command()
async def ping(ctx):
    em = discord.Embed(title="Ping", description="Shows Bot's latency to Discord's API.", color=ctx.author.color)
    em.add_field(name="**Syntax**", value = ".ping")
    await ctx.send(embed=em)

@help.command()
async def hello(ctx):
    em = discord.Embed(title="Hello", description="Says Hello back to you", color=ctx.author.color)
    em.add_field(name="**Syntax**", value = ".hello")
    await ctx.send(embed=em)
@help.command()
async def mute(ctx):
    em = discord.Embed(title="Mute", description="Mutes mentioned user from the guild", color=ctx.author.color)
    em.add_field(name="**Syntax**", value = ".mute <member>")
    await ctx.send(embed=em)

@help.command()
async def unmute(ctx):
    em = discord.Embed(title="Unmute", description="Unmutes a muted member from the guild", color=ctx.author.color)
    em.add_field(name="**Syntax**", value = ".unmute <member>")
    await ctx.send(embed=em)
@help.command()
async def yeet(ctx):
    em = discord.Embed(title="Yeet", description="Yeet the Child", color=ctx.author.color)
    em.add_field(name="**Syntax**", value = ".yeet")
    await ctx.send(embed=em)
    
    
client.run(token)        
