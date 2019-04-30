# -*- coding: utf-8 -*-
DESC = "tbp-2019-03-11"
INFO = {
  "Reset": {
    "params": [
      {
        "name": "BotId",
        "desc": "机器人标识"
      },
      {
        "name": "UserId",
        "desc": "子账户id，每个终端对应一个"
      },
      {
        "name": "BotVersion",
        "desc": "机器人版本号。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev"
      },
      {
        "name": "BotEnv",
        "desc": "机器人环境{dev:测试;release:线上}。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev"
      }
    ],
    "desc": "对当前机器人的会话状态进行复位"
  },
  "PostText": {
    "params": [
      {
        "name": "BotId",
        "desc": "机器人标识"
      },
      {
        "name": "InputText",
        "desc": "请求的文本"
      },
      {
        "name": "UserId",
        "desc": "子账户id，每个终端对应一个"
      },
      {
        "name": "BotVersion",
        "desc": "机器人版本号。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev"
      },
      {
        "name": "SessionAttributes",
        "desc": "透传字段，传递给后台"
      },
      {
        "name": "NeedTts",
        "desc": "是否将机器人回答合成音频并返回url"
      },
      {
        "name": "Volume",
        "desc": "音量大小，范围：[0，10]。默认值为0，代表正常音量"
      },
      {
        "name": "Speed",
        "desc": "语速，范围：[-2，2]。0代表1.0倍"
      },
      {
        "name": "VoiceType",
        "desc": "音色,{0：女声,1:男声}"
      },
      {
        "name": "SampleRate",
        "desc": "返回音频的采样率{8k,16k}。默认16k"
      },
      {
        "name": "BotEnv",
        "desc": "机器人环境{dev:测试;release:线上}。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev"
      },
      {
        "name": "TtsVoiceFormat",
        "desc": "TTS合成音频格式，{0：wav}。该字段在当前版本仅支持取值为0。"
      }
    ],
    "desc": "机器人会话接口，接收文本信息，传递给后台机器人"
  },
  "PostAudio": {
    "params": [
      {
        "name": "BotId",
        "desc": "机器人标识"
      },
      {
        "name": "EngineModelType",
        "desc": "语音识别引擎类型,{8k_0、16k_0、16k_en}"
      },
      {
        "name": "AsrVoiceFormat",
        "desc": "输入音频文件编码格式。1：wav(pcm)；4：speex(sp)；6：silk"
      },
      {
        "name": "VoiceId",
        "desc": "asr请求Id。长度为16位的字符串，同一句话VoiceId保持一致"
      },
      {
        "name": "Seq",
        "desc": "语音分片序列号。同一句话必须从0开始，依次递增"
      },
      {
        "name": "IsEnd",
        "desc": "是否为尾包。传递最后一个语音分片时为true，其他为false"
      },
      {
        "name": "WaveData",
        "desc": "待识别音频字节流"
      },
      {
        "name": "UserId",
        "desc": "子账户id，每个终端对应一个"
      },
      {
        "name": "BotVersion",
        "desc": "机器人版本号。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev"
      },
      {
        "name": "ResultTextFormat",
        "desc": "识别返回文本编码格式\t0：UTF-8（默认）；1：GB2312；2：GBK；3：BIG5"
      },
      {
        "name": "SessionAttributes",
        "desc": "透传字段，传递给后台"
      },
      {
        "name": "NeedTts",
        "desc": "是否将机器人回答合成音频并返回url"
      },
      {
        "name": "Volume",
        "desc": "音量大小，范围：[0，10]。默认值为0，代表正常音量"
      },
      {
        "name": "Speed",
        "desc": "语速，范围：[-2，2]。0代表1.0倍"
      },
      {
        "name": "VoiceType",
        "desc": "音色,{0：女声,1:男声}"
      },
      {
        "name": "SampleRate",
        "desc": "返回音频的采样率{8k,16k}。默认16k"
      },
      {
        "name": "BotEnv",
        "desc": "机器人环境{dev:测试;release:线上}。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev"
      },
      {
        "name": "TtsVoiceFormat",
        "desc": "TTS合成音频格式，{0：wav}。该字段在当前版本仅支持取值为0。"
      }
    ],
    "desc": "机器人会话接口，接收音频信息，传递给后台机器人"
  }
}