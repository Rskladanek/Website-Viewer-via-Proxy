Website Viewer via Proxy
This program allows users to view a specific website through a proxy multiple times using the Firefox browser. The main use case is to increase views or test website loading through different proxy instances.

Requirements
Python 3
Firefox Browser installed
pip install -r requirements.txt
Usage
Clone the repository or download the Python script.
Navigate to the directory containing the script.
Run the script using the command: python Main.py
You'll be prompted to enter the website domain you want to view.
Next, specify the number of viewers (proxy windows) you want to open.
The program will open Firefox windows and navigate to the website through a proxy.
Once you're done, you can close all windows by pressing Enter.
Note
Each proxy window opens the website https://www.blockaway.net/ and then navigates to the specified website domain.
Make sure the program is allowed through any firewall or security software to ensure the proxy sites can be accessed.
Troubleshooting
If you face any issues with the driver or the Firefox path, make sure:

Firefox is installed correctly.
There's a stable internet connection.
You've allowed the program through any firewall or antivirus software.
You can save the above content to a README.md file and place it in the directory containing your Python script. Adjust any information as necessary to better fit your program's specifics or usage instructions.
