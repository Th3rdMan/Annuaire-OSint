import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

AVATAR_URL = "https://raw.githubusercontent.com/Th3rdMan/Wrench-Userscript/main/wrench.png"

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f"Wrench Jr connecté en tant que {client.user}")


@tree.command(name="flag", description="Soumettre un flag OSINT avec sa réponse")
@app_commands.describe(
    nom="Nom du flag OSINT",
    reponse="Réponse soumise pour ce flag",
    valide="Le flag est-il validé ?",
)
async def flag(
    interaction: discord.Interaction,
    nom: str,
    reponse: str,
    valide: bool,
):
    color = discord.Color.green() if valide else discord.Color.red()
    status_text = "✅ Validé" if valide else "❌ Non validé"

    embed = discord.Embed(
        title=f"🚩 {nom}",
        color=color,
    )
    embed.add_field(name="Réponse soumise", value=f"`{reponse}`", inline=False)
    embed.add_field(name="Statut", value=status_text, inline=False)
    embed.set_footer(text="Wrench Jr • OSINT Flag Tracker", icon_url=AVATAR_URL)

    await interaction.response.send_message(embed=embed)


client.run(os.environ["DISCORD_TOKEN"])
