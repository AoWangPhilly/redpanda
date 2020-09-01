import discord
from discord.ext import commands
import sympy
from cogs.math_parser import parse_pt, parse_matrix


class Plane(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file_location = 'temp/output.png'

    @commands.command(pass_context=True, aliases=['3pointplane'])
    async def three_points(self, ctx, p1: parse_pt, p2: parse_pt, p3: parse_pt):
        sympy.preview(sympy.Plane(p1, p2, p3).equation(),
                      viewer='file', filename=self.file_location)
        await ctx.send(file=discord.File(self.file_location))

    @commands.command(pass_context=True, aliases=['pointnormal'])
    async def point_normal(self, ctx, p1: parse_pt, normal: parse_matrix):
        sympy.preview(sympy.Plane(p1, normal_vector=list(normal)),
                      viewer='file', filename=self.file_location)
        await ctx.send(file=discord.File(self.file_location))
