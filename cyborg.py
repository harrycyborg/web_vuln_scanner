import re
import urllib
from headers import *
from vulnz import *

print ga.green+'''
            
    ,o888888o.  `8.`8888.      ,8' 8 888888888o       ,o888888o.     8 888888888o.      ,o888888o.    
   8888     `88. `8.`8888.    ,8'  8 8888    `88.  . 8888     `88.   8 8888    `88.    8888     `88.  
,8 8888       `8. `8.`8888.  ,8'   8 8888     `88 ,8 8888       `8b  8 8888     `88 ,8 8888       `8. 
88 8888            `8.`8888.,8'    8 8888     ,88 88 8888        `8b 8 8888     ,88 88 8888           
88 8888             `8.`88888'     8 8888.   ,88' 88 8888         88 8 8888.   ,88' 88 8888           
88 8888              `8. 8888      8 8888888888   88 8888         88 8 888888888P'  88 8888           
88 8888               `8 8888      8 8888    `88. 88 8888        ,8P 8 8888`8b      88 8888   8888888 
`8 8888       .8'      8 8888      8 8888      88 `8 8888       ,8P  8 8888 `8b.    `8 8888       .8' 
   8888     ,88'       8 8888      8 8888    ,88'  ` 8888     ,88'   8 8888   `8b.     8888     ,88'  
    `8888888P'         8 8888      8 888888888P       `8888888P'     8 8888     `88.    `8888888P'    
	
	'''+ga.end

def urls_or_list():
	url_or_list = raw_input(" [!] Scan URL or List of URLs? [1/2]: ")
	if url_or_list == "1":
	 	 url = raw_input(" [!] Enter the URL: ")
		 if "?" in url:
		 	rce_func(url)
		 	xss_func(url)
		 	error_based_sqli_func(url)
		 else:
			print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" is not a valid URL"+ga.end			
			print ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end
			exit()
	if url_or_list =="2":
		 urls_list = raw_input( ga.green+" [#] Enter the list file name .e.g [list.txt]: "+ga.end)
		 open_list = open(urls_list).readlines()
		 for line in open_list:
			 if "?" in line:
			 	links = line.strip()
		  	 	url = links
		  	 	print ga.green+" \n [#] Now Scanning %s"%url +ga.end
		  	 	rce_func(url)
			 	xss_func(url)
			 	error_based_sqli_func(url)
			 else:
			 	links = line.strip()
		  	 	url = links
				print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" is not a valid URL"+ga.end				
				print ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end
		 exit()				

urls_or_list()





