#0x0B. SSH

##Introduction

When accessing a computer over a network, system administrators need a secure connection to hide from malicious cyber-attacks, such as password-sniffing. As large networks have security flaws, encryption protocols such as TLS/SSL, IPsec, S/MIME, PGP, and SSH are necessary to ensure necessary protection.

0-use_a_private_key

Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:

Only use ssh single-character flags
You cannot use -l
You do not need to handle the case of a private key protected by a passphrase

1-create_ssh_key_pair
Write a Bash script that creates an RSA key pair.

Requirements:

Name of the created private key must be school
Number of bits in the created key to be created 4096
The created key must be protected by the passphrase betty


