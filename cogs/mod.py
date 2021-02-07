import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role("admin", "mod", "Owner")
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        if ctx.message.author == member:
            await ctx.send(f"{ctx.message.author.mention}, you wanna ban yourself\nlmao")
        else:
            await member.ban(reason=reason)
            await ctx.send(f"Banned {member.mention}\nReason={reason}")


    @commands.command()
    @commands.has_any_role("admin","mod","Owner")
    async def unban(self, ctx, *, member):
        banned_user = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for banned_entry in banned_user:
            user = banned_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return
        await ctx.send(f"{member} was not found")

    @commands.command(aliases=["purge"])
    @commands.has_any_role("admin","mod","Owner")
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_any_role("admin","mod","Owner")
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if ctx.message.author == member:
            await ctx.send(f"{ctx.message.author.mention}, Why you wanna kick yourself?")
        
        else:
            await member.kick(reason=reason)
            await ctx.send(f"Kicked {member.mention}\nReason={reason}")

    @commands.command(aliases=['m'])
    @commands.has_any_role("admin","mod","Owner")
    async def mute(self, ctx, member : discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        if ctx.message.author == member:
            await ctx.send(f"{ctx.message.author.mention}, is this a joke?\nBecause it ain't funny")
        if muted_role in member.roles:
            await ctx.send(f"{member.mention} is already muted")
        else:
            await member.add_roles(muted_role)
            await ctx.send(f"{member.mention} has been muted by {ctx.author.mention}")

    @commands.command()
    @commands.has_any_role("admin","mod","Owner")
    async def unmute(self, ctx, member : discord.Member):
        # muted_role = ctx.guild.get_role(785417099131486239)
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        if ctx.message.author == member:
            await ctx.send(f"{member.mention}, you can't unmute yourself")
        if muted_role not in member.roles:
            await ctx.send(f"{member.mention} is not muted\n you need to mute him first")
        else:
            await member.remove_roles(muted_role)
            await ctx.send(f"{member.mention} has been unmuted by {ctx.author.mention}")

    @commands.command(aliases=["giverole"])
    @commands.has_any_role("admin", "mod", "Owner")
    async def addrole(self, ctx, role : discord.Role, *, member: discord.Member):
        if role not in member.roles:
            await member.add_roles(role)
            await ctx.send("Successfully added role")
        else:
            await ctx.send("Mentioned member already has that role")
    @commands.command()
    @commands.has_any_role('admin', 'mod', 'Owner')
    async def removerole(self, ctx, role : discord.Role, member : discord.Member):
        if role not in member.roles:
            await ctx.send(f"{member.mention} does not have that role\n try adding it with .addrole command")
        else:
            await member.remove_roles(role)
            await ctx.send(f"Successfully updated roles of {member.mention}")

def setup(client):
    client.add_cog(Mod(client))