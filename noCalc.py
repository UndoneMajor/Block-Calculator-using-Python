import psutil
import time
import os
import platform

# Known calculator-related process name fragments (lowercase)
CALCULATOR_KEYWORDS = {
    'Windows': ['calculator', 'calc', 'wincalc', 'applicationframehost'],
    'Darwin': ['calculator'],  # macOS
    'Linux': ['calc', 'gnome-calc', 'kcalc', 'galculator', 'mate-calc', 'qalculate']
}

def kill_calculators():
    current_os = platform.system()
    keywords = CALCULATOR_KEYWORDS.get(current_os, [])
    
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.info['name'].lower()
            if any(keyword in name for keyword in keywords):
                os.kill(proc.info['pid'], 9)
                print(f"[✖] Killed: {proc.info['name']} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == "__main__":
    print(f"🔒 Blocking Calculator on {platform.system()}... Press Ctrl+C to stop.")
    while True:
        kill_calculators()
        time.sleep(0.5)
