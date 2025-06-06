# import pywhatkit
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
import sys 

sys.path.insert(0, 'C:/Users/yasha/Desktop/Assistant/utils')
from util import speak, listen

# def music_yt(song_name):
#         speak(f"Playing {song_name} on YouTube")

#         chrome_options = Options()
#         chrome_options.add_experimental_option("detach", True)  # So it stays open
#         chrome_options.add_argument("--log-level=3")  # Less verbose

#         driver = webdriver.Chrome(options=chrome_options)
#         search_url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
#         driver.get(search_url)

#         # Click the first result
#         time.sleep(2)
#         video = driver.find_elements(By.ID, "video-title")[0]
#         video.click()

#         # Wait until user closes the tab
#         try:
#             while len(driver.window_handles) > 0:
#                 time.sleep(5)
#         except:
#             pass

#         speak("The music has ended or the tab was closed. Ready for the next command.")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def music_yt(song_name):
    print(f"[INFO] Playing: {song_name}")

    # Path to Brave browser (edit this path if needed)
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

    # Setup options for Brave
    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")

    # Setup driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(f"https://www.youtube.com/results?search_query={song_name}+official+video")
        time.sleep(3)
        
        first_result = driver.find_element(By.ID, "video-title")
        first_result.click()
        time.sleep(5)

        # Wait for the video element
        video_loaded = False
        for _ in range(10):
            is_video_present = driver.execute_script("return !!document.querySelector('video');")
            if is_video_present:
                video_loaded = True
                break
            time.sleep(1)

        if not video_loaded:
            print("[ERROR] Video element not found.")
            driver.quit()
            return

        driver.execute_script("document.querySelector('video').play();")
        print("[INFO] Video started playing.")

        # Wait until the video finishes
        print("[INFO] Waiting for video to finish...")
        while True:
            ended = driver.execute_script("return document.querySelector('video').ended;")
            if ended:
                print("[INFO] Video finished.")
                break
            time.sleep(2)

    except Exception as e:
        print(f"[ERROR] {e}")
        driver.quit()
        return

    driver.quit()
    print("[INFO] Assistant ready now.")



