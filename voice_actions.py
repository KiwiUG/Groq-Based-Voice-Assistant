# voice_actions.py
import subprocess
import webbrowser
import os
import sys

# Define the normalization for app names to standardize variations
app_normalizations = {
    "ms word": "word",
    "microsoft word": "word",
    "google chrome": "chrome",
    "chrome": "chrome",
    "whatsapp": "whatsapp",
    "explorer": "explorer",
    "task manager": "taskmgr",
    "notepad": "notepad",
    "calc": "calc",
    "music": "music",
    "videos": "videos",
    "documents": "documents",
    "mail": "mail",
    "word": "word",
    "excel": "excel",
    "lock": "lock",
    "shutdown": "shutdown",
    "restart": "restart",
    "youtube": "youtube",
    "google": "google"
}

def perform_action(action_type, action_data):
    if action_type == "open_app":
        open_app(action_data)
    elif action_type == "open_url":
        open_url(action_data)
    elif action_type == "none":
        pass
    else:
        print(f"Unknown action type: {action_type}")

def normalize_app_name(app_name):
    """
    Normalize the app name by checking against a dictionary of known names.
    """
    return app_normalizations.get(app_name.lower(), app_name.lower())

def open_app(app_name):
    app_name = normalize_app_name(app_name)
    try:
        if sys.platform == "win32":
            apps = {
                "calc": "calc.exe",
                "notepad": "notepad.exe",
                "mail": "outlook.exe",
                "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                "explorer": "explorer.exe",
                "taskmgr": "taskmgr.exe",
                "music": os.path.expanduser("~\\Music"),
                "videos": os.path.expanduser("~\\Videos"),
                "documents": os.path.expanduser("~\\Documents"),
                "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
                "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
                "whatsapp": "C:\\Users\\%USERNAME%\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            }

            # Special folder paths
            if app_name in ["music", "videos", "documents"]:
                folder_path = apps[app_name]
                subprocess.Popen(["explorer", folder_path])
            elif app_name == "lock":
                subprocess.call("rundll32.exe user32.dll,LockWorkStation")
            elif app_name == "shutdown":
                subprocess.call("shutdown /s /t 0")
            elif app_name == "restart":
                subprocess.call("shutdown /r /t 0")
            else:
                app_path = apps.get(app_name, None)
                if app_path:
                    subprocess.Popen(app_path)
                else:
                    print(f"Failed to open app '{app_name}': App not found.")
        else:
            print("This voice assistant currently supports Windows. Add Linux/macOS paths as needed.")
    except Exception as e:
        print(f"Failed to open app '{app_name}': {e}")

def open_url(url):
    # Handle basic search shortcuts
    search_sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "whatsapp": "https://web.whatsapp.com",
    }

    if url.lower() in search_sites:
        webbrowser.open(search_sites[url.lower()])
    elif "search:" in url.lower():
        query = url.split("search:")[-1].strip()
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
    else:
        if not url.startswith("http"):
            url = "http://" + url
        webbrowser.open(url)
#end