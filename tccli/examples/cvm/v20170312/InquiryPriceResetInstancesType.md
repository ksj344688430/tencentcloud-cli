**Example 1: 包年包月实例调整配置询价**



Input: 

```
tccli cvm InquiryPriceResetInstancesType --cli-unfold-argument  \
    --InstanceIds ins-2zvpghhc \
    --InstanceType S5.16XLARGE256
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": "67.33",
                "DiscountPrice": "67.33",
                "Discount": 100
            }
        },
        "RequestId": "d9f36a23-7bc4-4f02-99c5-00b4a77431df"
    }
}
```

