# 📱 Guide d'Installation sur Termux

## 🎯 Vue d'ensemble

Ce guide vous permettra d'installer et d'exécuter le Snapchat Discord Bot sur **Termux** (Android).

---

## ✅ Prérequis

- Android 7+
- [Termux](https://termux.com/) installé
- Connexion Internet stable
- ~500MB d'espace disque

---

## 🚀 Installation Complète

### Étape 1: Mise à jour du système

```bash
# Mettre à jour la liste des paquets
pkg update

# Mettre à jour tous les paquets
pkg upgrade -y
```

### Étape 2: Installation des dépendances système

```bash
# Installer Python
pkg install python -y

# Installer pip
pkg install python-pip -y

# Installer Git
pkg install git -y

# Installer wget (optionnel)
pkg install wget -y

# Installer curl (optionnel)
pkg install curl -y

# Installer nano (éditeur de texte)
pkg install nano -y
```

### Étape 3: Cloner le repository

```bash
# Créer un dossier pour les projets
mkdir -p ~/projects
cd ~/projects

# Cloner le bot
git clone https://github.com/chauferra90k-cmyk/snapchat-discord-bot.git

# Aller dans le dossier
cd snapchat-discord-bot

# Vérifier le contenu
ls -la
```

### Étape 4: Créer un environnement virtuel

```bash
# Créer l'environnement
python -m venv venv

# Activer l'environnement
source venv/bin/activate

# Vous devriez voir (venv) au début du prompt
```

### Étape 5: Installer les dépendances Python

```bash
# Mettre à jour pip
pip install --upgrade pip

# Installer les dépendances
pip install -r requirements.txt

# En cas d'erreur:
pip install --no-cache-dir -r requirements.txt
```

### Étape 6: Configuration

```bash
# Copier l'exemple de configuration
cp .env.example .env

# Éditer la configuration
nano .env
```

**Remplir les champs:**
```env
DISCORD_TOKEN=your_token_here
SNAPCHAT_USERNAME=your_username
SNAPCHAT_PASSWORD=your_password
ADMIN_ID=your_discord_id
```

**Pour sauvegarder avec nano:**
- Ctrl + O (Output)
- Entrée
- Ctrl + X (Exit)

---

## ▶️ Lancer le Bot

### Première utilisation

```bash
# S'assurer que l'environnement est activé
source venv/bin/activate

# Lancer le bot
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

### Quitter le bot

```bash
# Appuyer sur Ctrl+C
Ctrl+C
```

---

## 🔄 Maintenir le Bot Actif

### Option 1: Avec tmux (Recommandé ⭐)

#### Installation de tmux

```bash
pkg install tmux -y
```

#### Lancer le bot dans tmux

```bash
# Créer une session tmux nommée "bot"
tmux new-session -d -s bot "cd ~/projects/snapchat-discord-bot && source venv/bin/activate && python bot.py"

# Vérifier que la session fonctionne
tmux list-sessions
```

#### Voir les logs du bot

```bash
# Accrocher la session
tmux attach-session -t bot

# Quitter sans arrêter le bot:
# Ctrl+B puis D
```

#### Arrêter le bot

```bash
# Aller dans la session
tmux attach-session -t bot

# Appuyer sur Ctrl+C
Ctrl+C

# Quitter la session: exit ou Ctrl+D
```

#### Vérifier si le bot tourne

```bash
# Voir les sessions tmux
tmux list-sessions

# Voir les logs récents
grep "Bot connecté" ~/projects/snapchat-discord-bot/bot.log
```

### Option 2: Avec nohup

```bash
# Lancer le bot
cd ~/projects/snapchat-discord-bot
source venv/bin/activate
nohup python bot.py > bot_output.log 2>&1 &

# Voir le processus
ps aux | grep python

# Voir les logs
tail -f bot_output.log
```

### Option 3: Script de lancement

Créez `start_bot.sh`:

```bash
#!/bin/bash
cd ~/projects/snapchat-discord-bot
source venv/bin/activate
python bot.py
```

Puis:

```bash
# Rendre exécutable
chmod +x start_bot.sh

# Lancer
./start_bot.sh
```

---

## 📝 Commandes Utiles

### Navigation

```bash
# Aller dans le dossier du bot
cd ~/projects/snapchat-discord-bot

# Lister les fichiers
ls -la

# Voir l'espace disque
df -h

# Voir la RAM utilisée
free -h
```

### Gestion de l'environnement

```bash
# Activer l'environnement virtuel
source venv/bin/activate

# Désactiver
deactivate

# Vérifier la version de Python
python --version

# Lister les packages installés
pip list

# Mettre à jour pip
pip install --upgrade pip
```

### Logs et débogage

```bash
# Voir les 20 dernières lignes des logs
tail -20 bot.log

# Voir les logs en temps réel
tail -f bot.log

# Chercher une erreur spécifique
grep "ERROR" bot.log

# Compter les lignes des logs
wc -l bot.log

# Vider les logs
echo "" > bot.log
```

### Gestion des processus

```bash
# Voir les processus Python
ps aux | grep python

# Tuer un processus
kill -9 <PID>

# Tuer tous les processus python
killall python
```

---

## 🔧 Dépannage Termux

### Erreur: "Permission denied"

```bash
# Vérifier les permissions
ls -la bot.py

# Ajouter la permission d'exécution
chmod +x bot.py

# Relancer
python bot.py
```

### Erreur: "ModuleNotFoundError"

```bash
# S'assurer que l'environnement est activé
source venv/bin/activate

# Réinstaller les dépendances
pip install -r requirements.txt

# Ou installer le package spécifique
pip install discord.py
```

### Erreur: "No space left on device"

```bash
# Vérifier l'espace
df -h

# Nettoyer le cache pip
pip cache purge

# Supprimer les logs volumineux
rm bot.log
```

### Le bot s'arrête aléatoirement

- Utiliser **tmux** pour maintenir la session
- Vérifier la connexion Internet
- Vérifier que Termux a les permissions nécessaires
- Éviter les arrêts en mode économie d'énergie

### Erreur: "ModuleNotFoundError: No module named 'discord'"

```bash
# Vérifier l'activation de l'environnement
which python

# Doit afficher: /data/data/com.termux/files/usr/bin/python

# Sinon:
source venv/bin/activate
which python
# Doit afficher: /path/to/venv/bin/python
```

---

## 🌐 Configuration Firewall/Réseau

### Sur Termux

```bash
# Vérifier la connexion Internet
ping 8.8.8.8

# Vérifier la connectivité Discord
python -c "import socket; socket.create_connection(('discord.com', 443), timeout=5); print('OK')"

# Vérifier les ports en écoute
netstat -ln | grep LISTEN
```

---

## 📊 Monitoring

### Créer un script de monitoring

`monitor_bot.sh`:

```bash
#!/bin/bash
while true; do
  echo "=== État du bot ==="
  ps aux | grep python | grep -v grep
  echo ""
  echo "=== Derniers logs ==="
  tail -5 ~/projects/snapchat-discord-bot/bot.log
  echo ""
  sleep 60
done
```

Puis:

```bash
chmod +x monitor_bot.sh
./monitor_bot.sh
```

---

## ✨ Tips & Astuces

### 1. Garder Termux actif

- Settings > Keep-Alive > ON
- Mettre Termux en liste blanche du gestionnaire de batterie
- Ne pas nettoyer l'app en arrière-plan

### 2. Performance

```bash
# Lancer avec nice pour utiliser peu de CPU
nice -n 19 python bot.py

# Limiter la RAM
ulimit -v 512000  # 512MB
```

### 3. Mises à jour

```bash
# Mettre à jour le bot
cd ~/projects/snapchat-discord-bot
git pull origin main
pip install -r requirements.txt
```

### 4. Backup

```bash
# Sauvegarder la configuration
cp .env .env.backup
cp snapchat_data.json snapchat_data.json.backup
```

---

## 🎯 Workflow Complet

### Première utilisation

```bash
pkg update && pkg upgrade -y
pkg install python python-pip git tmux nano -y

cd ~/projects
git clone https://github.com/chauferra90k-cmyk/snapchat-discord-bot.git
cd snapchat-discord-bot

python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

cp .env.example .env
nano .env  # Configurer

python bot.py
```

### Lancer en arrière-plan

```bash
cd ~/projects/snapchat-discord-bot
source venv/bin/activate
tmux new-session -d -s bot "python bot.py"

# Vérifier
tmux list-sessions
```

### Accéder aux logs

```bash
cd ~/projects/snapchat-discord-bot
tail -f bot.log
```

---

## 🔗 Ressources

- [Termux Documentation](https://termux.com/)
- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [tmux Cheat Sheet](https://tmuxcheatsheet.com/)
- [Python 3 Documentation](https://docs.python.org/3/)

---

## 📞 Support

Pour toute question ou problème:
- Consultez les logs: `tail -f bot.log`
- Créez une issue sur GitHub
- Lisez le README principal

---

**Version:** 1.0.0
**Dernière mise à jour:** 2024
