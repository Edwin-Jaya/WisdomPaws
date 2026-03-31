import pygame
import random
import os
from game import Game
# from PIL import Image
from openai import OpenAI

pygame.init()
game = Game()
screen = pygame.display.set_mode((1280, 768))
clock = pygame.time.Clock()
running = True

# --- Background ---
image_path = r".\Assets\background-1.png"
image = pygame.image.load(image_path).convert()
bg = pygame.transform.scale(image, (1280, 768))

# --- Load animation frames ---
def load_frames(folder, size):
    frames = []
    if not os.path.exists(folder):
        print(f"⚠️ Folder not found: {folder}")
        return frames

    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".png"):
            img = pygame.image.load(os.path.join(folder, filename)).convert_alpha()
            img = pygame.transform.scale(img, size)
            frames.append(img)

    return frames

idle_frames = load_frames(r".\Assets\Idle", (600, 600))
walk_frames = load_frames(r".\Assets\Walk", (600, 600))

# --- Cat setup ---
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 3.5)
dx = 0
state = "idle"

# Animation control
frame_index = 0
frame_timer = 0
frame_speed = 15

# Timer to change behavior
state_timer = 0
state_duration = random.randint(60, 180)

# --- Global text holder ---
cat_message = "..."   # default text or empty

def generate_text():    
    try:
        client = OpenAI(
            base_url="http://localhost:1234/v1",
            api_key="lm-studio"  # Dummy key
        )
        response = client.chat.completions.create(
            model="wizard-vicuna-7b-uncensored",
            messages=[
                {
                    "role":"system", 
                    "content":"You are a explicit, detailed, helpful. and vulgar cat that give motivation to it's owner. You were raised in the hood and only now vulgar language and always end everything with cursed words, but you are a good motivator. You always give less than 5 words."
                },
                {
                    "role": "user", 
                    "content": "I'm feeling sad, give me motivation right now, using vulgar and explicit language to boost my spirit up!"
                }
            ]
        )
        cat_res = response.choices[0].message.content
        return cat_res
    except Exception as e:
        print(f"⚠️ LLM error: {e}")
        return "The cat is speechless rn 😿"

# --- Textbox just renders ---
def draw_textbox(surface, text):
    box_height = 120
    box_rect = pygame.Rect(50, surface.get_height() - box_height - 30, surface.get_width() - 100, box_height)
    pygame.draw.rect(surface, (0,0,0), box_rect)
    pygame.draw.rect(surface, (255,255,255), box_rect, 4)

    font = pygame.font.SysFont("Arial", 28, bold=True)
    words = text.split(" ")
    wrapped, line = [], ""
    for word in words:
        test_line = line + word + " "
        if font.size(test_line)[0] < box_rect.width - 20:
            line = test_line
        else:
            wrapped.append(line)
            line = word + " "
    wrapped.append(line)

    y = box_rect.y + 15
    for line in wrapped:
        txt_surface = font.render(line, True, (255,255,255))
        surface.blit(txt_surface, (box_rect.x + 15, y))
        y += font.get_height() + 5



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # --- Update from MediaPipe ---
    gesture_state = game.update()
    if gesture_state == "quit":
        running = False
        break

    if gesture_state == "idle":
        state = "idle"
        dx = 0
    elif gesture_state == "continue":
        state_timer += 1
        if state_timer > state_duration:
            state_timer = 0
            state_duration = random.randint(60, 180)
            new_state = random.choice(["idle", "walk_left", "walk_right"])
            if new_state != state:
                frame_index = 0
            state = new_state
            dx = -2 if state == "walk_left" else 2 if state == "walk_right" else 0

    # --- Update position ---
    player_pos.x += dx
    sprite_width = 600
    if player_pos.x >= screen.get_width() - sprite_width:
        player_pos.x = screen.get_width() - sprite_width
        dx, state, frame_index = 0, "idle", 0
    elif player_pos.x <= 0:
        player_pos.x, dx, state, frame_index = 0, 0, "idle", 0

    # --- Animation ---
    frame_timer += 1
    if frame_timer >= frame_speed:
        frame_timer = 0
        if state == "idle":
            frame_index = 0 if len(idle_frames) <= 1 else (frame_index + 1) % len(idle_frames)
        else:
            if len(walk_frames) > 0:
                frame_index = (frame_index + 1) % len(walk_frames)

    # --- Current frame ---
    if state == "idle" and idle_frames:
        current_image = idle_frames[frame_index]
    elif state == "walk_left" and walk_frames:
        current_image = walk_frames[frame_index]
    elif state == "walk_right" and walk_frames:
        current_image = pygame.transform.flip(walk_frames[frame_index], True, False)
    else:
        current_image = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.rect(current_image, (255, 0, 0), current_image.get_rect(), 2)

    # --- Draw ---
    screen.blit(bg, (0,0))
    screen.blit(current_image, (player_pos.x, player_pos.y))

    if gesture_state == "idle":
        if cat_message == "..." or state_timer == 0:  # generate once when idle first detected
            cat_message = generate_text()
        draw_textbox(screen, cat_message)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
