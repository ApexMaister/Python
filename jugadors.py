#coding: utf-8
sortir = False
jugador1=raw_input("Player 1     Introduce pi,pa o ti para jugar o S para Salir")
jugador2=raw_input("Player 2     Introduce pi,pa o ti para jugar o S para Salir")

if jugador1 == jugador2:
	
	print "Empate"
	
	

if jugador1  == "pi" and jugador2 == "pa":
	print "Player 2 wins"
	
if jugador1 == "pa" and jugador2 == "ti":
	print "Player 2 wins"
	
if jugador1 == "ti" and jugador2 == "pi":
	print "Player 2 wins"
	
	


if jugador1 == "pa" and jugador2 == "pi":
	print "Player 1 wins"
	
if jugador1 == "ti" and jugador2 == "pa"
	print "Player 1 wins"
	
if jugador1 == "pi" and jugador2 == "ti"
	print "Player 1 wins"
	
	
	
if jugador1 == "s" or jugador1 == "S"
	sortir = True
