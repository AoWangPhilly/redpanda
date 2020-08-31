import discord
from discord.ext import commands
import sympy
from sympy.parsing.sympy_parser import parse_expr


def parse_eq(eq):
    eq = eq.replace('^', '**').replace('e', 'E')
    return parse_expr(eq)


class Calculus(commands.Cog):
    """
    Contains various calculus tools
    """

    def __init__(self, bot):
        self.bot = bot
        self.file_location = 'temp/output.png'

    @commands.command()
    async def derive(self, ctx, *, eq: parse_eq):
        """Derives single variable equations"""
        sympy.preview(sympy.diff(eq), viewer='file',
                      filename=self.file_location, dvioptions=['-D', '200'])
        await ctx.send(file=discord.File(self.file_location))

    @commands.command()
    async def integrate(self, ctx, *, eq: parse_eq):
        """Integrates single variable equations"""
        sympy.preview(sympy.integrate(eq), viewer='file',
                      filename=self.file_location, dvioptions=['-D', '200'])
        await ctx.send(file=discord.File(self.file_location))
