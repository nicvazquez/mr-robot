import discord
import datetime 

def getEmbed(ctx, var):
    embed = discord.Embed(title="Soy Mr Robot",url="https://0xtaylor.github.io/img/thm_mrrobot/card.png",description = var,
    timestamp = datetime.datetime.utcnow(),
    color = discord.Color.blue())
    embed.set_footer(text="solicitado por: {}".format(ctx.author.name))
    return embed