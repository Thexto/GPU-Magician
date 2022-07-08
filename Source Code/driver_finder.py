from selenium.webdriver import Chrome, Firefox, Ie, Edge
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from winreg import OpenKey, HKEY_CURRENT_USER, QueryValueEx

def get_driver():
    #Checks for preferred browser | Will probably fail on linux
    try:
        with OpenKey(HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice") as key:
            browser = QueryValueEx(key, 'Progid')[0]
    except:
        return Chrome(service=Service(ChromeDriverManager().install()))
    try:
        if browser[0:11] == 'ChromiumHTM':
            browser = browser[0:11]
        if browser[0:10] == 'FirefoxURL':
            browser = browser[0:10]
            
        #Downloads specified driver
        match browser:
            case 'ChromeHTML':
                return Chrome(service=Service(ChromeDriverManager().install()))
            case 'FirefoxURL':
                return Firefox(service=Service(GeckoDriverManager().install()))
            case 'IE.HTTP':
                return Ie(service=Service(IEDriverManager().install()))
            case 'MSEdgeHTM':
                return Edge(service=Service(EdgeChromiumDriverManager().install()))
            case 'ChromiumHTM':
                return Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    except:
        print(f'Browser: {browser} not supported.\nSupported: Chrome, Firefox, IE, Edge, Chromium\n')
        return None

if __name__ == "__main__":
    get_driver()