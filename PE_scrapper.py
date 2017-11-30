import requests, re
from multiprocessing import Pool
from datetime import datetime

n = datetime.today().date()
vdat, count = str(n), 0
DOWNLOAD_PATH = '/home/PE/'

# Below is a dictionary containing the some sample stocks with their Symbol as key 
# and  links from moneycontrol.com as value
# for eg: CROMPTON's link in money control is 
# http://www.moneycontrol.com/india/stockpricequote/electricals/cromptongreavesconsumerelectrical/CGC01

# http://www.moneycontrol.com/india/stockpricequote/ - this part of the link is common to all stocks in moneycontrol.com
# so if you are adding your stocks, add their NSE symbol as key and later part of the link of that stock from moneycontrol 

md = {'CROMPTON':'electricals/cromptongreavesconsumerelectrical/CGC01',
      'GLENMARK':'pharmaceuticals/glenmarkpharma/GP08',
      'WOCKPHARMA':'pharmaceuticals/wockhardt/W05',
      'RELIANCE':'refineries/relianceindustries/RI',
      'POLARIS':'computerssoftware/polarisconsultingservices/PSL01', 
      'BRITANNIA': 'food-processing/britanniaindustries/BI', 
      'SINTEX': 'diversified/sintexindustries/SI27', 
      'FSL': 'computerssoftwaremediumsmall/firstsourcesolutions/FS07', 
      'M%26M': 'autocarsjeeps/mahindramahindra/MM', 
      'ADANIENT': 'trading/adanienterprises/AE13', 
      'SRTRANSFIN': 'finance-leasing-hire-purchase/shriramtransportfinancecorporation/STF',
      'RENUKA':'sugar/shreerenukasugars/SRS03',
      'PENIND': 'steel-cr-hr-strips/pennarindustries/PI28', 
      'BANKBARODA': 'bankspublicsector/bankofbaroda/BOB', 
      'DIVISLAB': 'pharmaceuticals/divislaboratories/DL03', 
      'RECLTD': 'financetermlendinginstitutions/ruralelectrificationcorporation/REC02', 
      'BHARATFORG': 'castingsforgings/bharatforge/BF03', 
      'TATASTEEL': 'steellarge/tatasteel/TIS', 
      'OBEROIRLTY': 'constructioncontractingrealestate/oberoirealty/OR', 
      'ADANIPOWER': 'powergenerationdistribution/adanipower/AP11', 
      'MINDTREE': 'computerssoftware/mindtree/MT13', 
      'VIPIND': 'plastics/vipindustries/VIP', 
      'DRREDDY': 'pharmaceuticals/drreddyslaboratories/DRL', 
      'NATIONALUM': 'aluminium/nationalaluminiumcompany/NAC', 
      'L%26TFH': 'financeinvestments/ltfinanceholdings/LFH', 
      'IDBI': 'bankspublicsector/idbibank/IDB05', 
      'DELTACORP': 'financegeneral/deltacorp/DC11', 
      'ONGC': 'oildrillingandexploration/ongc/ONG', 
      'ACE': 'engineering-heavy/actionconstructionequipment/ACE3',
      'VEDL': 'miningminerals/vedanta/SG', 
      'CENTURYPLY': 'miscellaneous/centuryplyboards/CP9', 
      'HINDCOPPER': 'metalsnonferrous/hindustancopper/HC07', 
      'CENTURYTEX': 'diversified/centurytextilesindustries/CTI', 
      'COX%26KINGS': 'miscellaneous/coxkings/CK', 
      'FORTIS': 'hospitalsmedicalservices/fortishealthcare/FH', 
      'SUZLON': 'powergenerationdistribution/suzlonenergy/SE17', 
      'PERSISTENT': 'computerssoftware/persistentsystems/PS15', 
      'TITAN': 'miscellaneous/titancompany/TI01', 
      'LICHSGFIN': 'financehousing/lichousingfinance/LIC', 
      'ALLCARGO': 'transportlogistics/allcargologistics/AGL02' }
      
for k in md.items:
    if not os.path.isfile(DOWNLOAD_PATH+k+'P/E_history.csv'):
        file = open(DOWNLOAD_PATH+k+'P/E_history.csv','w')
        file.write('DATE, STANDALONE_P/E,	INDUSTRY_P/E,	CONSOLIDATED_P/E\n')
        file.close()

def work(k, v, count):
        p = requests.get('http://www.moneycontrol.com/india/stockpricequote/'+v).text
        a = open('/tmp/'+k+vdat+'.txt', 'w') #temporary storage of the webpage to extract the data.
        a.write(p)
        a.close()
        
        b = open('/tmp/'+k+vdat+'.txt','r')
        c = open(DOWNLOAD_PATH+k+'_PEhist.csv','a')
        prev , cou, data = '', 0, []
        data.append(vdat)
        
        for line in b:
            if cou <= 2 and 'P/E' in prev :
                d = re.findall('">([0-9]+.[0-9]+)', line) #var 'd' is a list here
                if len(d) == 0:
                    d.append('nan')
                data.append(d[0])
                cou += 1
                if c == 3 :
                    break
            prev=line  #REMEMBER THE PREVIOUS LINE.
            
        for j in data:
            li = ','.join(data)
        c.write(li)  # print this line
        c.write('\n')
        b.close()
        c.close()
        print(k,count)
        
if __name__ == '__main__' :
    pool = Pool(processes = 14)
    for k, v in md.items():
        count+ = 1
        pool.apply_async(func = work, args = (k, v, count))
