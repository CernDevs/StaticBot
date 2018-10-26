from discord.ext import commands
import discord
import os, sys

description = "Hi, this is a bot."
extensions = (
    'cogs.basic',
    'cogs.info',
    'cogs.fflogs',
    'cogs.static'
)

class StaticBot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix="!", pm_help=None, description=description)
        for extension in extensions:
            self.load_extension(extension)


    async def on_ready(self):
        print("Username: {0.user}".format(self))
        print("ClientID: {0.user.id}".format(self))
        print("Python Version: {0.version}".format(sys))
        print("Discordpy Version: {0.__version__}".format(discord))
        print("Guilds: {0}".format(len(self.guilds)))
        await self.change_presence(activity=discord.Game(name="{0}help".format(self.command_prefix)))
    
    async def on_message(self, message):
        await self.process_commands(message)

    async def on_command_error(self, ctx, error):
        if not isinstance(error, commands.CommandNotFound):
            await ctx.send("`{0}`".format(error))

    def run(self):
        super().run(os.environ['BOT_TOKEN'], reconnect=True)

bot = StaticBot()
bot.run()