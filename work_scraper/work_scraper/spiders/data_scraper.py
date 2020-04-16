import scrapy
from scrapy.crawler import CrawlerProcess
import json

#trademe spider
class TradeMe(scrapy.Spider):
    name = 'trademe'
    
    def start_requests(self):
        url = "https://api.trademe.co.nz/v1/Search/Jobs.json?category=5000&page=1&photo_size=Gallery&return_did_you_mean=true&return_metadata=true&return_variants=true&rows=50&user_initiated=true"

        headers = {
            'Host' : 'api.trademe.co.nz',
            'X-TradeMe-UniqueClientID' : '5DD3C041-6218-47CA-985A-ECAFB83BBB08',
            'Accept' : '*/*',
            'User-Agent' : 'trademe/50.0 (iPhone; iOS 13.3; Scale/3.00)',
            'Accept-Language' : 'en-NZ;q=1',
            'Authorization' : 'OAuth oauth_consumer_key="E83DD89A2F73BBDD15E4C3CD757576DE37", oauth_nonce="1581261907284.49", oauth_signature="593wU44lEx2ewdTEyDi%2BOBYIjTs%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1581261907", oauth_token="BDD0D8F4D1F869962A768A75B0A659A6", oauth_version="1.0"' 
        }

        yield scrapy.http.Request(url, headers = headers)

    def parse(self, response):
        trademe_data = json.loads(response.body)
        for line in trademe_data['List']:
            yield line

# seek spider
class Seek(scrapy.Spider):
    name = 'seek'

    def start_requests(self):
        url = "https://jobsearch-api-mobile.cloud.seek.com.au/search?Location=3001&Page=1&PageSize=20&SiteKey=nz&highlight=false&seekSelectAllPages=true&userid=5BDD3CFE43E64C089E9FB9E353EAA50D"

        headers = {
            'Host' : 'jobsearch-api-mobile.cloud.seek.com.au',
            'X-Seek-iOS-App-Version' : '2.50.1',
            'Accept' : '*/*',
            'X-Seek-EC-SessionId' : 'A9EA01F126934F41BDFAEA151B9213A7',
            'User-Agent' : 'seek/2.50.1 (com.seek.jobseeker; build:1196; iOS 13.3.0; iPhone10,2) Alamofire/4.8.1',
            'Accept-Language' : 'en-NZ;q=1.0',
            'seek-client-context' : 'ewogICJkZXZpY2UiIDogewogICAgIm1vZGVsIiA6ICJpUGhvbmUxMCwyIgogIH0sCiAgImNsaWVudCIgOiB7CiAgICAiY291bnRyeV9jb2RlIiA6ICJueiIsCiAgICAidmlzaXRvcklkIiA6ICI1QkREM0NGRTQzRTY0QzA4OUU5RkI5RTM1M0VBQTUwRCIsCiAgICAiYXBwX2luc3RhbGxfaWQiIDogIjVCREQzQ0ZFNDNFNjRDMDg5RTlGQjlFMzUzRUFBNTBEIgogIH0KfQ==',
            'X-Request-Id' : 'AE8AE424-BE7D-4FA8-88A6-C1E46C4DEE46',
        }
        yield scrapy.http.Request(url, headers = headers)

    def parse(self, response):
        seek_data = json.loads(response.body)
        for line in seek_data['data']:
            yield line  

# jora spider
class Jora(scrapy.Spider):
    name = 'jora'

    def start_requests(self):
        url = 'https://au.jora.com/api/v3/jobs/search?includeSponsoredJobs=true&keywords=&location=&onlyNew=false&siteId=au'

        headers = {
            'Host' : 'au.jora.com',
            'accept' : '*/*',
            'content-type' : 'application/vnd.api+json',
            'x-client-id' : 'a177e89c1ed84ed147a0e60627fcbf0cc92d4b56542e77aa2aa947f15ea6955f',
            'if-none-match' : 'W/"87c20793d1e8843d69b503f95ec0dbf6"',
            'x-device-id' : '9956F20B-7726-4D07-B5FF-577A829F5A30',
            'user-agent' : 'Jora com.jora.Jobseeker/2.10.2 iOS/13.3 Apple/iPhone',
            'accept-language' : 'en-NZ;q=1.0',
        }
        yield scrapy.http.Request(url, headers = headers)

    def parse(self, response):
        jora_data = json.loads(response.body)
        for line in jora_data['data']:
            yield line  

# run trademe and seek spiders
def main():
    process = CrawlerProcess({
        'FEED_URI': '/Users/TJ/Documents/GitHub/work_scraper/work_scraper/work_scraper/spiders/trademe.jl',
    })
    process.crawl(TradeMe)

    process = CrawlerProcess({
        'FEED_URI': '/Users/TJ/Documents/GitHub/work_scraper/work_scraper/work_scraper/spiders/seek.jl',
    })
    process.crawl(Seek)

    process.start()

main()