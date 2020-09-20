import discord
from discord.ext import commands
import sympy
import axiomathbf
from utility.math_parser import convert, parse_eq


class Vector(commands.Cog):
    """
    Contains various linear algebra tools
    """

    def __init__(self, bot):
        self.bot = bot
        self.file_location = 'temp/vector.png'

    @commands.command()
    async def dot(self, ctx, v1: convert, v2: convert):
        """Computes dot product"""
        await ctx.send(v1.dot(v2))

    @commands.command()
    async def cross(self, ctx, v1: convert, v2: convert):
        """Computes cross product"""
        sympy.preview(v1.cross(v2), viewer='file', filename=self.file_location)
        await ctx.send(file=discord.File(self.file_location))

    @commands.command()
    async def norm(self, ctx, vec: convert):
        """Computes norm of vector"""
        await ctx.send(vec.magnitude())

    @commands.command()
    async def normalize(self, ctx, vec: convert):
        """Normalizes vector"""
        sympy.preview(vec.normalize(), viewer='file',
                      filename=self.file_location)
        await ctx.send(file=discord.File(self.file_location))

    @commands.command()
    async def proj(self, ctx, vec1: convert, vec2: convert):
        """Finds projection of first vector onto second"""
        sympy.preview(vec1.projection(vec2),
                      viewer='file', filename=self.file_location)
        await ctx.send(file=discord.File(self.file_location))

    @commands.command()
    async def integvect(self, ctx, v1: parse_eq, v2: parse_eq, v3: parse_eq):
        sympy.preview(axiomathbf.VectorFunction([v1, v2, v3]).integrate().get_vector(),
                      viewer='file', filename=self.file_location)
        await ctx.send(file=discord.File(self.file_location))

    @commands.command()
    async def diffvect(self, ctx, v1: parse_eq, v2: parse_eq, v3: parse_eq):
        sympy.preview(axiomathbf.VectorFunction([v1, v2, v3]).derive().get_vector(),
                      viewer='file', filename=self.file_location)
        await ctx.send(file=discord.File(self.file_location))

    @commands.command()
    async def domain(self, ctx, v1: parse_eq, v2: parse_eq, v3: parse_eq):
        sympy.preview(axiomathbf.VectorFunction([v1, v2, v3]).get_domain(),
                      viewer='file', filename=self.file_location)
        await ctx.send(file=discord.File(self.file_location))
