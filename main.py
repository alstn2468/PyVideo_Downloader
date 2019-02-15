import os
import pytube

__author__ = '''
Kim Min Su
Soonchunhyang University
Department of CSE

Github : https://github.com/alstn2468
Blog : https://alstn2468.github.io
'''

try:
    yt = pytube.YouTube(input("Youtube 링크를 입력하세요 : "))
    stream = yt.streams \
                .filter(progressive=True,
                        file_extension="mp4") \
                .order_by('resolution') \
                .desc() \
                .first()

    select_video_title = yt.title
    title = input("저장할 이름을 입력하세요 : ")
    file_size = stream.filesize

    print("➤ 선택한 영상 제목\n  "
          + select_video_title
          + "\n➤ 저장할 영상 제목\n  "
          + title
          + "\n➤ 저장할 영상 크기\n  "
          +  str(file_size) + " bytes")

except Exception as ex:
    print("Error Occurrence \n"
          + str(ex))
