# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 21:12:47 2025

Programmet simulerer et support dashboard hos telefonselskapet MORSE
Dashboardet benytter supportloggen som føres av supportavdelingen.
Vi skal analysere loggen for uke 24
Alle de 6 deloppgaven er besvart i denne .py filen

@author: ole.skurdal (olsku9661@usn.no)
"""

import pandas as pd  # Funksjoner for å behandle Excel filer
import numpy as np  # Bl.a NumPy-arrays
import matplotlib.pyplot as plt  # Plotte bibliotek m.m.
from collections import Counter  # Brukes i del B


#%% Del a) Les inn filen support_uke_24.xlsx 
# Den underliggende data strukturen fra innlesingen med Pandas blir NumPy arrays

print("\nProsjektoppgave - PY1010-1 24H Grunnleggende programmering med Python")

supportData = pd.read_excel("support_uke_24.xlsx")

u_dag = supportData["Ukedag"].values
kl_slett = supportData["Klokkeslett"].values
varighet = supportData["Varighet"].values
score = supportData["Tilfredshet"].values

N = len(u_dag)
print("\n\tAnalyse for telefonselskapet MORSE")
print("\nOppgave Del A)")
# Kan bruke ANSI escape sekvenser for å markere tekst i enkelte console vinduer (underline)
print("\033[4m\nSupportloggen for uke 24 viser at vi hadde", N, "henvendelser\n\033[0m")

"""
# Bruk denne for å sjekke at alt fra filen er lest inn riktig
for i in range(0, N):
    print("i =", i, u_dag[i], kl_slett[i], varighet[i], score[i])
"""

#%% Del b) Finn antall henvendelser per ukedag, visualiser med stolpediagram

print("Oppgave Del B)")
print("Se visualisert søylediagram\n")

# Bruker collections hvor elementene (ukedagene) lagres som dictionary nøkler og antall lagres som dictionary verdier
# Tell hvor mange ganger hver ukedag forekommer
alleDager = Counter(u_dag)

# Lag 2 lister fra dictionaryen
ukedager = list(alleDager.keys())
antall = list(alleDager.values())
#print(ukedager, antall)  # Bare sjekke at alt er der

# Visualisering av henvendelsene ved søyle/stople diagram
plt.close('all')
plt.figure(1, figsize=(8, 5))

# Bruk av fonter og farger
font1 = {'family':'serif','color':'blue','size':15}
font2 = {'family':'serif','color':'darkred','size':12}
useColors = ["deepskyblue", "darkcyan", "darkmagenta", "darkorchid", "darkseagreen"]

# Lag labels
plt.title("Oversikt henvendelser uke 24", fontdict = font1)
plt.xlabel("Ukedager", fontdict = font2)
plt.ylabel("Henvendelser", fontdict = font2)

plt.grid(axis = 'y', color = 'green', linestyle = '--', linewidth = 0.5)

plt.bar(ukedager, antall, color = useColors[:len(ukedager)])

# Plott antall henvendelser på toppen av hver søyle som tekst (Ref: Prog 4.5 fra boka)
offset_antall = 0.5
for k in range(0, len(ukedager)):
    plt.text(ukedager[k], antall[k]+offset_antall, str(antall[k]))
    
plt.savefig('HenvendelserBarOle.pdf', format='pdf')
plt.show()


#%% Del c) Finn minste og lengste samtaletid i loggen for uke 24
# Varighet ser slik ut: 00:10:29 

print("Oppgave Del C)")
# Funksjon som deler opp tiden (varigheten) - ingen retur verdi
def delOppTid(heleTiden):
    # Splitt opp varigheten i time, minutt og sekund
    time, minutt, sekund = heleTiden.split(":")
    print(f"Samtalen varte i {time} timer, {minutt} minutter og {sekund} sekunder\n")

# Finn minste samtaletid og kall funksjonen for å splitte tiden, bruker arrayen: varighet
minsteS = min(varighet)
print("I uke 24 var den korteste support samtalen på:", minsteS)
# Kall funksjon for å splitte tids elementene - trenger ikke retur verdier
delOppTid(minsteS)

# Finn lengste samtaletid
lengsteS = max(varighet)
print("I uke 24 var den lengste support samtalen på:", lengsteS)
delOppTid(lengsteS)


#%% Del d) Finn gjennomsnittelig samtaletid for alle henvendelser i loggen for uke 24

# Bruker to funksjoner
# Leser arryen "varighet"

def varighetSekunder(enTid):
    # Splitt opp varigheten i time, minutt og sekunder, legg de sammen og returner alt i sekunder
    timer, minutter, sekunder = map(int, enTid.split(":"))
    #print("Timer:", timer, "Minutter:", minutter, "Sekunder:", sekunder)  # Sjekkpunkt
    return timer * 3600 + minutter * 60 + sekunder

def beregnGjennomsnitt(varighet):
    # Gjør om alle tidene til sekunder, legg sammen og beregn gjennomsnitt
    totaltSekunder = sum(varighetSekunder(tid) for tid in varighet)
    gjSnittSekunder = totaltSekunder / len(varighet)
    return gjSnittSekunder

# Formatet på en varighet: "00:09:53"
gjSnittSekunder = beregnGjennomsnitt(varighet)

# Konverter gjennomsnitt tilbake til hh:mm:ss formatet
timer = int(gjSnittSekunder // 3600)  # Rund ned til nærmeste hele tall
minutter = int((gjSnittSekunder % 3600) // 60)
sekunder = int(gjSnittSekunder % 60)

print("Oppgave Del D)")
print(f"Gjennomsnittelig samtaletid alle henvendelser uke 24: {timer:02}:{minutter:02}:{sekunder:02}")
print(f"Den gjennomsnittelige samtalen varte i {timer} timer, {minutter} minutter og {sekunder} sekunder")


#%% Del e) Finn antall henvendelser i de 4 periodene 08-10, 10-12, 12-14 og 14-16
# Kan gjenbruke oppdelingen fra tidligere
# Ressurrs: https://www.w3schools.com/python/matplotlib_pie_charts.asp

print("\nOppgave Del E)")
print("Se visualisert sektordiagram")

sTid1 = sTid2 = sTid3 = sTid4 = 0

# Splitt opp kl_slett i time, minutt og sekund, trenger bare timen
for klsTid in kl_slett:
    time, minutt, sekund = map(int, klsTid.split(":"))
    #print(f"Klokken {time} timer, {minutt} minutter og {sekund} sekunder\n")  # Sjekkpunkt
    # Gjør det enkelt med en if-elif kjede
    if time < 10:
        sTid1 += 1
    elif time >= 10 and time < 12:
        sTid2 += 1 
    elif time >= 12 and time < 14:
        sTid3 += 1 
    elif time >= 14 and time < 16:
        sTid4 += 1 
        
# Data til sektordiagrammet, en liste med henvendelser i gitt tidsrom
#tidsRom = [sTid1, sTid2, sTid3, sTid4]
#myLabels = ["08-10", "10-12", "12-14", "14-16"]
# Flytter litt på rekkefølgen for en bedre visning av tiden på dagen
tidsRom = [sTid4, sTid3, sTid2, sTid1]
myLabels = ["14-16", "12-14", "10-12", "08-10"]

# Skriver tallene til konsollet
print("Antall henvendelser i løpet av dagen:")
print("Kl: 08-10 =", sTid1, " - Kl: 10-12 =", sTid2, " - Kl: 12-14 =", sTid3, " - Kl: 14-16 =", sTid4)

# Plotting
plt.close('all')
plt.figure(2, figsize=(12, 9))

# Lag labels
plt.title("Henvendelser til supportavdelingen\nFordeling i tidsrom")

plt.pie(tidsRom, labels = myLabels, autopct='%1.1f%%', startangle = 270, colors = useColors[:len(tidsRom)])
plt.legend(title = "Tidsrom")

plt.savefig('HenvendelserPieOle.pdf', format='pdf')
plt.show()


#%% Del f) Regn ut et fornøydhetsmål kalt NPS
# Forutsetning: "Ubesvart tilbakemelding" utelates, vi har da 43 svar som utgjør 100%
# Ressurrs: https://www.blueprnt.com/2018/09/17/net-promoter-score/

import webbrowser  # Importerer denne modulen for å vise Net Promoter siden 
url = "https://www.blueprnt.com/2018/09/17/net-promoter-score/"
webbrowser.open(url)  # Åpner URLen i din default nettleser

negativ = noytral = positiv = 0
for scor in score:
    if scor >= 1 and scor <= 6:
        negativ += 1 
    elif scor >= 7 and scor <= 8:
        noytral += 1 
    elif scor >= 9 and scor <= 10:
        positiv += 1 

# 43 respondenter = 100%
# NPS = % positive - % negative (positiv/43*100 - negativ/43*100 = NPS)
alleSvar = negativ + noytral + positiv
NPS = (positiv/alleSvar*100) - (negativ/alleSvar*100)
#print(negativ, noytral, positiv, NPS)

svar = [negativ, noytral, positiv]
myLabels = ["Negativ", "Nøytral", "Positiv"]

plt.close('all')
#plt.figure(3, figsize=(12, 9))
plt.figure(3, figsize=(10, 7))

# I Matplotlib kan du lage et smultringdiagram (donut chart) ved å bruke et pie chart og sette en "hullstørrelse" ved hjelp av parameteren wedgeprops.
# Lage et "smultringdiagram" ved å sette 'width' i wedgeprops
plt.pie(svar, labels=myLabels, colors=useColors, wedgeprops={'width': 0.5}, autopct='%1.1f%%')

# Tegn en sirkel i midten for å forsterke smultringeffekten
plt.gca().set_aspect('equal')  # Sørger for at sirkelen blir rund
plt.title("Net Promoter Score")
plt.text(0, 0, f'NPS = {NPS:.1f}', ha='center', va='center')
plt.axis('equal')
plt.savefig('NetPromoterScoreOle.pdf', format='pdf')
plt.show()

print("\nOppgave Del F)")
print(f"Supportavdelingens Net Promoter Score, NPS er {NPS:.1f}")
print("Se smultring diagrammets fordeling \U0001F600")

# The End - Takk for nå og takk for meg - #
