**Example 1: 查询实时质量数据**



Input: 

```
tccli trtc DescribeRealtimeQuality --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --StartTime 1587879309 \
    --EndTime 1587882309
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Content": [
                    {
                        "Time": 1587879300,
                        "Value": 1
                    },
                    {
                        "Time": 1587879360,
                        "Value": 1
                    },
                    {
                        "Time": 1587879420,
                        "Value": 1
                    },
                    {
                        "Time": 1587879480,
                        "Value": 1
                    },
                    {
                        "Time": 1587879540,
                        "Value": 1
                    },
                    {
                        "Time": 1587879600,
                        "Value": 1
                    },
                    {
                        "Time": 1587879660,
                        "Value": 1
                    },
                    {
                        "Time": 1587879720,
                        "Value": 1
                    },
                    {
                        "Time": 1587879780,
                        "Value": 0.987342
                    },
                    {
                        "Time": 1587879840,
                        "Value": 0.971014
                    },
                    {
                        "Time": 1587879900,
                        "Value": 1
                    },
                    {
                        "Time": 1587879960,
                        "Value": 1
                    },
                    {
                        "Time": 1587880020,
                        "Value": 1
                    },
                    {
                        "Time": 1587880080,
                        "Value": 1
                    },
                    {
                        "Time": 1587880140,
                        "Value": 0.98
                    },
                    {
                        "Time": 1587880200,
                        "Value": 1
                    },
                    {
                        "Time": 1587880260,
                        "Value": 1
                    },
                    {
                        "Time": 1587880320,
                        "Value": 1
                    },
                    {
                        "Time": 1587880380,
                        "Value": 0.993151
                    },
                    {
                        "Time": 1587880440,
                        "Value": 1
                    },
                    {
                        "Time": 1587880500,
                        "Value": 1
                    },
                    {
                        "Time": 1587880560,
                        "Value": 1
                    },
                    {
                        "Time": 1587880620,
                        "Value": 1
                    },
                    {
                        "Time": 1587880680,
                        "Value": 1
                    },
                    {
                        "Time": 1587880740,
                        "Value": 0.993464
                    },
                    {
                        "Time": 1587880800,
                        "Value": 1
                    },
                    {
                        "Time": 1587880860,
                        "Value": 0.995261
                    },
                    {
                        "Time": 1587880920,
                        "Value": 0.994152
                    },
                    {
                        "Time": 1587880980,
                        "Value": 1
                    },
                    {
                        "Time": 1587881040,
                        "Value": 1
                    },
                    {
                        "Time": 1587881100,
                        "Value": 1
                    },
                    {
                        "Time": 1587881160,
                        "Value": 1
                    },
                    {
                        "Time": 1587881220,
                        "Value": 1
                    },
                    {
                        "Time": 1587881280,
                        "Value": 1
                    },
                    {
                        "Time": 1587881340,
                        "Value": 1
                    },
                    {
                        "Time": 1587881400,
                        "Value": 1
                    },
                    {
                        "Time": 1587881460,
                        "Value": 1
                    },
                    {
                        "Time": 1587881520,
                        "Value": 1
                    },
                    {
                        "Time": 1587881580,
                        "Value": 1
                    },
                    {
                        "Time": 1587881640,
                        "Value": 1
                    },
                    {
                        "Time": 1587881700,
                        "Value": 1
                    },
                    {
                        "Time": 1587881760,
                        "Value": 1
                    },
                    {
                        "Time": 1587881820,
                        "Value": 1
                    },
                    {
                        "Time": 1587881880,
                        "Value": 1
                    },
                    {
                        "Time": 1587881940,
                        "Value": 1
                    },
                    {
                        "Time": 1587882000,
                        "Value": 0.990385
                    },
                    {
                        "Time": 1587882060,
                        "Value": 1
                    },
                    {
                        "Time": 1587882120,
                        "Value": 0.984127
                    },
                    {
                        "Time": 1587882180,
                        "Value": 1
                    },
                    {
                        "Time": 1587882240,
                        "Value": 1
                    }
                ],
                "DataType": "enterTotalSuccPercent"
            },
            {
                "Content": [
                    {
                        "Time": 1587879300,
                        "Value": 0.675676
                    },
                    {
                        "Time": 1587879360,
                        "Value": 0.846154
                    },
                    {
                        "Time": 1587879420,
                        "Value": 0.813953
                    },
                    {
                        "Time": 1587879480,
                        "Value": 0.744681
                    },
                    {
                        "Time": 1587879540,
                        "Value": 0.821429
                    },
                    {
                        "Time": 1587879600,
                        "Value": 0.711538
                    },
                    {
                        "Time": 1587879660,
                        "Value": 0.79661
                    },
                    {
                        "Time": 1587879720,
                        "Value": 0.736842
                    },
                    {
                        "Time": 1587879780,
                        "Value": 0.745098
                    },
                    {
                        "Time": 1587879840,
                        "Value": 0.816667
                    },
                    {
                        "Time": 1587879900,
                        "Value": 0.666667
                    },
                    {
                        "Time": 1587879960,
                        "Value": 0.847826
                    },
                    {
                        "Time": 1587880020,
                        "Value": 0.814815
                    },
                    {
                        "Time": 1587880080,
                        "Value": 0.734694
                    },
                    {
                        "Time": 1587880140,
                        "Value": 0.846154
                    },
                    {
                        "Time": 1587880200,
                        "Value": 0.809524
                    },
                    {
                        "Time": 1587880260,
                        "Value": 0.693548
                    },
                    {
                        "Time": 1587880320,
                        "Value": 0.774194
                    },
                    {
                        "Time": 1587880380,
                        "Value": 0.74026
                    },
                    {
                        "Time": 1587880440,
                        "Value": 0.869565
                    },
                    {
                        "Time": 1587880500,
                        "Value": 0.851064
                    },
                    {
                        "Time": 1587880560,
                        "Value": 0.842105
                    },
                    {
                        "Time": 1587880620,
                        "Value": 0.7125
                    },
                    {
                        "Time": 1587880680,
                        "Value": 0.775
                    },
                    {
                        "Time": 1587880740,
                        "Value": 0.742857
                    },
                    {
                        "Time": 1587880800,
                        "Value": 0.786517
                    },
                    {
                        "Time": 1587880860,
                        "Value": 0.733333
                    },
                    {
                        "Time": 1587880920,
                        "Value": 0.813725
                    },
                    {
                        "Time": 1587880980,
                        "Value": 0.759036
                    },
                    {
                        "Time": 1587881040,
                        "Value": 0.770115
                    },
                    {
                        "Time": 1587881100,
                        "Value": 0.846154
                    },
                    {
                        "Time": 1587881160,
                        "Value": 0.77686
                    },
                    {
                        "Time": 1587881220,
                        "Value": 0.706667
                    },
                    {
                        "Time": 1587881280,
                        "Value": 0.719101
                    },
                    {
                        "Time": 1587881340,
                        "Value": 0.74359
                    },
                    {
                        "Time": 1587881400,
                        "Value": 0.753846
                    },
                    {
                        "Time": 1587881460,
                        "Value": 0.764706
                    },
                    {
                        "Time": 1587881520,
                        "Value": 0.696429
                    },
                    {
                        "Time": 1587881580,
                        "Value": 0.685714
                    },
                    {
                        "Time": 1587881640,
                        "Value": 0.763636
                    },
                    {
                        "Time": 1587881700,
                        "Value": 0.736842
                    },
                    {
                        "Time": 1587881760,
                        "Value": 0.802632
                    },
                    {
                        "Time": 1587881820,
                        "Value": 0.642857
                    },
                    {
                        "Time": 1587881880,
                        "Value": 0.671053
                    },
                    {
                        "Time": 1587881940,
                        "Value": 0.714286
                    },
                    {
                        "Time": 1587882000,
                        "Value": 0.776471
                    },
                    {
                        "Time": 1587882060,
                        "Value": 0.72
                    },
                    {
                        "Time": 1587882120,
                        "Value": 0.768293
                    },
                    {
                        "Time": 1587882180,
                        "Value": 0.736111
                    },
                    {
                        "Time": 1587882240,
                        "Value": 0.829268
                    }
                ],
                "DataType": "fistFreamInSecRate"
            },
            {
                "Content": [
                    {
                        "Time": 1587879300,
                        "Value": 0.0516673
                    },
                    {
                        "Time": 1587879360,
                        "Value": 0.0420073
                    },
                    {
                        "Time": 1587879420,
                        "Value": 0.0164823
                    },
                    {
                        "Time": 1587879480,
                        "Value": 0.0172463
                    },
                    {
                        "Time": 1587879540,
                        "Value": 0.03537
                    },
                    {
                        "Time": 1587879600,
                        "Value": 0.0170948
                    },
                    {
                        "Time": 1587879660,
                        "Value": 0.0238174
                    },
                    {
                        "Time": 1587879720,
                        "Value": 0.0263193
                    },
                    {
                        "Time": 1587879780,
                        "Value": 0.0263528
                    },
                    {
                        "Time": 1587879840,
                        "Value": 0.021749
                    },
                    {
                        "Time": 1587879900,
                        "Value": 0.0204263
                    },
                    {
                        "Time": 1587879960,
                        "Value": 0.0641088
                    },
                    {
                        "Time": 1587880020,
                        "Value": 0.0582364
                    },
                    {
                        "Time": 1587880080,
                        "Value": 0.00673699
                    },
                    {
                        "Time": 1587880140,
                        "Value": 0.0392587
                    },
                    {
                        "Time": 1587880200,
                        "Value": 0.00982329
                    },
                    {
                        "Time": 1587880260,
                        "Value": 0.0157532
                    },
                    {
                        "Time": 1587880320,
                        "Value": 0.0281576
                    },
                    {
                        "Time": 1587880380,
                        "Value": 0.0577111
                    },
                    {
                        "Time": 1587880440,
                        "Value": 0.0528128
                    },
                    {
                        "Time": 1587880500,
                        "Value": 0.0229709
                    },
                    {
                        "Time": 1587880560,
                        "Value": 0.0121996
                    },
                    {
                        "Time": 1587880620,
                        "Value": 0.0480692
                    },
                    {
                        "Time": 1587880680,
                        "Value": 0.0403535
                    },
                    {
                        "Time": 1587880740,
                        "Value": 0.027401
                    },
                    {
                        "Time": 1587880800,
                        "Value": 0.0207513
                    },
                    {
                        "Time": 1587880860,
                        "Value": 0.0233762
                    },
                    {
                        "Time": 1587880920,
                        "Value": 0.024576
                    },
                    {
                        "Time": 1587880980,
                        "Value": 0.0743958
                    },
                    {
                        "Time": 1587881040,
                        "Value": 0.0786275
                    },
                    {
                        "Time": 1587881100,
                        "Value": 0.0170895
                    },
                    {
                        "Time": 1587881160,
                        "Value": 0.0429576
                    },
                    {
                        "Time": 1587881220,
                        "Value": 0.0378077
                    },
                    {
                        "Time": 1587881280,
                        "Value": 0.0317765
                    },
                    {
                        "Time": 1587881340,
                        "Value": 0.0627094
                    },
                    {
                        "Time": 1587881400,
                        "Value": 0.0580849
                    },
                    {
                        "Time": 1587881460,
                        "Value": 0.0480873
                    },
                    {
                        "Time": 1587881520,
                        "Value": 0.112652
                    },
                    {
                        "Time": 1587881580,
                        "Value": 0.0830964
                    },
                    {
                        "Time": 1587881640,
                        "Value": 0.0214749
                    },
                    {
                        "Time": 1587881700,
                        "Value": 0.0213392
                    },
                    {
                        "Time": 1587881760,
                        "Value": 0.0338993
                    },
                    {
                        "Time": 1587881820,
                        "Value": 0.0248327
                    },
                    {
                        "Time": 1587881880,
                        "Value": 0.0643011
                    },
                    {
                        "Time": 1587881940,
                        "Value": 0.0367101
                    },
                    {
                        "Time": 1587882000,
                        "Value": 0.0114235
                    },
                    {
                        "Time": 1587882060,
                        "Value": 0.0237085
                    },
                    {
                        "Time": 1587882120,
                        "Value": 0.048085
                    },
                    {
                        "Time": 1587882180,
                        "Value": 0.0338324
                    },
                    {
                        "Time": 1587882240,
                        "Value": 0.0390847
                    }
                ],
                "DataType": "blockPercent"
            },
            {
                "Content": [
                    {
                        "Time": 1587879300,
                        "Value": 0.0100244
                    },
                    {
                        "Time": 1587879360,
                        "Value": 0.00389113
                    },
                    {
                        "Time": 1587879420,
                        "Value": 0.00540931
                    },
                    {
                        "Time": 1587879480,
                        "Value": 0.00457188
                    },
                    {
                        "Time": 1587879540,
                        "Value": 0.00858422
                    },
                    {
                        "Time": 1587879600,
                        "Value": 0.00493737
                    },
                    {
                        "Time": 1587879660,
                        "Value": 0.00737031
                    },
                    {
                        "Time": 1587879720,
                        "Value": 0.00932698
                    },
                    {
                        "Time": 1587879780,
                        "Value": 0.00293782
                    },
                    {
                        "Time": 1587879840,
                        "Value": 0.00384333
                    },
                    {
                        "Time": 1587879900,
                        "Value": 0.00504729
                    },
                    {
                        "Time": 1587879960,
                        "Value": 0.00563395
                    },
                    {
                        "Time": 1587880020,
                        "Value": 0.0109955
                    },
                    {
                        "Time": 1587880080,
                        "Value": 0.00541831
                    },
                    {
                        "Time": 1587880140,
                        "Value": 0.00346741
                    },
                    {
                        "Time": 1587880200,
                        "Value": 0.00411463
                    },
                    {
                        "Time": 1587880260,
                        "Value": 0.00537389
                    },
                    {
                        "Time": 1587880320,
                        "Value": 0.00463891
                    },
                    {
                        "Time": 1587880380,
                        "Value": 0.0072554
                    },
                    {
                        "Time": 1587880440,
                        "Value": 0.00224726
                    },
                    {
                        "Time": 1587880500,
                        "Value": 0.00543683
                    },
                    {
                        "Time": 1587880560,
                        "Value": 0.00314986
                    },
                    {
                        "Time": 1587880620,
                        "Value": 0.00601674
                    },
                    {
                        "Time": 1587880680,
                        "Value": 0.00976329
                    },
                    {
                        "Time": 1587880740,
                        "Value": 0.00532366
                    },
                    {
                        "Time": 1587880800,
                        "Value": 0.00364146
                    },
                    {
                        "Time": 1587880860,
                        "Value": 0.00700881
                    },
                    {
                        "Time": 1587880920,
                        "Value": 0.0043198
                    },
                    {
                        "Time": 1587880980,
                        "Value": 0.00640316
                    },
                    {
                        "Time": 1587881040,
                        "Value": 0.0157437
                    },
                    {
                        "Time": 1587881100,
                        "Value": 0.0120293
                    },
                    {
                        "Time": 1587881160,
                        "Value": 0.0136746
                    },
                    {
                        "Time": 1587881220,
                        "Value": 0.00640311
                    },
                    {
                        "Time": 1587881280,
                        "Value": 0.00571906
                    },
                    {
                        "Time": 1587881340,
                        "Value": 0.010903
                    },
                    {
                        "Time": 1587881400,
                        "Value": 0.0100748
                    },
                    {
                        "Time": 1587881460,
                        "Value": 0.00638894
                    },
                    {
                        "Time": 1587881520,
                        "Value": 0.00475456
                    },
                    {
                        "Time": 1587881580,
                        "Value": 0.0058012
                    },
                    {
                        "Time": 1587881640,
                        "Value": 0.00588038
                    },
                    {
                        "Time": 1587881700,
                        "Value": 0.00419676
                    },
                    {
                        "Time": 1587881760,
                        "Value": 0.00325692
                    },
                    {
                        "Time": 1587881820,
                        "Value": 0.00713454
                    },
                    {
                        "Time": 1587881880,
                        "Value": 0.0284122
                    },
                    {
                        "Time": 1587881940,
                        "Value": 0.00933655
                    },
                    {
                        "Time": 1587882000,
                        "Value": 0.0047432
                    },
                    {
                        "Time": 1587882060,
                        "Value": 0.00462398
                    },
                    {
                        "Time": 1587882120,
                        "Value": 0.0149698
                    },
                    {
                        "Time": 1587882180,
                        "Value": 0.00340317
                    },
                    {
                        "Time": 1587882240,
                        "Value": 0.00511883
                    }
                ],
                "DataType": "audioBlockPercent"
            }
        ],
        "RequestId": "56b89272-cdff-46a3-a399-87ec6f209b53"
    }
}
```

