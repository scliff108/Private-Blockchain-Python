# Private-Blockchain-Python
You will need to complete the following functions to complete this project.
## block.py
1. `validate(self)`
2. `get_block_data(self)`
## blockchain.py
1. `add_block(self, block)`
2. `submit_star(self, address, star)`
3. `get_block_by_hash(self, hash)`

## What problem will you solve implementing this private Blockchain application?
Your employer is trying to make a test of concept on how a Blockchain application can be implemented in his company. He is an astronomy fan and he spends most of his free time on searching stars in the sky, that's why he would like to create a test application that will allow him to register stars.

### What is the process to be implemented in the applicatoin?
1. The application will create a Genesis Block when the application is run.
2. The application will allow a user to submit a star using the `submit_star` function.
3. The user can get a block by its hash value using the `get_block_by_hash` function.
4. The user can get a block by its height (already created for you in api.py).
5. The welcome screen will show the blockchain represented by each blocks hash value (already created for you in api.py).

### Getting Started
To get started, download the boilerplate code. Once you do, you can navigate through the 3 important files:
1. api.py (DO NOT CHANGE THIS FILE)
2. block.py
3. blockchain.py
Before you can run and test your application, you will need to install a few things.
1. [Install Visual Studio Code](https://code.visualstudio.com/download)
2. [Install Git](https://git-scm.com/downloads)
3. [Install Python](https://www.python.org/downloads/)
4. Install Flask py -m install Flask

### How do I test my application?
Once you have everything installed, you can test your application. In a terminal window, navigate to your project root folder and type in `py api.py`. The application will start. There will be a link in the terminal telling you where the website is. Follow that link to see how your application is working. Here are some other things you can test:
1. `/` This is the welcome page. It should provide a list of block hashes currently on your blockchain.
2. `/block/height?height={height}` Will show you the block at the height you specify.
3. `/submit_star?address={address}&star={star}` Will add a block to the blockchain with the address and star you specify.
4. `/block/hash?hash={hash}` Will show you the block with the hash you specify.
