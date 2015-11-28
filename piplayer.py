import sys, pygame
from pygame.locals import *
import time, datetime
import subprocess
import os
import glob
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()


#define function that checks for mouse location
def on_click():
	click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
	#Rafraichissement de la page
	refresh_menu_screen()
	#check to see if exit has been pressed
	if 420 <= click_pos[0] <= 455 and 10 <= click_pos[1] <=50:
		print "You pressed exit" 
		button(0)
	#now check to see if play was pressed
	if 20 <= click_pos[0] <= 70 and 80 <= click_pos[1] <=130:
                print "You pressed button play"
                button(1)	
	#now check to see if stop  was pressed
        if 80 <= click_pos[0] <= 135 and 80 <= click_pos[1] <=130:
                print "You pressed button stop"
                button(2)
	#now check to see if refreshed  was pressed
        if 270 <= click_pos[0] <= 320 and 70 <= click_pos[1] <=120:
                print "You pressed button refresh"
                button(3)
	#now check to see if previous  was pressed
        if 10 <= click_pos[0] <= 60 and 280 <= click_pos[1] <=300:
                print "You pressed button previous"
                button(4)

	 #now check to see if next  was pressed
        if 80 <= click_pos[0] <= 120 and 280 <= click_pos[1] <=300:
                print "You pressed button next"
                button(5)

	 #now check to see if volume down was pressed
        if 170 <= click_pos[0] <= 200 and 280 <= click_pos[1] <=300:
                print "You pressed volume down"
                button(6)

	 #now check to see if button 7 was pressed
        if 240 <= click_pos[0] <= 280 and 280 <= click_pos[1] <=300:
                print "You pressed volume up"
                button(7)

	 #now check to see if button 8 was pressed
        if 420 <= click_pos[0] <= 460 and 280 <= click_pos[1] <=300:
                print "You pressed mute"
                button(8)

	 #now check to see if button 9 was pressed
        if 15 <= click_pos[0] <= 125 and 165 <= click_pos[1] <=200:
                print "You pressed button 9"
                button(9)


#define action on pressing buttons
def button(number):
	print "You pressed button ",number
	if number == 0:    #specific script when exiting
		screen.fill(black)
		font=pygame.font.Font(None,24)
        	label=font.render("Radioplayer will continue in background", 1, (white))
        	screen.blit(label,(80,160))
		pygame.display.flip()
		time.sleep(5)
		sys.exit()

	if number == 1:	
		subprocess.call("mpc play ", shell=True)
		refresh_menu_screen()

	if number == 2:
		subprocess.call("mpc stop ", shell=True)
		refresh_menu_screen()

	if number == 3:
		subprocess.call("mpc stop ", shell=True)
		subprocess.call("mpc play ", shell=True)
		refresh_menu_screen() 
		
	if number == 4:
		subprocess.call("mpc prev ", shell=True)
		refresh_menu_screen()

	if number == 5:
		subprocess.call("mpc next ", shell=True)
		refresh_menu_screen()

	if number == 6:
		subprocess.call("mpc volume -10 ", shell=True)
		refresh_menu_screen()

	if number == 7:
		subprocess.call("mpc volume +10 ", shell=True)
		refresh_menu_screen()

	if number == 8:
		subprocess.call("mpc volume 0 ", shell=True)
		refresh_menu_screen()	

def refresh_menu_screen():
#set up the fixed items on the menu
	screen.fill(black) #change the colours if needed
	font=pygame.font.Font(None,34)
	title_font=pygame.font.Font(None,38)
	playing_font=pygame.font.Font(None,48)
	station_font=pygame.font.Font(None,32)
	volume_font=pygame.font.Font(None,26)
	status_font=pygame.font.Font(None,26)
	label=title_font.render("PiPlayer HOME RADIO", 1, (white))
	label2=volume_font.render("Volume:", 1,(white))
	label3=status_font.render("Status:", 1,(white))
	screen.blit(label,(100, 25))
	screen.blit(label2,(185, 90))
	screen.blit(label3,(320, 90))
	play=pygame.image.load("play.png")
	pause=pygame.image.load("pause.png")
	refresh=pygame.image.load("refresh.tiff")
	previous=pygame.image.load("previous.png")
	next=pygame.image.load("next.png")
	vol_down=pygame.image.load("volume_down.png")
	vol_up=pygame.image.load("volume_up.png")
	mute=pygame.image.load("mute.png")
	exit=pygame.image.load("exit.png")
	radio=pygame.image.load("piplayer.png")
	# draw the main elements on the screen
	screen.blit(play,(15,85))	
	screen.blit(pause,(100,85))
	pygame.draw.rect(screen, white, (8, 75, 464, 170),1)
	pygame.draw.line(screen, white, (8,165),(470,165),1)
	pygame.draw.rect(screen, black, (10, 173, 460, 33),0)
	screen.blit(refresh,(270,70))
	screen.blit(previous,(10,250))
	screen.blit(next,(80,250))
        screen.blit(vol_down,(170,250))
	screen.blit(vol_up,(240,250))
	screen.blit(mute,(410,250))	
        screen.blit(exit,(408,8))
	screen.blit(radio,(10,8))
	pygame.draw.rect(screen, white, (0,0,480,320),3)
	##### display the station name and split it into 2 parts : 
	station = subprocess.check_output("mpc current", shell=True )
	lines=station.split(":")
	length = len(lines) 
	if length==1:
		line1 = lines[0]
		line1 = line1[:-1]
		line2 = "No additional info: "
	else:
		line1 = lines[0]
		line2 = lines[1]

	line2 = line2[:42]
	line2 = line2[:-1]
	#trap no station data
	if line1 =="":
		line2 = "Press PLAY or REFRESH"
		station_status = "stopped"
		status_font = red
	else:
		station_status = "Playing"
		status_font = green
	station_name=station_font.render(line1, 1, (white))
	additional_data=station_font.render(line2, 1, (white))
	station_label=playing_font.render(station_status, 1, (status_font))
	screen.blit(station_label,(255,115))
	screen.blit(station_name,(15,175))
	screen.blit(additional_data,(20,205))
	######## add volume number
	volume = subprocess.check_output("mpc volume", shell=True )
	volume = volume[8:]
	volume = volume[:-1]
	volume_tag=font.render(volume, 1, (white))
	screen.blit(volume_tag,(255,85))
	####### check to see if the Radio is connected to the internet
	IP = subprocess.check_output("hostname -I", shell=True )
	IP=IP[:3]
	if IP =="192":
		network_status = "Online"
		status_font = green

	else:
		network_status = "Offline"
		status_font = red

	network_status_label = font.render(network_status, 1, (status_font))
	screen.blit(network_status_label, (385,85))
	pygame.display.flip()
	
def main():
        while 1:
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                print "screen pressed" #for debugging purposes
                                pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                print pos #for checking
                                pygame.draw.circle(screen, white, pos, 2, 0) #for debugging purposes - adds a small dot where the screen is pressed
                                on_click()

#ensure there is always a safe way to end the program if the touch screen fails

                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        sys.exit()
        time.sleep(0.2)        
	pygame.display.update()
	

#################### EVERTHING HAS NOW BEEN DEFINED ###########################

#set size of the screen
size = width, height = 480, 320
screen = pygame.display.set_mode((480, 320))

#define colours
blue = 26, 0, 255
cream = 254, 255, 25
black = 0, 0, 0
white = 255, 255, 255
yellow = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
refresh_menu_screen()  #refresh the menu interface 
main() #check for key presses and start emergency exit
station_name()

