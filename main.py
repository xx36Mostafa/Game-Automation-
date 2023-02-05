from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from colorama import Fore,Style,init
from termcolor import cprint, colored
from pyfiglet import figlet_format

succ = '<input id="colonizeBtn" class="button action_bubble" title="" type="submit" value="أسِّس مستعمرة!">'

class bot():
    
    def __init__(self,user,password,zore):
        self.user,self.password= user,password
        self.time = zore
        links = open('links.txt','r').read().splitlines()
        self.options = webdriver.ChromeOptions() 
        self.options.add_argument("start-maximized")
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        CHROMEDRIVER_PATH = r'./chromedriver.exe'
        self.broswer = webdriver.Chrome(chrome_options=self.options,executable_path=CHROMEDRIVER_PATH)
        self.actions = ActionChains(self.broswer)
        if self.login():
            self.broswer.execute_script("window.open('');")
            for link in links:
                self.check(link)
            input('[ Press any key to exit..... ]')
    def login(self):
        # <!.. Go To Link ...!>
        self.broswer.get('https://lobby.ikariam.gameforge.com/ar_AE/')
        try:
            self.broswer.implicitly_wait(30)
            self.broswer.find_element(By.XPATH, '//*[@id="loginRegisterTabs"]/ul/li[1]').click()
            user = self.broswer.find_element(By.NAME, 'email')
            user.send_keys(self.user)
            password = self.broswer.find_element(By.NAME, 'password')
            password.send_keys(self.password)
            time.sleep(1.5)
            self.actions.send_keys(Keys.RETURN)
            self.actions.perform()
            if self.active():
                return True
        except:
            return False

    def active(self):
        try:
            # <!..... Click To Join Game .....!>
            time.sleep(5)
            self.broswer.find_element(By.XPATH, '//*[@id="joinGame"]/button').click()
            windows = self.broswer.window_handles
            if len(windows) == 2:
                time.sleep(4)
                self.broswer.switch_to.window(windows[1])
                self.broswer.close()
                self.broswer.switch_to.window(windows[0])
                return True
            else:
                input('Press any key To Exit....')
        except:
            return False            

    def check(self,link):
        self.link = link
        try:
            self.broswer.switch_to.window(self.broswer.window_handles[1])
            self.broswer.get(self.link)
            time.sleep(self.time)
            if succ in self.broswer.page_source:
                self.broswer.find_element(By.ID, 'colonizeBtn').click()
                time.sleep(2)
                x = open('done.txt','a+')
                x.write(link+'\n')
                print(Fore.RED+f'{link} ==> is Done Collect')
            else:
                print(f'{link} ==> Cant Collect')
        except Exception as e:
            print(e)
            return False

def intro():
    cprint(figlet_format('MR JUBA'),
           'green', attrs=['bold'])
    print(Fore.RED + 'Developed Mustafa Nasser , PhoneNumber [+201098974486]'+Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX)

if __name__ == '__main__':
    intro()
    account = open('account.txt','r').read().split(':')
    name , password = account[0] , account[1]
    timee_ = int(input('[ Enter Time each links.. ]\n<> '))
    star = bot(name,password,timee_) 