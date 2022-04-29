# from urllib.request import Request
# import scrapy
# import csv

# class ColonySpider(scrapy.Spider):
#     name = "colony_spider"
    
#     def start_requests(self):
#         start_urls = [
#         'https://nwcmc.gov.in/ptsearch_data.php?colony=206&houseno=&name=&address=&serno=',
#     ]

#         for url in start_urls:
#             yield scrapy.Request(url,callback=self.parse)
            
#     def parse(self, response):
        
#         pincode=response.xpath('/html/body/table//tr/td/div/div/a/text()').extract()
#         sr_no=response.xpath('/html/body/table//tr/td[1]/div/span/text()').extract()
#         service_no=response.xpath('/html/body/table//tr/td[3]/div/text()').extract()
#         Name=response.xpath('/html/body/table//tr/td[4]/div/div/text()').extract()
#         Address=response.xpath('/html/body/table//tr/td[5]/div/span/text()').extract()
            
#         with open('sr_no.csv','w') as f:
#             for sr in sr_no:
#                 f.write(sr)
#                 f.write("\n")
        
#         with open('pincode.csv','w') as f1:
#             for pin in pincode:
#                 f1.write(pin)
#                 f1.write("\n")
                
#         with open('service_no.csv','w') as f2:
#             for serv_no in service_no:
#                 f2.write(serv_no)
#                 f2.write("\n")
        
#         with open('name.csv','w') as f3:
#             for name in Name:
#                 f3.write(name)
#                 f3.write("\n")
        
#         with open('address.csv','w') as f4:
#             for address in Address:
#                 f4.write(address)
#                 f4.write("\n")
                
      
import scrapy

class SchoolSpider(scrapy.Spider):
    name = "school"
    start_urls = ('https://nwcmc.gov.in/ptsearch_data.php?colony=206&houseno=&name=&address=&serno=',)

    def parse_products(self, response):
        
        products =self.xpath('/html/body/table/tbody')
        
        for p in products[1:]:
            
            item = dict()
            item['sr_no'] = p.xpath('/html/body/table//tr/td[1]/div/span/text()').extract()
            item['pincode'] = p.xpath('/html/body/table//tr/td/div/div/a/text()').extract()
            item['service_no'] = p.xpath('/html/body/table//tr/td[3]/div/text()').extract()
            item['name'] = p.xpath('/html/body/table//tr/td[4]/div/div/text()').extract()
            item['address'] = p.xpath('/html/body/table//tr/td[5]/div/span/text()').extract()
            print(item,"*************************************************************************")
            
            yield item