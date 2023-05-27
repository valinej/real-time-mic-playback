import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# 定义参数
FORMAT = pyaudio.paInt16  # 输入音频的格式为16位整数
CHANNELS = 1  # 单声道
RATE = 44100  # 采样率为44100Hz
CHUNK = 256   # 每个缓冲区的帧数

# 初始化PyAudio
p = pyaudio.PyAudio()

# 创建一个音量增益系数
volume_gain = 2.0  # 音量增益倍数

# 打开麦克风进行录制
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# 打开扬声器进行播放
output_stream = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       output=True,
                       frames_per_buffer=CHUNK)

# 实时录制和播放音频数据
print("开始录制和播放...")
while True:
    # 从麦克风读取音频数据
    data = stream.read(CHUNK)

    # 将音频数据转换为NumPy数组
    audio_array = np.frombuffer(data, dtype=np.int16)

    # 增大音量
    amplified_audio = audio_array * volume_gain

    # 将增大音量后的音频数据转换为字节流
    amplified_data = amplified_audio.astype(np.int16).tobytes()

    # 播放增大音量后的音频数据
    output_stream.write(amplified_data)

    # 可以在这里对音频数据进行处理或分析
    # 例如，可以使用matplotlib绘制音频波形图
    '''
    plt.plot(audio_array)
    plt.show(block=False)
    plt.pause(0.001)
    plt.clf()
    '''

# 停止录制和播放
stream.stop_stream()
stream.close()
output_stream.stop_stream()
output_stream.close()

# 关闭PyAudio
p.terminate()
