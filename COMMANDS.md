# 📚 Liste Complète des Commandes Discord

## 🎮 Commandes du Panel

### `/panel`
**Description**: Affiche le panel principal avec tous les menus disponibles

**Permissions**: Admin

**Exemple**:
```
/panel
```

**Réponse**: Panel avec tous les sous-menus

---

## 👥 Gestion des Membres

### `/add_user`
**Description**: Ajouter un utilisateur Snapchat au groupe

**Paramètres**:
- `username` (requis): Le username Snapchat à ajouter

**Permissions**: Admin

**Exemple**:
```
/add_user username123
```

**Réponse**:
```
✅ Utilisateur Ajouté
username123 a été ajouté au groupe
```

---

### `/remove_user`
**Description**: Retirer un utilisateur Snapchat du groupe

**Paramètres**:
- `username` (requis): Le username Snapchat à retirer

**Permissions**: Admin

**Exemple**:
```
/remove_user username123
```

**Réponse**:
```
✅ Utilisateur Retiré
username123 a été retiré du groupe
```

---

### `/remove_all`
**Description**: Retirer TOUS les membres du groupe Snapchat

⚠️ **ATTENTION**: Cette action est irréversible!

**Permissions**: Admin

**Exemple**:
```
/remove_all
```

**Résultat**: Tous les membres sont supprimés

---

### `/list_members`
**Description**: Lister tous les membres du groupe Snapchat

**Paramètres**: Aucun

**Exemple**:
```
/list_members
```

**Réponse**:
```
👥 Membres du Groupe
Total: 5 membre(s)

• user1
• user2
• user3
• user4
• user5
```

---

## 📊 Gestion du Groupe

### `/group_info`
**Description**: Afficher les informations du groupe Snapchat

**Paramètres**: Aucun

**Exemple**:
```
/group_info
```

**Réponse**:
```
📊 Informations du Groupe

Nom: Mon Groupe
ID: 123456
Membres: 10
Créateur: votreusername
Statut: 🟢 Actif
Plateforme: Linux
```

---

### `/set_name`
**Description**: Changer le nom du groupe Snapchat

**Paramètres**:
- `name` (requis): Le nouveau nom du groupe

**Permissions**: Admin

**Exemple**:
```
/set_name "Nouveau Nom du Groupe"
```

**Réponse**:
```
✅ Nom Changé
Le nom du groupe a été changé en: Nouveau Nom du Groupe
```

---

### `/set_description`
**Description**: Changer la description du groupe

**Paramètres**:
- `description` (requis): La nouvelle description

**Permissions**: Admin

**Exemple**:
```
/set_description "Ceci est une nouvelle description"
```

**Réponse**:
```
✅ Description Changée
La description a été changée
```

---

## 🔧 Commandes Administration

### `/connect_snapchat`
**Description**: Se connecter au compte Snapchat

**Paramètres**: Aucun

**Permissions**: Admin

**Exemple**:
```
/connect_snapchat
```

**Réponse**:
```
✅ Connexion Réussie
Connecté au compte Snapchat avec succès!
```

---

### `/disconnect_snapchat`
**Description**: Se déconnecter du compte Snapchat

**Paramètres**: Aucun

**Permissions**: Admin

**Exemple**:
```
/disconnect_snapchat
```

**Réponse**:
```
✅ Déconnexion Réussie
Déconnecté du compte Snapchat.
```

---

### `/status`
**Description**: Afficher l'état du bot (Discord et Snapchat)

**Paramètres**: Aucun

**Exemple**:
```
/status
```

**Réponse**:
```
🤖 État du Bot

Discord: 🟢 Connecté
Snapchat: 🟢 Connecté
Plateforme: Linux
Latence: 45ms
```

---

### `/logs`
**Description**: Afficher les 20 dernières lignes des logs du bot

**Paramètres**: Aucun

**Permissions**: Admin

**Exemple**:
```
/logs
```

**Réponse**: Affiche les logs du bot

---

## 📋 Table Résumée

| Commande | Paramètres | Admin | Description |
|----------|-----------|-------|-------------|
| `/panel` | - | ✅ | Panel principal |
| `/add_user` | username | ✅ | Ajouter un utilisateur |
| `/remove_user` | username | ✅ | Retirer un utilisateur |
| `/remove_all` | - | ✅ | Retirer tous les membres |
| `/list_members` | - | ✅ | Lister les membres |
| `/group_info` | - | - | Info du groupe |
| `/set_name` | name | ✅ | Changer le nom |
| `/set_description` | description | ✅ | Changer la description |
| `/connect_snapchat` | - | ✅ | Se connecter |
| `/disconnect_snapchat` | - | ✅ | Se déconnecter |
| `/status` | - | - | État du bot |
| `/logs` | - | ✅ | Voir les logs |

---

## 🎯 Workflows Typiques

### Workflow 1: Démarrage complet

```bash
/panel                    # Voir les options
/status                   # Vérifier la connexion
/connect_snapchat         # Connecter Snapchat
```

### Workflow 2: Gestion des membres

```bash
/list_members             # Voir la liste actuelle
/add_user user1           # Ajouter des users
/add_user user2
/add_user user3
/list_members             # Vérifier les ajouts
```

### Workflow 3: Nettoyage complet

```bash
/list_members             # Voir qui est dedans
/remove_all               # Retirer TOUS d'un coup
/list_members             # Vérifier (liste vide)
```

### Workflow 4: Maintenance

```bash
/group_info               # Infos du groupe
/status                   # État du bot
/logs                     # Voir l'historique
```

---

## ⚠️ Notes Importantes

### Permissions
- 🔐 Seuls les **admins** peuvent utiliser les commandes d'administration
- ✅ N'importe qui peut voir `/group_info` et `/status`
- 📝 Toutes les actions sont **loggées** dans `bot.log`

### Sécurité
- 🔒 Ne JAMAIS partager les logs avec les identifiants
- ⚠️ `/remove_all` est irréversible!
- 🔄 Les actions Snapchat demandent une connexion active

### Performance
- ⏱️ Le bot met à jour son statut toutes les minutes
- 🌐 Les requêtes Snapchat peuvent être throttlées
- 📊 Les statistiques se mettent à jour en temps réel

---

## 🔍 Dépannage des Commandes

### "Slash command not found"
- Attendre quelques minutes (sync des commands)
- Redémarrer le bot
- Vérifier que le bot a les permissions

### "You don't have permission"
- Vérifier que votre ID est dans ADMIN_ID du .env
- Vérifier que vous êtes admin du serveur

### "Bot is not connected to Snapchat"
- Utiliser `/connect_snapchat` d'abord
- Vérifier les logs: `tail -f bot.log`

---

## 📞 Support

Pour toute question:
- Consultez le README.md
- Consultez SETUP_TERMUX.md pour Termux
- Vérifiez les logs: `tail -f bot.log`
- Créez une issue sur GitHub

---

**Version:** 1.0.0
**Dernière mise à jour:** 2024
