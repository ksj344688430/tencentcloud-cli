**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveTranscodeRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "CreateTime": "2018-09-12 15:52:01",
                "UpdateTime": "2018-10-12 18:00:05",
                "TemplateId": 1000,
                "DomainName": "5000.livepush.myqcloud.com",
                "AppName": "live",
                "StreamName": "stream1"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

