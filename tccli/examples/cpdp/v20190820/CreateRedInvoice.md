**Example 1: CreateRedInvoice**



Input: 

```
tccli cpdp CreateRedInvoice --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --InvoicePlatformId 0 \
    --Invoices.0.OrderId test195992
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1585106019061",
        "Result": {
            "Message": "success",
            "Data": [
                {
                    "Message": "success",
                    "InvoiceId": "",
                    "OrderSn": "",
                    "Code": 0
                }
            ],
            "Code": 0
        }
    }
}
```

