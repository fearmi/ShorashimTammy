#!/usr/bin/env python
 
import os
from time import sleep
import pygame
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(26, GPIO.IN)
pygame.mixer.init()

while True:
    if (GPIO.input(23) == True):
        print ("23")
        pygame.mixer.music.load("Prueba.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            if (GPIO.input(26) == True):
                pygame.mixer.music.stop()
            continue

    if (GPIO.input(24) == True):
        print ("24")
        pygame.mixer.music.load("Prueba2.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            if (GPIO.input(26) == True):
                pygame.mixer.music.stop()
            continue

        
      
 
    if (GPIO.input(25)== True):
        print ("25")
        pygame.mixer.music.load("Prueba3.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            if (GPIO.input(26) == True):
                pygame.mixer.music.stop()
            continue
 
   
