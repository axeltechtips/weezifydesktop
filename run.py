import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weezify")
        self.setGeometry(100, 100, 1024, 768)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Load the website
        self.web_view.load(QUrl("https://weezify.web.app/"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())
