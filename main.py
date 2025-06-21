import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtSvg import QSvgRenderer

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Web Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Create a central widget and a layout
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        
        self.setCentralWidget(self.browser)

        # Create a navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)
        # Set a border for the toolbar using setStyleSheet
        navbar.setStyleSheet("""
            QToolBar {
                border: 2px solid #333;       /* Dark border around the toolbar */
                border-radius: 5px;           /* Rounded corners */
                background-color: #f0f0f0;    /* Background color */
            }
        """)

        # Add back, forward, reload, and home buttons to the navbar with icons
        back_button = QAction(QIcon("icons/back_icon.png"), 'Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)
        # Customize the style of the back button (border, padding, etc.)
        # To style the action button, we need to apply style to its widget (which is a QToolButton or similar)
        back_button_widget = navbar.widgetForAction(back_button)  # Get the widget associated with the action

        # Set border for the button
        if back_button_widget:
            back_button_widget.setStyleSheet("""
                border: 2px solid #333;       /* Dark border */
                border-radius: 5px;           /* Rounded corners */
                padding: 5px;                 /* Padding inside the button */
                background-color: #f0f0f0;    /* Light background color */
            """)

        forward_button = QAction(QIcon("icons/forward_icon.png"), 'Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)
        # Customize the style of the back button (border, padding, etc.)
        # To style the action button, we need to apply style to its widget (which is a QToolButton or similar)
        forward_button_widget = navbar.widgetForAction(forward_button)  # Get the widget associated with the action

        # Set border for the button
        if forward_button_widget:
            forward_button_widget.setStyleSheet("""
                border: 2px solid #333;       /* Dark border */
                border-radius: 5px;           /* Rounded corners */
                padding: 5px;                 /* Padding inside the button */
                background-color: #f0f0f0;    /* Light background color */
            """)

        reload_button = QAction(QIcon("icons/reload_icon.png"), 'Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)
        # Customize the style of the back button (border, padding, etc.)
        # To style the action button, we need to apply style to its widget (which is a QToolButton or similar)
        reload_button_widget = navbar.widgetForAction(reload_button)  # Get the widget associated with the action

        # Set border for the button
        if reload_button_widget:
            reload_button_widget.setStyleSheet("""
                border: 2px solid #333;       /* Dark border */
                border-radius: 5px;           /* Rounded corners */
                padding: 5px;                 /* Padding inside the button */
                background-color: #f0f0f0;    /* Light background color */
            """)
        

        home_button = QAction(QIcon("icons/home_icon.png"), 'Home', self)
        home_button.triggered.connect(self.load_homepage)
        navbar.addAction(home_button)
        # Customize the style of the back button (border, padding, etc.)
        # To style the action button, we need to apply style to its widget (which is a QToolButton or similar)
        home_button_widget = navbar.widgetForAction(home_button)  # Get the widget associated with the action

        # Set border for the button
        if home_button_widget:
            home_button_widget.setStyleSheet("""
                border: 2px solid #333;       /* Dark border */
                border-radius: 5px;           /* Rounded corners */
                padding: 5px;                 /* Padding inside the button */
                background-color: #f0f0f0;    /* Light background color */
            """)

        # Add a URL bar for navigation with larger font size
        self.url_bar = QLineEdit(self)
        self.url_bar.setFont(QFont('Arial', 14))
        # Set the border for the search bar
        self.url_bar.setStyleSheet("border: 2px solid #333; border-radius: 5px; padding: 5px;")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Add a search engine combo box
        self.search_engines = {
            'Google': 'https://www.google.com/search?q=',
            'Bing': 'https://www.bing.com/search?q=',
            'DuckDuckGo': 'https://duckduckgo.com/?q=',
            'Yahoo': 'https://search.yahoo.com/search?p='
        }

        self.search_dropdown = QComboBox(self)
        self.search_dropdown.addItems(self.search_engines.keys())
        navbar.addWidget(self.search_dropdown)
        # Make the font size larger
        self.search_dropdown.setFont(QFont('Arial', 14))  # Set font to Arial, size 14

        # Optionally, set a fixed size for the dropdown (width, height)
        # self.search_dropdown.setFixedSize(200, 40)  # Adjust the width and height as per your needs

        # Alternatively, you can set minimum size to make it flexible
        self.search_dropdown.setMinimumSize(200, 40)
                
        # Add a bookmark button
        bookmark_button = QAction(QIcon("icons/bookmark_icon.png"), 'Bookmark', self)
        bookmark_button.triggered.connect(self.bookmark_page)
        navbar.addAction(bookmark_button)
        # Customize the style of the back button (border, padding, etc.)
        # To style the action button, we need to apply style to its widget (which is a QToolButton or similar)
        bookmark_button_widget = navbar.widgetForAction(bookmark_button)  # Get the widget associated with the action

        # Set border for the button
        if bookmark_button_widget:
            bookmark_button_widget.setStyleSheet("""
                border: 2px solid #333;       /* Dark border */
                border-radius: 5px;           /* Rounded corners */
                padding: 5px;                 /* Padding inside the button */
                background-color: #f0f0f0;    /* Light background color */
            """)


        # Add new tab` and close tab functionality
        new_tab_button = QAction(QIcon("icons/new_tab_icon.png"), 'New Tab', self)
        new_tab_button.triggered.connect(self.new_tab)
        navbar.addAction(new_tab_button)
        # Customize the style of the back button (border, padding, etc.)
        # To style the action button, we need to apply style to its widget (which is a QToolButton or similar)
        new_tab_button_widget = navbar.widgetForAction(new_tab_button)  # Get the widget associated with the action

        # Set border for the button
        if new_tab_button_widget:
            new_tab_button_widget.setStyleSheet("""
                border: 2px solid #333;       /* Dark border */
                border-radius: 5px;           /* Rounded corners */
                padding: 5px;                 /* Padding inside the button */
                background-color: #f0f0f0;    /* Light background color */
            """)

        self.browser.urlChanged.connect(self.update_url)

        # Add a loading indicator
        self.loading_indicator = QLabel("Loading...", self)
        self.loading_indicator.setVisible(False)
        navbar.addWidget(self.loading_indicator)

        self.browser.loadStarted.connect(self.on_load_started)
        self.browser.loadFinished.connect(self.on_load_finished)

        # Bookmarks list
        self.bookmarks = []

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def navigate_to_url(self):
        url = self.url_bar.text()

        # Check if the URL is a search query
        if ' ' in url:
            search_engine = self.search_dropdown.currentText()
            search_url = self.search_engines[search_engine] + url
            self.browser.setUrl(QUrl(search_url))
        else:
            self.browser.setUrl(QUrl(url))

    def load_homepage(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def on_load_started(self):
        self.loading_indicator.setVisible(True)

    def on_load_finished(self, success):
        self.loading_indicator.setVisible(False)

    def bookmark_page(self):
        url = self.browser.url().toString()
        if url not in self.bookmarks:
            self.bookmarks.append(url)
            print(f"Bookmarked: {url}")
        else:
            print(f"Already bookmarked: {url}")

    def new_tab(self):
        new_browser = QWebEngineView()
        new_browser.setUrl(QUrl("http://www.google.com"))
        new_browser.show()

def main():
    app = QApplication(sys.argv)
    QApplication.setApplicationName("Web Browser")
    window = Browser()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
