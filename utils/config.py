#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration Module
Gère les variables d'environnement et la configuration
"""

import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

class Config:
    """Classe de configuration"""
    
    def __init__(self):
        """Initialiser la configuration"""
        load_dotenv()
        
        # Discord
        self.discord_token = os.getenv('DISCORD_TOKEN')
        self.discord_guild_id = os.getenv('DISCORD_GUILD_ID')
        
        # Snapchat
        self.snapchat_username = os.getenv('SNAPCHAT_USERNAME')
        self.snapchat_password = os.getenv('SNAPCHAT_PASSWORD')
        self.snapchat_group_id = os.getenv('SNAPCHAT_GROUP_ID')
        
        # Bot
        self.admin_id = int(os.getenv('ADMIN_ID', 0))
        self.bot_prefix = os.getenv('BOT_PREFIX', '!')
        
        # Logging
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')
        self.log_file = os.getenv('LOG_FILE', 'bot.log')
        
        # Validation
        self._validate()
    
    def _validate(self):
        """Valider la configuration"""
        errors = []
        
        if not self.discord_token:
            errors.append("DISCORD_TOKEN not set")
        if not self.snapchat_username:
            errors.append("SNAPCHAT_USERNAME not set")
        if not self.snapchat_password:
            errors.append("SNAPCHAT_PASSWORD not set")
        if self.admin_id == 0:
            errors.append("ADMIN_ID not set")
        
        if errors:
            logger.warning("⚠️ Configuration warnings:")
            for error in errors:
                logger.warning(f"  - {error}")
        else:
            logger.info("✅ Configuration validée")
    
    def get_all(self) -> dict:
        """Récupérer toute la configuration (sans données sensibles)"""
        return {
            'discord_token': '***' if self.discord_token else None,
            'discord_guild_id': self.discord_guild_id,
            'snapchat_username': self.snapchat_username,
            'snapchat_group_id': self.snapchat_group_id,
            'admin_id': self.admin_id,
            'bot_prefix': self.bot_prefix,
            'log_level': self.log_level
        }
