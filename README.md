# PE-ratio
P/E ratio is an important financial ratio for stock selection and investment. 

The P/E data for NSE listed stocks from moneycontrol.com is scrapped 
using this script and saved in a csv file on a daily basis.

This script extracts Stand alone P/E, Consolidated P/E and Indusry P/E as given in moneycontrol.com

The script has a dictionary named "stock_list" containing the some sample 
stocks with their Symbol as key and  links from moneycontrol.com as value.

for eg: CROMPTON's link in money control is 
http://www.moneycontrol.com/india/stockpricequote/electricals/cromptongreavesconsumerelectrical/CGC01

http://www.moneycontrol.com/india/stockpricequote/ - this part of the link is common to all stocks in moneycontrol.com
so if you are adding your stocks, add their NSE symbol as key and later(remaining) part of the link of that stock from moneycontrol as value.
