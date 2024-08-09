```markdown
# copy.ai

# Gemini Clipboard Automation

This script integrates with the Gemini API to process text content copied to the clipboard, allowing users to send text to the Gemini model, receive a generated response, and perform keyboard actions based on the response's availability.

## Features

- **Clipboard Integration**: Automatically send clipboard content to the Gemini AI model for processing.
- **Keyboard Shortcuts**: Use keyboard shortcuts to trigger specific actions:
  - `Shift+1`: Send clipboard content to the Gemini AI.
  - `Shift+2`: Copy the response from Gemini AI to the clipboard.
  - `Shift+3`: Press '1' if a response is available, otherwise press '0'.
- **Automated Key Press**: Automate key presses based on the availability of a response.

## Requirements

- Python 3.x
- [keyboard](https://pypi.org/project/keyboard/)
- [pyperclip](https://pypi.org/project/pyperclip/)
- [google.generativeai](https://pypi.org/project/google-generativeai/)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/gemini-clipboard-automation.git
   cd gemini-clipboard-automation
   ```

2. **Install Dependencies**

   Install the necessary Python packages using pip:

   ```bash
   pip install keyboard pyperclip google-generativeai
   ```

3. **Configure the Google API Key**

   Open the script and replace `'your gemini api key'` with your actual Google API key:

   ```python
   GOOGLE_API_KEY = 'your gemini api key'
   ```

## Usage

1. **Run the Script**

   Start the script by executing:

   ```bash
   python gemini_clipboard_automation.py
   ```

2. **Use Keyboard Shortcuts**

   - **Shift+1**: Sends the current clipboard text to the Gemini model.
   - **Shift+2**: Copies the response from the Gemini model back to the clipboard.
   - **Shift+3**: Simulates a key press:
     - Presses `1` if a response is received.
     - Presses `0` if no response is available.

3. **Terminate the Script**

   To exit the script, press `Ctrl+Esc`.

## Notes

- Ensure your clipboard contains text content before using `Shift+1`.
- Make sure your Google API key is correctly set up and has the necessary permissions to access the Gemini model.

## Troubleshooting

- **Error Communicating with Gemini API**: Ensure your API key is valid and has the correct permissions.
- **Keyboard Module Not Functioning**: You might need to run the script with administrative privileges.