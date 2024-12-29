# aztool/core.py
import subprocess
import platform

def greet():
    """Return a greeting message."""
    return "Hello from aztool!"

def get_wifi_details():
    """Fetch the Wi-Fi SSID and Password."""
    try:
        if platform.system() == "Windows":
            # Windows Command to Fetch Wi-Fi Details
            result = subprocess.check_output(
                "netsh wlan show profiles",
                shell=True,
                text=True
            )
            profiles = [line.split(":")[1].strip() for line in result.split("\n") if "All User Profile" in line]
            
            wifi_details = {}
            for profile in profiles:
                try:
                    details = subprocess.check_output(
                        f'netsh wlan show profile name="{profile}" key=clear',
                        shell=True,
                        text=True
                    )
                    password_line = [line for line in details.split("\n") if "Key Content" in line]
                    password = password_line[0].split(":")[1].strip() if password_line else "No Password"
                    wifi_details[profile] = password
                except subprocess.CalledProcessError:
                    wifi_details[profile] = "Could not retrieve details"
            
            return wifi_details

        elif platform.system() == "Linux" or platform.system() == "Darwin":
            # Linux/Mac Command to Fetch Wi-Fi Details
            result = subprocess.check_output(
                "nmcli -t -f active,ssid dev wifi | grep '^yes'",
                shell=True,
                text=True
            )
            ssid = result.split(":")[1].strip()
            password_result = subprocess.check_output(
                f"sudo grep psk= /etc/NetworkManager/system-connections/{ssid}.nmconnection",
                shell=True,
                text=True
            )
            password = password_result.split("=")[1].strip()
            return {ssid: password}

        else:
            return "Unsupported OS"
    
    except Exception as e:
        return {"error": str(e)}
