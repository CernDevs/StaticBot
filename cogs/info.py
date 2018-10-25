import discord
from discord.ext import commands
import sys

class Info:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def info(self, ctx):
        """Bot Information"""
        await ctx.send("""```Markdown
Bot Info
========
<Name: {0.user}>
<Nickname: {0.user.display_name}>
<Client ID: {0.user.id}>
<Icon: {0.user.avatar_url}>
<Created: {0.user.created_at}>
<Discordpy: {1.__version__}>
<Python: {2.version}>
<Guilds: {3}>
```""".format(self.bot, discord, sys, len(self.bot.guilds)))

    @commands.command(pass_context=True)
    async def server(self, ctx):
        """Current Server Information"""
        roles = []
        for role in ctx.guild.roles:
            roles.append(role.name) 
        roles = ", ".join(roles)
        await ctx.send("""```Markdown
Server Info
===========
<Name: {0.guild.name}>
<ID: {0.guild.id}>
<Owner: {0.guild.owner}>
<Region: {0.guild.region}>
<Roles: {1}>
<Members: {0.guild.member_count}>
<Created: {0.guild.created_at}>
<Icon: {0.guild.icon_url}>
<Shard: {0.guild.shard_id}>
```""".format(ctx, roles))

def setup(bot):
    bot.add_cog(Info(bot))
