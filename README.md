# Target Loader
Target Loader serves a niche function for my job: automates the installation of packages for the PS4 and PS5 target managers. Since it's required to install packages before I can perform my duties and the target managers do not allow for package queueing, any delay with installing packages slows down my work.

# What It Does
Target Loader creates a queue to automatically install PS4 and PS5 packages. This is why the app is being made, because the existing target managers don't allow this. The app performs the same actions as a regular user, by manipulating the mouse and keyboard. If the target manager isn't in view on the screen, it will quickly `alt-tab` to the manager before either performing it's tasks or using `alt-tab` to bring the user back to the screen they were on before.

# How It Works
This is a GUI app that queues `.pkg` files for installing to Sony consoles. This app uses [kivy](https://kivy.org/#home) for the GUI, [imagesearch](https://brokencode.io/how-to-easily-image-search-with-python/) to find the necessary buttons, and [pyautogui](https://pyautogui.readthedocs.io/en/latest/screenshot.html) to perform keyboard and mouse inputs. These choices were made for two simple reasons: fast development times and laziness.

# Contributing
Unfortunately for you, unless the IT and Security departments for my company approve of an open source project being distributed on their intranet, no pull requests will be accepted and the application herein is explicitly for use by Activision Publishing.
