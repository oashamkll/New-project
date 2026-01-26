#!/usr/bin/env python3
"""
Beautiful Animation Script for Termux
This script creates various animations in the terminal using ANSI escape codes.
"""

import time
import sys
import math
import random
from typing import List, Tuple


def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()


def set_cursor_position(x: int, y: int):
    """Set cursor position using ANSI escape codes."""
    sys.stdout.write(f'\033[{y};{x}H')
    sys.stdout.flush()


def set_color(r: int, g: int, b: int):
    """Set text color using RGB values."""
    sys.stdout.write(f'\033[38;2;{r};{g};{b}m')
    sys.stdout.flush()


def reset_color():
    """Reset text color to default."""
    sys.stdout.write('\033[0m')
    sys.stdout.flush()


def get_terminal_size() -> Tuple[int, int]:
    """Get the size of the terminal window."""
    try:
        import os
        rows, cols = os.popen('stty size', 'r').read().split()
        return int(cols), int(rows)
    except:
        # Default values if we can't get terminal size
        return 80, 24


def loading_bar_animation():
    """Create a loading bar animation."""
    print("Loading animation...")
    width, height = get_terminal_size()
    
    for i in range(51):  # 0 to 50
        percent = i * 2  # To get 0 to 100
        bar_length = min(int((width - 20) * i / 50), width - 20)
        
        # Create gradient effect
        r = min(255, int(255 * i / 50))
        g = min(255, int(255 * (50 - i) / 50))
        b = 100
        
        set_color(r, g, b)
        
        bar = '[' + '#' * bar_length + ' ' * (width - 20 - bar_length) + ']'
        sys.stdout.write(f'\r{bar} {percent}%')
        sys.stdout.flush()
        
        time.sleep(0.05)
    
    reset_color()
    print("\nLoading complete!\n")
    time.sleep(1)


def bouncing_balls_animation():
    """Create bouncing balls animation."""
    print("Bouncing balls animation...")
    time.sleep(1)
    
    width, height = get_terminal_size()
    width -= 2  # Leave some margin
    height -= 4
    
    # Initialize balls
    balls = []
    num_balls = min(5, (width // 4) * (height // 3))  # Don't overcrowd
    
    for _ in range(num_balls):
        ball = {
            'x': random.randint(1, width - 2),
            'y': random.randint(1, height - 2),
            'dx': random.choice([-1, 1]) * random.uniform(0.3, 0.7),
            'dy': random.choice([-1, 1]) * random.uniform(0.3, 0.7),
            'char': random.choice(['●', '○', '◉', '◎']),
            'color': (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        }
        balls.append(ball)
    
    for frame in range(100):  # Run for 100 frames
        clear_screen()
        print(f"Bouncing Balls Animation - Frame {frame + 1}/100")
        
        for ball in balls:
            # Update position
            ball['x'] += ball['dx']
            ball['y'] += ball['dy']
            
            # Bounce off walls
            if ball['x'] <= 0 or ball['x'] >= width - 1:
                ball['dx'] *= -1
                ball['x'] = max(0, min(width - 1, ball['x']))
                
            if ball['y'] <= 0 or ball['y'] >= height - 1:
                ball['dy'] *= -1
                ball['y'] = max(0, min(height - 1, ball['y']))
        
        # Draw balls
        for ball in balls:
            set_cursor_position(int(ball['x']) + 1, int(ball['y']) + 2)
            set_color(*ball['color'])
            print(ball['char'], end='', flush=True)
        
        time.sleep(0.05)
    
    reset_color()
    print("\nAnimation complete!\n")
    time.sleep(1)


def wave_animation():
    """Create a wave animation."""
    print("Wave animation...")
    time.sleep(1)
    
    width, height = get_terminal_size()
    width -= 2
    height -= 4
    
    for frame in range(100):
        clear_screen()
        print(f"Sine Wave Animation - Frame {frame + 1}/100")
        
        # Calculate wave points
        wave_points = []
        for x in range(width):
            y = int(height / 2 + (height / 4) * math.sin((x + frame) * 0.3))
            wave_points.append((x, y))
        
        # Draw the wave
        for x, y in wave_points:
            set_cursor_position(x + 1, y + 2)
            # Color varies based on wave position
            r = int(128 + 127 * math.sin(frame * 0.1))
            g = int(128 + 127 * math.cos(frame * 0.1))
            b = int(200 + 55 * math.sin(frame * 0.05))
            set_color(r, g, b)
            print('*', end='', flush=True)
        
        time.sleep(0.05)
    
    reset_color()
    print("\nAnimation complete!\n")
    time.sleep(1)


def matrix_rain_animation():
    """Create a Matrix-style rain animation."""
    print("Matrix rain animation...")
    time.sleep(1)
    
    width, height = get_terminal_size()
    width -= 2
    height -= 4
    
    # Initialize columns
    drops = [0] * width  # Track position of each drop
    
    for frame in range(100):
        clear_screen()
        print(f"Matrix Rain Animation - Frame {frame + 1}/100")
        
        for i in range(width):
            # Reset drop if it reaches bottom or randomly
            if drops[i] > height or random.random() > 0.975:
                drops[i] = 0
            
            # Get character - mostly katakana for authentic Matrix feel
            char = random.choice([
                chr(random.randint(0x30A0, 0x30FF)),  # Katakana
                chr(random.randint(0xFF10, 0xFF19)),  # Full-width digits
                chr(random.randint(0xFF21, 0xFF3A)),  # Full-width uppercase
                chr(random.randint(0xFF41, 0xFF5A)),  # Full-width lowercase
                str(random.randint(0, 9))  # Regular digits
            ])
            
            # Draw the character
            if drops[i] < height:
                set_cursor_position(i + 1, drops[i] + 2)
                
                # Head of the raindrop is brighter green
                if frame % len(drops[i:i+1]) == 0:  # For leading character
                    set_color(255, 255, 255)  # White for head
                else:
                    # Fade green intensity based on position in trail
                    intensity = max(50, 255 - (drops[i] * 3))
                    set_color(0, intensity, 0)  # Green
                
                print(char, end='', flush=True)
            
            # Move drop down
            drops[i] += 1
        
        time.sleep(0.05)
    
    reset_color()
    print("\nAnimation complete!\n")
    time.sleep(1)


def fireworks_animation():
    """Create a fireworks animation."""
    print("Fireworks animation...")
    time.sleep(1)
    
    width, height = get_terminal_size()
    width -= 2
    height -= 4
    
    for firework_num in range(10):
        # Choose a random position for the firework
        center_x = random.randint(5, width - 5)
        center_y = random.randint(5, height - 5)
        
        # Set a random bright color for this firework
        r, g, b = (
            random.randint(200, 255),
            random.randint(200, 255),
            random.randint(200, 255)
        )
        
        # Draw the explosion
        for angle in range(0, 360, 15):  # Every 15 degrees
            rad = math.radians(angle)
            for dist in range(1, 6):  # Radius of explosion
                x = int(center_x + dist * math.cos(rad))
                y = int(center_y + dist * math.sin(rad))
                
                if 0 <= x < width and 0 <= y < height:
                    set_cursor_position(x + 1, y + 2)
                    set_color(r, g, b)
                    print('*', end='', flush=True)
        
        sys.stdout.flush()
        time.sleep(0.3)
        
        # Clear the explosion
        time.sleep(0.2)
        clear_screen()
        print(f"Fireworks Animation - Firework {firework_num + 1}/10")
    
    reset_color()
    print("\nFireworks complete!\n")
    time.sleep(1)


def main():
    """Main function to run all animations."""
    print("Termux Beautiful Animations")
    print("=" * 40)
    print("This script creates beautiful animations in your terminal!")
    print("Press Ctrl+C to exit early.\n")
    
    try:
        # Run each animation
        loading_bar_animation()
        bouncing_balls_animation()
        wave_animation()
        matrix_rain_animation()
        fireworks_animation()
        
        print("All animations completed! Thanks for watching!")
        
    except KeyboardInterrupt:
        print("\n\nAnimation interrupted by user. Goodbye!")


if __name__ == "__main__":
    main()