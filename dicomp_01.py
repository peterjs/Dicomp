#!/bin/python
# coding=utf-8
import dicom
import sys #potrebná ?
from glob import glob
# k vyhľadávaniu spraviť progres bar lebo to fakt dlho trvá
#hlavný program
print "\n\033[1;34mDICOMP\n\033[1;m"
print "\033[1;32mPROGRAM SPRACÚVA ÚDAJE Z CELEJ DATABÁZY. OPERÁCIA TRVÁ NIEKOĽKO MINÚT, ČAKAJTE PROSÍM.\033[1;m"
name=[]  #pole so všetkými menami
print "\n"
for file in glob("home/ludo/dokumenty/terminal_stuffs/pajton/*/*/*.dcm")+glob("*/*/*/*.dcm"):  
    ds=dicom.read_file(file)  
    mena=ds.PatientName 
    name.append(mena)
    print "\r.\b"  # snaha bola ...
riadok=5 #pocet mien v riadku; teraz dat for cyklus na uhladnejsie vypisanie;zalamovat riadky
print "\033[1;37m",name[0:],"\033[1;m\t\t\t" #výpis všetkých mien, vymyslieť ako formátovať
dlzka=len(name)
print "\033[1;33mPočet snímkov:\033[1;m ",dlzka,"\n"
