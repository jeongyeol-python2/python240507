# 파이썬을 사용해서 윈도우의 다운로드된 폴더에서 
# *.jpg, *jpeg를 \images폴더로 이동, *.csv, *.xls,*.xlsx파일은 \data 폴더로 *.txt, *.doc, *.pdf는 \docs 폴더로 *.zip 은 \archive폴더로 이동하는 코드를 생성해줘. 
# 해당 폴더가 없으면 폴더를 생성해야하고 윈도우 다운로드 폴더는 C:\Users\son\Downloads 야

import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\son\Downloads'

# 이동할 폴더 경로 설정
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 폴더가 없으면 생성
for folder in [image_folder, data_folder, docs_folder, archive_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 다운로드 폴더 내 파일들을 확인하고 분류하여 이동
for filename in os.listdir(download_folder):
    if filename.lower().endswith(('.jpg', '.jpeg')):
        shutil.move(os.path.join(download_folder, filename), image_folder)
    elif filename.lower().endswith(('.csv', '.xls', '.xlsx')):
        shutil.move(os.path.join(download_folder, filename), data_folder)
    elif filename.lower().endswith(('.txt', '.doc', '.pdf')):
        shutil.move(os.path.join(download_folder, filename), docs_folder)
    elif filename.lower().endswith('.zip'):
        shutil.move(os.path.join(download_folder, filename), archive_folder)

print("파일 분류 및 이동이 완료되었습니다.")
