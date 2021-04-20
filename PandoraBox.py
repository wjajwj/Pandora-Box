#-*- coding: utf-8 -*-
import os
import sys
from art import *

tprint("Pandora Box")

def chooseCategory():
 print('1: Port Scan\n 2: LFI/RCE\n 3: SQL\n 4: Info gathering\n 5: Website Scanner\n 6: Exploiting/Bruteforcing (includes metasploit)\n 7: DoS\n 8: Wireless attacks\n 9: Programming (Ruby/PHP/Perl)\n 10: WebServer (apache)')
 category = input('Please, choose a category: \n')
   
 if category=='1':
      print('Port Scan')
      print('11: NMAP')
 elif category=='2':
      print('LFI/RCE')
      print('12: LFI-Scanner')
 elif category=='3':
      print('SQL')      
      print('13: sqlmap, 14: sqlscan') 
 elif category=='4':
     print('Info gathering')
     print('15: Sherlock, 16: Infoga')   
 elif category=='5':
     print('Website scanner')
     print('17: admin-panel-finder') 
     print('24: Rapidscan')
     print('25: dirsearch')
 elif category=='6':
     print('Exploiting/Bruteforcing')
     print('20: Metasploit')     
     print('27: WebSploit')

 elif category=='7':
     print('DoS')
     print('22: Slowloris')   
 elif category=='8':
     print('Wireless Attacks')
     print('23: Wifite')  
 elif category=='9':
     print('Programming (Ruby/PHP/Perl)')
     print('24: Ruby, 25: PHP, 26: Perl')  
 elif category=='10':
     print('Web Server') 
     print('28: Apache')   
 elif category >= '11':
     print("Invalid! Please, choose a valid category :)")    
     quit()        

def chooseTool():
 tool = input('Choose the tool (input the number)\n')

 if tool=='11':
      os.system('apt install nmap')
 elif tool=='12':
      os.system('git clone https://github.com/sUbc0ol/LFI-scanner && cd LFI-scanner && python lfiscan.py')
 elif tool=='13':
      os.system('apt install sqlmap')
 elif tool=='14':
      os.system('apt install php php-bz2 php-curl php-mbstring curl && curl https://raw.githubusercontent.com/Cvar1984/sqlscan/dev/build/main.phar --output /usr/local/bin/sqlscan &&chmod +x /usr/local/bin/sqlscan ')             
 elif tool=='15':
    os.system('git clone https://github.com/sherlock-project/sherlock.git && cd sherlock && python3 -m pip install -r requirements.txt')
 elif tool=='16':
    os.system('git clone https://github.com/m4ll0k/Infoga.git && cd Infoga && python setup.py install ')
 elif tool=='17':
    os.system('git clone https://github.com/bdblackhat/admin-panel-finder && cd admin-panel-finder && python admin_panel_finder.py ') 
 elif tool=='18':
     os.system('pkg install wget && wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh && chmod +x metasploit.sh && ./metasploit.sh')  
 elif tool=='19':
     os.system('pip3 install slowloris')
 elif tool=='20':
     os.system('wget https://raw.github.com/derv82/wifite/master/wifite.py && chmod +x wifite.py ')    
 elif tool=='21':
     os.system('apt update && apt upgrade && pkg install clang && apt install ruby vim git nodejs && apt install ruby-dev libxml2-dev libxslt-dev pkg-config make clang && gem install nokogiri -- --use-system-libraries && apt install libsqlite-dev && gem install sqlite3 && apt install libffi-dev && gem install rb-inotify && gem install ffi && apt install openssh && pkg install postgresql postgresql-contrib postgresql-dev && gem install pg && initdb -D ~/postgres/') 
 elif tool=='22':
     os.system('pkg install php')
 elif tool=='23':
     os.system('pkg install perl')   
 elif tool=='24':
     os.system('wget -O rapidscan.py https://raw.githubusercontent.com/skavngr/rapidscan/master/rapidscan.py && chmod +x rapidscan.py')
 elif tool=='25':
     os.system('git clone https://github.com/maurosoria/dirsearch.git && cd dirsearch && pip install -r requirements.txt')       
 elif tool=='27':
     os.system('git clone https://github.com/websploit/websploit.git && cd websploit && python setup.py install') 
 elif tool=='28':
     os.system('pkg install git -y && cd ~/ && git clone https://github.com/viliyam2811/termux-apache2-server && cd ~/termux-apache2-server && bash setup && cd ~/ && rm -rf termux-apache2-server')      
                                      
 elif tool >= '29':
     print("Invalid! please, choose a valid value") 
     quit()   
   
chooseCategory()  
chooseTool()


  

  
    

  
