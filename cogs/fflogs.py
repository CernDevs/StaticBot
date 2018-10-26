from discord.ext import commands
import discord
import requests

class FFlogs:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def percentile(self, ctx, job, dps):
        """Displays the percentile for a dps number, for a job"""
        pass

def setup(bot):
    bot.add_cog(FFlogs(bot))