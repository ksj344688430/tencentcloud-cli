**Example 1: 修改雪碧图模板**



Input: 

```
tccli vod ModifyImageSpriteTemplate --cli-unfold-argument  \
    --Definition 10001 \
    --Name 雪碧图模板1 \
    --Width 128 \
    --Height 128 \
    --SampleType Percent \
    --SampleInterval 10 \
    --RowCount 5 \
    --ColumnCount 10
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

