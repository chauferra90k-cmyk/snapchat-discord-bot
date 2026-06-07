#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Logger Module
Gestion personnalisée des logs
"""

import logging
import os
from datetime import datetime

try:
    from colorama import Fore, Style, init
    HAS_COLORAMA = True
    init(autoreset=True)
except ImportError:
    HAS_COLORAMA = False

class ColoredFormatter(logging.Formatter):
    """Formateur personnalisé avec couleurs"""
    
    COLORS = {
        'DEBUG': '\033[36m',      # Cyan
        'INFO': '\033[32m',       # Green
        'WARNING': '\033[33m',    # Yellow
        'ERROR': '\033[31m',      # Red
        'CRITICAL': '\033[1;31m'  # Bright Red
    }
    RESET = '\033[0m'
    
    def format(self, record):
        """Formater les logs avec couleurs"""
        if HAS_COLORAMA:
            log_color = self.COLORS.get(record.levelname, '')
            record.levelname = f"{log_color}{record.levelname}{self.RESET}"
        else:
            log_color = self.COLORS.get(record.levelname, '')
            if log_color:
                record.levelname = f"{log_color}{record.levelname}{self.RESET}"
        
        return super().format(record)

def setup_logger(name: str, log_file: str = None, level: str = 'INFO') -> logging.Logger:
    """Configurer un logger personnalisé"""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Handler console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # Formateur console avec couleurs
    console_formatter = ColoredFormatter(
        '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # Handler fichier si spécifié
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(level)
        
        file_formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S'
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    
    return logger
