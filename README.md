# UndipMealAutomator
Effortlessly automate the submission of Undip's free meal form using Selenium and ChromeDriver. This bot is designed to save your time and ensure you never miss out on free meals!

## Features
- Automatically fills out and submits Undip's free meal form.
- Bypasses CAPTCHAs with integrated 2CAPTCHA solving.
- Efficient and undetected browsing using `undetected-chromedriver`.

## Requirements
Before running the bot, ensure you have the following installed:

- Python 3.7+
- Google Chrome (latest version)
- Required Python libraries:
  ```
  selenium
  undetected-chromedriver
  requests
  ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/bruhismyname/UndipMealAutomator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd UndipMealAutomator
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Configure the bot:
   - Open the script file and update your **Undip form credentials** and any other required details.

2. Run the bot:
   ```bash
   python main.py
   ```

3. The bot will open a browser window, navigate to the form, and handle the submission process automatically.

## Important Notes
- Ensure that the Chrome version matches the version of the ChromeDriver used by the `undetected-chromedriver` library.
- Use this bot responsibly and only for personal purposes.

## Troubleshooting
- If the bot fails to bypass CAPTCHA, ensure the `2Captcha` function is properly configured and functional.
- Update Chrome and `undetected-chromedriver` if compatibility issues occur.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer
This project is for educational purposes only. The creator is not responsible for any misuse of this bot.
