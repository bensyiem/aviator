import platform
import os

def play_sound():
    try:
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(1000, 300)
        else:
            os.system('play -nq -t alsa synth 0.3 sine 1000')
    except:
        print("Sound alert failed")

def track_stats(rounds, safe):
    return f"""
    ## 📊 Stats
    - Total Predictions: `{rounds}`
    - Safe Signals: `{safe}`
    - Accuracy: `{(safe / rounds * 100):.2f}%` if rounds > 0 else "0%"
    """
