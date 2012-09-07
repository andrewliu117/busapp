#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib  

headers={
		"User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
		"Accept-Encoding": "gzip, deflate",
		"Connection": "keep-alive",
		"Cookie": "CNZZDATA2220450=cnzz_eid=29138425-1346728769-http%253A%252F%252Fwww.cdgjbus.com%252F&ntime=1346915900&cnzz_a=1&retime=1346915958460&sin=none&ltime=1346915958460&rtime=1; CheckCode=4483; ASP.NET_SessionId=31snbjjurln1rr55ubdynjag"}

conn = httplib.HTTPConnection("www.cdgjbus.com:8802")  
#conn.request('get', '/BusLine/BusLine.aspx', headers=headers)  
conn.request('get', '/BusTravelGuide/Default.aspx', headers=headers)  
#print conn.getresponse().getheaders()  
print conn.getresponse().read()  
conn.close() 
