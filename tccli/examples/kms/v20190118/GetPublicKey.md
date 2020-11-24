**Example 1: 获取非对称密钥的公钥。**



Input: 

```
tccli kms GetPublicKey --cli-unfold-argument  \
    --KeyId 554ef4b3-3071-11ea-a86a-5254006d0810
```

Output: 
```
{
    "Response": {
        "RequestId": "8918bd5b-e189-4e2d-b718-01c9f99acd45",
        "KeyId": "554ef4b3-3071-11ea-a86a-5254006d0810",
        "PublicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAz0OTVMh28VCjOE5DMlBM8a2qIjgipYByb7WE/GyTRLUiIGDUq44VIM5fNI9nVeIf2D+4pIiU0s4LUYnLxkGcFKUVWkz3nubUzbNdSHRbNjKhbFyyRGT6YYxqMfvCmNXMA3OE56EmvsWU9VwVXqRPOFTaODCx8bRd+R6O+Aho9GaRfwLKHtlX7dochdDs9SWC6iybRISgpLEh4tvzcSlBemEuyx5U/X/BoL+sVnSsC/XT8J9w0EvJVHZaBW7OhIbBOolhzWTF8TpL/7ncZZUbtfP4SrAkvKgoEIEfRhv5vh5LfSxiS2zQzIShrT6JYqh5IgDIHTdCcPiYmTsk/lmM2wIDAQAB",
        "PublicKeyPem": "-----BEGIN PUBLIC KEY-----\nTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUF6ME9U\nVk1oMjhWQ2pPRTVETWxCTThhMnFJamdpcFlCeWI3V0UvR3lUUkxVaUlHRFVxNDRW\nSU01Zk5JOW5WZUlmMkQrNHBJaVUwczRMVVluTHhrR2NGS1VWV2t6M251YlV6Yk5k\nU0hSYk5qS2hiRnl5UkdUNllZeHFNZnZDbU5YTUEzT0U1NkVtdnNXVTlWd1ZYcVJQ\nT0ZUYU9EQ3g4YlJkK1I2TytBaG85R2FSZndMS0h0bFg3ZG9jaGREczlTV0M2aXli\nUklTZ3BMRWg0dHZ6Y1NsQmVtRXV5eDVVL1gvQm9MK3NWblNzQy9YVDhKOXcwRXZK\nVkhaYUJXN09oSWJCT29saHpXVEY4VHBMLzduY1paVWJ0ZlA0U3JBa3ZLZ29FSUVm\nUmh2NXZoNUxmU3hpUzJ6UXpJU2hyVDZKWXFoNUlnRElIVGRDY1BpWW1Uc2svbG1N\nMndJREFRQUI=\n-----END PUBLIC KEY-----\n"
    }
}
```
