import discord
from discord.ext import commands

class Static:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def setup(self, ctx):
        """Sets up discord server with various channels for static purposes (permissions needed)"""
        pass
    
def setup(bot):
    bot.add_cog(Static(bot))