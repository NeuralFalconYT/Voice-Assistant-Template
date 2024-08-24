#making a realtime wave sign from audio input
#Code copied from https://youtu.be/675teI6-_-g?si=Oi-MhJ1-M-MohQ0n
#@Anding Analytics on Youtube
import pyaudio
import pygame
import math
#pygame initialization
screen_width = 500
screen_height = 500
pygame.init()
pygame.display.set_caption("Realtime Wave Sign")
screen=pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

#pyaudio initialization
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
p=pyaudio.PyAudio()
stream=p.open(format=FORMAT,channels=CHANNELS,
              rate=RATE,input=True,
              frames_per_buffer=CHUNK)

def get_microphone_input_level():
    data = stream.read(CHUNK)
    rms=0
    for i in range(0,len(data),2):
        sample=int.from_bytes(data[i:i+2], byteorder='little', signed=True)
        rms= rms + sample**2
    rms = math.sqrt(rms / CHUNK)
    return rms

def hex_to_rgb(hex_code):
    # Remove the '#' symbol if present
    hex_code = hex_code.strip('#')
    # Convert the hex string to a list of integer values
    hex_list = [int(hex_code[i:i+2], 16) for i in (0, 2, 4)]
    # Convert the list of values to an RGB tuple
    rgb_tuple = tuple(hex_list)
    return rgb_tuple


def draw_sine_wave(amplitude):
    screen.fill((0,0,0))
    points=[]
    if amplitude>10:
        for x in range(0, screen_width):
            y = screen_height/2 + int(amplitude*math.sin(x*0.02))
            points.append((x,y))
    else:
        points.append((0,screen_height/2))
        points.append((screen_width,screen_height/2))
    hex_code = '#5ce65c'
    color = hex_to_rgb(hex_code)
    pygame.draw.lines(screen, color, False, points, 2)
    pygame.display.flip()
    
running=True
amplitude=100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    amplitude_adjustment = get_microphone_input_level()/50
    amplitude = max(10, amplitude_adjustment)
    draw_sine_wave(amplitude)
    clock.tick(60)
pygame.quit()


