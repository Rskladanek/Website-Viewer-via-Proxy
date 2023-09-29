# Website Viewer via Proxy

This program allows users to view a specific website through a proxy multiple times using the Firefox browser. The main use case is to increase views or test website loading through different proxy instances.

## Requirements

- Python 3
- Firefox Browser installed
- Install dependencies using: `pip install -r requirements.txt`

## Usage

1. Clone the repository or download the Python script.
2. Navigate to the directory containing the script.
3. Run the script using the command: `python Main.py`
4. You'll be prompted to enter the website domain you want to view.
5. Next, specify the number of viewers (proxy windows) you want to open.
6. The program will open Firefox windows and navigate to the website through a proxy.
7. Once you're done, you can close all windows by pressing `Enter`.

## Note

- Each proxy window opens the website `https://www.blockaway.net/` and then navigates to the specified website domain.
- Make sure the program is allowed through any firewall or security software to ensure the proxy sites can be accessed.

## Troubleshooting

If you face any issues with the driver or the Firefox path, make sure:

- Firefox is installed correctly.
- There's a stable internet connection.
- You've allowed the program through any firewall or antivirus software.
