#!/usr/bin/python3.5
# -*-coding:utf-8 -

"""Program "Help MacGyver to escape!"""

from constant import*

#Open game window
pygame.display.set_icon(ICONE)
pygame.display.set_caption(TITLE_WINDOW)



while MAIN_LOOP:
	#Load home screen
	WINDOW.blit(HOME,(0,0))
	#Reload display
	pygame.display.flip()
	#loop delay
	pygame.time.Clock().tick(30)
	for event in pygame.event.get():
		#Quit main loop
		if event.type == QUIT:
			print("Bye bye!")
			MAIN_LOOP = False




