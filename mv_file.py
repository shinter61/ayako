import shutil
import os

def copy_specific_files(source_dir, destination_dir):
    # ディレクトリ内のファイルを取得
    files = os.listdir(source_dir)

    # 移動させたいファイル名の配列を作成
    target_filename_arr = []
    for i in range (1, 11):
        if (i % 5 == 0):
            target_filename_arr.append('A{}.txt'.format(i))

    print(target_filename_arr)

    for file in files:
        print(file)
        # 特定の拡張子のファイルだけをコピー
        if file in target_filename_arr:
            source_path = os.path.join(source_dir, file)
            destination_path = os.path.join(destination_dir, file)
            
            # ファイルをコピー
            shutil.copy2(source_path, destination_path)
            print(f'コピー完了: {file}')

# 使用例
source_directory = './sample_data/'  # ここを実際のディレクトリに変更
destination_directory = './result'  # ここを実際のディレクトリに変更

copy_specific_files(source_directory, destination_directory)

