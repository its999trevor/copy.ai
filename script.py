import keyboard
import pyperclip
import google.generativeai as genai
import os

GOOGLE_API_KEY='your gemini api key'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

response_text = ""

def send_to_gemini():
    global response_text
    text = pyperclip.paste()
    
    try:
        response = model.generate_content(text)
        
        response_text = response.text
        print("Received response from Gemini:", response_text)
    
    except Exception as e:
        print("Error communicating with Gemini API:", e)
        response_text = ""

def paste_response():
    global response_text
    pyperclip.copy(response_text)
    print("Response copied to clipboard.")

def press_based_on_response():
    import time
    time.sleep(.30)
    if response_text:
        
        keyboard.press_and_release('1')
    else:
        keyboard.press_and_release('0')
    print("Key pressed based on response availability.")


keyboard.add_hotkey('shift+1', send_to_gemini)
keyboard.add_hotkey('shift+2', paste_response)
keyboard.add_hotkey('shift+3', press_based_on_response)


print("Press Shift+1 to send clipboard content to Gemini AI.")
print("Press Shift+2 to paste the response from Gemini AI.")
print("Press Shift+3 to press 1 if response available, else press 0.")


keyboard.wait('ctrl+esc')  
