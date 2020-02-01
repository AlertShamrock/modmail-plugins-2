import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, 'Cog', object)


class Information(Cog):
    """Information plugin"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMIN)
    async def information(self, ctx):
        """Command center."""

        embed = discord.Embed(
            title="__**Commands**__",
            color=self.bot.main_color,
            description="__**Update your Discord rank**__\nSay this command `!getroles`\n\n__**Report**__\nReporting a Discord User!\n**Command**\n`?report <Discord User> <Reason>`\n\n__**Inactivity notice**__\nGoing on vacation, or not going be on base?\n**Say these commands**\n`!apply`\n`/apply`\n**NOTE:** Can be demoted until HQ (Head Quarters) approves of your inactivity request.\n\n__**Suggestions**__\nWant to suggest something to Army discord or on to a base?\n**Say these commands**\n**Add these before you MESSAGE**\n***Message Prefix***\n`[BASE]`\n`[DISCORD]`\n`[GROUP]`\n\n**Command:**\n`!suggest (PREFIX) (message)`\n\n__**Quote**__\nAdd a quote onto quotes channel!\n**Command**\n`!quote <Quote here>`\n\n--------------------------------------\n__Say ***THESE*** commands in ***THIS*** channel **ONLY!**__\n--------------------------------------",
        )
        ##embed.add_field(name="__Update your Discord rank__",value="**Command** \n `!getroles`", inline=false)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/bprmtEGvGNYJFqRHOEkFYvTsuK_uUHx_vLrxb7dct68/%3Fsize%3D1024/https/cdn.discordapp.com/icons/630865258751328256/34b8b5556bebd2f6d27868aa9ab4165f.webp?width=470&height=470")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
