import os
from pydub import AudioSegment


def convert_flac_to_wav(flac_file_path, wav_file_path):
    # 加载 FLAC 文件
    audio = AudioSegment.from_file(flac_file_path, format="flac")

    # 将音频文件转换为 WAV 格式
    audio.export(wav_file_path, format="wav")


def batch_convert_flac_to_wav(folder_path):
    # 遍历指定文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        # 检查文件是否为 FLAC 文件
        if file_name.endswith('.flac'):
            flac_file_path = os.path.join(folder_path, file_name)
            wav_file_path = os.path.join(folder_path, file_name[:-5] + '.wav')
            convert_flac_to_wav(flac_file_path, wav_file_path)
            print(f"Converted: {flac_file_path} to {wav_file_path}")


if __name__ == '__main__':
    path = '/Users/cheolhwilee/Downloads/converter'  # 替换为你的 FLAC 文件所在的文件夹路径
    batch_convert_flac_to_wav(path)

