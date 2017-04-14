"""
Copyright (C) 2016  Sota Kaneko

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

#coding: utf-8
from random import randint
from sys import exit
from time import sleep

"""

			*******  Project Palabras v.0.0.1.2   *******

***Change Log***
-v0.0.1.0
	First step done, playable needs further testing and debuging
-v0.0.1.1
	Debugged first step
	No longer need to capitalize input
	Enabled number input
-v0.0.1.2
	Building stage 2
	Added number input guide
	Trying to use functions
	Added items
	Items parcially alter conditions

		***TODO***
Cleaner spaces
Clean code
Cheazt codes ;)
Item IDs:
Rusty knife  -- 1
Shovel -- 2
Knife -- 3
Shoes -- 4
Sketchy ID -- 5
Street gang ID -- 6
Dark web ID -- 7
Clear web ID --8
Debit card -- 9

"""
#player HP
php = 25
#Item check
items = ["Rusty knife(1)"]
rknife = 1
shovel = 0
knife = 0
shoes = 0
skid = 0
stid = 0
dkid = 0
clid = 0
debit = 0
#Finance
money = 200
bank = 0


#First sequence
print "Welcome to Project Palabras"
print "In this game, you will be specified what you can do."
print "Do you understand?"
print 'Type in "Yes"(1)'
while True:
	conf = raw_input('\n\n>>> ').lower()
	if conf == "yes" or conf == "1":
		break
print "This game runs on the world's fastest graphics processor, the human brain."
print "Imagine away!"


#Buy fake ID
def stage2(ID):
	mon(dep = 0 , withd = 0 , chk = 0 , ty = 1)
	print "Now you can choose where to buy your " + ID
	print 'Choices are: 1. A sketchy person with a shirt printed "I make ID" ; Price: 200'
	print "2. A street gang ; Price: 100"
	print "3. Dark web ; Price: 400"
	print "4. Clearnet ; Price: 300"
	print "5. Give up ; Price: Life"


#Buy general items
def itembuy(ss , sk , ssh , sid):   #show shovel, show knife , show shoes , show id
	global rknife ; global shovel ; global knife ; global shoes
	if ss == 1 or sk == 1 or ssh == 1 and sid == 0:
		while True:
			mon(dep = 0 , withd = 0 , chk = 80 , ty = 2)
			if chkt == 0:
				break
			mon(dep = 0 , withd = 0 , chk = 0 , ty = 1)
			print "You can buy:"
			if shovel == 0 and ss == 1:
				print "A shovel(1) 80 pesos"
			if knife == 0 and sk == 1:
				print "A knife(2) 100 pesos"
			if shoes == 0 and ssh == 1:
				print "A pair of shoes(3) 90 pesos"
			print "Or exit(4)"
			while True:
				itm = raw_input("\n\n>>>   ").lower()
				if itm == "shovel" or itm == "1" and shovel == 0:
					mon(dep = 0 , withd = 0 , chk = 80 , ty = "buy") #Balance check for 80 pesos, type:buy
					if chkt == 1:
						shovel = 1
						print "You bought a shovel!"
						items.append("Shovel(2)")
						mon(dep = 0 , withd = 80 , chk = 0 , ty = 0) #Withdraw 80 pesos
						break
					else:
						break
				elif itm == "knife" or itm == "2" and knife == 0:
					mon(dep = 0 , withd = 0 , chk = 100 , ty = "buy") #Balance check for 100 pesos, type:buy
					if chkt == 1:
						knife = 1
						print "You bought a knife!"
						items.append("Knife(3)")
						mon(dep = 0 , withd = 100 , chk = 0 , ty = 0) #Withdraw 100 pesos
						break
					else:
						break
				elif itm == "shoes" or itm == "3" and shoes == 0:
					mon(dep = 0 , withd = 0 , chk = 90 , ty = "buy") #Balance check for 90 pesos, type:buy
					if chkt == 1:
						shoes = 1
						print "You bought a pair of shoes!"
						items.append("Shoes(4)")
						mon(dep = 0 , withd = 90 , chk = 0 , ty = 0) #Withdraw 90 pesos
						break
					else:
						break
				elif itm == "exit" or itm == "4":
					exit = 1
					return
	elif sid == 1 or sid == 2:
		global skid ; global stid ; global dkid ; global clid
		if sid == 1:
			stage2(ID = "passport")
			i = "passport"
		elif sid == 2:
			stage2(ID = "green card")
			i = "green card"
		while True:
			st2 = raw_input("\n\n>>>   ")
			suc = randint(1,2)
			if st2 == "the sketchy person" or st2 == "1":    #Price  200   Adequate quality 50% Chance
				mon(dep = 0 , withd = 0 , chk = 200 , ty = "obtain")
				if suc == 1 and chkt == 1:
					print "He didn't like the way you looked at him and killed you"
					print "Game over"
					exit()
				elif suc == 2 and chkt == 1:
					print "You got a fair quality %s!" % (i)
					mon(dep = 0 , withd = 200 , chk = 0, ty = 0)
					skid = 1
					if sid == 1:
						items.append("Counterfeit Passport(5)")
					elif sid == 2:
						items.append("Counterfeit Green card(5)")
					print "On to the next step!"
					return
			elif st2 == "street gang" or st2 == "2":   #Price 100 Poor quality 10% Chance
				mon(dep = 0 , withd = 0 , chk = 100 , ty = "obtain")
				if suc == 1 and chkt == 1:
					mon(dep = 0 , withd = 100 , chk = 0 , ty = 0)
					print "You were scammed!"
					print "You can still go to other places"
				elif  suc == 2 and chkt == 1:
					print "You got a poor quality %s" % (i)
					mon(dep = 0 , withd = 100 , chk = 0 , ty = 0)
					if sid == 1:
						items.append("Counterfeit Passport(6)")
					elif sid == 2:
						items.append("Couterfeit Green card(6)")
					return
			elif st2 == "dark web" or st2 == "3":  #Price 400   Top quality 85% Chance
				mon(dep = 0 , withd = 0 , chk = 400 , ty = "obtain")
				if chkt == 1:
					mon(dep = 0 , withd = 400 , chk = 0 , ty = 0)
					dkid = 1
					print "You got a high quality %s" % (i)
					if sid == 1:
						items.append("Counterfeit Passport(7)")
					elif sid == 2:
						items.append("Counterfeit Green card(7)")
					return
			elif st2 == "clear net" or st2 == "4":   #Price 300   Normal quality 65% Chance
				mon(dep = 0 , withd = 0 , chk = 300 , ty = "obtain")
				if chkt == 1:
					if suc == 1:
						print "Knock knock?"
						print "Who's there?"
						print "FBI."
						print "FBI who?"
						print "Shut up you're under arrest"
						print "Game over!"
						exit()
					elif suc == 2:
						mon(dep = 0 , withd = 300 , chk = 0 , ty = 0)
						clid = 1
						print "You got your %s!" % (i)
						if sid == 1:
							items.append("Counterfeit Passport(8)")
						if sid == 2:
							items.append("Counterfeit Green card(8)")
						return
			elif st2 == "give up!" or st2 == "5": #Price life    Poor quality
				print "You gave up!"
				print "Game over"
				exit()


#Money services; Types ty1 = balance check, ty2 = buy
def mon(dep , withd , chk , ty):
	global chkt ; global money ; global bank ; global debit
	mon = money + bank
	money = money + dep
	money = money - withd
	if money < 0:
		bank = money + bank
	if dep > 0:
		print "You %s %d pesos!" % (ty , dep)

	if ty == 1 and debit == 0:
		print "You have %d Pesos in your possesion!" % (money)
	elif ty == 1 and debit == 1:
		print "You have %d pesos in your possesion and have %d pesos in your bank account!" % (money , bank)

	if mon >= chk:
		chkt = 1
	elif mon < chk and ty == 2:
		print "You don't have enough money to buy anything anymore!"
		chkt = 0
	elif mon < chk:
		chkt = 0
		print "You don't have enough money to %s that!" % (ty)

def bank(dep):
	pass
	global bank ; global money
	if dep > 0:
		money = money + dep
		bank = bank + dep


print "But first, you will have to prepare your self for the journey ahead"
print "As a gift, I will give you a Rusty knife!"
itembuy(ss = 1 , sk = 1 , ssh = 1 , sid = 0)


#Combat sequence
def combat(hp , mob):
	global php ; global items
	while True:
		nope = "You don't have that!"
		atkp = 0
		print "The %s has %d HP left" % (mob , hp)
		print "You have the following items: "
		print items
		cch = raw_input(">>>  ").lower()
		if cch == "rusty knife" or cch == "1" and rknife == 1:
			atkp = randint(1,6)
			print "You gave the %s %d damage!" % (mob , atkp)
		elif cch == "shovel" or cch == "2" and shovel == 1:
			atkp = randint(5,10)
			print "You gave the %s %d damage!" % (mob , atkp)
		elif cch == "knife" or cch == "3" and knife == 1:
			aktp = randint(9,18)
			print "You gave the %s %d damage!" % (mob , atkp)
		elif cch == "shoes" or cch == "4" and shoes == 1:
			if shoes == 1:
				aktp = randint(1,2)
				print "You gave the %s %d damage!" % (mob , atkp)
			elif shoes == 0:
				print nope
		else:
			print nope
		hp = hp - atkp
		if hp <= 0:
			print "You beat the %s!" % (mob)
			break
		else:
			print "\n\nThe %s's attack!" % (mob)
			if mob == "officer":
				mobatk = randint(1,9)
			elif mob == "bank guard":
				a = randint(1,2)
				if a == 1:
					mobatk == 25
				if a == 2:
					mobatk == 20
			php = php - mobatk
			print "The %s gave you %d damage!" % (mob , mobatk)
			if php <= 0:
				print "You lost!"
				print "Game over!"
				exit()
			else:
				print "You have %d HP left" % (php)


#Chances of fake ID eligable
def cha():
	global cha
	cha = 0
	if skid == 1:
		cha = randint(1,2)
		if cha == 2:
			cha = 0
	elif stid == 1:
		cha = randint(1,10)
		if cha == 4:
			cha = 1
		else:
			cha = 0
	elif  dkid == 1:
		cha = randint(1,20)
		if cha == 5 or cha == 14 or cha == 19:
			cha = 0:
		else:
			cha = 1
	elif clid == 1:
		cha = randint(1,20)
		if cha == 3 or cha == 6 or cha == 8 or cha == 11 or cha == 15 or cha == 17 or cha == 19:
			cha == 0
		else:
			cha == 1


"""
Entering the country
"""

#Directions; Step 1
while True:
	print "Which direction do you desire to go?"
	print "Front(1), Right(2), or Left(3) "
	a = raw_input("\n\n>>> ").lower()
	if a == "front" or a == "1":
		stage = 1
		break
	elif a == "right" or a == "2":
		stage = 2
		break
	elif a == "left" or a == "3":
		stage = 3
		break
	else:
		print "I don't know what %d means!" % (a)
		print "Please try again!"



#First Step, Front or 1
cle11 = 0
if stage == 1:
	s1ch = 0
	while True:
		if cle11 == 1:
			print "On to the next step!"
			break
		else:
			print "You encountered a great big wall, built by Donald Trump."
			print "What will you do?"
			print "Break the wall like an illegal immigrant Trump hates(1),or dig a tunnel like El Chapo(2). "
			stage1 = raw_input("\n\n>>> ").lower()
			if stage1 == "break the wall" or stage1 == "1":
				while True:
					if cle11 == 1:
						break
					else:
						print "A angry border patrol officer has found you!"
						print "Would you like to Fight(1) or Run(2)?"
						s1ch = raw_input("\n\n>>> ").lower()
						cl11 = 0
						if s1ch == "fight" or s1ch == "1": #Survival rate 99%
							cle11 = 0
							combat(hp = 20 , mob = "officer")
							mon(dep = 100 , withd = 0 , chk = 0 , ty = "took")
							cle11 = 1
						elif s1ch == "run" or s1ch == "2" and shoes == 1: #Survival rate 75%
							runch = randint(1,4)
							if runch == 2:
								print "You have failed to outrun the officer!"
								print "The office used his baton to beat you to death."
								print "Game over"
								exit()
							elif runch == 1 or runch == 3 or runch == 4:
								print "You have outruned the officer!"
								cle11 = 1
								break
			elif stage1 == "dig a tunnel" or stage1 == "2": #Survival rate 50%
				tuou = randint(1,2)
				if tuou == 1:
					tuou2 = randint(1,2)
					if tuou2 == 1:
						print "You dug a tunnel, however it collapsed over you and suffocated you to death."
						print "Game over"
						exit()
					elif tuou2 == 2:
						print "You successfully dug a tunnel, however an officer was stainding in front of the tunnel exit"
						print "You were deported"
						print "Game over"
						exit()
				elif tuou == 2:
					tuou3 = randint(1,2)
					if tuou3 == 1:
						print "You succeeded!"
						print "You kept your head down and worked until the day you died from a heart attack"
						exit()
					elif tuou3 == 2:
						print "You succeeded but need to keep going"
						mon(dep = 280 , withd = 0 , chk = 0 , ty = "dug up")
						print "On to the next stage!"
						cle11 = 1
						break



#First step, Right or 2
elif stage == 2:
	cle12 = 0
	print 'A police officer wants to "Ask questions"'
	print "What do you want to do?"
	print "Run(1) or cooporate(2)"
	while True:
		s12ch = raw_input("\n\n>>> ").lower()
		if s12ch == "run" or s12ch == "1":   #Survial rate 50%
			if shoes == 1:
				runspeed == randint(1,3)
			else:
				runspeed =  randint(1,2)

			if runspeed == 1 or runspeed == 3:
				print "You have succesfully outrunned the police officer!"
				mon(dep = 180 , withd = 0 , chk = 0 , ty = "found")
				cle12 = 1
				break
			elif runspeed == 2:
				runsuc = randint(1,2)
				print "You tripped, but you can still run."
				print "You can either Run(1) or Cooporate(2) now."
				s12c = raw_input("\n\n>>> ").lower()
				if s12c == "run" or s12c == "1" and runsuc == 1:   #Survival rate 50%
					print "You have successfully outrunned the officer"
					cle12 == 1
					break
				elif s12c == "run" or s12c == "1" and runsuc == 2:
					print "It seems you have broken your leg, and cannot run anymore."
					print "The officer used you for shooting practice!"
					print "Game over"
					exit()
				elif s12c == "cooporate" or s12c == "2" and runsuc == 1:
					print "You were found by an friendly officer."
					print "He sponsored you a way into the U.S."
					print "You later became successful, bought a nice car, got a loving wife, and purchased a house and lived happily ever after"
					exit()
				elif s12c == "cooporate" or s12c == "2" and runsuc == 2:
					print 'The officer shot you in "Defense" and was declared a "Clean shooting"'
					print "Of course you died"
					print "Game over"
					exit()
		elif s12ch == "cooporate" or s12ch == "2":
			coop = randint(1,2)
			if coop == 1:
				print "You were deported"
				print "Game over"
				exit()
			elif coop == 2:
				print "You were found by an friendly officer."
				print "He sponsored you a way into the U.S."
				print "You later became successful, bought a nice car, got a loving wife, and purchased a house and lived happily ever after"
				exit()



#First step, Left or 3
elif stage == 3:
	print 'You have boarded a freight train known as "La Bestia", translated: The Beast'
	print "It is entirely up to fate now."
	print "This is your last chance if you want to bail."
	print "Do you want to bail?"
	print "Yes(1) or No(2)"
	while True:
		lachoice = raw_input("\n\n>>> ").lower()
		if lachoice == "yes" or lachoice == "1":
			print "You bailed."
			print "Game over"
			exit()
		elif lachoice == "no" or lachoice == "2":
			labestia = randint(1,3)
			if labestia == 1:
				print "You hanged on the roof of the containers, and successfully made it into the U.S.!"
				print "You published a book about your journey after legally obtaining citizenship by marrying your beloved wife, Rose"
				exit()
			elif labestia == 2:   #Survival rate 33%
				print "You made it into the U.S. but still need to move on"
				mon(dep = 300 , withd = 0 , chk = 0 , ty = "found")
				break
			elif labestia == 3:
				print "You were pushed off the container by a fellow immigrant"
				print "Instant death"
				exit()


"""
Second Step
Obtaining an ID
"""


print "Congrats!"
print "You made it to the States!"
print "But now to make a living here, you'll need an ID..."
print "Now, you can either get a fake passport or green card"
print "Which would you like to obtain?"
print "Passport(1) or Green card(2)"
sta2 = raw_input("\n\n>>> ").lower()

if sta2 == "passport" or sta2 == "1":
	itembuy(ss = 0 , sk = 0 , ssh = 0, sid = 1)
	print "Now that you got your passport, you'll have to know it'll work anywhere."
	print 'You: "I want to open a bank account"'
	print 'Bank clerk:  "May I see an ID?"'
	print 'You: "OK."'
	print "\n Now hand out your passport."
	print items
	while True:
		st = raw_input(">>>  ").lower()
		if st == "rusty knife" or st == "1" or st == "knife" or st == "3" or st == "shovel" or st == "2" and rknife == 1 or knife == 1 or shovel == 1:
			print 'Bank clerk "AAAAAAAHHHHHHH IT\'S A ROBBERY!!!"'
			print '"SHOOT THIS MAN!!!"'
			combat(hp = 20 , mob = "bank guard")
			mon(dep = 1000 , withd = 0 , chk = 0 , ty = "stole")
		elif st == "shoes" or st == "4":
			print 'Bank clerk "Sir? Are you on drugs?"'
			print '"Please leave"'
			sh = raw_input("Do you want to fight the bank guard?\nYes(1) or No(2)\n>>>   ".lower()
			if sh == "yes" or sh == "y" or sh == "1":
				combat(hp = 20 , mob "bank guard")
				print "Now the police has arrived!"
				print "FIGHT THEM!"
				combat(hp = 50 , mob "police officer")
				print "Great you survived!"
				mon(dep = 1500 , withd = 0 , chk = 0 , ty = "stole")
			elif sh == "no" or sh == "n" or sh == "2":
				print "You surrendered"
				print "Game over"
				exit()
		elif st == "counterfiet passport" or st == "5" or st == "6" or st == "7" or st == "8" and skid == 1 or stid == 1 or dkid == 1 or clid == 1:
			cha()
			if cha == 1:
				print "You got a bank account!"
				print "How much money do you want to deposit into your account?"
				mon(dep = 0 , withd = 0 , chk = 0 , ty = 1)
				depo = input(">>>   ")
				mon(dep = 0 , withd = 0 , chk = depo , ty = 0)
				if chkt == 1:
					bank(dep = depo):

				items.append("Debit card (9)")
				debit = 1
			elif cha == 0:
				print 'Bank clerk "I\'m sorry but this is fake, I\'m calling the cops!"'
				print "Game over"
				exit()





elif sta2 == "green card" or sta2 == "2":
	itembuy(ss = 0 , sk = 0 , ssh = 0 , sid = 2)




print "ok"
print "item check"
print items
