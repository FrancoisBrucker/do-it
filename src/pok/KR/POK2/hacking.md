---
layout: layout/post.njk

title: "Hacking-Guide"
authors:
  - Kasimir Romer
---
## Collection de thèmes
(en allemand seulement, va etre supprimé a la fin)
1. Einleitung
    1. Was ist ein CTF?
    2. Vorgehen: alles mitschreiben, was man gemacht hat, was funktioniert hat und was nicht funktioniert hat (Writeup)
2. Wichtige Kommandozeilen-Befehle und Tools (z.B. CyberChef)
    1. Kali Linux (Tutorial verlinken, um das in VirtualBox zu nutzen)
    2. CyberChef - Kann quasi alles, sehr mächtiges “magic”-tool
    3. Linux-Basics benötigt (ls, cd, Kommandozeilenparameter…)
2. Informationsbeschaffung/Recon (Google, Shodan, Social Media, nmap …)
    1. nmap auf eine IP-Range
    2. Shodan
3. Passwort-Cracking
    1. Passwort-Listen
    2. Jack the ripper
4. Web Exploitation
    1. Verändern von GET-Parametern
    2. SQL Injection
5. Forensik (Filetype herausfinden, strings, …)
    1. file und string commands
    2. pcap 
6. Vulnerabilities ausnutzen mit Metasploit
7. Ausblick auf weiteres
    1. Wichtig, selbst zu googeln
    2. Cryptographie…

## Introduction
### Hacking, das ist doch etwas schlechtes
- Sich gegen Angreifer wehren können
- Denken wie angreifer und ihnen zuvorkommen

### CTFs
- spielerische Art, verschiedene IT-Security-Techniken zu lernen und anzuwenden
- es gibt nicht so viele Möglichkeiten außerhalb, Hacking auszuprobieren, da es illegal ist, wenn die andere Partei nicht zustimmt

### Prerequis
- Umgang mit der Kommandozeile
- Googeln können (wie nutzt man tools richtig)
- alles andere lernt man im Prozess selbst

### Ce document
- entstand als POK, Themenauswahl mehr oder weniger willkürlich
- soll eine Einführung in basic Hacking-Technologien geben
- darf sehr gerne erweitert werden

{% exercice %}
Aufgaben, die helfen können, den Abschnitt zu verstehen
{% endexercice %}

## Outils importants
- für verschiedene Aufgaben gibt es verschiedene Tools

### Schweizer Taschenmesser: CyberChef
(https://gchq.github.io/CyberChef/)
- Base64
- Unzip
- erkennen von eingebetteten Daten
- Verbinden von Operationen als sogenannte Rezepte

{% exercice %}
Rumprobieren, was alles geht.
{% endexercice %}
