import pygame
import os
import importlib.util
from engine.py_game_engine import *

scripts = []


def add_scripts(dir="./scripts/"):
    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        if filename.endswith(".py"):
            script_name = filename[:-3]  # Remove the .py extension
            script_path = os.path.join(dir, filename)

            # Dynamically load the module
            spec = importlib.util.spec_from_file_location(script_name, script_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Append the loaded module to the scripts list
            scripts.append(module)


def start():
    global get_ticks_last_frame
    get_ticks_last_frame = 0.0

    for script in scripts:
        try:
            script.start()
        except AttributeError:
            print(f"Start function not found in script {script.__name__}")


def update() -> bool:
    global get_ticks_last_frame, delta_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False

    for script in scripts:
        try:
            script.update()
        except AttributeError:
            print(f"Update function not found in script {script.__name__}")

    pygame.display.flip()

    get_ticks_last_frame, delta_time = manage_frame_rate(clock, get_ticks_last_frame)

    return True


def run():
    global SCREEN, clock, delta_time, arial

    # PyGame Setup
    pygame.init()
    SCREEN = pygame.display.set_mode(RESOLUTION, pygame.FULLSCREEN if FULLSCREEN else 0)
    pygame.display.set_caption(game_name)
    # pygame.display.set_icon(pygame.image.load(ICON_LOCATION))  # Uncomment if an icon is present

    clock = pygame.time.Clock()
    delta_time = 0.0
    arial = pygame.font.SysFont("Arial", 32)

    running = True

    start()

    while running:
        running = update()
