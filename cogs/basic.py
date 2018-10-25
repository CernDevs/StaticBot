import discord
from discord.ext import commands
from urllib.parse import urlencode

class Basic:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Ping!"""
        message = await ctx.send("`Pong!`")
        time = message.created_at - ctx.message.created_at
        await message.edit(content="`Pong! {0}ms`".format(time.microseconds/1000))

    @commands.command(pass_context=True)
    async def invite(self, ctx):
        """Bot's Invite Link"""
        await ctx.send("{0.author.mention} {1}".format(ctx, discord.utils.oauth_url(self.bot.user.id)))
    
def setup(bot):
    bot.add_cog(Basic(bot))