import discord
from discord.ext import commands
import sympy
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot

class Calculus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def derive(self, ctx, *, eq):
        try:
            eq = parse_expr(eq.replace('^', '**'))
            sympy.preview(sympy.diff(eq), viewer='file',
                        filename='output.png', dvioptions=['-D', '200'])
            await ctx.send(file=discord.File('output.png'))
        except:
            await ctx.send('Error! Try again :<')
            

    @commands.command()
    async def integrate(self, ctx, *, eq):
        try:
            eq = parse_expr(eq.replace('^', '**'))
            sympy.preview(sympy.integrate(eq), viewer='file',
                        filename='output.png', dvioptions=['-D', '200'])
            await ctx.send(file=discord.File('output.png'))
        except:
            await ctx.send('Error! Try again :<')

    @commands.command()
    async def graph(self, ctx, *, eq):
        eq = parse_expr(eq.replace('^', '**'))
        p1 = plot(eq, show=False)
        p1.save('graph.png')
        await ctx.send(file=discord.File('graph.png'))

