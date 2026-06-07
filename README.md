# 🤖 Snapchat Discord Bot

**Un bot Discord puissant capable de se connecter à un compte Snapchat et de modérer un groupe Snapchat avec un panel de contrôle complet.**

> ✅ **Compatible**: Termux (Android) | Linux | macOS | Windows

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Discord.py](https://img.shields.io/badge/Discord.py-2.3.2-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Fonctionnalités

✅ Connexion à un compte Snapchat
✅ Panel Discord interactif pour contrôler le bot Snapchat
✅ Ajouter/Supprimer des utilisateurs du groupe
✅ Supprimer tous les membres du groupe
✅ Gestion des permissions
✅ **Compatible avec Termux (Android)**
✅ Compatible Linux, macOS, Windows
✅ Logs et historique des actions
✅ Détection automatique de la plateforme
✅ Support Unicode/Émojis complet

---

## 📋 Table des matières

- [Installation](#installation)
- [Configuration](#configuration)
- [Lancement](#lancement)
- [Commandes](#commandes)
- [Dépannage](#dépannage)
- [Structure](#structure)
- [License](#license)

---

## 🚀 Installation

### Prérequis

- **Python 3.8+**
- **Git**
- **pip** (gestionnaire de paquets Python)

### Sur Termux (Android)

```bash
# Mettre à jour les packages
pkg update && pkg upgrade -y

# Installer les dépendances
pkg install python python-pip git -y

# Cloner le repository
git clone https://github.com/chauferra90k-cmyk/snapchat-discord-bot.git
cd snapchat-discord-bot

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate

# Installer les dépendances Python
pip install --upgrade pip
pip install -r requirements.txt
```

### Sur Linux / macOS

```bash
# Cloner le repository
git clone https://github.com/chauferra90k-cmyk/snapchat-discord-bot.git
cd snapchat-discord-bot

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt
```

### Sur Windows

```bash
# Cloner le repository
git clone https://github.com/chauferra90k-cmyk/snapchat-discord-bot.git
cd snapchat-discord-bot

# Créer un environnement virtuel
python -m venv venv
venv\Scripts\activate

# Installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### 1. Créer un bot Discord

1. Allez sur [Discord Developer Portal](https://discord.com/developers/applications)
2. Cliquez sur "New Application"
3. Donnez un nom à votre application
4. Allez dans l'onglet "Bot"
5. Cliquez sur "Add Bot"
6. Copiez le token sous le nom du bot

### 2. Obtenir vos IDs Discord

1. Activez le mode développeur (User Settings > Advanced > Developer Mode)
2. Clic droit sur votre profil > Copier l'ID utilisateur

### 3. Créer le fichier .env

```bash
# Copier le fichier d'exemple
cp .env.example .env

# Éditer avec un éditeur (nano, vim, etc.)
nano .env
```

### 4. Configurer les variables

```env
# Discord
DISCORD_TOKEN=votre_token_discord
DISCORD_GUILD_ID=id_du_serveur_discord

# Snapchat
SNAPCHAT_USERNAME=votre_username_snapchat
SNAPCHAT_PASSWORD=votre_password_snapchat
SNAPCHAT_GROUP_ID=id_du_groupe_snapchat

# Admin
ADMIN_ID=votre_id_discord

# Logging
LOG_LEVEL=INFO
LOG_FILE=bot.log
```

---

## ▶️ Lancement

### Activation de l'environnement

**Termux/Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### Démarrage du bot

```bash
python bot.py
```

Vous devriez voir:
```
╔════════════════════════════════════════╗
║   🤖 SNAPCHAT DISCORD BOT 🤖         ║
║   Multi-Platform Bot Manager           ║
║   Compatible: Termux, Linux, macOS    ║
╚════════════════════════════════════════╝

Platform: Linux
Python: 3.10.12

🚀 Démarrage du bot...
```

### Maintenir le bot en arrière-plan

#### Option 1: Avec tmux (Recommandé)

```bash
# Installer tmux
pkg install tmux  # Termux
brew install tmux  # macOS
apt install tmux  # Linux

# Créer une session
tmux new-session -d -s bot "cd ~/snapchat-discord-bot && source venv/bin/activate && python bot.py"

# Voir les logs
tmux attach-session -t bot

# Quitter sans arrêter: Ctrl+B puis D
```

#### Option 2: Avec nohup

```bash
nohup python bot.py > bot_output.log 2>&1 &
tail -f bot_output.log
```

#### Option 3: Avec systemd (Linux)

Créez `/etc/systemd/system/snapchat-bot.service`:

```ini
[Unit]
Description=Snapchat Discord Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/snapchat-discord-bot
ExecStart=/usr/bin/python3 bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Puis:
```bash
sudo systemctl daemon-reload
sudo systemctl enable snapchat-bot
sudo systemctl start snapchat-bot
```

---

## 🎮 Commandes Discord

### Panel Principal

| Commande | Description |
|----------|-------------|
| `/panel` | Affiche le panel de contrôle principal |
| `/status` | État du bot |

### Gestion des Membres

| Commande | Description |
|----------|-------------|
| `/add_user <username>` | Ajouter un utilisateur |
| `/remove_user <username>` | Retirer un utilisateur |
| `/remove_all` | Retirer TOUS les membres ⚠️ |
| `/list_members` | Lister les membres |

### Gestion du Groupe

| Commande | Description |
|----------|-------------|
| `/group_info` | Informations du groupe |
| `/set_name <nom>` | Changer le nom |
| `/set_description <desc>` | Changer la description |

### Administration

| Commande | Description |
|----------|-------------|
| `/connect_snapchat` | Se connecter à Snapchat |
| `/disconnect_snapchat` | Se déconnecter |
| `/logs` | Afficher les logs |

---

## 🐛 Dépannage

### Erreur: "Token Discord invalide"

```bash
# Vérifier que le token est correct dans .env
grep DISCORD_TOKEN .env

# Régénérer le token dans Discord Developer Portal
```

### Erreur: "Module not found"

```bash
# Réinstaller les dépendances
pip install -r requirements.txt

# Ou mettre à jour pip
pip install --upgrade pip
```

### Le bot se ferme immédiatement

```bash
# Vérifier les logs
tail -f bot.log

# Vérifier que .env existe
ls -la .env
```

### Problème de connexion Snapchat

- Vérifier le username et password
- Vérifier la connexion internet
- Vérifier que le compte n'est pas banni
- Vérifier les logs: `tail -f bot.log`

### Sur Termux: "Permission denied"

```bash
# Rendre le script exécutable
chmod +x bot.py

# Ou utiliser python explicitement
python bot.py
```

---

## 📁 Structure du Projet

```
.
├── bot.py                 # Bot Discord principal
├── snapchat_client.py    # Client Snapchat
├── requirements.txt      # Dépendances Python
├── package.json          # Métadonnées du projet
├── .env.example          # Exemple de configuration
├── .gitignore            # Fichiers à ignorer
├── README.md             # Documentation
├── SETUP_TERMUX.md       # Guide Termux détaillé
├── COMMANDS.md           # Liste des commandes
└── utils/
    ├── config.py         # Configuration
    └── logger.py         # Logging
```

---

## 📊 Utilisation Typique

### 1. Démarrage
```bash
/panel
/status
/connect_snapchat
```

### 2. Gestion des membres
```bash
/list_members
/add_user username1
/add_user username2
/list_members
```

### 3. Maintenance
```bash
/group_info
/logs
/status
```

---

## ⚠️ Notes Importantes

🔐 **Sécurité:**
- Ne JAMAIS partager votre `.env`
- Ne JAMAIS publier vos tokens
- Utiliser un compte Snapchat dédié si possible

⏱️ **Throttling:**
- Snapchat peut limiter les requêtes
- Ajouter des délais entre les actions si nécessaire

📱 **Termux:**
- Garder l'application active en arrière-plan
- Utiliser tmux ou nohup pour les sessions longues

---

## 🤝 Contribution

Les contributions sont bienvenues! N'hésitez pas à:
- Signaler des bugs
- Proposer des améliorations
- Faire des pull requests

---

## 📜 License

Ce projet est sous license **MIT**. Voir [LICENSE](LICENSE) pour plus de détails.

---

## 📞 Support

Pour les problèmes:
- Consultez [COMMANDS.md](COMMANDS.md) pour la liste complète des commandes
- Vérifiez [SETUP_TERMUX.md](SETUP_TERMUX.md) pour l'installation sur Termux
- Consultez les logs: `tail -f bot.log`
- Créez une issue sur GitHub

---

## 🙏 Crédits

Créé par: **chauferra90k-cmyk**

Propulsé par:
- [discord.py](https://github.com/Rapptz/discord.py)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [aiofiles](https://github.com/Tinche/aiofiles)

---

**Dernière mise à jour:** 2024
**Version:** 1.0.0
