# This is a work in progress

# What and why?
Space Surfer is a simple cross-platform browser built on top of PyQt 5.4. It
aims to improve upon Chrome's and Firefox's horrid user interface. Here are the
issues I have with their UI:
* So damn confusing
* Bookmarking and accessing the bookmarks is a pain in the ass
* I suspect that with some customization I could adjust the UI to my liking,
but screw that. I'd rather make my own browser.
* Overcrowded UI
* I feel frustrated just thinking about it

# What about performance?
Space Surfer uses Qt's WebKit backend. It's not exactly the most modern rendering
engine anymore, but it's good enough. When PyQt gets bindings for the new
Chromium Embedded Framework-based WebEngine backend, then it'll be safe to say
that it's as fast as the other kids in town, but until then it will be using
WebKit. I'll do some speed tests and post actual data one day.

On Windows the browser is rather laggy, but on Linux (Debian, GNOME) it's blazing
fast. I have no idea why ¯\\\_(ツ)_/¯.

# Build settings
* Python 2.7
* PyQt 5.4 (compiled from source on Linux)

# TODO - short-term
* Check out QWebSettings
* History menu

# TODO - long-term
* Recent tabs menu
* Bookmarks
* Zoom
* Download manager
* Built-in 'About' page and docs
* Regex search
