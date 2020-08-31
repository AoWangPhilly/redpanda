import discord
from discord.ext import commands
import sympy
from sympy.matrices import Matrix
from sympy.vector import CoordSys3D, matrix_to_vector


def convert(vec):
    C = CoordSys3D('')
    vec = vec.replace('<', '').replace('>', '').split(',')
    return matrix_to_vector(Matrix(list(map(int, vec))), C)


class Vector(commands.Cog):
    """
    Contains various linear algebra tools
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dot(self, ctx, v1: convert, v2: convert):
        """Computes dot product"""
        await ctx.send(v1.dot(v2))

    @commands.command()
    async def cross(self, ctx, v1: convert, v2: convert):
        """Computes cross product"""
        sympy.preview(v1.cross(v2), viewer='file', filename='vector.png')
        await ctx.send(file=discord.File('vector.png'))

    @commands.command()
    async def norm(self, ctx, vec: convert):
        """Computes norm of vector"""
        await ctx.send(vec.magnitude())

    @commands.command()
    async def normalize(self, ctx, vec: convert):
        """Normalizes vector"""
        sympy.preview(vec.normalize(), viewer='file', filename='vector.png')
        await ctx.send(file=discord.File('vector.png'))

    @commands.command()
    async def proj(self, ctx, vec1: convert, vec2: convert):
        """Finds projection of first vector onto second"""
        sympy.preview(vec1.projection(vec2),
                      viewer='file', filename='vector.png')
        await ctx.send(file=discord.File('vector.png'))
