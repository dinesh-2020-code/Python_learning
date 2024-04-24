import webbrowser

# webbrowser.open('https://www.python.org')
# help(webbrowser)

# for i in range(10):
#     print(1, 2, 3, 4, 5, sep='; ', end=' ') 
# chrome = webbrowser.get(using='windows-default')
chrome = webbrowser.get('google-chrome %s').open("https://www.python.org/")
# chrome.open_new("https://www.python.org/")
