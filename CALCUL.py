from math import *
from tkinter import *
from tkinter.messagebox import *
import turtle
import tkinter as tk
from tkinter import ttk
from sympy import *
import webbrowser


fichier1= open("Ressource/txt/background.txt", "rt")
backgroundColor=fichier1.readlines()
fichier2= open("Ressource/txt/button.txt", "rt")
buttonColor=fichier2.readlines()
fichier3=open("Ressource/txt/fontColor.txt", "rt")
fontColor=fichier3.readlines()
fichier4=open("Ressource/txt/infoTheme.txt", "rt")
infoTheme=fichier4.readlines()
fichier5=open("Ressource/txt/font.txt", "rt")
fontInfo=fichier5.readlines()


fontTitle=(fontInfo, 24, "bold underline")
fontButton=(fontInfo, 18, "bold")
fontTexte=(fontInfo, 12, "bold")



def principal():

    boutonRetour=PhotoImage(file="Ressource/bouton/boutonRetour.png")
    
    
    def chap1Menu():
        framePrincipal.destroy()
        frameChap1=Frame(fenetrePrincipal, bg=backgroundColor)
        frameChap1.pack(side=TOP)

        #Partie des perimetres

        #deplacement turtle

        def forward(a):
            t.forward(a)

        def back(a):
            t.back(a)

        def left(a):
            t.left(a)

        def right(a):
            t.right(a)

        frameDessin=LabelFrame(fenetrePrincipal, text="Dessin", fg=fontColor, bg=backgroundColor)
        frameDessin.configure(font=fontTitle)
        canvas=Canvas(frameDessin, width=1000, height=350)
        canvas.grid(row=1, column=1)

        t=turtle.RawTurtle(canvas)
        t.pensize(1)
        t.color("#ff0000", 'yellow')
        def erase():
            t.clear()
            t.penup()
        eraseButton=Button(frameDessin, text="Effacer", command=erase, fg=fontColor, bg=buttonColor, font=fontTexte)
        eraseButton.grid(row=1, column=2)

        #Couleur de trait

        def colorBlue():
            t.pencolor("blue")
        def colorRed():
            t.pencolor("red")
        def colorGreen():
            t.pencolor("green")
        def colorBlack():
            t.pencolor("black")
        def colorGrey():
            t.pencolor("grey")
        def colorCyan():
            t.pencolor("cyan")
        
        #Couleur de fond

        def colorFillBlue():
            t.fillcolor("blue")
        def colorFillRed():
            t.fillcolor("red")
        def colorFillGreen():
            t.fillcolor("green")
        def colorFillBlack():
            t.fillcolor("black")
        def colorFillGrey():
            t.fillcolor("grey")
        def colorFillCyan():
            t.fillcolor("cyan")
        
        #Taille crayon

        frameTaille=LabelFrame(frameDessin,text="Taille de trait :", fg=fontColor, bg=backgroundColor, font=fontTexte)
        frameTaille.grid(row=1, column=3)
        
        penSizeSelector=Scale(frameTaille, variable=int,  from_=1, to=25, resolution=1, fg=fontColor, bg=backgroundColor, font=fontTexte)
        penSizeSelector.grid(row=1, column=3)
        
        def penSizeSettings():
            penSizeSet=float(penSizeSelector.get())
            t.pensize(penSizeSet)
        penSizeSetButton=Button(frameTaille, command=penSizeSettings, text="Set", fg=fontColor, bg=buttonColor, font=fontTexte)
        penSizeSetButton.grid(row=1, column=4)
        
        
        #Couleur

        frameColorDessin=LabelFrame(frameDessin, text="Couleur de trait :", fg=fontColor, bg=backgroundColor, font=fontTexte)
        frameColorDessin.grid(row=2, column=3)
        frameColorFillDessin=LabelFrame(frameDessin, text="Couleur de remplissage :", fg=fontColor, bg=backgroundColor, font=fontTexte)
        frameColorFillDessin.grid(row=3, column=3)

        #Bouton de trait

        blue=Button(frameColorDessin, background="blue", command=colorBlue, width=6, fg=fontColor)
        blue.grid(row=2, column=4)
        red=Button(frameColorDessin, background="red", command=colorRed, width=6, fg=fontColor)
        red.grid(row=2, column=5)
        green=Button(frameColorDessin, background="green", command=colorGreen, width=6, fg=fontColor)
        green.grid(row=2, column=6)
        black=Button(frameColorDessin, background="black", command=colorBlack, width=6, fg=fontColor)
        black.grid(row=2, column=7)
        grey=Button(frameColorDessin, background="grey", command=colorGrey, width=6, fg=fontColor)
        grey.grid(row=2, column=8)
        cyan=Button(frameColorDessin, background="cyan", command=colorCyan, width=6, fg=fontColor)
        cyan.grid(row=2, column=9)

        #Bouton de fond
        
        blue=Button(frameColorFillDessin, background="blue", command=colorFillBlue, width=6, fg=fontColor)
        blue.grid(row=3, column=4)
        red=Button(frameColorFillDessin, background="red", command=colorFillRed, width=6, fg=fontColor)
        red.grid(row=3, column=5)
        green=Button(frameColorFillDessin, background="green", command=colorFillGreen, width=6, fg=fontColor)
        green.grid(row=3, column=6)
        black=Button(frameColorFillDessin, background="black", command=colorFillBlack, width=6, fg=fontColor)
        black.grid(row=3, column=7)
        grey=Button(frameColorFillDessin, background="grey", command=colorFillGrey, width=6, fg=fontColor)
        grey.grid(row=3, column=8)
        cyan=Button(frameColorFillDessin, background="cyan", command=colorFillCyan, width=6, fg=fontColor)
        cyan.grid(row=3, column=9)

        def perimetre():
            frameChap1.destroy()
            framePerimetre=Frame(fenetrePrincipal, bg=backgroundColor)
            framePerimetre.pack()
            

            

            #Fonctions pour le carr??

            def carre():
                framePerimetre.destroy()
                frameCarre=LabelFrame(fenetrePrincipal, text="1. P??rim??tre d'un carr??", padx=450, fg=fontColor, bg=backgroundColor)
                frameCarre.configure(font=fontTitle)
                frameCarre.pack(side=TOP)

                frameDessin.pack()

                entree=Spinbox(frameCarre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entree.grid(row=1,column=1)

                #Dessin
                
                def resultat():
                    c=float(entree.get())
                    if c != 0:
                        perimetreCarre.set("Perimetre = " + str(c*4) + " unit??s")
                        if (c) < 176:
                            t.pendown()
                            t.begin_fill()
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessin??e")                        
                    else: 
                        showerror("Error", "Un c??t?? ne peut pas ??tre ??gal ?? 0")
                        perimetreCarre.set("P??rim??tre = ERROR")
                
                perimetreCarre = StringVar()

                Resultat=Label(frameCarre, textvariable=perimetreCarre, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCarre, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=3,column=1)

                

                def retourCarre():
                    frameCarre.destroy()
                    frameDessin.pack_forget()
                    perimetre()
                retourCarreButton=Button(frameCarre, image=boutonRetour, command=retourCarre, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourCarreButton.grid(row=1, column=10)
                t.penup()
                
                
            #Fonction pour le rectangle

            def rectangle():
                framePerimetre.destroy()
                frameRectangle=LabelFrame(fenetrePrincipal, text="2. P??rim??tre d'un rectangle", padx=450, fg=fontColor, bg=backgroundColor)
                frameRectangle.configure(font=fontTitle)  
                frameRectangle.pack(side=TOP)

                longueur=Label(frameRectangle, text="Longueur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                longueur.grid(row=1, column=1)
                entreel=Spinbox(frameRectangle, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreel.grid(row=1,column=2)

                largeur=Label(frameRectangle, text="Largeur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                largeur.grid(row=2, column=1)
                entreeL=Spinbox(frameRectangle, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeL.grid(row=2,column=2)

                #Dessin

                frameDessin.pack()

                def resultat():
                    l=float(entreel.get())
                    L=float(entreeL.get())
                    if l and L != 0:
                        perimetreRectangle.set("Perim??tre = " + str(l*2+L*2)+" unit??s")
                        if (l or L) < 176:
                            t.pendown()
                            t.begin_fill()
                            forward(l)
                            left(90)
                            forward(L)
                            left(90)
                            forward(l)
                            left(90)
                            forward(L)
                            left(90)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessin??e")
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre ??gale ?? 0")
                        perimetreRectangle.set("P??rim??tre = ERROR")
                
                perimetreRectangle = StringVar()

                Resultat=Label(frameRectangle, textvariable=perimetreRectangle, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameRectangle, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=4,column=1)
                def retourRectangle():
                    frameRectangle.destroy()
                    frameDessin.pack_forget()
                    perimetre()
                retourRectangleButton=Button(frameRectangle, image=boutonRetour, command=retourRectangle, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourRectangleButton.grid(row=1, column=10)
                t.penup()
                    
                
            #Fonction pour le cercle

            def cercle():
                framePerimetre.destroy()
                frameCercle=LabelFrame(fenetrePrincipal, text="3. P??rim??tre d'un cercle", padx=400, fg=fontColor, bg=backgroundColor)
                frameCercle.configure(font=fontTitle)
                frameCercle.pack(side=TOP)

                rayon=Label(frameCercle, text="Rayon =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                rayon.grid(row=1, column=1)

                entree=Spinbox(frameCercle, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entree.grid(row=1,column=2)

                frameDessin.pack()
                
                def resultat():
                    r=float(entree.get())
                    if r != 0:
                        perimetreCercle.set("Perimetre = " + str(r*2*pi)+ " unit??s")
                        if (r) < 84:
                            t.pendown()
                            t.begin_fill()
                            t.circle(r, 360)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessin??e")
                        
                        
                    else: 
                        showerror("Error", "Un rayon ne peut pas ??tre ??gal ?? 0")
                        perimetreCercle.set("P??rim??tre = ERROR")
                
                perimetreCercle = StringVar()

                Resultat=Label(frameCercle, textvariable=perimetreCercle, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCercle, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=3,column=1)
                def retourCercle():
                    frameCercle.destroy()
                    frameDessin.pack_forget()
                    perimetre()
                retourCercleButton=Button(frameCercle, image=boutonRetour, command=retourCercle, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourCercleButton.grid(row=1, column=10)
                t.penup()
            
            
            

            #Boutons Perimetre

            carreButton=Button(framePerimetre, image=carrePerimetreImage, command=carre, fg=fontColor, bg=buttonColor)
            carreButton.grid(row=1,column=1)
            rectangleButton=Button(framePerimetre, image=rectanglePerimetreImage, command=rectangle, height=96, fg=fontColor, bg=buttonColor)
            rectangleButton.grid(row=1, column=2)
            cercleButton=Button(framePerimetre, image=cerclePerimetreImage, command=cercle, fg=fontColor, bg=buttonColor)
            cercleButton.grid(row=2, column=1)

            def retourPerimetre():
                framePerimetre.destroy()
                chap1Menu()
            retourPerimetreButton=Button(framePerimetre, image=boutonRetour, command=retourPerimetre, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
            retourPerimetreButton.grid(row=1, column=10)
        
            
        
        #Partie aire

        def aire():
            
            frameChap1.destroy()
            frameAire=Frame(fenetrePrincipal, bg=backgroundColor)
            frameAire.pack(side=TOP)

            #Fonctions pour le carr??

            def carre():
                frameAire.destroy()
                frameCarre=LabelFrame(fenetrePrincipal, text="1. Aire d'un Carr??", fg=fontColor, bg=backgroundColor)
                frameCarre.configure(font=fontTitle)
                frameCarre.pack(side=TOP)

                entree=Spinbox(frameCarre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entree.grid(row=1,column=1)

                #Dessin

                frameDessin.pack()
                
                def resultat():
                    c=float(entree.get())
                    if c != 0:
                        aireCarre.set("Aire = " + str(float(entree.get())**2)+" unit??s??")
                        if (c) < 176:
                            t.pendown()
                            t.begin_fill()
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            forward(c)
                            left(90)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessin??e") 
                    else: 
                        showerror("Error", "Un c??t?? ne peut pas ??tre ??gal ?? 0")
                        aireCarre.set("Aire = ERROR")
                
                aireCarre = StringVar()

                Resultat=Label(frameCarre, textvariable=aireCarre, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCarre, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=3,column=1)
                def retourCarre():
                    frameCarre.destroy()
                    frameDessin.pack_forget()
                    aire()
                retourCarreButton=Button(frameCarre, image=boutonRetour, command=retourCarre, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourCarreButton.grid(row=1, column=10)

            #Fonction pour le rectangle

            def rectangle():
                frameAire.destroy()
                frameRectangle=LabelFrame(fenetrePrincipal, text="2. Aire d'un Rectangle", fg=fontColor, bg=backgroundColor)
                frameRectangle.configure(font=fontTitle)
                frameRectangle.pack(side=TOP)

                longueur=Label(frameRectangle, text="Longueur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                longueur.grid(row=1, column=1)
                entreel=Spinbox(frameRectangle, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreel.grid(row=1,column=2)

                largeur=Label(frameRectangle, text="Largeur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                largeur.grid(row=2, column=1)
                entreeL=Spinbox(frameRectangle, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeL.grid(row=2,column=2)

                #Dessin

                frameDessin.pack()

                def resultat():
                    l=float(entreel.get())
                    L=float(entreeL.get())
                    if l and L != 0:
                        aireRectangle.set("Aire = " + str(l*L)+" unit??s??")
                        if (l or L) < 176:
                            t.pendown()
                            t.begin_fill()
                            forward(l)
                            left(90)
                            forward(L)
                            left(90)
                            forward(l)
                            left(90)
                            forward(L)
                            left(90)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessin??e")
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre ??gale ?? 0")
                        aireRectangle.set("Aire = ERROR")
                
                aireRectangle = StringVar()

                Resultat=Label(frameRectangle, textvariable=aireRectangle, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameRectangle, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=4,column=1)
                def retourRectangle():
                    frameRectangle.destroy()
                    frameDessin.pack_forget()
                    aire()
                retourRectangleButton=Button(frameRectangle, image=boutonRetour, command=retourRectangle, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourRectangleButton.grid(row=1, column=10)    
                
            #Fonction pour le cercle

            def cercle():
                frameAire.destroy()
                frameCercle=LabelFrame(fenetrePrincipal, text="3. Aire d'un cercle", fg=fontColor, bg=backgroundColor)
                frameCercle.configure(font=fontTitle)
                frameCercle.pack(side=TOP)

                rayon=Label(frameCercle, text="Rayon =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                rayon.grid(row=1, column=1)

                entree=Spinbox(frameCercle, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entree.grid(row=1,column=2)

                #Dessin

                frameDessin.pack()
                
                def resultat():
                    r=float(entree.get())
                    if r != 0:
                        aireCercle.set("Aire = " + str((r**2)*pi)+" unit??s??")
                        if (r) < 176:
                            t.pendown()
                            t.begin_fill()
                            t.circle(r, 360)
                            t.end_fill()
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessin??e")
                    else: 
                        showerror("Error", "Un rayon ne peut pas ??tre ??gal ?? 0")
                        aireCercle.set("Aire = ERROR")
                
                aireCercle = StringVar()

                Resultat=Label(frameCercle, textvariable=aireCercle, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCercle, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=3,column=1)
                def retourCercle():
                    frameCercle.destroy()
                    frameDessin.pack_forget()
                    aire()
                retourCercleButton=Button(frameCercle, image=boutonRetour, command=retourCercle, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourCercleButton.grid(row=1, column=10)

            #Fonctions pour le triangle

            def triangle():
                frameAire.destroy()
                frameTriangle=LabelFrame(fenetrePrincipal, text="4. Aire d'un triangle", fg=fontColor, bg=backgroundColor)
                frameTriangle.configure(font=fontTitle)
                frameTriangle.pack(side=TOP)

                base=Label(frameTriangle, text="Longueur de la Base =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                base.grid(row=1, column=1)
                entreeB=Spinbox(frameTriangle, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeB.grid(row=1,column=2)

                hauteur=Label(frameTriangle, text="Hauteur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(frameTriangle, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeH.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeH.get()) and float(entreeB.get()) != 0:
                        aireTriangle.set("Aire = " + str((float(entreeB.get())*float(entreeH.get()))/2)+" unit??s??")

                    else: 
                        showerror("Error", "Un rayon ne peut pas ??tre ??gal ?? 0")
                        aireTriangle.set("Aire = ERROR")
                
                aireTriangle = StringVar()

                Resultat=Label(frameTriangle, textvariable=aireTriangle, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameTriangle, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=4,column=1)
                def retourTriangle():
                    frameTriangle.destroy()
                    
                    aire()
                retourTriangleButton=Button(frameTriangle, image=boutonRetour, command=retourTriangle, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourTriangleButton.grid(row=1, column=10)
            
            #Fonction pour le Parrallelogramme

            def parrallelogramme():
                frameAire.destroy()
                frameParrallelogramme=LabelFrame(fenetrePrincipal, text="5. Aire d'un parrall??logramme", fg=fontColor, bg=backgroundColor)
                frameParrallelogramme.configure(font=fontTitle)
                frameParrallelogramme.pack(side=TOP)

                base=Label(frameParrallelogramme, text="Longueur de la Base =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                base.grid(row=1, column=1)
                entreeB=Spinbox(frameParrallelogramme, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeB.grid(row=1,column=2)

                hauteur=Label(frameParrallelogramme, text="Hauteur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(frameParrallelogramme, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeH.grid(row=2,column=2)

                frameDessin.pack()

                def resultat():
                    B=float(entreeB.get())
                    H=float(entreeH.get())
                    if B and H != 0:
                        aireParrallelogramme.set("Aire = " + str(B*H)+" unit??s??")
                        if B or H < 176:
                            for i in range (2):
                                t.forward(B)
                                t.left(120)
                                t.forward(H*1.4)
                                t.left(60)
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessin??e") 
                    else: 
                        showerror("Error", "Une longueur de la Base ou une hauteur ne peut pas etre ??gale ?? 0")
                        aireParrallelogramme.set("Aire = ERROR")
                
                aireParrallelogramme = StringVar()

                Resultat=Label(frameParrallelogramme, textvariable=aireParrallelogramme, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameParrallelogramme, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=4,column=1)
                def retourParrallelogramme():
                    frameParrallelogramme.destroy()
                    frameDessin.pack_forget()
                    aire()

                retourParrallelogrammeButton=Button(frameParrallelogramme, image=boutonRetour, command=retourParrallelogramme, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourParrallelogrammeButton.grid(row=1, column=10) 
            
            #Fonction pour le losange

            def losange():
                frameAire.destroy()
                frameLosange=LabelFrame(fenetrePrincipal, text="6. Aire d'un losange", fg=fontColor, bg=backgroundColor)
                frameLosange.configure(font=fontTitle)
                frameLosange.pack(side=TOP)

                diagonal1=Label(frameLosange, text="Diagonale 1 =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                diagonal1.grid(row=1, column=1)
                entree1=Spinbox(frameLosange, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entree1.grid(row=1,column=2)

                diagonal2=Label(frameLosange, text="Diagonale 2 =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                diagonal2.grid(row=2, column=1)
                entree2=Spinbox(frameLosange, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entree2.grid(row=2,column=2)

                def resultat():
                    if float(entree1.get()) and float(entree2.get()) != 0:
                        aireLosange.set("Aire = " + str((float(entree1.get())*float(entree2.get()))/2)+" unit??s??")
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre ??gale ?? 0")
                        aireLosange.set("Aire = ERROR")
                
                aireLosange = StringVar()

                Resultat=Label(frameLosange, textvariable=aireLosange, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameLosange, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=4,column=1)
                def retourLosange():
                    frameLosange.destroy()
                    
                    aire()
                retourLosangeButton=Button(frameLosange, image=boutonRetour, command=retourLosange, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourLosangeButton.grid(row=1, column=10) 

            #Fonction pour le trapeze

            def trapeze():
                frameAire.destroy()
                frameTrapeze=LabelFrame(fenetrePrincipal, text="7. Aire d'un trap??ze", fg=fontColor, bg=backgroundColor, font=fontTexte)
                frameTrapeze.configure(font=fontTitle)
                frameTrapeze.pack(side=TOP)

                petitcote=Label(frameTrapeze, text="Petit C??t?? =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                petitcote.grid(row=1, column=1)
                entreeP=Spinbox(frameTrapeze, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeP.grid(row=1,column=2)

                grandcote=Label(frameTrapeze, text="Grand C??t?? =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                grandcote.grid(row=2, column=1)
                entreeG=Spinbox(frameTrapeze, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeG.grid(row=2,column=2)

                hauteur=Label(frameTrapeze, text="Hauteur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                hauteur.grid(row=3, column=1)
                entreeH=Spinbox(frameTrapeze, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeH.grid(row=3,column=2)

                def resultat():
                    if float(entreeP.get()) and float(entreeG.get()) and float(entreeH.get()) != 0:
                        aireTrapeze.set("Aire = " + str(((float(entreeP.get())+float(entreeG.get()))/2)*float(entreeH.get()))+" unit??s??")
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre ??gale ?? 0")
                        aireTrapeze.set("Aire = ERROR")
                
                aireTrapeze = StringVar()

                Resultat=Label(frameTrapeze, textvariable=aireTrapeze, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=4,column=1)
                            
                
                validerButton=Button(frameTrapeze, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=5,column=1)
                def retourTrapeze():
                    frameTrapeze.destroy()
                    
                    aire()
                retourTrapezeButton=Button(frameTrapeze, image=boutonRetour, command=retourTrapeze, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourTrapezeButton.grid(row=1, column=10) 

            #Fonctions pour le cube

            def cube():
                frameAire.destroy()
                frameCube=LabelFrame(fenetrePrincipal, text="8. Aire d'un cube", fg=fontColor, bg=backgroundColor)
                frameCube.configure(font=fontTitle)
                frameCube.pack(side=TOP)

                entree=Spinbox(frameCube, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entree.grid(row=1,column=1)

                frameDessin.pack()
                
                def resultat():
                    c=float(entree.get())
                    if c != 0:
                        aireCube.set("Aire = " + str((c**2)*6)+" unit??s??")
                        if c<176:
                            t.goto(0,0)
                            t.pendown()
                            for i in range(4):
                                t.forward(c)
                                t.left(90)
                            
                            t.goto(((1/2)*c),((1/2)*c))
                            
                            for i in range(4):
                                t.forward(c)
                                t.left(90)
                            
                            t.goto(((3/2)*c),((1/2)*c))
                            t.goto(c,0)
                            
                            t.goto(c,c)
                            t.goto(((3/2)*c),((3/2)*c))
                            
                            t.goto(((1/2)*c),((3/2)*c))
                            t.goto(0,c)
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessin??e") 
                    else: 
                        showerror("Error", "Un c??t?? ne peut pas ??tre ??gal ?? 0")
                        aireCube.set("Aire = ERROR")
                
                aireCube = StringVar()

                Resultat=Label(frameCube, textvariable=aireCube, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCube, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=3,column=1)
                def retourCube():
                    frameCube.destroy()
                    frameDessin.pack_forget()
                    aire()
                retourCubeButton=Button(frameCube, image=boutonRetour, command=retourCube, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourCubeButton.grid(row=1, column=10)
            
            #Fonction pour le pave droit

            def pave():
                frameAire.destroy()
                framePave=LabelFrame(fenetrePrincipal, text="9. Aire d'un pav?? droit", fg=fontColor, bg=backgroundColor) 
                framePave.configure(font=fontTitle) 
                framePave.pack(side=TOP)

                longueur=Label(framePave, text="Longueur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                longueur.grid(row=1, column=1)
                entreel=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreel.grid(row=1,column=2)

                largeur=Label(framePave, text="Largeur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                largeur.grid(row=2, column=1)
                entreeL=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeL.grid(row=2,column=2)

                hauteur=Label(framePave, text="Hauteur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                hauteur.grid(row=3, column=1)
                entreeH=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeH.grid(row=3,column=2)

                frameDessin.pack()

                def resultat():
                    l=float(entreel.get())
                    L=float(entreeL.get())
                    H=float(entreeH.get())
                    if l and L and H != 0:
                        airePave.set("Aire = " + str(2*(l*L+L*H+l*H))+" unit??s??")

                        if l or L or H < 176:

                            t.goto(0,0)
                            t.pendown()
                            for i in range(2):
                                t.forward(l)
                                t.left(90)
                                t.forward(L)
                                t.left(90)
                            
                            t.goto((1/2)*H,(1/2)*L)
                            
                            for i in range(2):
                                t.forward(l)
                                t.left(90)
                                t.forward(L)
                                t.left(90)
                            t.forward(l)
                            t.goto(l,0)
                            
                            t.goto(l,L)
                            t.goto((3/2)*l,(3/2)*L)
                            t.back(l)
                            
                            t.goto(0,L)

                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessin??e") 
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre ??gale ?? 0")
                        airePave.set("Aire = ERROR")
                
                airePave = StringVar()

                Resultat=Label(framePave, textvariable=airePave, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=4,column=1)
                            
                
                validerButton=Button(framePave, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=5,column=1)
                def retourPave():
                    framePave.destroy()
                    frameDessin.pack_forget()
                    aire()
                retourPaveButton=Button(framePave, image=boutonRetour, command=retourPave, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourPaveButton.grid(row=1, column=10) 
            
            #Fonctions pour le cylindre

            def cylindre():
                frameAire.destroy()
                frameCylindre=LabelFrame(fenetrePrincipal, text="10. Aire d'un cylindre", fg=fontColor, bg=backgroundColor)
                frameCylindre.configure(font=fontTitle)
                frameCylindre.pack(side=TOP)

                rayon=Label(frameCylindre, text="Rayon =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                rayon.grid(row=1, column=1)
                entreeR=Spinbox(frameCylindre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeR.grid(row=1,column=2)

                hauteur=Label(frameCylindre, text="Hauteur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(frameCylindre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeH.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeH.get()) and float(entreeR.get()) != 0:
                        aireCylindre.set("Aire = " + str(2*pi*float(entreeR.get())*float(entreeH.get()))+" unit??s??")
                    else: 
                        showerror("Error", "Un rayon ne peut pas ??tre ??gal ?? 0")
                        aireCylindre.set("Aire = ERROR")
                
                aireCylindre = StringVar()

                Resultat=Label(frameCylindre, textvariable=aireCylindre, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameCylindre, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=4,column=1)
                def retourCylindre():
                    frameCylindre.destroy()
                    
                    aire()
                retourCylindreButton=Button(frameCylindre, image=boutonRetour, command=retourCylindre, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourCylindreButton.grid(row=1, column=10)
            
            #Fonctions pour le sphere

            def sphere():
                frameAire.destroy()
                frameSphere=LabelFrame(fenetrePrincipal, text="11. Aire d'une sph??re", fg=fontColor, bg=backgroundColor)
                frameSphere.configure(font=fontTitle)
                frameSphere.pack(side=TOP)

                entree=Spinbox(frameSphere, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entree.grid(row=1,column=1)
                
                def resultat():
                    if float(entree.get()) != 0:
                        aireSphere.set("Aire = " + str((float(entree.get())**2)*4*pi)+" unit??s??")
                    else: 
                        showerror("Error", "Un rayon ne peut pas ??tre ??gal ?? 0")
                        aireSphere.set("Aire = ERROR")
                
                aireSphere = StringVar()

                Resultat=Label(frameSphere, textvariable=aireSphere, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameSphere, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=3,column=1)
                def retourSphere():
                    frameSphere.destroy()
                    
                    aire()
                retourSphereButton=Button(frameSphere, image=boutonRetour, command=retourSphere, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourSphereButton.grid(row=1, column=10)
            
            #Boutons aire

            carreButton=Button(frameAire, image=carreAireImage, command=carre,  fg=fontColor, bg=buttonColor)
            carreButton.grid(row=1,column=1)
            rectangleButton=Button(frameAire, image=rectangleAireImage, command=rectangle, height=96, fg=fontColor, bg=buttonColor)
            rectangleButton.grid(row=1, column=2)
            cercleButton=Button(frameAire, image=cercleAireImage, command=cercle, fg=fontColor, bg=buttonColor)
            cercleButton.grid(row=2, column=1)
            triangleButton=Button(frameAire,image=triangleAireImage, command=triangle, fg=fontColor, bg=buttonColor)
            triangleButton.grid(row=2, column=2)
            parrallelogrammeButton=Button(frameAire, image=parallelogrammeImage, command=parrallelogramme, fg=fontColor, bg=buttonColor)
            parrallelogrammeButton.grid(row=3, column=1)
            losangeButton=Button(frameAire, image=losangeImage, command=losange, fg=fontColor, bg=buttonColor)
            losangeButton.grid(row=3, column=2)
            trapezeButton=Button(frameAire, image=trapezeImage, command=trapeze, fg=fontColor, bg=buttonColor)
            trapezeButton.grid(row=4, column=1)
            cubeButton=Button(frameAire, image=cubeImage, command=cube, fg=fontColor, bg=buttonColor)
            cubeButton.grid(row=4, column=2)
            paveButton=Button(frameAire, image=paveImage, command=pave, fg=fontColor, bg=buttonColor)
            paveButton.grid(row=5, column=1)
            cylindreButton=Button(frameAire, image=cylindreImage, command=cylindre, fg=fontColor, bg=buttonColor)
            cylindreButton.grid(row=5, column=2)
            sphereButton=Button(frameAire, image=sphereImage, command=sphere, fg=fontColor, bg=buttonColor)
            sphereButton.grid(row=6, column=1)

            #Bouton Retour

            def retourAire():
                frameAire.destroy()
                chap1Menu()
            retourAireButton=Button(frameAire, image=boutonRetour, command=retourAire, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
            retourAireButton.grid(row=1, column=10)

        #Partie Volume

        def volume():

            frameChap1.destroy()
            frameVolume=Frame(fenetrePrincipal, bg=backgroundColor)
            frameVolume.pack(side=TOP)

            #Fonctions pour le cube

            def cube():
                frameVolume.destroy()
                frameCube=LabelFrame(fenetrePrincipal, text="1. Volume d'un cube", fg=fontColor, bg=backgroundColor)
                frameCube.configure(font=fontTitle)
                frameCube.pack(side=TOP)

                entree=Spinbox(frameCube, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entree.grid(row=1,column=1)
                
                frameDessin.pack()
                
                def resultat():
                    c=float(entree.get())
                    if c != 0:
                        volumeCube.set("Volume = " + str((c**2)*6)+" unit??s??")
                        if c<176:
                            t.goto(0,0)
                            t.pendown()
                            for i in range(4):
                                t.forward(c)
                                t.left(90)
                            
                            t.goto(((1/2)*c),((1/2)*c))
                            
                            for i in range(4):
                                t.forward(c)
                                t.left(90)
                            
                            t.goto(((3/2)*c),((1/2)*c))
                            t.goto(c,0)
                            
                            t.goto(c,c)
                            t.goto(((3/2)*c),((3/2)*c))
                            
                            t.goto(((1/2)*c),((3/2)*c))
                            t.goto(0,c)
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessin??e") 
                    else: 
                        showerror("Error", "Un c??t?? ne peut pas ??tre ??gal ?? 0")
                        volumeCube.set("Volume = ERROR")
                
                volumeCube = StringVar()

                Resultat=Label(frameCube, textvariable=volumeCube, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameCube, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=3,column=1)
                def retourCube():
                    frameCube.destroy()
                    frameDessin.pack_forget()
                    volume()
                retourCubeButton=Button(frameCube, image=boutonRetour, command=retourCube, background=backgroundColor, activebackground=backgroundColor, relief=FLAT, font=fontTexte)
                retourCubeButton.grid(row=1, column=10)
            
            #Fonction pour le pave droit

            def pave():
                frameVolume.destroy()
                framePave=LabelFrame(fenetrePrincipal, text="2. Volume d'un pav?? droit", fg=fontColor, bg=backgroundColor) 
                framePave.configure(font=fontTitle) 
                framePave.pack(side=TOP)

                longueur=Label(framePave, text="Longueur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                longueur.grid(row=1, column=1)
                entreel=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreel.grid(row=1,column=2)

                largeur=Label(framePave, text="Largeur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                largeur.grid(row=2, column=1)
                entreeL=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeL.grid(row=2,column=2)

                hauteur=Label(framePave, text="Hauteur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                hauteur.grid(row=3, column=1)
                entreeH=Spinbox(framePave, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeH.grid(row=3,column=2)

                frameDessin.pack()

                def resultat():
                    l=float(entreel.get())
                    L=float(entreeL.get())
                    H=float(entreeH.get())
                    if l and L and H != 0:
                        volumePave.set("Aire = " + str(2*(l*L+L*H+l*H))+" unit??s??")

                        if l or L or H < 176:

                            t.goto(0,0)
                            t.pendown()
                            for i in range(2):
                                t.forward(l)
                                t.left(90)
                                t.forward(L)
                                t.left(90)
                            
                            t.goto((1/2)*H,(1/2)*L)
                            
                            for i in range(2):
                                t.forward(l)
                                t.left(90)
                                t.forward(L)
                                t.left(90)
                            t.forward(l)
                            t.goto(l,0)
                            
                            t.goto(l,L)
                            t.goto((3/2)*l,(3/2)*L)
                            t.back(l)
                            
                            t.goto(0,L)
                        else:
                            showinfo("Error", "La distance est trop grande pour que la figure soit dessin??e") 
                    else: 
                        showerror("Error", "Une longueur ou une largeur ne peut pas etre ??gale ?? 0")
                        volumePave.set("Volume = ERROR")
                
                volumePave = StringVar()

                Resultat=Label(framePave, textvariable=volumePave, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=4,column=1)
                            
                
                validerButton=Button(framePave, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=5,column=1)
                def retourPave():
                    framePave.destroy()
                    frameDessin.pack_forget()
                    volume()
                retourPaveButton=Button(framePave, image=boutonRetour, command=retourPave, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourPaveButton.grid(row=1, column=10) 

            #Fonctions pour le cylindre

            def cylindre():
                frameVolume.destroy()
                frameCylindre=LabelFrame(fenetrePrincipal, text="3. Volume d'un cylindre", fg=fontColor, bg=backgroundColor)
                frameCylindre.configure(font=fontTitle)
                frameCylindre.pack(side=TOP)

                rayon=Label(frameCylindre, text="Rayon =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                rayon.grid(row=1, column=1)
                entreeR=Spinbox(frameCylindre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeR.grid(row=1,column=2)

                hauteur=Label(frameCylindre, text="Hauteur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(frameCylindre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeH.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeH.get()) and float(entreeR.get()) != 0:
                        volumeCylindre.set("Volume = " + str(2*pi*float(entreeR.get())*float(entreeH.get()))+" unit??s??")
                    else: 
                        showerror("Error", "Un rayon ne peut pas ??tre ??gal ?? 0")
                        volumeCylindre.set("Volume = ERROR")
                
                volumeCylindre = StringVar()

                Resultat=Label(frameCylindre, textvariable=volumeCylindre, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameCylindre, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=4,column=1)
                def retourCylindre():
                    frameCylindre.destroy()
                    volume()
                retourCylindreButton=Button(frameCylindre, image=boutonRetour, command=retourCylindre, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourCylindreButton.grid(row=1, column=10)
            
            #Fonctions pour la pyramide a base carr??

            def pyramide():
                frameVolume.destroy()
                framePyramideCarre=LabelFrame(fenetrePrincipal, text="4. Volume d'une pyramide ?? base carr??e", fg=fontColor, bg=backgroundColor)
                framePyramideCarre.configure(font=fontTitle)
                framePyramideCarre.pack(side=TOP)

                cote=Label(framePyramideCarre, text="Cot?? =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                cote.grid(row=1, column=1)
                entreeC=Spinbox(framePyramideCarre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeC.grid(row=1,column=2)

                hauteur=Label(framePyramideCarre, text="Hauteur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(framePyramideCarre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeH.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeH.get()) and float(entreeC.get()) != 0:
                        volumePyramideCarre.set("Volume = " + str(((float(entreeC.get())**2)*float(entreeH.get()))/3)+" unit??s??")
                    else: 
                        showerror("Error", "Un cot?? ou une hauteur ne peut pas ??tre ??gal ?? 0")
                        volumePyramideCarre.set("Volume = ERROR")
                
                volumePyramideCarre = StringVar()

                Resultat=Label(framePyramideCarre, textvariable=volumePyramideCarre, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(framePyramideCarre, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=4,column=1)
                def retourPyramideCarre():
                    framePyramideCarre.destroy()
                    volume()
                retourPyramideCarreButton=Button(framePyramideCarre, image=boutonRetour, command=retourPyramideCarre, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourPyramideCarreButton.grid(row=1, column=10)
            
            #Fonctions pour le cone

            def cone():
                frameVolume.destroy()
                frameCone=LabelFrame(fenetrePrincipal, text="6. Volume d'un c??ne", fg=fontColor, bg=backgroundColor)
                frameCone.configure(font=fontTitle)
                frameCone.pack(side=TOP)

                rayon=Label(frameCone, text="Rayon =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                rayon.grid(row=1, column=1)
                entreeR=Spinbox(frameCone, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeR.grid(row=1,column=2)

                hauteur=Label(frameCone, text="Hauteur =", fg=fontColor, bg=backgroundColor, font=fontTexte)
                hauteur.grid(row=2, column=1)
                entreeH=Spinbox(frameCone, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeH.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeH.get()) and float(entreeR.get()) != 0:
                        volumeCone.set("Volume = " + str((pi*(float(entreeR.get())**2)*float(entreeH.get()))/3)+" unit??s??")
                    else: 
                        showerror("Error", "Un rayon ou la hauteur ne peut pas ??tre ??gal ?? 0")
                        volumeCone.set("Volume = ERROR")
                
                volumeCone = StringVar()

                Resultat=Label(frameCone, textvariable=volumeCone, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameCone, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=4,column=1)
                def retourCone():
                    frameCone.destroy()
                    volume()
                retourConeButton=Button(frameCone, image=boutonRetour, command=retourCone, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourConeButton.grid(row=1, column=10)
            
            #Fonctions pour le sphere

            def sphere():
                frameVolume.destroy()
                frameSphere=LabelFrame(fenetrePrincipal, text="7. Volume d'une sph??re", fg=fontColor, bg=backgroundColor)
                frameSphere.configure(font=fontTitle)
                frameSphere.pack(side=TOP)

                entree=Spinbox(frameSphere, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entree.grid(row=1,column=1)
                
                def resultat():
                    if float(entree.get()) != 0:
                        volumeSphere.set("Volume = " + str((float(entree.get())**2)*(4/3)*pi)+" unit??s??")
                    else: 
                        showerror("Error", "Un rayon ne peut pas ??tre ??gal ?? 0")
                        volumeSphere.set("Volume = ERROR")
                
                volumeSphere = StringVar()

                Resultat=Label(frameSphere, textvariable=volumeSphere, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=2,column=1)
                            
                
                validerButton=Button(frameSphere, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=3,column=1)
                def retourSphere():
                    frameSphere.destroy()
                    volume()
                retourSphereButton=Button(frameSphere, image=boutonRetour, command=retourSphere, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourSphereButton.grid(row=1, column=10)

            #Boutons volume

            cubeButton=Button(frameVolume, image=cubeImage, command=cube,  fg=fontColor, bg=buttonColor)
            cubeButton.grid(row=1, column=1)
            paveButton=Button(frameVolume, image=paveImage, command=pave,  fg=fontColor, bg=buttonColor)
            paveButton.grid(row=1, column=2)
            cylindreButton=Button(frameVolume, image=cylindreImage, command=cylindre,  fg=fontColor, bg=buttonColor)
            cylindreButton.grid(row=2, column=1)
            pyramidecarreButton=Button(frameVolume, image=pyramideImage, command=pyramide, fg=fontColor, bg=buttonColor)
            pyramidecarreButton.grid(row=2, column=2)
            coneButton=Button(frameVolume, image=coneImage, command=cone,  fg=fontColor, bg=buttonColor)
            coneButton.grid(row=3, column=1)
            sphereButton=Button(frameVolume, image=sphereImage, command=sphere, fg=fontColor, bg=buttonColor)
            sphereButton.grid(row=3, column=2)

            def retourVolume():
                frameVolume.destroy()
                chap1Menu()
            retourVolumeButton=Button(frameVolume, image=boutonRetour, command=retourVolume, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
            retourVolumeButton.grid(row=1, column=10)

        def retourChap1():
            frameChap1.destroy()
            principal()
            
        retourChap1Button=Button(frameChap1, image=boutonRetour, command=retourChap1, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
        retourChap1Button.grid(row=1, column=10)

        perimetreButton=Button(frameChap1, command=perimetre, image=carrePerimetreImage, fg=fontColor, bg=buttonColor)
        perimetreButton.grid(row=1,column=1)
        aireButton=Button(frameChap1, image=carreAireImage, command=aire, fg=fontColor, bg=buttonColor)
        aireButton.grid(row=1,column=2)
        volumeButton=Button(frameChap1, image=cubeImage, command=volume, fg=fontColor, bg=buttonColor)
        volumeButton.grid(row=2,column=1)

    def chap2Menu():
        framePrincipal.destroy()
        frameChap2=Frame(fenetrePrincipal, bg=backgroundColor)
        frameChap2.pack()

        def denombrement():
            frameChap2.destroy()
            frameDenombrement=Frame(fenetrePrincipal, bg=backgroundColor)
            frameDenombrement.pack()

            def ordre():
                frameDenombrement.destroy()
                frameOrdre=LabelFrame(fenetrePrincipal, text="1. Ordre pris en compte", fg=fontColor, bg=backgroundColor, font=fontTexte)
                frameOrdre.configure(font=fontTitle)
                frameOrdre.pack()

                N=Label(frameOrdre, text="L'effectif N = ", fg=fontColor, bg=backgroundColor, font=fontTexte)
                N.grid(row=1,column=1)
                entreeN=Spinbox(frameOrdre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeN.grid(row=1,column=2)

                K=Label(frameOrdre, text="Nombre d'??l??ments K de N = ", fg=fontColor, bg=backgroundColor, font=fontTexte)
                K.grid(row=2,column=1)
                entreeK=Spinbox(frameOrdre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeK.grid(row=2,column=2)

                def resultat():
                    if float(entreeK.get()) > float(entreeN.get()):
                        showerror("Error", "Il y a plus d'??l??ments de K que d'effectif N")
                        valeurOrdre.set("Arangements = ERROR")
                    elif float(entreeK.get()) == float(entreeN.get()):
                        valeurOrdre.set("Permutations = " + str(factorial(float(entreeN.get()))))
                    else:
                        valeurOrdre.set("Arangements = "+str((factorial(float(entreeN.get())))/factorial((float(entreeN.get()))-float(entreeK.get()))))

                valeurOrdre = StringVar()

                Resultat=Label(frameOrdre, textvariable=valeurOrdre, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameOrdre, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=4,column=1)

                def retourOrdre():
                    frameOrdre.destroy()
                    denombrement()
            
                retourOrdreButton=Button(frameOrdre, image=boutonRetour, command=retourOrdre, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourOrdreButton.grid(row=1, column=10)
            

            def noOrdre():
                frameDenombrement.destroy()
                frameNoOrdre=LabelFrame(fenetrePrincipal, text="2. Ordre non pris en compte", fg=fontColor, bg=backgroundColor, font=fontTexte)
                frameNoOrdre.configure(font=fontTitle)
                frameNoOrdre.pack()

                N=Label(frameNoOrdre, text="L'effectif N = ", fg=fontColor, bg=backgroundColor, font=fontTexte)
                N.grid(row=1,column=1)
                entreeN=Spinbox(frameNoOrdre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeN.grid(row=1,column=2)

                K=Label(frameNoOrdre, text="Nombre d'??l??ments K de N = ", fg=fontColor, bg=backgroundColor, font=fontTexte)
                K.grid(row=2,column=1)
                entreeK=Spinbox(frameNoOrdre, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
                entreeK.grid(row=2,column=2)
                
                def resultat():
                    if float(entreeK.get()) > float(entreeN.get()):
                        showerror("Error", "Il y a plus d'??l??ments de K que d'effectif N")
                        valeurNoOrdre.set("Nombre de combinaisons = ERROR")
                    else:
                        valeurNoOrdre.set("Nombre de combinaisons = "+str(factorial(float(entreeN.get()))/(factorial(float(entreeK.get()))*factorial(float(entreeN.get())-float(entreeK.get())))))
                
                valeurNoOrdre = StringVar()

                Resultat=Label(frameNoOrdre, textvariable=valeurNoOrdre, fg=fontColor, bg=backgroundColor, font=fontTexte)
                Resultat.grid(row=3,column=1)
                            
                
                validerButton=Button(frameNoOrdre, text="Valider", command=resultat, background="green", font=fontTexte)
                validerButton.grid(row=4,column=1)
            
                def retourNoOrdre():
                    frameNoOrdre.destroy()
                    denombrement()
            
                retourNoOrdreButton=Button(frameNoOrdre, image=boutonRetour, command=retourNoOrdre, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
                retourNoOrdreButton.grid(row=1, column=10)

            ordreButton=Button(frameDenombrement, text="1.Ordre pris en compte", command=ordre, pady=5, fg=fontColor, bg=buttonColor, font=fontButton)
            ordreButton.grid(row=1, column=1)
            noOrdreButton=Button(frameDenombrement, text="2.Ordre non pris en compte", command=noOrdre, pady=5, fg=fontColor, bg=buttonColor, font=fontButton)
            noOrdreButton.grid(row=1, column=2)

            def retourDenombrement():
                frameDenombrement.destroy()
                chap2Menu()
            
            retourDenombrementButton=Button(frameDenombrement, image=boutonRetour, command=retourDenombrement, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
            retourDenombrementButton.grid(row=1, column=10)

        denombrementButton=Button(frameChap2, text="1.D??nombrements et Combinaisons", command=denombrement, width=30, pady=5, fg=fontColor, bg=buttonColor, font=fontButton)
        denombrementButton.grid(row=1, column=1)


        def retourChap2():
            frameChap2.destroy()
            principal()
            
        retourChap2Button=Button(frameChap2, image=boutonRetour, command=retourChap2, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
        retourChap2Button.grid(row=1, column=10)
    
    def chap3Menu():
        framePrincipal.destroy()
        frameChap3=Frame(fenetrePrincipal, bg=backgroundColor)
        frameChap3.pack()
        framePremier=LabelFrame(frameChap3, text="Nombre Premier", fg=fontColor, bg=backgroundColor, font=fontTitle)
        framePremier.grid(row=1, column=0)

        entree=Spinbox(framePremier, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
        entree.grid(row=1, column=1)

        def estPremier():
            num=int(entree.get())
            
            def true():
                valeurResultat.set(str(num) + " est premier ")
            
            def false():
                valeurResultat.set(str(num) + " n'est pas premier ")

            if num > 2 and num % 2 == 0:
                return false()
            for x in range(2, num // 2):
                if num % x == 0:
                    return false()
                     
            return true()
                
        valeurResultat= StringVar()
        Resultat=Label(framePremier, textvariable=valeurResultat, fg=fontColor, bg=backgroundColor, font=fontTexte)
        Resultat.grid(row=2, column=1)
        
        estPremierButton=Button(framePremier, text="V??rifier", command=estPremier, bg="green", font=fontTexte)
        estPremierButton.grid(row=1, column=2)

        def retourChap3():
            frameChap3.destroy()
            principal()
            
        retourChap3Button=Button(frameChap3, image=boutonRetour, command=retourChap3, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
        retourChap3Button.grid(row=1, column=10)
    
    def chap4Menu():
        framePrincipal.destroy()
        frameChap4=Frame(fenetrePrincipal, bg=backgroundColor)
        frameChap4.pack()

        def distance():
            frameChap4.pack_forget()
            frameDistance=LabelFrame(fenetrePrincipal, text="1. Conversions de Distance", fg=fontColor, bg=backgroundColor)
            frameDistance.configure(font=fontTitle)
            frameDistance.pack()

            resultatConvertis=StringVar()

            def valider():
                entree2.grid_forget()

                if distance1.get() == 'kilom??tre':
                    if distance2.get() == 'kilom??tre':
                        resultatConvertis.set(str(float(entree1.get())))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'hectom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cam??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**2))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**4))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'centim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**5))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'millim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**6))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'microm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**9))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'nanom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**12))
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if distance1.get() == 'hectom??tre':
                    if distance2.get() == 'kilom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'hectom??tre':
                        resultatConvertis.set(str(float(entree1.get())))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cam??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**2))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'centim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**4))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'millim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**5))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'microm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**8))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'nanom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**11))
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if distance1.get() == 'd??cam??tre':
                    if distance2.get() == 'kilom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-2))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'hectom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cam??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**2))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'centim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'millim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**4))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'microm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**7))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'nanom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**10))
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                    
                if distance1.get() == 'm??tre':
                    if distance2.get() == 'kilom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'hectom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-2))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cam??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'centim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**2))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'millim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'microm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**6))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'nanom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**9))
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if distance1.get() == 'd??cim??tre':
                    if distance2.get() == 'kilom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-4))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'hectom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cam??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-2))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'centim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'millim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**2))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'microm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**5))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'nanom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**8))
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if distance1.get() == 'centim??tre':
                    if distance2.get() == 'kilom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-5))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'hectom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-4))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cam??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-2))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'centim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'millim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'microm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**4))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'nanom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**7))
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if distance1.get() == 'millim??tre':
                    if distance2.get() == 'kilom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-6))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'hectom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-5))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cam??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-4))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-2))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'centim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-1))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'millim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'microm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'nanom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**6))
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if distance1.get() == 'microm??tre':
                    if distance2.get() == 'kilom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-9))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'hectom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-8))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cam??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-7))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-6))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-5))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'centim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-4))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'millim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'microm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'nanom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**3))
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if distance1.get() == 'microm??tre':
                    if distance2.get() == 'kilom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-12))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'hectom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-11))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cam??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-10))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-9))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'd??cim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-8))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'centim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-7))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'millim??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-6))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'microm??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**-3))
                        entree2.grid(row=3,column=4)
                    elif distance2.get() == 'nanom??tre':
                        resultatConvertis.set(str(float(entree1.get())*10**0))
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)

                
            
            distance1=ttk.Combobox(frameDistance)
            distance1.grid(row=2,column=1)

            distance1['values']=('kilom??tre',
                                'hectom??tre',
                                'd??cam??tre',
                                'm??tre',
                                'd??cim??tre',
                                'centim??tre',
                                'millim??tre',
                                'microm??tre',
                                'nanom??tre',
                                '         ')
            distance1.current(9)

            distance2=ttk.Combobox(frameDistance)
            distance2.grid(row=2,column=3)

            distance2['values']=('kilom??tre',
                                'hectom??tre',
                                'd??cam??tre',
                                'm??tre',
                                'd??cim??tre',
                                'centim??tre',
                                'millim??tre',
                                'microm??tre',
                                'nanom??tre',
                                '          ')
            distance2.current(9)

            fleche1=Label(frameDistance, text="=>", fg=fontColor, bg=backgroundColor, font=fontTexte)
            fleche1.grid(row=2,column=2)
            fleche2=Label(frameDistance, text="=>", fg=fontColor, bg=backgroundColor, font=fontTexte)
            fleche2.grid(row=3,column=2)

            entree1=Spinbox(frameDistance, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
            entree1.grid(row=3,column=1)

            

            entree2=Label(frameDistance, textvariable=resultatConvertis, width=50, fg=fontColor, bg=backgroundColor, font=fontTexte)
            entree2.grid(row=3,column=3)

            valider=Button(frameDistance, text="Valider", command=valider, bg="green", font=fontTexte)
            valider.grid(row=3, column=4)

            def retourDistance():
                frameDistance.destroy()
                chap4Menu()
                
            retourDistanceButton=Button(frameDistance, image=boutonRetour, command=retourDistance, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
            retourDistanceButton.grid(row=2, column=10)
        
        def surface():
            frameChap4.pack_forget()
            frameSurface=LabelFrame(fenetrePrincipal, text="2. Conversion de Surface", fg=fontColor, bg=backgroundColor)
            frameSurface.configure(font=fontTitle)
            frameSurface.pack()

            resultatConvertis=StringVar()
            unite1=StringVar()
            unite2=StringVar()

            def valider():
                entree2.grid_forget()

                

                if surface1.get() == 'kilom??tre??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get()))+" km??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" hm??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**4)+" dam??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" m??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**8)+" dm??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**10)+" cm??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**12)+" mm??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**18)+" ??m??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**24)+" nm??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" ha")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**6)+" yard??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**7)+" pied??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**9)+" pouce??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*0.39)+" mille??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'hectom??tre??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("hm??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get()))+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("hm??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("hm??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**4)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("hm??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("hm??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10*8)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("hm??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**10)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("hm??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**16)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("hm??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**22)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("hm??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" ha")
                        unite1.set("hm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**5)+" yard??")
                        unite1.set("hm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**6)+" pied??")
                        unite1.set("hm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**8)+" pouce??")
                        unite1.set("hm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-1))+" mille??")
                        unite1.set("hm??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'd??cam??tre??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-4)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dam??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dam??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dam??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dam??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**4)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dam??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dam??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**8)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dam??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**14)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dam??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**20)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dam??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**1)+" ha")
                        unite1.set("dam??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**4)+" yard??")
                        unite1.set("dam??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**5)+" pied??")
                        unite1.set("dam??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**7)+" pouce??")
                        unite1.set("dam??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-2))+" mille??")
                        unite1.set("dam??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                    
                if surface2.get() == 'm??tre??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("m??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-4)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("m??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("m??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("m??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("m??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**4)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("m??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("m??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**12)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("m??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**18)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("m??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" ha")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**3)+" yard??")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**4)+" pied??")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**6)+" pouce??")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-3))+" mille??")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'd??cim??tre??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-8)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dm??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dm??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-4)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dm??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dm??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dm??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dm??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**4)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dm??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**10)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dm??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**16)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("dm??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**(-1))+" ha")
                        unite1.set("dm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**2)+" yard??")
                        unite1.set("dm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**3)+" pied??")
                        unite1.set("dm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**5)+" pouce??")
                        unite1.set("dm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-4))+" mille??")
                        unite1.set("dm??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'centim??tre??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-10)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("cm??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-8)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("cm??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("cm??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-4)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("cm??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("cm??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("cm??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("cm??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**8)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("cm??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**14)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("cm??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**(-2))+" ha")
                        unite1.set("cm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**1)+" yard??")
                        unite1.set("cm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**2)+" pied??")
                        unite1.set("cm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**4)+" pouce??")
                        unite1.set("cm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-5))+" mille??")
                        unite1.set("cm??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'millim??tre??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-12)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("mm??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-10)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("mm??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-8)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("mm??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("mm??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-4)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("mm??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("mm??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("mm??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("mm??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**12)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("mm??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**(-3))+" ha")
                        unite1.set("mm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**0)+" yard??")
                        unite1.set("mm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**1)+" pied??")
                        unite1.set("mm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**3)+" pouce??")
                        unite1.set("mm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-6))+" mille??")
                        unite1.set("mm??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'microm??tre??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-18)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("??m??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-16)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("??m??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-14)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("??m??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-12)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("??m??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-10)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("??m??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-8)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("??m??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("??m??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("??m??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("??m??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**(-4))+" ha")
                        unite1.set("??m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**(-1))+" yard??")
                        unite1.set("??m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**0)+" pied??")
                        unite1.set("??m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**2)+" pouce??")
                        unite1.set("??m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-7))+" mille??")
                        unite1.set("??m??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'nanom??tre??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-24)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("nm??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-22)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("nm??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-20)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("nm??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-18)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("nm??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-16)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("nm??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-14)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("nm??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-12)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("nm??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-6)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("nm??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("nm??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**(-5))+" ha")
                        unite1.set("nm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**(-2))+" yard??")
                        unite1.set("nm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**(-1))+" pied??")
                        unite1.set("nm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**1)+" pouce??")
                        unite1.set("nm??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-8))+" mille??")
                        unite1.set("nm??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                    
                if surface1.get() == 'hectare':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**-2)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("ha")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("ha")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**2)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("ha")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**4)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("ha")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("ha")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**8)+" cm??")
                        entree2.grid(row=3,column=3)
                        unite1.set("ha")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**10)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("ha")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**12)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("ha")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*10**14)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("ha")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*10**0)+" ha")
                        unite1.set("ha")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**4)+" yard??")
                        unite1.set("ha")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**5)+" pied??")
                        unite1.set("ha")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**7)+" pouce??")
                        unite1.set("ha")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*0.39*10**(-2))+" mille??")
                        unite1.set("ha")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'yard??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*8.36*10**-7)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("yard??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*8.36*10**-5)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("yard??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*8.36*10**-3)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("yard??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*8.36*10**-1)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("yard??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*8.36*10**1)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("yard??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*8.36*10**3)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("yard??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*8.36*10**5)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("yard??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*8.36*10**7)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("yard??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*8.36*10**9)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("yard??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*8.36*10**-5)+" ha")
                        unite1.set("yard??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*1.2*10**6)+" yard??")
                        unite1.set("yard??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1.076*10**7)+" pied??")
                        unite1.set("yard??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.6*10**9)+" pouce??")
                        unite1.set("yard??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*3.23*10**-7)+" mille??")
                        unite1.set("yard??")
                        entree2.grid(row=3,column=3)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                    
                if surface1.get() == 'pied??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*9.29*10**-8)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pied??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*9.29*10**-6)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pied??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*9.29*10**-4)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pied??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*9.29*10**-2)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pied??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*9.29*10**0)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pied??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*9.29*10**2)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pied??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*9.29*10**4)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pied??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*9.29*10**6)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pied??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*9.29*10**8)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pied??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*9.29*10**-3)+" ha")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*0.11*10**0)+" yard??")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1)+" pied??")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*144)+" pouce??")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*3.59*10**-8)+" mille??")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'pouce??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*6.45*10**-10)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*6.45*10**-8)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*6.45*10**-6)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*6.45*10**-4)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*6.45*10**-2)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*6.45*10**0)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*6.45*10**2)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*6.45*10**4)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*6.45*10**6)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*6.45*10**-8)+" ha")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*7.71*10**-4)+" yard??")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*6.94*10**-3)+" pied??")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1)+" pouce??")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*2.491*10**-10)+" mille??")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'mille??':
                    if surface2.get() == 'kilom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*2.59*10**0)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'hectom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*2.59*10**2)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'd??cam??tre??':
                        resultatConvertis.set(str(float(entree1.get())*2.59*10**4)+" dam??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*2.59*10**6)+" m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'd??cim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*2.59*10**8)+" dm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'centim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*2.59*10**10)+" cm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'millim??tre??':
                        resultatConvertis.set(str(float(entree1.get())*2.59*10**12)+" mm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'microm??tre??':
                        resultatConvertis.set(str(float(entree1.get())*2.59*10**14)+" ??m??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'nanom??tre??':
                        resultatConvertis.set(str(float(entree1.get())*2.59*10**16)+" nm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'hectare':
                        resultatConvertis.set(str(float(entree1.get())*2.59*10**2)+" ha")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'yard??':
                        resultatConvertis.set(str(float(entree1.get())*3.1*10**6)+" yard??")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*2.8*10**7)+" pied??")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*4.017*10**9)+" pouce??")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'mille??':
                        resultatConvertis.set(str(float(entree1.get())*1)+" mille??")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)

                
            
            surface1=ttk.Combobox(frameSurface)
            surface1.grid(row=2,column=1)

            surface1['values']=('kilom??tre??',
                                'hectom??tre??',
                                'd??cam??tre??',
                                'm??tre??',
                                'd??cim??tre??',
                                'centim??tre??',
                                'millim??tre??',
                                'microm??tre??',
                                'nanom??tre??',
                                'hectare',
                                'yard??',
                                'pied??',
                                'pouce??',
                                'mille??',
                                '         ')
            surface1.current(14)

            surface2=ttk.Combobox(frameSurface)
            surface2.grid(row=2,column=4)

            surface2['values']=('kilom??tre??',
                                'hectom??tre??',
                                'd??cam??tre??',
                                'm??tre??',
                                'd??cim??tre??',
                                'centim??tre??',
                                'millim??tre??',
                                'microm??tre??',
                                'nanom??tre??',
                                'hectare',
                                'yard??',
                                'pied??',
                                'pouce??',
                                'mille??',
                                '          ')
            surface2.current(14)

            uniteLabel1=Label(frameSurface, textvariable=unite1, fg=fontColor, bg=backgroundColor, font=fontTexte)
            uniteLabel1.grid(row=3,column=2)

            fleche1=Label(frameSurface, text="=>", fg=fontColor, bg=backgroundColor, font=fontTexte)
            fleche1.grid(row=2,column=3)
            fleche2=Label(frameSurface, text="=>", fg=fontColor, bg=backgroundColor, font=fontTexte)
            fleche2.grid(row=3,column=3)

            entree1=Spinbox(frameSurface, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
            entree1.grid(row=3,column=1)

            

            entree2=Label(frameSurface, textvariable=resultatConvertis, width=50, fg=fontColor, bg=backgroundColor, font=fontTexte)
            entree2.grid(row=3,column=4)

            valider=Button(frameSurface, text="Valider", command=valider, bg="green", font=fontTexte)
            valider.grid(row=3, column=6)

            def retourSurface():
                frameSurface.destroy()
                chap4Menu()
                
            retourSurfaceButton=Button(frameSurface, image=boutonRetour, command=retourSurface, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
            retourSurfaceButton.grid(row=2, column=10)
        
        def volume():
            frameChap4.pack_forget()
            frameVolume=LabelFrame(fenetrePrincipal, text="3. Conversion de Volume", fg=fontColor, bg=backgroundColor)
            frameVolume.configure(font=fontTitle)
            frameVolume.pack()

            resultatConvertis=StringVar()
            unite1=StringVar()
            unite2=StringVar()

            def valider():
                entree2.grid_forget()

                

                if surface1.get() == 'Gallon am??ricain':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get()))+" Gallon am??ricain")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*4)+" Quart am??ricain")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())*8)+" Pinte am??ricaine liquide")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*15.773)+" Tasse am??ricaine")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*128)+" Once liquide am??ricaine")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*256)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*768)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/264)+" m??")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())*3.785)+" L")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*3785)+" mL")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/1.201)+" Gallon imp??rial")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())*3.331)+" Quart imp??rial")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*6.661)+" Pinte imp??riale")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*13.323)+" Tasse imp??riale")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*133)+" Once liquide imp??riale")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*213)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*639)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/7.481)+" pied??")
                        unite1.set("Gallon am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*231)+" pouce??")
                        unite1.set("km??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Quart am??ricain':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/4)+" Gallon am??ricain")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Quart am??ricain")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())*2)+" Pinte am??ricaine liquide")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*3.943)+" Tasse am??ricaine")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*32)+" Once liquide am??ricaine")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*64)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*192)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/1057)+" m??")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/1.057)+" L")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*946)+" mL")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/4.804)+" Gallon imp??rial")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/1.201)+" Quart imp??rial")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1.665)+" Pinte imp??riale")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*3.331)+" Tasse imp??riale")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*33.307)+" Once liquide imp??riale")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*53.291)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*160)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/29.922)+" pied??")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*57.75)+" pouce??")
                        unite1.set("Quart am??ricain")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Pinte am??ricaine liquide':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*8)+" Gallon am??ricain")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*2)+" Quart am??ricain")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Pinte am??ricaine liquide")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*1.972)+" Tasse am??ricaine")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*16)+" Once liquide am??ricaine")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*32)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*96)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/2113)+" metre??")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/2.113)+" L")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*473)+" mL")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/9.608)+" Gallon imp??rial")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/2.402)+" Quart imp??rial")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/1.201)+" Pinte imp??riale")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1.665)+" Tasse imp??riale")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*16.653)+" Once liquide imp??riale")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*26.646)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*79.937)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/59.844)+" pied??")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*29.975)+" pouce??")
                        unite1.set("Pinte am??ricaine liquide")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Tasse am??ricaine':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/15.773)+" Gallon am??ricain")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/3.943)+" Quart am??ricain")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())/1.972)+" Pinte am??ricaine liquide")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Tasse am??ricaine")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*8.115)+" Once liquide am??ricaine")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*16.231)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*48.692)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/4167)+" m??")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/4.167)+" L")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*240)+" mL")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/18.942)+" Gallon imp??rial")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/4.736)+" Quart imp??rial")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/2.368)+" Pinte imp??riale")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/1.184)+" Tasse imp??riale")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*8.447)+" Once liquide imp??riale")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*13.515)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*40.545)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/118)+" pied??")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*14.646)+" pouce??")
                        unite1.set("Tasse am??ricaine")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Once liquide am??ricaine':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/128)+" Gallon am??ricain")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/32)+" Quart am??ricain")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())/16)+" Pinte am??ricaine liquide")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/8.115)+" Tasse am??ricaine")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Once liquide am??ricaine")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*2)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*6)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/33814)+" m??")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/33.814)+" L")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*29.574)+" mL")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/154)+" Gallon imp??rial")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/38.43)+" Quart imp??rial")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/19.215)+" Pinte imp??riale")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/9.608)+" Tasse imp??riale")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1.041)+" Once liquide imp??riale")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1.665)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*4.996)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/958)+" pied??")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.805)+" pouce??")
                        unite1.set("Once liquide am??ricaine")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Cuill??re ?? soupe am??ricaine':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/256)+" Gallon am??ricain")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/64)+" Quart am??ricain")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())/32)+" Pinte am??ricaine liquide")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/16.231)+" Tasse am??ricaine")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/2)+" Once liquide am??ricaine")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*3)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/67628)+" m??")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/67.628)+" L")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*14.787)+" mL")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/307)+" Gallon imp??rial")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/76.861)+" Quart imp??rial")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/38.43)+" Pinte imp??riale")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/19.215)+" Tasse imp??riale")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/1.922)+" Once liquide imp??riale")
                        unite1.set("TCuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/1.201)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*2.498)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/1915)+" pied??")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())/1.108)+" pouce??")
                        unite1.set("Cuill??re ?? soupe am??ricaine")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Cuill??re ?? caf?? am??ricaine':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/768)+" Gallon am??ricain")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/192)+" Quart am??ricain")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())/96)+" Pinte am??ricaine liquide")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/48.692)+" Tasse am??ricaine")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/6)+" Once liquide am??ricaine")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/3)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/202884)+" m??")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/203)+" L")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*4.929)+" mL")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/922)+" Gallon imp??rial")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/231)+" Quart imp??rial")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/115)+" Pinte imp??riale")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/57.646)+" Tasse imp??riale")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/5.765)+" Once liquide imp??riale")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/3.603)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/1.201)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/5745)+" pied??")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())/3.325)+" pouce??")
                        unite1.set("Cuill??re ?? caf?? am??ricaine")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'metre??':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*264)+" Gallon am??ricain")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*1057)+" Quart am??ricain")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())*2113)+" Pinte am??ricaine liquide")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*4167)+" Tasse am??ricaine")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*33814)+" Once liquide am??ricaine")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*67628)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*202884)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())*1)+" m??")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())*1000)+" L")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*10**6)+" mL")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())*220)+" Gallon imp??rial")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())*880)+" Quart imp??rial")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1760)+" Pinte imp??riale")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*3520)+" Tasse imp??riale")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*35195)+" Once liquide imp??riale")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*56312)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*168936)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*35.315)+" pied??")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*61024)+" pouce??")
                        unite1.set("m??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'litre':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/3.785)+" Gallon am??ricain")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*1.057)+" Quart am??ricain")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())*2.113)+" Pinte am??ricaine liquide")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*4.167)+" Tasse am??ricaine")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*33.814)+" Once liquide am??ricaine")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*67.628)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*202.884)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())*1000)+" m??")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())*1)+" L")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*1000)+" mL")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/4.546)+" Gallon imp??rial")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/1.137)+" Quart imp??rial")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1.760)+" Pinte imp??riale")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*3.520)+" Tasse imp??riale")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*35.195)+" Once liquide imp??riale")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*56.312)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*168.936)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/28.317)+" pied??")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*61.024)+" pouce??")
                        unite1.set("litre")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'millilitre':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/3785)+" Gallon am??ricain")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/946)+" Quart am??ricain")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())/473)+" Pinte am??ricaine liquide")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/240)+" Tasse am??ricaine")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/29.574)+" Once liquide am??ricaine")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/14.787)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/4.929)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/10**6)+" m??")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/1000)+" L")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*1)+" mL")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/4546)+" Gallon imp??rial")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/1137)+" Quart imp??rial")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/568)+" Pinte imp??riale")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/284)+" Tasse imp??riale")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/28.413)+" Once liquide imp??riale")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/17.758)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/5.919)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/28317)+" pied??")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())/16.387)+" pouce??")
                        unite1.set("millilitre")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Gallon imp??rial':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*1.201)+" Gallon am??ricain")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*4.804)+" Quart am??ricain")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())*9.608)+" Pinte am??ricaine liquide")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*18.942)+" Tasse am??ricaine")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*154)+" Once liquide am??ricaine")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*307)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*922)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/220)+" m??")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())*4.546)+" L")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*4546)+" mL")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Gallon imp??rial")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())*4)+" Quart imp??rial")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*8)+" Pinte imp??riale")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*16)+" Tasse imp??riale")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*160)+" Once liquide imp??riale")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*256)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*768)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/6.229)+" pied??")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*277)+" pouce??")
                        unite1.set("Gallon imp??rial")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Quart imp??rial':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/3.331)+" Gallon am??ricain")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*1.201)+" Quart am??ricain")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())*2.402)+" Pinte am??ricaine liquide")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*4.736)+" Tasse am??ricaine")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*38.43)+" Once liquide am??ricaine")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*76.861)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*231)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/880)+" m??")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())*1.137)+" L")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*1137)+" mL")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/4)+" Gallon imp??rial")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Quart imp??rial")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*2)+" Pinte imp??riale")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*4)+" Tasse imp??riale")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*40)+" Once liquide imp??riale")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*64)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*192)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*24.915)+" pied??")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*69.355)+" pouce??")
                        unite1.set("Quart imp??rial")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Pinte imp??rial':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/6.661)+" Gallon am??ricain")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/1.665)+" Quart am??ricain")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())*1.201)+" Pinte am??ricaine liquide")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*2.368)+" Tasse am??ricaine")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*19.215)+" Once liquide am??ricaine")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*38.43)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*115)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/1760)+" m??")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/1.76)+" L")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*568)+" mL")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/8)+" Gallon imp??rial")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/2)+" Quart imp??rial")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Pinte imp??riale")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*2)+" Tasse imp??riale")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*20)+" Once liquide imp??riale")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*32)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*96)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/49.831)+" pied??")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*34.677)+" pouce??")
                        unite1.set("Pinte imp??rial")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Tasse imp??rial':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/13.323)+" Gallon am??ricain")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/3.331)+" Quart am??ricain")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())/1.665)+" Pinte am??ricaine liquide")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*1.184)+" Tasse am??ricaine")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*9.608)+" Once liquide am??ricaine")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*19.215)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*57.646)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/3520)+" m??")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/3.52)+" L")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*284)+" mL")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/16)+" Gallon imp??rial")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/4)+" Quart imp??rial")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/2)+" Pinte imp??riale")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Tasse imp??riale")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*10)+" Once liquide imp??riale")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*16)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*48)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/99.661)+" pied??")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*17.339)+" pouce??")
                        unite1.set("Tasse imp??rial")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Once liquide imp??riale':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/133)+" Gallon am??ricain")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/33.307)+" Quart am??ricain")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())/16.653)+" Pinte am??ricaine liquide")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/8.447)+" Tasse am??ricaine")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/1.041)+" Once liquide am??ricaine")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*1.922)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*5.765)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/35195)+" m??")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/35.195)+" L")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*28.413)+" mL")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/160)+" Gallon imp??rial")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/40)+" Quart imp??rial")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/20)+" Pinte imp??riale")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/10)+" Tasse imp??riale")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Once liquide imp??riale")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1.6)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*4.8)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/997)+" pied??")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.734)+" pouce??")
                        unite1.set("Once liquide imp??riale")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Cuill??re ?? soupe imp??riale':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/213)+" Gallon am??ricain")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/53.291)+" Quart am??ricain")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())/26.646)+" Pinte am??ricaine liquide")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/13.515)+" Tasse am??ricaine")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/1665)+" Once liquide am??ricaine")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*1.201)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*3.603)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/56312)+" m??")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/56.312)+" L")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*17.758)+" mL")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/256)+" Gallon imp??rial")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/64)+" Quart imp??rial")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/32)+" Pinte imp??riale")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/16)+" Tasse imp??riale")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/1.6)+" Once liquide imp??riale")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*3)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/1595)+" pied??")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1.084)+" pouce??")
                        unite1.set("Cuill??re ?? soupe imp??riale")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Cuill??re ?? caf?? imp??riale':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/639)+" Gallon am??ricain")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/160)+" Quart am??ricain")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())/79.937)+" Pinte am??ricaine liquide")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/40.545)+" Tasse am??ricaine")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/4.996)+" Once liquide am??ricaine")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/2.498)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*1.201)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/168936)+" m??")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/169)+" L")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*5.919)+" mL")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/768)+" Gallon imp??rial")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/192)+" Quart imp??rial")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/96)+" Pinte imp??riale")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/48)+" Tasse imp??riale")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/4.8)+" Once liquide imp??riale")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/3)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())/4784)+" pied??")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())/2.768)+" pouce??")
                        unite1.set("Cuill??re ?? caf?? imp??riale")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'pied??':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*7.481)+" Gallon am??ricain")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())*29.922)+" Quart am??ricain")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())*59.844)+" Pinte am??ricaine liquide")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*118)+" Tasse am??ricaine")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*958)+" Once liquide am??ricaine")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*1915)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*5745)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/35.315)+" m??")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())*28.317)+" L")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*28317)+" mL")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())*6.229)+" Gallon imp??rial")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())*24.915)+" Quart imp??rial")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*49.831)+" Pinte imp??riale")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*99.661)+" Tasse imp??riale")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*997)+" Once liquide imp??riale")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*1595)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*4784)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1)+" pied??")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1728)+" pouce??")
                        unite1.set("pied??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'pouce??':
                    if surface2.get() == 'Gallon am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/231)+" Gallon am??ricain")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart am??ricain':
                        resultatConvertis.set(str(float(entree1.get())/57.75)+" Quart am??ricain")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte am??ricaine liquide':
                        resultatConvertis.set(str(float(entree1.get())/28.875)+" Pinte am??ricaine liquide")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/14.646)+" Tasse am??ricaine")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())/1.805)+" Once liquide am??ricaine")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*1.108)+" Cuill??re ?? soupe am??ricaine")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? am??ricaine':
                        resultatConvertis.set(str(float(entree1.get())*3.325)+" Cuill??re ?? caf?? am??ricaine")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'metre??':
                        resultatConvertis.set(str(float(entree1.get())/61024)+" m??")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'litre':
                        resultatConvertis.set(str(float(entree1.get())/61.024)+" L")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'millilitre':
                        resultatConvertis.set(str(float(entree1.get())*16.387)+" mL")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Gallon imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/277)+" Gallon imp??rial")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Quart imp??rial':
                        resultatConvertis.set(str(float(entree1.get())/69.355)+" Quart imp??rial")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Pinte imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/34.677)+" Pinte imp??riale")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Tasse imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/17.339)+" Tasse imp??riale")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Once liquide imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/1.734)+" Once liquide imp??riale")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? soupe imp??riale':
                        resultatConvertis.set(str(float(entree1.get())/1.084)+" Cuill??re ?? soupe imp??riale")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'Cuill??re ?? caf?? imp??riale':
                        resultatConvertis.set(str(float(entree1.get())*2.768)+" Cuill??re ?? caf?? imp??riale")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pied??':
                        resultatConvertis.set(str(float(entree1.get())*1728)+" pied??")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    elif surface2.get() == 'pouce??':
                        resultatConvertis.set(str(float(entree1.get())*1)+" pouce??")
                        unite1.set("pouce??")
                        entree2.grid(row=3,column=4)
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                

                
            
            surface1=ttk.Combobox(frameVolume)
            surface1.grid(row=2,column=1)

            surface1['values']=('Gallon am??ricain',
                                'Quart am??ricain',
                                'Pinte am??ricaine liquide',
                                'Tasse am??ricaine',
                                'Once liquide am??ricaine',
                                'Cuill??re ?? soupe am??ricaine',
                                'Cuill??re ?? caf?? am??ricaine',
                                'metre??',
                                'litre',
                                'millilitre',
                                'Gallon imp??rial',
                                'Quart imp??rial',
                                'Pinte imp??riale',
                                'Tasse imp??riale',
                                'Once liquide imp??riale',
                                'Cuill??re ?? soupe imp??riale',
                                'Cuill??re ?? caf?? imp??riale',
                                'pied??',
                                'pouce??',
                                '         ')
            surface1.current(19)

            surface2=ttk.Combobox(frameVolume)
            surface2.grid(row=2,column=4)

            surface2['values']=('Gallon am??ricain',
                                'Quart am??ricain',
                                'Pinte am??ricaine liquide',
                                'Tasse am??ricaine',
                                'Once liquide am??ricaine',
                                'Cuill??re ?? soupe am??ricaine',
                                'Cuill??re ?? caf?? am??ricaine',
                                'metre??',
                                'litre',
                                'millilitre',
                                'Gallon imp??rial',
                                'Quart imp??rial',
                                'Pinte imp??riale',
                                'Tasse imp??riale',
                                'Once liquide imp??riale',
                                'Cuill??re ?? soupe imp??riale',
                                'Cuill??re ?? caf?? imp??riale',
                                'pied??',
                                'pouce??',
                                '         ')
            surface2.current(19)

            uniteLabel1=Label(frameVolume, textvariable=unite1, fg=fontColor, bg=backgroundColor, font=fontTexte)
            uniteLabel1.grid(row=3,column=2)

            fleche1=Label(frameVolume, text="=>", fg=fontColor, bg=backgroundColor, font=fontTexte)
            fleche1.grid(row=2,column=3)
            fleche2=Label(frameVolume, text="=>", fg=fontColor, bg=backgroundColor, font=fontTexte)
            fleche2.grid(row=3,column=3)

            entree1=Spinbox(frameVolume, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
            entree1.grid(row=3,column=1)

            

            entree2=Label(frameVolume, textvariable=resultatConvertis, width=50, fg=fontColor, bg=backgroundColor, font=fontTexte)
            entree2.grid(row=3,column=4)

            valider=Button(frameVolume, text="Valider", command=valider, bg="green", font=fontTexte)
            valider.grid(row=3, column=6)

            def retourSurface():
                frameVolume.destroy()
                chap4Menu()
                
            retourVolumeButton=Button(frameVolume, image=boutonRetour, command=retourSurface, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
            retourVolumeButton.grid(row=2, column=10)
        
        def temperature():
            frameChap4.pack_forget()
            frameTemperature=LabelFrame(fenetrePrincipal, text="2. Conversion de Temperature", fg=fontColor, bg=backgroundColor)
            frameTemperature.configure(font=fontTitle)
            frameTemperature.pack()

            resultatConvertis=StringVar()
            unite1=StringVar()
            unite2=StringVar()

            def valider():
                entree2.grid_forget()


                if surface1.get() == 'Degr?? Celsius':
                    if surface2.get() == 'Degr?? Fahrenheit':
                        resultatConvertis.set(str(float(entree1.get())*(9/5)+32)+" ??F")
                        entree2.grid(row=3,column=4)
                        unite1.set("??C")
                    elif surface2.get() == 'Degr?? Celsius':
                        resultatConvertis.set(str(float(entree1.get())*1)+" ??C")
                        entree2.grid(row=3,column=4)
                        unite1.set("??C")
                    elif surface2.get() == 'Kelvin':
                        resultatConvertis.set(str(float(entree1.get())+273.15)+" K")
                        entree2.grid(row=3,column=4)
                        unite1.set("??C")
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Degr?? Fahrenheit':
                    if surface2.get() == 'Degr?? Fahrenheit':
                        resultatConvertis.set(str(float(entree1.get())*1)+" ??F")
                        entree2.grid(row=3,column=4)
                        unite1.set("??F")
                    elif surface2.get() == 'Degr?? Celsius':
                        resultatConvertis.set(str((float(entree1.get())-32)*(5/9))+" ??C")
                        entree2.grid(row=3,column=4)
                        unite1.set("??F")
                    elif surface2.get() == 'Kelvin':
                        resultatConvertis.set(str(((float(entree1.get())-32)*(5/9))+273.15)+" K")
                        entree2.grid(row=3,column=4)
                        unite1.set("??F")
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)
                
                if surface1.get() == 'Kelvin':
                    if surface2.get() == 'Degr?? Fahrenheit':
                        resultatConvertis.set(str((float(entree1.get())-273.15)*(9/5)+32)+" km??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'Degr?? Celsius':
                        resultatConvertis.set(str(float(entree1.get())-273.15)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    elif surface2.get() == 'Kelvin':
                        resultatConvertis.set(str(float(entree1.get())*1)+" hm??")
                        entree2.grid(row=3,column=4)
                        unite1.set("pouce??")
                    else :
                        resultatConvertis.set("ERROR")
                        entree2.grid(row=3,column=4)

                
            
            surface1=ttk.Combobox(frameTemperature)
            surface1.grid(row=2,column=1)

            surface1['values']=('Degr?? Celsius',
                                'Degr?? Fahrenheit',
                                'Kelvin',
                                '         ')
            surface1.current(3)

            surface2=ttk.Combobox(frameTemperature)
            surface2.grid(row=2,column=4)

            surface2['values']=('Degr?? Celsius',
                                'Degr?? Fahrenheit',
                                'Kelvin',
                                '          ')
            surface2.current(3)

            uniteLabel1=Label(frameTemperature, textvariable=unite1, fg=fontColor, bg=backgroundColor, font=fontTexte)
            uniteLabel1.grid(row=3,column=2)

            fleche1=Label(frameTemperature, text="=>", fg=fontColor, bg=backgroundColor, font=fontTexte)
            fleche1.grid(row=2,column=3)
            fleche2=Label(frameTemperature, text="=>", fg=fontColor, bg=backgroundColor, font=fontTexte)
            fleche2.grid(row=3,column=3)

            entree1=Spinbox(frameTemperature, textvariable=int, width=50, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
            entree1.grid(row=3,column=1)

            

            entree2=Label(frameTemperature, textvariable=resultatConvertis, width=50, fg=fontColor, bg=backgroundColor, font=fontTexte)
            entree2.grid(row=3,column=4)

            valider=Button(frameTemperature, text="Valider", command=valider, bg="green", font=fontTexte)
            valider.grid(row=3, column=6)

            def retourSurface():
                frameTemperature.destroy()
                chap4Menu()
                
            retourSurfaceButton=Button(frameTemperature, image=boutonRetour, command=retourSurface, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
            retourSurfaceButton.grid(row=2, column=10)
        

        distanceButton=Button(frameChap4, command=distance, text="Distance", width=20, pady=5, fg=fontColor, bg=buttonColor, font=fontButton)
        distanceButton.grid(row=1,column=1)
        surfaceButton=Button(frameChap4, command=surface, text="Surface", width=20, pady=5, fg=fontColor, bg=buttonColor, font=fontButton)
        surfaceButton.grid(row=1,column=2)
        volumeButton=Button(frameChap4, command=volume, text="Volume", width=20, pady=5, fg=fontColor, bg=buttonColor, font=fontButton)
        volumeButton.grid(row=2,column=1)
        temperatureButton=Button(frameChap4, command=temperature, text="Temperature", width=20, pady=5, fg=fontColor, bg=buttonColor, font=fontButton)
        temperatureButton.grid(row=2,column=2)

        def retourChap4():
            frameChap4.destroy()
            principal()
            
        retourChap4Button=Button(frameChap4, image=boutonRetour, command=retourChap4, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
        retourChap4Button.grid(row=1, column=10)

    def chap5Menu():
        framePrincipal.destroy()
        frameChap5=LabelFrame(fenetrePrincipal, text="5. Triangles rectangles", fg=fontColor, bg=backgroundColor)
        frameChap5.configure(font=fontTitle)
        frameChap5.pack()


        def valider():
            a=float(entreeA.get())
            b=float(entreeB.get())
            c=float(entreeC.get())
            if a**2+b**2==c**2:
                valeurResultat.set("Le triangle est rectangle")
            else:
                valeurResultat.set("Le triangle n'est pas rectangle")

        valeurResultat=StringVar()
        Resultat=Label(frameChap5, textvariable=valeurResultat, fg=fontColor, bg=backgroundColor, font=fontTexte)
        Resultat.grid(row=3,column=2)

        labelA=Label(frameChap5, text="Premier cot??", fg=fontColor, bg=backgroundColor, font=fontTexte)
        labelA.grid(row=1,column=1)
        entreeA=Spinbox(frameChap5, textvariable=int, width=30, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
        entreeA.grid(row=2,column=1)
        
        labelB=Label(frameChap5, text="Second cot??", fg=fontColor, bg=backgroundColor, font=fontTexte)
        labelB.grid(row=1,column=2)
        entreeB=Spinbox(frameChap5, textvariable=int, width=30, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
        entreeB.grid(row=2,column=2)

        labelC=Label(frameChap5, text="Plus long cot??", fg=fontColor, bg=backgroundColor, font=fontTexte)
        labelC.grid(row=1,column=3)
        entreeC=Spinbox(frameChap5, textvariable=int, width=30, from_=0, to=1000000, fg=fontColor, bg=buttonColor, font=fontTexte)
        entreeC.grid(row=2,column=3)

        validerButton=Button(frameChap5, text="Valider", command=valider, width=10, bg="green", font=fontTexte)
        validerButton.grid(row=2,column=4)

        def retourChap5():
            frameChap5.destroy()
            principal()
            
        retourChap5Button=Button(frameChap5, image=boutonRetour, command=retourChap5, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
        retourChap5Button.grid(row=1, column=10)
    
    def chap6Menu():
        framePrincipal.destroy()
        frameChap6=LabelFrame(fenetrePrincipal, text="6. D??rivation", fg=fontColor, bg=backgroundColor)
        frameChap6.configure(font=fontTitle)
        frameChap6.pack()
        frameEspaceChap6=Frame(fenetrePrincipal, pady=30, bg=backgroundColor)
        frameEspaceChap6.pack()
        frameNoticeChap6=LabelFrame(fenetrePrincipal, text="Notice :", pady=30, fg=fontColor, bg=backgroundColor)
        frameNoticeChap6.configure(font=fontTitle)
        frameNoticeChap6.pack()
        
        

        x=Symbol('x')

        def valider():
            fstr=str(fonctionsEntree.get())
            f=sympify(fstr)
            f_prime=f.diff(x)
            resultatValeur.set(f_prime)

        resultatValeur=StringVar()

        fonctionsEntree=Entry(frameChap6, width=70, fg=fontColor, font=fontTexte)
        fonctionsEntree.grid(row=1,column=2)
        fonctionsDerive=Label(frameChap6, textvariable=resultatValeur, width=20, pady=5, fg=fontColor, bg=backgroundColor, font=fontTexte)
        fonctionsDerive.grid(row=3,column=2)
        validerButton=Button(frameChap6, text="Valider", command=valider, width=20, pady=5, bg="green", font=fontTexte)
        validerButton.grid(row=1,column=3)

        labelNotice=Label(frameNoticeChap6, text="Voici le formats a utiliser dans le champs d'entr??e :\n pour x?? => x**2\n pour 4x => 4*x", width=100, pady=10, fg=fontColor, bg=backgroundColor, font=fontTexte)
        labelNotice.grid(row=1, column=1)

        def retourChap6():
            frameChap6.destroy()
            frameNoticeChap6.destroy()
            principal()
            
        retourChap5Button=Button(frameChap6, image=boutonRetour, command=retourChap6, background=backgroundColor, activebackground=backgroundColor, relief=FLAT)
        retourChap5Button.grid(row=1, column=10)

    framePrincipal=Frame(fenetrePrincipal, borderwidth=2, bg=backgroundColor)
    framePrincipal.pack(side=TOP)
    chap1Button=Button(framePrincipal,  command=chap1Menu, bg=buttonColor, image=geometrieImage, activebackground=buttonColor)
    chap1Button.grid(row=1,column=1)
    chap1Label=Label(framePrincipal, text="Perimetre, Aire, Volume  ", fg=fontColor, font=fontButton, bg=backgroundColor)
    chap1Label.grid(row=1,column=0)

    chap2Button=Button(framePrincipal, command=chap2Menu, bg=buttonColor, image=probaImage, activebackground=buttonColor)
    chap2Button.grid(row=1,column=4)
    chap1Label=Label(framePrincipal, text="Probabilit??  ", fg=fontColor, font=fontButton, bg=backgroundColor)
    chap1Label.grid(row=1,column=3)

    chap3Button=Button(framePrincipal, command=chap3Menu, bg=buttonColor, image=nombreImage, activebackground=buttonColor)
    chap3Button.grid(row=2,column=1)
    chap1Label=Label(framePrincipal, text="Nombre Premier  ", fg=fontColor, font=fontButton, bg=backgroundColor)
    chap1Label.grid(row=2,column=0)

    chap4Button=Button(framePrincipal, command=chap4Menu, bg=buttonColor, image=conversionImage, activebackground=buttonColor)
    chap4Button.grid(row=2,column=4)
    chap1Label=Label(framePrincipal, text="Conversion  ", fg=fontColor, font=fontButton, bg=backgroundColor)
    chap1Label.grid(row=2,column=3)

    chap5Button=Button(framePrincipal, command=chap5Menu, bg=buttonColor, image=triangleImage, activebackground=buttonColor)
    chap5Button.grid(row=3,column=1)
    chap1Label=Label(framePrincipal, text="Triangle Rectangle  ", fg=fontColor, font=fontButton, bg=backgroundColor)
    chap1Label.grid(row=3,column=0)

    chap6Button=Button(framePrincipal, command=chap6Menu, bg=buttonColor, image=derivationImage, activebackground=buttonColor)
    chap6Button.grid(row=3,column=4)
    chap1Label=Label(framePrincipal, text="D??rivation  ", fg=fontColor, font=fontButton, bg=backgroundColor)
    chap1Label.grid(row=3,column=3)

    espace=Label(framePrincipal, text="                ", bg=backgroundColor)
    espace.grid(row=1,column=2)

    #chap11Button=Button(framePrincipal, text="11.Equation", command=chap11Menu)
    #chap7Button=Button(framePrincipal, text="7.Espaces", command=chap7Menu)
    #chap8Button=Button(framePrincipal, text="8.Th??or??me de Thal??s", command=chap8Menu)
    #chap9Button=Button(framePrincipal, text="9.Orthogonalit??", command=chap9Menu)
    #chap10Button=Button(framePrincipal, text="10.Trigonom??trie", command=chap10Menu)

    def theme():
        fenetreTheme=Tk()
        fenetreTheme.title('Th??me')
        fenetreTheme.config(background=backgroundColor)
        frameTheme=LabelFrame(fenetreTheme, text="Theme et Personnalisation", bg=backgroundColor, fg=fontColor)
        frameTheme.config(font=fontTitle)
        frameTheme.grid(row=1,column=1)
        frameThemeActuel=LabelFrame(fenetreTheme, text="Theme Actuel", bg=backgroundColor, fg=fontColor)
        frameThemeActuel.config(font=fontTitle)
        frameThemeActuel.grid(row=1,column=2)

        darkThemeImage=PhotoImage(file="Ressource/bouton/theme/themeDarkCapture.png", master=fenetreTheme)
        lightThemeImage=PhotoImage(file="Ressource/bouton/theme/themeLightCapture.png", master=fenetreTheme)
        godThemeImage=PhotoImage(file="Ressource/bouton/theme/themeGodCapture.png", master=fenetreTheme)
        princessThemeImage=PhotoImage(file="Ressource/bouton/theme/themePrincessCapture.png", master=fenetreTheme)
        ultraGreenThemeImage=PhotoImage(file="Ressource/bouton/theme/themeContrastGreenCapture.png", master=fenetreTheme)
        ultraBlueThemeImage=PhotoImage(file="Ressource/bouton/theme/themeContrastBlueCapture.png", master=fenetreTheme)
        ultraPinkThemeImage=PhotoImage(file="Ressource/bouton/theme/themeContrastPinkCapture.png", master=fenetreTheme)
        
        def darkTheme():
            fichier1Set=open("Ressource/txt/background.txt", "w")
            fichier1Set.write("gray20")
            fichier2Set=open("Ressource/txt/button.txt", "w")
            fichier2Set.write("gray40")
            fichier3Set=open("Ressource/txt/fontColor.txt", "w")
            fichier3Set.write("gray70")
            fichier4Set=open("Ressource/txt/infoTheme.txt", "w")
            fichier4Set.write("DARKTHEME")
            showwarning("Application du Theme", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreTheme.destroy()
        
        def lightTheme():
            fichier1=open("Ressource/txt/background.txt", "w")
            fichier1.write("gray80")
            fichier2=open("Ressource/txt/button.txt", "w")
            fichier2.write("white")
            fichier3Set=open("Ressource/txt/fontColor.txt", "w")
            fichier3Set.write("black")
            fichier4Set=open("Ressource/txt/infoTheme.txt", "w")
            fichier4Set.write("LIGHTTHEME")
            showwarning("Application du Theme", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreTheme.destroy()
        
        def godTheme():
            fichier1=open("Ressource/txt/background.txt", "w")
            fichier1.write("white")
            fichier2=open("Ressource/txt/button.txt", "w")
            fichier2.write("snow")
            fichier3Set=open("Ressource/txt/fontColor.txt", "w")
            fichier3Set.write("gray70")
            fichier4Set=open("Ressource/txt/infoTheme.txt", "w")
            fichier4Set.write("GODTHEME")
            showwarning("Application du Theme", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreTheme.destroy()
        
        def contrasteGreenTheme():
            fichier1=open("Ressource/txt/background.txt", "w")
            fichier1.write("gray20")
            fichier2=open("Ressource/txt/button.txt", "w")
            fichier2.write("gray40")
            fichier3Set=open("Ressource/txt/fontColor.txt", "w")
            fichier3Set.write("green2")
            fichier4Set=open("Ressource/txt/infoTheme.txt", "w")
            fichier4Set.write("ULTRACONTRASTGREENTHEME")
            showwarning("Application du Theme", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreTheme.destroy()
        
        def contrasteBlueTheme():
            fichier1=open("Ressource/txt/background.txt", "w")
            fichier1.write("gray20")
            fichier2=open("Ressource/txt/button.txt", "w")
            fichier2.write("gray40")
            fichier3Set=open("Ressource/txt/fontColor.txt", "w")
            fichier3Set.write("DodgerBlue2")
            fichier4Set=open("Ressource/txt/infoTheme.txt", "w")
            fichier4Set.write("ULTRACONTRASTBLUETHEME")
            showwarning("Application du Theme", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreTheme.destroy()
        
        def contrastePinkTheme():
            fichier1=open("Ressource/txt/background.txt", "w")
            fichier1.write("gray20")
            fichier2=open("Ressource/txt/button.txt", "w")
            fichier2.write("gray40")
            fichier3Set=open("Ressource/txt/fontColor.txt", "w")
            fichier3Set.write("deepPink3")
            fichier4Set=open("Ressource/txt/infoTheme.txt", "w")
            fichier4Set.write("ULTRACONTRASTPINKTHEME")
            showwarning("Application du Theme", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreTheme.destroy()
        
        def princessTheme():
            fichier1=open("Ressource/txt/background.txt", "w")
            fichier1.write("lavender")
            fichier2=open("Ressource/txt/button.txt", "w")
            fichier2.write("HotPink2")
            fichier3Set=open("Ressource/txt/fontColor.txt", "w")
            fichier3Set.write("black")
            fichier4Set=open("Ressource/txt/infoTheme.txt", "w")
            fichier4Set.write("PRINCESSTHEME")
            showwarning("Application du Theme", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreTheme.destroy()
            
        

        darkThemeButton=Button(frameTheme, image=darkThemeImage, bg='gray20', activebackground='gray40', command=darkTheme)
        darkThemeButton.grid(row=0,column=1)
        darkThemeLabel=Label(frameTheme, text="Dark Theme", bg=backgroundColor, fg=fontColor, font=fontTexte)
        darkThemeLabel.grid(row=1,column=1)

        contrasteGreenThemeButton=Button(frameTheme, image=ultraGreenThemeImage, bg='gray20', activebackground='gray40', command=contrasteGreenTheme)
        contrasteGreenThemeButton.grid(row=0,column=2)
        contrasteGreenThemeLabel=Label(frameTheme, text="Ultra Contrast Green Theme", bg=backgroundColor, fg=fontColor, font=fontTexte)
        contrasteGreenThemeLabel.grid(row=1,column=2)

        contrasteBlueThemeButton=Button(frameTheme, image=ultraBlueThemeImage, bg='gray20', activebackground='gray40', command=contrasteBlueTheme)
        contrasteBlueThemeButton.grid(row=2,column=1)
        contrasteBlueThemeLabel=Label(frameTheme, text="Ultra Contrast Blue Theme", bg=backgroundColor, fg=fontColor, font=fontTexte)
        contrasteBlueThemeLabel.grid(row=3,column=1)

        contrastePinkThemeButton=Button(frameTheme, image=ultraPinkThemeImage, bg='gray20', activebackground='gray40', command=contrastePinkTheme)
        contrastePinkThemeButton.grid(row=2,column=2)
        contrastePinkThemeLabel=Label(frameTheme, text="Ultra Contrast Pink Theme", bg=backgroundColor, fg=fontColor, font=fontTexte)
        contrastePinkThemeLabel.grid(row=3,column=2)

        lightThemeButton=Button(frameTheme, image=lightThemeImage, bg='gray80', activebackground='white', command=lightTheme)
        lightThemeButton.grid(row=4,column=1)
        darkThemeLabel=Label(frameTheme, text="Light Theme", bg=backgroundColor, fg=fontColor, font=fontTexte)
        darkThemeLabel.grid(row=5,column=1)

        godThemeButton=Button(frameTheme, image=godThemeImage, bg='white', activebackground='snow', command=godTheme)
        godThemeButton.grid(row=4,column=2)
        godThemeLabel=Label(frameTheme, text="God Theme", bg=backgroundColor, fg=fontColor, font=fontTexte)
        godThemeLabel.grid(row=5,column=2)

        princessThemeButton=Button(frameTheme, image=princessThemeImage, bg='lavender', activebackground='HotPink2', command=princessTheme)
        princessThemeButton.grid(row=6,column=1)
        princessThemeLabel=Label(frameTheme, text="Princess Theme", bg=backgroundColor, fg=fontColor, font=fontTexte)
        princessThemeLabel.grid(row=7,column=1)

        themeActuel=Label(frameThemeActuel, text=infoTheme, bg=backgroundColor, font=fontTexte, fg=fontColor)
        themeActuel.pack()

        fenetreTheme.mainloop()

    def font():
        fenetreFont=Tk()
        fenetreFont.title("Police d'??criture")
        fenetreFont.config(background=backgroundColor)
        frameFont=LabelFrame(fenetreFont, text="Police d'??criture", bg=backgroundColor, fg=fontColor)
        frameFont.config(font=fontTitle)
        frameFont.grid(row=1,column=1)
        frameFontActuel=LabelFrame(fenetreFont, text="Theme Actuel", bg=backgroundColor, fg=fontColor)
        frameFontActuel.config(font=fontTitle)
        frameFontActuel.grid(row=1,column=2)

        def arial():
            fichier5Set=open("Ressource/txt/font.txt", "w")
            fichier5Set.write("Arial")
            showwarning("Application de la Police d'??criture", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreFont.destroy()
        
        def roman():
            fichier5Set=open("Ressource/txt/font.txt", "w")
            fichier5Set.write("Roman")
            showwarning("Application de la Police d'??criture", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreFont.destroy()

        def calibri():
            fichier5Set=open("Ressource/txt/font.txt", "w")
            fichier5Set.write("Calibri")
            showwarning("Application de la Police d'??criture", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreFont.destroy()

        def courier():
            fichier5Set=open("Ressource/txt/font.txt", "w")
            fichier5Set.write("Courier")
            showwarning("Application de la Police d'??criture", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreFont.destroy()

        def georgia():
            fichier5Set=open("Ressource/txt/font.txt", "w")
            fichier5Set.write("Georgia")
            showwarning("Application de la Police d'??criture", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreFont.destroy()
        
        def segoe():
            fichier5Set=open("Ressource/txt/font.txt", "w")
            fichier5Set.write("Segoe")
            showwarning("Application de la Police d'??criture", "Veuillez red??marrer le logiciel")
            fenetrePrincipal.destroy()
            fenetreFont.destroy()
        
        if infoTheme == ['DARKTHEME']:
            arialImage=PhotoImage(file="Ressource/bouton/police/arialButtonImageDark.png", master=fenetreFont)
            calibriImage=PhotoImage(file="Ressource/bouton/police/calibriButtonImageDark.png", master=fenetreFont)
            courierImage=PhotoImage(file="Ressource/bouton/police/courierButtonImageDark.png", master=fenetreFont)
            georgiaImage=PhotoImage(file="Ressource/bouton/police/georgiaButtonImageDark.png", master=fenetreFont)
            romanImage=PhotoImage(file="Ressource/bouton/police/romanButtonImageDark.png", master=fenetreFont)
            segoeImage=PhotoImage(file="Ressource/bouton/police/segoeButtonImageDark.png", master=fenetreFont)
            arialButton=Button(frameFont, image=arialImage, command=arial, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            arialButton.grid(row=0, column=0)
            romanButton=Button(frameFont, image=romanImage, command=roman, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            romanButton.grid(row=0, column=2)
            calibriButton=Button(frameFont,image=calibriImage, command=calibri, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            calibriButton.grid(row=2, column=0)
            courierButton=Button(frameFont, image=courierImage, command=courier, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            courierButton.grid(row=2, column=2)
            georgiaButton=Button(frameFont, image=georgiaImage, command=georgia, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            georgiaButton.grid(row=4, column=0)
            segoeButton=Button(frameFont, image=segoeImage, command=segoe, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            segoeButton.grid(row=4, column=2)

        if infoTheme == ['GODTHEME']:
            arialImage=PhotoImage(file="Ressource/bouton/police/arialButtonImageGod.png", master=fenetreFont)
            calibriImage=PhotoImage(file="Ressource/bouton/police/calibriButtonImageGod.png", master=fenetreFont)
            courierImage=PhotoImage(file="Ressource/bouton/police/courierButtonImageGod.png", master=fenetreFont)
            georgiaImage=PhotoImage(file="Ressource/bouton/police/georgiaButtonImageGod.png", master=fenetreFont)
            romanImage=PhotoImage(file="Ressource/bouton/police/romanButtonImageGod.png", master=fenetreFont)
            segoeImage=PhotoImage(file="Ressource/bouton/police/segoeButtonImageGod.png", master=fenetreFont)
            arialButton=Button(frameFont, image=arialImage, command=arial, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            arialButton.grid(row=0, column=0)
            romanButton=Button(frameFont, image=romanImage, command=roman, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            romanButton.grid(row=0, column=2)
            calibriButton=Button(frameFont,image=calibriImage, command=calibri, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            calibriButton.grid(row=2, column=0)
            courierButton=Button(frameFont, image=courierImage, command=courier, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            courierButton.grid(row=2, column=2)
            georgiaButton=Button(frameFont, image=georgiaImage, command=georgia, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            georgiaButton.grid(row=4, column=0)
            segoeButton=Button(frameFont, image=segoeImage, command=segoe, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            segoeButton.grid(row=4, column=2)

        if infoTheme == ['LIGHTTHEME']:
            arialImage=PhotoImage(file="Ressource/bouton/police/arialButtonImage.png", master=fenetreFont)
            calibriImage=PhotoImage(file="Ressource/bouton/police/calibriButtonImage.png", master=fenetreFont)
            courierImage=PhotoImage(file="Ressource/bouton/police/courierButtonImage.png", master=fenetreFont)
            georgiaImage=PhotoImage(file="Ressource/bouton/police/georgiaButtonImage.png", master=fenetreFont)
            romanImage=PhotoImage(file="Ressource/bouton/police/romanButtonImage.png", master=fenetreFont)
            SimSunImage=PhotoImage(file="Ressource/bouton/police/SimSunButtonImage.png", master=fenetreFont)
            arialButton=Button(frameFont, image=arialImage, command=arial, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            arialButton.grid(row=0, column=0)
            romanButton=Button(frameFont, image=romanImage, command=roman, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            romanButton.grid(row=0, column=2)
            calibriButton=Button(frameFont,image=calibriImage, command=calibri, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            calibriButton.grid(row=2, column=0)
            courierButton=Button(frameFont, image=courierImage, command=courier, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            courierButton.grid(row=2, column=2)
            georgiaButton=Button(frameFont, image=georgiaImage, command=georgia, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            georgiaButton.grid(row=4, column=0)
            SimSunButton=Button(frameFont, image=SimSunImage, command=segoe, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            SimSunButton.grid(row=4, column=2)

        if infoTheme == ['ULTRACONTRASTGREENTHEME']:
            arialImage=PhotoImage(file="Ressource/bouton/police/arialButtonImageGreen.png", master=fenetreFont)
            calibriImage=PhotoImage(file="Ressource/bouton/police/calibriButtonImageGreen.png", master=fenetreFont)
            courierImage=PhotoImage(file="Ressource/bouton/police/courierButtonImageGreen.png", master=fenetreFont)
            georgiaImage=PhotoImage(file="Ressource/bouton/police/georgiaButtonImageGreen.png", master=fenetreFont)
            romanImage=PhotoImage(file="Ressource/bouton/police/romanButtonImageGreen.png", master=fenetreFont)
            segoeImage=PhotoImage(file="Ressource/bouton/police/segoeButtonImageGreen.png", master=fenetreFont)
            arialButton=Button(frameFont, image=arialImage, command=arial, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            arialButton.grid(row=0, column=0)
            romanButton=Button(frameFont, image=romanImage, command=roman, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            romanButton.grid(row=0, column=2)
            calibriButton=Button(frameFont,image=calibriImage, command=calibri, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            calibriButton.grid(row=2, column=0)
            courierButton=Button(frameFont, image=courierImage, command=courier, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            courierButton.grid(row=2, column=2)
            georgiaButton=Button(frameFont, image=georgiaImage, command=georgia, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            georgiaButton.grid(row=4, column=0)
            segoeButton=Button(frameFont, image=segoeImage, command=segoe, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            segoeButton.grid(row=4, column=2)

        if infoTheme == ['ULTRACONTRASTBLUETHEME']:
            arialImage=PhotoImage(file="Ressource/bouton/police/arialButtonImageBlue.png", master=fenetreFont)
            calibriImage=PhotoImage(file="Ressource/bouton/police/calibriButtonImageBlue.png", master=fenetreFont)
            courierImage=PhotoImage(file="Ressource/bouton/police/courierButtonImageBlue.png", master=fenetreFont)
            georgiaImage=PhotoImage(file="Ressource/bouton/police/georgiaButtonImageBlue.png", master=fenetreFont)
            romanImage=PhotoImage(file="Ressource/bouton/police/romanButtonImageBlue.png", master=fenetreFont)
            segoeImage=PhotoImage(file="Ressource/bouton/police/segoeButtonImageBlue.png", master=fenetreFont)
            arialButton=Button(frameFont, image=arialImage, command=arial, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            arialButton.grid(row=0, column=0)
            romanButton=Button(frameFont, image=romanImage, command=roman, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            romanButton.grid(row=0, column=2)
            calibriButton=Button(frameFont,image=calibriImage, command=calibri, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            calibriButton.grid(row=2, column=0)
            courierButton=Button(frameFont, image=courierImage, command=courier, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            courierButton.grid(row=2, column=2)
            georgiaButton=Button(frameFont, image=georgiaImage, command=georgia, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            georgiaButton.grid(row=4, column=0)
            segoeButton=Button(frameFont, image=segoeImage, command=segoe, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            segoeButton.grid(row=4, column=2)

        if infoTheme == ['ULTRACONTRASTPINKTHEME']:
            arialImage=PhotoImage(file="Ressource/bouton/police/arialButtonImagePink.png", master=fenetreFont)
            calibriImage=PhotoImage(file="Ressource/bouton/police/calibriButtonImagePink.png", master=fenetreFont)
            courierImage=PhotoImage(file="Ressource/bouton/police/courierButtonImagePink.png", master=fenetreFont)
            georgiaImage=PhotoImage(file="Ressource/bouton/police/georgiaButtonImagePink.png", master=fenetreFont)
            romanImage=PhotoImage(file="Ressource/bouton/police/romanButtonImagePink.png", master=fenetreFont)
            segoeImage=PhotoImage(file="Ressource/bouton/police/segoeButtonImagePink.png", master=fenetreFont)
            arialButton=Button(frameFont, image=arialImage, command=arial, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            arialButton.grid(row=0, column=0)
            romanButton=Button(frameFont, image=romanImage, command=roman, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            romanButton.grid(row=0, column=2)
            calibriButton=Button(frameFont,image=calibriImage, command=calibri, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            calibriButton.grid(row=2, column=0)
            courierButton=Button(frameFont, image=courierImage, command=courier, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            courierButton.grid(row=2, column=2)
            georgiaButton=Button(frameFont, image=georgiaImage, command=georgia, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            georgiaButton.grid(row=4, column=0)
            segoeButton=Button(frameFont, image=segoeImage, command=segoe, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            segoeButton.grid(row=4, column=2)

        if infoTheme == ['PRINCESSTHEME']:
            arialImage=PhotoImage(file="Ressource/bouton/police/arialButtonImagePrincess.png", master=fenetreFont)
            calibriImage=PhotoImage(file="Ressource/bouton/police/calibriButtonImagePrincess.png", master=fenetreFont)
            courierImage=PhotoImage(file="Ressource/bouton/police/courierButtonImagePrincess.png", master=fenetreFont)
            georgiaImage=PhotoImage(file="Ressource/bouton/police/georgiaButtonImagePrincess.png", master=fenetreFont)
            romanImage=PhotoImage(file="Ressource/bouton/police/romanButtonImagePrincess.png", master=fenetreFont)
            segoeImage=PhotoImage(file="Ressource/bouton/police/segoeButtonImagePrincess.png", master=fenetreFont)
            arialButton=Button(frameFont, image=arialImage, command=arial, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            arialButton.grid(row=0, column=0)
            romanButton=Button(frameFont, image=romanImage, command=roman, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            romanButton.grid(row=0, column=2)
            calibriButton=Button(frameFont,image=calibriImage, command=calibri, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            calibriButton.grid(row=2, column=0)
            courierButton=Button(frameFont, image=courierImage, command=courier, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            courierButton.grid(row=2, column=2)
            georgiaButton=Button(frameFont, image=georgiaImage, command=georgia, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            georgiaButton.grid(row=4, column=0)
            segoeButton=Button(frameFont, image=segoeImage, command=segoe, bg= backgroundColor, activebackground=backgroundColor, relief="flat")
            segoeButton.grid(row=4, column=2)

        

        

        fenetreFont.mainloop()
        
        
    
    #Commande Menu

    def lienWiki():
        webbrowser.open('https://github.com/Brome78/CALCUL/wiki')


    menubar=Menu(fenetrePrincipal, bg=backgroundColor)
    menuPersonaliser=Menu(menubar,tearoff=0)
    menuPersonaliser.add_command(label="Th??me", command=theme)
    menuPersonaliser.add_command(label="Police", command=font)
    menubar.add_cascade(label="Personnalisation", menu=menuPersonaliser)
    menuAide=Menu(menubar, tearoff=0)
    menuAide.add_command(label="Wiki...", command=lienWiki)
    menubar.add_cascade(label="Aide", menu=menuAide)

    fenetrePrincipal.config(menu=menubar)
    

fenetrePrincipal = Tk()
fenetrePrincipal.title('CALCUL')
fenetrePrincipal.config(background=backgroundColor)

boutonFermer=PhotoImage(file="Ressource/bouton/boutonFermer.png")

def close():
    fenetrePrincipal.destroy()

closeButton=Button(fenetrePrincipal,image=boutonFermer, command=close, bg=backgroundColor, relief=FLAT, activebackground=backgroundColor)
closeButton.pack(side=BOTTOM)





#Commande de plein ??cran

def fullscreenDestroy():
    fenetrePrincipal.attributes('-fullscreen', False)
def fullscreenActive():
    fenetrePrincipal.attributes('-fullscreen', True)

fenetrePrincipal.attributes('-fullscreen', True)
fenetrePrincipal.bind('<Escape>', lambda e: fullscreenDestroy())
fenetrePrincipal.bind('<F11>', lambda e: fullscreenActive())

if infoTheme == ['DARKTHEME']:
    geometrieImage=PhotoImage(file="Ressource/bouton/chap1/geometrieImageDark.png")
    probaImage=PhotoImage(file="Ressource/bouton/chap2/probaImageDark.png")
    nombreImage=PhotoImage(file="Ressource/bouton/chap3/nombreImageDark.png")
    conversionImage=PhotoImage(file="Ressource/bouton/chap4/conversionImageDark.png")
    triangleImage=PhotoImage(file="Ressource/bouton/chap5/triangleImageDark.png")
    derivationImage=PhotoImage(file="Ressource/bouton/chap6/derivationImageDark.png")
    carreAireImage=PhotoImage(file="Ressource/bouton/chap1/carreAireImageDark.png")
    carrePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/carrePerimetreImageDark.png")
    cercleAireImage=PhotoImage(file="Ressource/bouton/chap1/cercleAireImageDark.png")
    cerclePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/cerclePerimetreImageDark.png")
    coneImage=PhotoImage(file="Ressource/bouton/chap1/coneImageDark.png")
    cubeImage=PhotoImage(file="Ressource/bouton/chap1/cubeImageDark.png")
    cylindreImage=PhotoImage(file="Ressource/bouton/chap1/cylindreImageDark.png")
    losangeImage=PhotoImage(file="Ressource/bouton/chap1/losangeImageDark.png")
    parallelogrammeImage=PhotoImage(file="Ressource/bouton/chap1/parallelogrammeImageDark.png")
    paveImage=PhotoImage(file="Ressource/bouton/chap1/paveImageDark.png")
    pyramideImage=PhotoImage(file="Ressource/bouton/chap1/pyramideImageDark.png")
    rectangleAireImage=PhotoImage(file="Ressource/bouton/chap1/rectangleAireImageDark.png")
    rectanglePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/rectanglePerimetreImageDark.png")
    sphereImage=PhotoImage(file="Ressource/bouton/chap1/sphereImageDark.png")
    trapezeImage=PhotoImage(file="Ressource/bouton/chap1/trapezeImageDark.png")
    triangleAireImage=PhotoImage(file="Ressource/bouton/chap1/triangleAireImageDark.png")
    
    
    
    

if infoTheme == ['GODTHEME']:
    geometrieImage=PhotoImage(file="Ressource/bouton/chap1/geometrieImageDark.png")
    probaImage=PhotoImage(file="Ressource/bouton/chap2/probaImageDark.png")
    nombreImage=PhotoImage(file="Ressource/bouton/chap3/nombreImageDark.png")
    conversionImage=PhotoImage(file="Ressource/bouton/chap4/conversionImageDark.png")
    triangleImage=PhotoImage(file="Ressource/bouton/chap5/triangleImageDark.png")
    derivationImage=PhotoImage(file="Ressource/bouton/chap6/derivationImageDark.png")
    carreAireImage=PhotoImage(file="Ressource/bouton/chap1/carreAireImageDark.png")
    carrePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/carrePerimetreImageDark.png")
    cercleAireImage=PhotoImage(file="Ressource/bouton/chap1/cercleAireImageDark.png")
    cerclePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/cerclePerimetreImageDark.png")
    coneImage=PhotoImage(file="Ressource/bouton/chap1/coneImageDark.png")
    cubeImage=PhotoImage(file="Ressource/bouton/chap1/cubeImageDark.png")
    cylindreImage=PhotoImage(file="Ressource/bouton/chap1/cylindreImageDark.png")
    losangeImage=PhotoImage(file="Ressource/bouton/chap1/losangeImageDark.png")
    parallelogrammeImage=PhotoImage(file="Ressource/bouton/chap1/parallelogrammeImageDark.png")
    paveImage=PhotoImage(file="Ressource/bouton/chap1/paveImageDark.png")
    pyramideImage=PhotoImage(file="Ressource/bouton/chap1/pyramideImageDark.png")
    rectangleAireImage=PhotoImage(file="Ressource/bouton/chap1/rectangleAireImageDark.png")
    rectanglePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/rectanglePerimetreImageDark.png")
    sphereImage=PhotoImage(file="Ressource/bouton/chap1/sphereImageDark.png")
    trapezeImage=PhotoImage(file="Ressource/bouton/chap1/trapezeImageDark.png")
    triangleAireImage=PhotoImage(file="Ressource/bouton/chap1/triangleAireImageDark.png")
    

if infoTheme == ['LIGHTTHEME']:
    geometrieImage=PhotoImage(file="Ressource/bouton/chap1/geometrieImage.png")
    probaImage=PhotoImage(file="Ressource/bouton/chap2/probaImage.png")
    nombreImage=PhotoImage(file="Ressource/bouton/chap3/nombreImage.png")
    conversionImage=PhotoImage(file="Ressource/bouton/chap4/conversionImage.png")
    triangleImage=PhotoImage(file="Ressource/bouton/chap5/triangleImage.png")
    derivationImage=PhotoImage(file="Ressource/bouton/chap6/derivationImage.png")
    carreAireImage=PhotoImage(file="Ressource/bouton/chap1/carreAireImage.png")
    carrePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/carrePerimetreImage.png")
    cercleAireImage=PhotoImage(file="Ressource/bouton/chap1/cercleAireImage.png")
    cerclePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/cerclePerimetreImage.png")
    coneImage=PhotoImage(file="Ressource/bouton/chap1/coneImage.png")
    cubeImage=PhotoImage(file="Ressource/bouton/chap1/cubeImage.png")
    cylindreImage=PhotoImage(file="Ressource/bouton/chap1/cylindreImage.png")
    losangeImage=PhotoImage(file="Ressource/bouton/chap1/losangeImage.png")
    parallelogrammeImage=PhotoImage(file="Ressource/bouton/chap1/parallelogrammeImage.png")
    paveImage=PhotoImage(file="Ressource/bouton/chap1/paveImage.png")
    pyramideImage=PhotoImage(file="Ressource/bouton/chap1/pyramideImage.png")
    rectangleAireImage=PhotoImage(file="Ressource/bouton/chap1/rectangleAireImage.png")
    rectanglePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/rectanglePerimetreImage.png")
    sphereImage=PhotoImage(file="Ressource/bouton/chap1/sphereImage.png")
    trapezeImage=PhotoImage(file="Ressource/bouton/chap1/trapezeImage.png")
    triangleAireImage=PhotoImage(file="Ressource/bouton/chap1/triangleAireImage.png")
    

if infoTheme == ['ULTRACONTRASTGREENTHEME']:
    geometrieImage=PhotoImage(file="Ressource/bouton/chap1/geometrieImage.png")
    probaImage=PhotoImage(file="Ressource/bouton/chap2/probaImage.png")
    nombreImage=PhotoImage(file="Ressource/bouton/chap3/nombreImage.png")
    conversionImage=PhotoImage(file="Ressource/bouton/chap4/conversionImage.png")
    triangleImage=PhotoImage(file="Ressource/bouton/chap5/triangleImage.png")
    derivationImage=PhotoImage(file="Ressource/bouton/chap6/derivationImage.png")
    carreAireImage=PhotoImage(file="Ressource/bouton/chap1/carreAireImage.png")
    carrePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/carrePerimetreImage.png")
    cercleAireImage=PhotoImage(file="Ressource/bouton/chap1/cercleAireImage.png")
    cerclePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/cerclePerimetreImage.png")
    coneImage=PhotoImage(file="Ressource/bouton/chap1/coneImage.png")
    cubeImage=PhotoImage(file="Ressource/bouton/chap1/cubeImage.png")
    cylindreImage=PhotoImage(file="Ressource/bouton/chap1/cylindreImage.png")
    losangeImage=PhotoImage(file="Ressource/bouton/chap1/losangeImage.png")
    parallelogrammeImage=PhotoImage(file="Ressource/bouton/chap1/parallelogrammeImage.png")
    paveImage=PhotoImage(file="Ressource/bouton/chap1/paveImage.png")
    pyramideImage=PhotoImage(file="Ressource/bouton/chap1/pyramideImage.png")
    rectangleAireImage=PhotoImage(file="Ressource/bouton/chap1/rectangleAireImage.png")
    rectanglePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/rectanglePerimetreImage.png")
    sphereImage=PhotoImage(file="Ressource/bouton/chap1/sphereImage.png")
    trapezeImage=PhotoImage(file="Ressource/bouton/chap1/trapezeImage.png")
    triangleAireImage=PhotoImage(file="Ressource/bouton/chap1/triangleAireImage.png")

if infoTheme == ['ULTRACONTRASTBLUETHEME']:
    geometrieImage=PhotoImage(file="Ressource/bouton/chap1/geometrieImage.png")
    probaImage=PhotoImage(file="Ressource/bouton/chap2/probaImage.png")
    nombreImage=PhotoImage(file="Ressource/bouton/chap3/nombreImage.png")
    conversionImage=PhotoImage(file="Ressource/bouton/chap4/conversionImage.png")
    triangleImage=PhotoImage(file="Ressource/bouton/chap5/triangleImage.png")
    derivationImage=PhotoImage(file="Ressource/bouton/chap6/derivationImage.png")
    carreAireImage=PhotoImage(file="Ressource/bouton/chap1/carreAireImage.png")
    carrePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/carrePerimetreImage.png")
    cercleAireImage=PhotoImage(file="Ressource/bouton/chap1/cercleAireImage.png")
    cerclePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/cerclePerimetreImage.png")
    coneImage=PhotoImage(file="Ressource/bouton/chap1/coneImage.png")
    cubeImage=PhotoImage(file="Ressource/bouton/chap1/cubeImage.png")
    cylindreImage=PhotoImage(file="Ressource/bouton/chap1/cylindreImage.png")
    losangeImage=PhotoImage(file="Ressource/bouton/chap1/losangeImage.png")
    parallelogrammeImage=PhotoImage(file="Ressource/bouton/chap1/parallelogrammeImage.png")
    paveImage=PhotoImage(file="Ressource/bouton/chap1/paveImage.png")
    pyramideImage=PhotoImage(file="Ressource/bouton/chap1/pyramideImage.png")
    rectangleAireImage=PhotoImage(file="Ressource/bouton/chap1/rectangleAireImage.png")
    rectanglePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/rectanglePerimetreImage.png")
    sphereImage=PhotoImage(file="Ressource/bouton/chap1/sphereImage.png")
    trapezeImage=PhotoImage(file="Ressource/bouton/chap1/trapezeImage.png")
    triangleAireImage=PhotoImage(file="Ressource/bouton/chap1/triangleAireImage.png")

if infoTheme == ['ULTRACONTRASTPINKTHEME']:
    geometrieImage=PhotoImage(file="Ressource/bouton/chap1/geometrieImage.png")
    probaImage=PhotoImage(file="Ressource/bouton/chap2/probaImage.png")
    nombreImage=PhotoImage(file="Ressource/bouton/chap3/nombreImage.png")
    conversionImage=PhotoImage(file="Ressource/bouton/chap4/conversionImage.png")
    triangleImage=PhotoImage(file="Ressource/bouton/chap5/triangleImage.png")
    derivationImage=PhotoImage(file="Ressource/bouton/chap6/derivationImage.png")
    carreAireImage=PhotoImage(file="Ressource/bouton/chap1/carreAireImage.png")
    carrePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/carrePerimetreImage.png")
    cercleAireImage=PhotoImage(file="Ressource/bouton/chap1/cercleAireImage.png")
    cerclePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/cerclePerimetreImage.png")
    coneImage=PhotoImage(file="Ressource/bouton/chap1/coneImage.png")
    cubeImage=PhotoImage(file="Ressource/bouton/chap1/cubeImage.png")
    cylindreImage=PhotoImage(file="Ressource/bouton/chap1/cylindreImage.png")
    losangeImage=PhotoImage(file="Ressource/bouton/chap1/losangeImage.png")
    parallelogrammeImage=PhotoImage(file="Ressource/bouton/chap1/parallelogrammeImage.png")
    paveImage=PhotoImage(file="Ressource/bouton/chap1/paveImage.png")
    pyramideImage=PhotoImage(file="Ressource/bouton/chap1/pyramideImage.png")
    rectangleAireImage=PhotoImage(file="Ressource/bouton/chap1/rectangleAireImage.png")
    rectanglePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/rectanglePerimetreImage.png")
    sphereImage=PhotoImage(file="Ressource/bouton/chap1/sphereImage.png")
    trapezeImage=PhotoImage(file="Ressource/bouton/chap1/trapezeImage.png")
    triangleAireImage=PhotoImage(file="Ressource/bouton/chap1/triangleAireImage.png")

if infoTheme == ['PRINCESSTHEME']:
    geometrieImage=PhotoImage(file="Ressource/bouton/chap1/geometrieImage.png")
    probaImage=PhotoImage(file="Ressource/bouton/chap2/probaImage.png")
    nombreImage=PhotoImage(file="Ressource/bouton/chap3/nombreImage.png")
    conversionImage=PhotoImage(file="Ressource/bouton/chap4/conversionImage.png")
    triangleImage=PhotoImage(file="Ressource/bouton/chap5/triangleImage.png")
    derivationImage=PhotoImage(file="Ressource/bouton/chap6/derivationImage.png")
    carreAireImage=PhotoImage(file="Ressource/bouton/chap1/carreAireImage.png")
    carrePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/carrePerimetreImage.png")
    cercleAireImage=PhotoImage(file="Ressource/bouton/chap1/cercleAireImage.png")
    cerclePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/cerclePerimetreImage.png")
    coneImage=PhotoImage(file="Ressource/bouton/chap1/coneImage.png")
    cubeImage=PhotoImage(file="Ressource/bouton/chap1/cubeImage.png")
    cylindreImage=PhotoImage(file="Ressource/bouton/chap1/cylindreImage.png")
    losangeImage=PhotoImage(file="Ressource/bouton/chap1/losangeImage.png")
    parallelogrammeImage=PhotoImage(file="Ressource/bouton/chap1/parallelogrammeImage.png")
    paveImage=PhotoImage(file="Ressource/bouton/chap1/paveImage.png")
    pyramideImage=PhotoImage(file="Ressource/bouton/chap1/pyramideImage.png")
    rectangleAireImage=PhotoImage(file="Ressource/bouton/chap1/rectangleAireImage.png")
    rectanglePerimetreImage=PhotoImage(file="Ressource/bouton/chap1/rectanglePerimetreImage.png")
    sphereImage=PhotoImage(file="Ressource/bouton/chap1/sphereImage.png")
    trapezeImage=PhotoImage(file="Ressource/bouton/chap1/trapezeImage.png")
    triangleAireImage=PhotoImage(file="Ressource/bouton/chap1/triangleAireImage.png")



principal()

fenetrePrincipal.mainloop()