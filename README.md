bobByDew.py (BTC Order Book by Mr Dew)
Overview
bobByDew.py is a Python package crafted by Mr. Dew to offer a real-time visualization of cryptocurrency order books, specifically targeting the BTC/USDT trading pair on the Binance exchange. This package leverages the power of asynchronous programming and WebSockets to stream and display market depth updates. The interface is built with the curses library, providing a dynamic, terminal-based graphical display of bids, asks, and crucial trading metrics like the spread, weighted averages, total volume, and order flow imbalance.
Features
Real-time Data Streaming: Connects to Binance via WebSocket to receive live updates.
Trading Metrics: Calculates and displays metrics such as the highest bid, lowest ask, market spread, weighted average prices, total trading volume, and order flow imbalance.
Dynamic Terminal Interface: Utilizes the curses library for an interactive, real-time graphical display in the terminal.
Cross-Platform Compatibility: Works on both Unix-like systems and Windows (using windows-curses for compatibility).
Installation
To install bobByDew.py, follow these instructions based on your operating system:
For Mac/Linux:
pip install bobByDew
Use code with caution.
Bash
For Windows:
Windows users need to ensure windows-curses is installed for curses support:
pip install windows-curses
pip install bobByDew
Use code with caution.
Bash
Usage
After installation, you can run the package directly from the command line:
bobByDew
Use code with caution.
Bash
This command initializes the script and starts the real-time visualization. Ensure you have a stable internet connection to receive real-time updates without interruption.
Configuration
No additional configuration is needed post-installation. However, you must ensure you are legally permitted to use real-time data from Binance, as this script connects directly to Binance APIs.
Contributing
Contributions to bobByDew.py are welcome. Please fork the repository, make your changes, and submit a pull request for review.
License
bobByDew.py is open-sourced under the MIT License. See the LICENSE file for more details.