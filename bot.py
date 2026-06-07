#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Snapchat Discord Bot - Main Bot File
Gère la connexion Discord et le contrôle du bot Snapchat
"""

import os
import sys
import asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from discord import app_commands
import logging
from datetime import datetime
import platform

# Charger les variables d'environnement
load_dotenv()

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Import des modules
from utils.config import Config
from snapchat_client import SnapchatClient

class SnapchatDiscordBot(commands.Cog):
    """Cog principal pour le bot Discord"""
    
    def __init__(self, bot):
        self.bot = bot
        self.config = Config()
        self.snapchat_client = None
        self.is_snapchat_connected = False
        self.status_update_loop.start()
        logger.info(f"Bot initialized on {platform.system()} {platform.release()}")
    
    @tasks.loop(minutes=1)
    async def status_update_loop(self):
        """Met à jour le statut du bot toutes les minutes"""
        if self.is_snapchat_connected:
            status = "🟢 Snapchat connecté"
        else:
            status = "🔴 Snapchat déconnecté"
        
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=status
            )
        )
    
    @app_commands.command(name="panel", description="Affiche le panel de contrôle principal")
    async def panel(self, interaction: discord.Interaction):
        """Commande pour afficher le panel principal"""
        if not await self.is_admin(interaction):
            await interaction.response.send_message(
                "❌ Vous n'avez pas les permissions pour utiliser cette commande.",
                ephemeral=True
            )
            return
        
        embed = discord.Embed(
            title="🎮 Panel de Contrôle Snapchat",
            description="Gérez votre groupe Snapchat depuis Discord",
            color=discord.Color.yellow(),
            timestamp=datetime.now()
        )
        
        embed.add_field(
            name="📊 État du Connexion",
            value=f"{('🟢 Connecté' if self.is_snapchat_connected else '🔴 Déconnecté')}",
            inline=False
        )
        
        embed.add_field(
            name="👥 Gestion des Membres",
            value="• `/add_user` - Ajouter un utilisateur\n"
                  "• `/remove_user` - Retirer un utilisateur\n"
                  "• `/remove_all` - Retirer tous les membres\n"
                  "• `/list_members` - Lister les membres",
            inline=False
        )
        
        embed.add_field(
            name="⚙️ Gestion du Groupe",
            value="• `/group_info` - Infos du groupe\n"
                  "• `/set_name` - Changer le nom\n"
                  "• `/set_description` - Changer la description",
            inline=False
        )
        
        embed.add_field(
            name="🔧 Admin",
            value="• `/connect_snapchat` - Se connecter à Snapchat\n"
                  "• `/disconnect_snapchat` - Se déconnecter\n"
                  "• `/restart_bot` - Redémarrer\n"
                  "• `/logs` - Afficher les logs",
            inline=False
        )
        
        embed.set_footer(text=f"Bot Snapchat Discord | {self.bot.user.name}")
        
        await interaction.response.send_message(embed=embed)
        logger.info(f"Panel affiché par {interaction.user}")
    
    @app_commands.command(name="connect_snapchat", description="Se connecter à Snapchat")
    async def connect_snapchat(self, interaction: discord.Interaction):
        """Se connecter au compte Snapchat"""
        if not await self.is_admin(interaction):
            await interaction.response.send_message(
                "❌ Vous n'avez pas les permissions.",
                ephemeral=True
            )
            return
        
        await interaction.response.defer(ephemeral=True)
        
        try:
            logger.info("Tentative de connexion à Snapchat...")
            self.snapchat_client = SnapchatClient(
                self.config.snapchat_username,
                self.config.snapchat_password
            )
            
            if await self.snapchat_client.connect():
                self.is_snapchat_connected = True
                embed = discord.Embed(
                    title="✅ Connexion Réussie",
                    description="Connecté au compte Snapchat avec succès!",
                    color=discord.Color.green()
                )
                logger.info("Connexion Snapchat réussie")
            else:
                embed = discord.Embed(
                    title="❌ Échec de la Connexion",
                    description="Impossible de se connecter à Snapchat.",
                    color=discord.Color.red()
                )
                logger.error("Échec de la connexion Snapchat")
        
        except Exception as e:
            embed = discord.Embed(
                title="❌ Erreur",
                description=f"Erreur lors de la connexion: {str(e)}",
                color=discord.Color.red()
            )
            logger.error(f"Erreur de connexion: {str(e)}")
        
        await interaction.followup.send(embed=embed, ephemeral=True)
    
    @app_commands.command(name="disconnect_snapchat", description="Se déconnecter de Snapchat")
    async def disconnect_snapchat(self, interaction: discord.Interaction):
        """Se déconnecter du compte Snapchat"""
        if not await self.is_admin(interaction):
            await interaction.response.send_message(
                "❌ Vous n'avez pas les permissions.",
                ephemeral=True
            )
            return
        
        await interaction.response.defer(ephemeral=True)
        
        try:
            if self.snapchat_client:
                await self.snapchat_client.disconnect()
                self.is_snapchat_connected = False
                embed = discord.Embed(
                    title="✅ Déconnexion Réussie",
                    description="Déconnecté du compte Snapchat.",
                    color=discord.Color.green()
                )
                logger.info("Déconnexion Snapchat réussie")
            else:
                embed = discord.Embed(
                    title="⚠️ Info",
                    description="Aucune connexion active.",
                    color=discord.Color.orange()
                )
        except Exception as e:
            embed = discord.Embed(
                title="❌ Erreur",
                description=f"Erreur: {str(e)}",
                color=discord.Color.red()
            )
            logger.error(f"Erreur de déconnexion: {str(e)}")
        
        await interaction.followup.send(embed=embed, ephemeral=True)
    
    @app_commands.command(name="add_user", description="Ajouter un utilisateur au groupe")
    async def add_user(self, interaction: discord.Interaction, username: str):
        """Ajouter un utilisateur au groupe Snapchat"""
        if not await self.is_admin(interaction):
            await interaction.response.send_message(
                "❌ Vous n'avez pas les permissions.",
                ephemeral=True
            )
            return
        
        if not self.is_snapchat_connected or not self.snapchat_client:
            await interaction.response.send_message(
                "❌ Le bot n'est pas connecté à Snapchat.",
                ephemeral=True
            )
            return
        
        await interaction.response.defer(ephemeral=True)
        
        try:
            result = await self.snapchat_client.add_member(username)
            if result:
                embed = discord.Embed(
                    title="✅ Utilisateur Ajouté",
                    description=f"{username} a été ajouté au groupe",
                    color=discord.Color.green()
                )
                logger.info(f"Utilisateur {username} ajouté par {interaction.user}")
            else:
                embed = discord.Embed(
                    title="❌ Échec",
                    description=f"Impossible d'ajouter {username}",
                    color=discord.Color.red()
                )
        except Exception as e:
            embed = discord.Embed(
                title="❌ Erreur",
                description=f"Erreur: {str(e)}",
                color=discord.Color.red()
            )
            logger.error(f"Erreur lors de l'ajout: {str(e)}")
        
        await interaction.followup.send(embed=embed, ephemeral=True)
    
    @app_commands.command(name="remove_user", description="Retirer un utilisateur du groupe")
    async def remove_user(self, interaction: discord.Interaction, username: str):
        """Retirer un utilisateur du groupe Snapchat"""
        if not await self.is_admin(interaction):
            await interaction.response.send_message(
                "❌ Vous n'avez pas les permissions.",
                ephemeral=True
            )
            return
        
        if not self.is_snapchat_connected or not self.snapchat_client:
            await interaction.response.send_message(
                "❌ Le bot n'est pas connecté à Snapchat.",
                ephemeral=True
            )
            return
        
        await interaction.response.defer(ephemeral=True)
        
        try:
            result = await self.snapchat_client.remove_member(username)
            if result:
                embed = discord.Embed(
                    title="✅ Utilisateur Retiré",
                    description=f"{username} a été retiré du groupe",
                    color=discord.Color.green()
                )
                logger.info(f"Utilisateur {username} retiré par {interaction.user}")
            else:
                embed = discord.Embed(
                    title="❌ Échec",
                    description=f"Impossible de retirer {username}",
                    color=discord.Color.red()
                )
        except Exception as e:
            embed = discord.Embed(
                title="❌ Erreur",
                description=f"Erreur: {str(e)}",
                color=discord.Color.red()
            )
            logger.error(f"Erreur lors du retrait: {str(e)}")
        
        await interaction.followup.send(embed=embed, ephemeral=True)
    
    @app_commands.command(name="remove_all", description="Retirer tous les membres du groupe")
    async def remove_all(self, interaction: discord.Interaction):
        """Retirer tous les membres du groupe"""
        if not await self.is_admin(interaction):
            await interaction.response.send_message(
                "❌ Vous n'avez pas les permissions.",
                ephemeral=True
            )
            return
        
        if not self.is_snapchat_connected or not self.snapchat_client:
            await interaction.response.send_message(
                "❌ Le bot n'est pas connecté à Snapchat.",
                ephemeral=True
            )
            return
        
        await interaction.response.defer(ephemeral=True)
        
        try:
            result = await self.snapchat_client.remove_all_members()
            if result:
                embed = discord.Embed(
                    title="✅ Tous les membres retirés",
                    description=f"Tous les membres ont été supprimés du groupe",
                    color=discord.Color.green()
                )
                logger.warning(f"Tous les membres retirés par {interaction.user}")
            else:
                embed = discord.Embed(
                    title="❌ Échec",
                    description=f"Impossible de retirer tous les membres",
                    color=discord.Color.red()
                )
        except Exception as e:
            embed = discord.Embed(
                title="❌ Erreur",
                description=f"Erreur: {str(e)}",
                color=discord.Color.red()
            )
            logger.error(f"Erreur lors de la suppression: {str(e)}")
        
        await interaction.followup.send(embed=embed, ephemeral=True)
    
    @app_commands.command(name="list_members", description="Lister les membres du groupe")
    async def list_members(self, interaction: discord.Interaction):
        """Lister les membres du groupe Snapchat"""
        if not self.is_snapchat_connected or not self.snapchat_client:
            await interaction.response.send_message(
                "❌ Le bot n'est pas connecté à Snapchat.",
                ephemeral=True
            )
            return
        
        await interaction.response.defer()
        
        try:
            members = await self.snapchat_client.get_members()
            
            if not members:
                embed = discord.Embed(
                    title="👥 Membres du Groupe",
                    description="Aucun membre dans le groupe",
                    color=discord.Color.blue()
                )
            else:
                member_list = "\n".join([f"• {member}" for member in members[:20]])
                if len(members) > 20:
                    member_list += f"\n... et {len(members) - 20} autres"
                
                embed = discord.Embed(
                    title="👥 Membres du Groupe",
                    description=f"**Total: {len(members)} membre(s)**\n\n{member_list}",
                    color=discord.Color.blue()
                )
            
            logger.info(f"Liste des membres affichée à {interaction.user}")
        except Exception as e:
            embed = discord.Embed(
                title="❌ Erreur",
                description=f"Erreur: {str(e)}",
                color=discord.Color.red()
            )
            logger.error(f"Erreur lors de la récupération des membres: {str(e)}")
        
        await interaction.followup.send(embed=embed)
    
    @app_commands.command(name="group_info", description="Informations du groupe")
    async def group_info(self, interaction: discord.Interaction):
        """Afficher les informations du groupe Snapchat"""
        if not self.is_snapchat_connected or not self.snapchat_client:
            await interaction.response.send_message(
                "❌ Le bot n'est pas connecté à Snapchat.",
                ephemeral=True
            )
            return
        
        await interaction.response.defer()
        
        try:
            info = await self.snapchat_client.get_group_info()
            
            embed = discord.Embed(
                title="📊 Informations du Groupe",
                color=discord.Color.blue()
            )
            
            for key, value in info.items():
                embed.add_field(name=key.replace('_', ' ').title(), value=value, inline=True)
            
            logger.info(f"Info groupe affichée à {interaction.user}")
        except Exception as e:
            embed = discord.Embed(
                title="❌ Erreur",
                description=f"Erreur: {str(e)}",
                color=discord.Color.red()
            )
            logger.error(f"Erreur lors de la récupération des infos: {str(e)}")
        
        await interaction.followup.send(embed=embed)
    
    @app_commands.command(name="set_name", description="Changer le nom du groupe")
    async def set_name(self, interaction: discord.Interaction, name: str):
        """Changer le nom du groupe"""
        if not await self.is_admin(interaction):
            await interaction.response.send_message(
                "❌ Vous n'avez pas les permissions.",
                ephemeral=True
            )
            return
        
        if not self.is_snapchat_connected or not self.snapchat_client:
            await interaction.response.send_message(
                "❌ Le bot n'est pas connecté à Snapchat.",
                ephemeral=True
            )
            return
        
        await interaction.response.defer(ephemeral=True)
        
        try:
            result = await self.snapchat_client.set_group_name(name)
            if result:
                embed = discord.Embed(
                    title="✅ Nom Changé",
                    description=f"Le nom du groupe a été changé en: {name}",
                    color=discord.Color.green()
                )
                logger.info(f"Nom du groupe changé en '{name}' par {interaction.user}")
            else:
                embed = discord.Embed(
                    title="❌ Échec",
                    description="Impossible de changer le nom",
                    color=discord.Color.red()
                )
        except Exception as e:
            embed = discord.Embed(
                title="❌ Erreur",
                description=f"Erreur: {str(e)}",
                color=discord.Color.red()
            )
            logger.error(f"Erreur lors du changement de nom: {str(e)}")
        
        await interaction.followup.send(embed=embed, ephemeral=True)
    
    @app_commands.command(name="set_description", description="Changer la description du groupe")
    async def set_description(self, interaction: discord.Interaction, description: str):
        """Changer la description du groupe"""
        if not await self.is_admin(interaction):
            await interaction.response.send_message(
                "❌ Vous n'avez pas les permissions.",
                ephemeral=True
            )
            return
        
        if not self.is_snapchat_connected or not self.snapchat_client:
            await interaction.response.send_message(
                "❌ Le bot n'est pas connecté à Snapchat.",
                ephemeral=True
            )
            return
        
        await interaction.response.defer(ephemeral=True)
        
        try:
            result = await self.snapchat_client.set_group_description(description)
            if result:
                embed = discord.Embed(
                    title="✅ Description Changée",
                    description=f"La description a été changée",
                    color=discord.Color.green()
                )
                logger.info(f"Description du groupe changée par {interaction.user}")
            else:
                embed = discord.Embed(
                    title="❌ Échec",
                    description="Impossible de changer la description",
                    color=discord.Color.red()
                )
        except Exception as e:
            embed = discord.Embed(
                title="❌ Erreur",
                description=f"Erreur: {str(e)}",
                color=discord.Color.red()
            )
            logger.error(f"Erreur lors du changement de description: {str(e)}")
        
        await interaction.followup.send(embed=embed, ephemeral=True)
    
    @app_commands.command(name="logs", description="Afficher les logs récents")
    async def logs(self, interaction: discord.Interaction):
        """Afficher les logs du bot"""
        if not await self.is_admin(interaction):
            await interaction.response.send_message(
                "❌ Vous n'avez pas les permissions.",
                ephemeral=True
            )
            return
        
        await interaction.response.defer(ephemeral=True)
        
        try:
            with open('bot.log', 'r', encoding='utf-8') as f:
                lines = f.readlines()[-20:]
            
            logs_text = ''.join(lines)
            
            if len(logs_text) > 2000:
                chunks = [logs_text[i:i+1900] for i in range(0, len(logs_text), 1900)]
                for chunk in chunks:
                    await interaction.followup.send(f"```\n{chunk}\n```", ephemeral=True)
            else:
                await interaction.followup.send(f"```\n{logs_text}\n```", ephemeral=True)
            
            logger.info(f"Logs affichés à {interaction.user}")
        except Exception as e:
            await interaction.followup.send(
                f"❌ Erreur: {str(e)}",
                ephemeral=True
            )
    
    @app_commands.command(name="status", description="Afficher l'état du bot")
    async def status(self, interaction: discord.Interaction):
        """Afficher l'état du bot"""
        embed = discord.Embed(
            title="🤖 État du Bot",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="Discord",
            value="🟢 Connecté",
            inline=True
        )
        
        embed.add_field(
            name="Snapchat",
            value="🟢 Connecté" if self.is_snapchat_connected else "🔴 Déconnecté",
            inline=True
        )
        
        embed.add_field(
            name="Plateforme",
            value=f"{platform.system()} {platform.release()}",
            inline=True
        )
        
        embed.add_field(
            name="Latence",
            value=f"{self.bot.latency * 1000:.0f}ms",
            inline=True
        )
        
        await interaction.response.send_message(embed=embed)
        logger.info(f"Status affiché à {interaction.user}")
    
    async def is_admin(self, interaction: discord.Interaction) -> bool:
        """Vérifier si l'utilisateur est admin"""
        admin_id = self.config.admin_id
        return interaction.user.id == admin_id or interaction.user.guild_permissions.administrator
    
    def cog_unload(self):
        """Nettoyer quand le cog est déchargé"""
        self.status_update_loop.cancel()
        if self.snapchat_client:
            asyncio.create_task(self.snapchat_client.disconnect())


async def setup(bot):
    """Setup du bot"""
    await bot.add_cog(SnapchatDiscordBot(bot))


if __name__ == "__main__":
    print("""\n
    ╔════════════════════════════════════════╗
    ║   🤖 SNAPCHAT DISCORD BOT 🤖         ║
    ║   Multi-Platform Bot Manager           ║
    ║   Compatible: Termux, Linux, macOS    ║
    ╚════════════════════════════════════════╝
    """)
    
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version.split()[0]}\n")
    
    # Créer le bot
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = commands.Bot(
        command_prefix="!",
        intents=intents,
        help_command=None
    )
    
    config = Config()
    
    @bot.event
    async def on_ready():
        """Événement de démarrage du bot"""
        logger.info(f"✅ Bot connecté en tant que {bot.user}")
        logger.info(f"📊 Serveurs: {len(bot.guilds)}")
        logger.info(f"🖥️ Plateforme: {platform.system()} {platform.release()}")
        
        try:
            synced = await bot.tree.sync()
            logger.info(f"✅ Commandes synchronisées: {len(synced)}")
        except Exception as e:
            logger.error(f"❌ Erreur lors de la synchronisation: {e}")
    
    @bot.event
    async def on_error(event, *args, **kwargs):
        """Gestion des erreurs"""
        logger.error(f"❌ Erreur dans {event}: {sys.exc_info()}")
    
    async def load_cogs():
        await setup(bot)
    
    try:
        asyncio.run(load_cogs())
        print("🚀 Démarrage du bot...\n")
        bot.run(config.discord_token)
    except KeyboardInterrupt:
        logger.info("⛔ Bot arrêté par l'utilisateur")
    except ValueError as e:
        logger.error("❌ Erreur: Token Discord invalide ou manquant")
        logger.error("📝 Assurez-vous que DISCORD_TOKEN est configuré dans .env")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Erreur fatale: {e}")
        sys.exit(1)
