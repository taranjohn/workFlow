# trademe headers

headers = {
    'Host' : 'api.trademe.co.nz',
    'X-TradeMe-UniqueClientID' : '5DD3C041-6218-47CA-985A-ECAFB83BBB08',
    'Accept' : '*/*',
    'User-Agent' : 'trademe/50.0 (iPhone; iOS 13.3; Scale/3.00)',
    'Accept-Language' : 'en-NZ;q=1',
    'Authorization' : 'OAuth oauth_consumer_key="E83DD89A2F73BBDD15E4C3CD757576DE37", oauth_nonce="1581261907284.49", oauth_signature="593wU44lEx2ewdTEyDi%2BOBYIjTs%3D", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1581261907", oauth_token="BDD0D8F4D1F869962A768A75B0A659A6", oauth_version="1.0"' 
}

# seek headers
curl -H 'Host: jobsearch-api-mobile.cloud.seek.com.au' -H 'X-Seek-iOS-App-Version: 2.50.1' -H 'Accept: */*' -H 'X-Seek-EC-SessionId: A9EA01F126934F41BDFAEA151B9213A7' -H 'User-Agent: seek/2.50.1 (com.seek.jobseeker; build:1196; iOS 13.3.0; iPhone10,2) Alamofire/4.8.1' -H 'Accept-Language: en-NZ;q=1.0' -H 'seek-client-context: ewogICJkZXZpY2UiIDogewogICAgIm1vZGVsIiA6ICJpUGhvbmUxMCwyIgogIH0sCiAgImNsaWVudCIgOiB7CiAgICAiY291bnRyeV9jb2RlIiA6ICJueiIsCiAgICAidmlzaXRvcklkIiA6ICI1QkREM0NGRTQzRTY0QzA4OUU5RkI5RTM1M0VBQTUwRCIsCiAgICAiYXBwX2luc3RhbGxfaWQiIDogIjVCREQzQ0ZFNDNFNjRDMDg5RTlGQjlFMzUzRUFBNTBEIgogIH0KfQ==' -H 'X-Request-Id: AE8AE424-BE7D-4FA8-88A6-C1E46C4DEE46' --compressed 'https://jobsearch-api-mobile.cloud.seek.com.au/search?Location=3001&Page=1&PageSize=20&SiteKey=nz&highlight=false&seekSelectAllPages=true&userid=5BDD3CFE43E64C089E9FB9E353EAA50D'

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

# jora headers
curl -H 'Host: au.jora.com' -H 'Cookie: __cfduid=dced998062b4054ec26a6ee5e250518ff1581654086' -H 'accept: */*' -H 'content-type: application/vnd.api+json' -H 'x-client-id: a177e89c1ed84ed147a0e60627fcbf0cc92d4b56542e77aa2aa947f15ea6955f' -H 'if-none-match: W/"87c20793d1e8843d69b503f95ec0dbf6"' -H 'x-device-id: 9956F20B-7726-4D07-B5FF-577A829F5A30' -H 'user-agent: Jora com.jora.Jobseeker/2.10.2 iOS/13.3 Apple/iPhone' -H 'accept-language: en-NZ;q=1.0' --compressed 'https://au.jora.com/api/v3/jobs/search?includeSponsoredJobs=true&keywords=&location=&onlyNew=false&siteId=au'

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