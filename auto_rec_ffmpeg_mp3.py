# coding=utf-8
import ffmpy3
import sys
import multiprocessing
import datetime
import os


URL = "rtsp://admin:QYJUPD@192.168.50.116:554/h265/ch1/main/av_stream"
PATH_LOG = r"F:\code\auto_rec_ffmpeg_video.log"
PATH_LOG_CONCAT = r"F:\code\auto_rec_ffmpeg_concat.log"
PATH_LOG_AUDIO = r"F:\code\auto_rec_ffmpeg_audio.log"
PATH_REC_FILES = r"F:\code\monitor"
CONCAT_FILES_LIST = r"F:\code\ffmpeg_concat_list.txt"


# 录制音频
def auto_rec_ffmpeg_audio(url, rec_path, log_path):
    log_file = open(log_path, "a+")
    log_file.write("start rec audio at {0}\n".format(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
    ff = ffmpy3.FFmpeg(
        inputs={url: '-t 00:00:10 -rtsp_transport tcp'},
        outputs={rec_path: '-map 0:1 -c:a:1 libmp3lame -y'}
    )
    log_file.write(ff.cmd)
    log_file.write("\n")
    ff.run(stdout=log_file, stderr=log_file)
    log_file.write("end rec audio at {0}\n".format(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
    log_file.write("\n")
    log_file.close()


# 录制视频
def auto_rec_ffmpeg_video(url, rec_path, log_path):
    log_file = open(log_path, "a+")
    log_file.write("start rec video at {0}\n".format(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
    ff = ffmpy3.FFmpeg(
        inputs={url: '-t 00:00:10 -rtsp_transport tcp'},
        outputs={rec_path: '-map 0:0 -c:v:0 libx265 -y'}
    )
    log_file.write(ff.cmd)
    log_file.write("\n")
    ff.run(stdout=log_file, stderr=log_file)
    log_file.write("end rec video at {0}\n".format(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
    log_file.write("\n")
    log_file.close()


# 删除合并前的文件
def del_rec(file_video, file_audio, log_path):
    log_file = open(log_path, "a+")
    log_file.write("start del files at {0}\n".format(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
    if os.path.exists(file_audio) and os.path.exists(file_video):
        os.unlink(file_audio)
        log_file.write("remove {0} file success!\n".format(file_audio))
        os.unlink(file_video)
        log_file.write("remove {0} file success!\n".format(file_video))
        log_file.write("end del files at {0}\n".format(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
        log_file.write("\n")
        log_file.close()
    else:
        log_file.write("remove failed!\n")
        log_file.write("quit by exception at {0}\n".format(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
        log_file.write("\n")
        log_file.close()


# 合并视频音频
def concat_mp4(file_video, file_audio, file_out, log_path):
    log_file = open(log_path, "a+")
    log_file.write("start concat video at {0}\n".format(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
    ff = ffmpy3.FFmpeg(
        inputs={file_video: None, file_audio: None},
        outputs={file_out: None}
    )
    log_file.write(ff.cmd)
    log_file.write("\n")
    ff.run(stdout=log_file, stderr=log_file)
    log_file.write("end concat {0} at {1}\n".format(file_out, datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
    log_file.write("\n")
    log_file.close()
    del_rec(file_video, file_audio, log_path)


if __name__ == '__main__':
    log_file_main = open(PATH_LOG, "a+")
    start_time = datetime.datetime.now()
    log_file_main.write("program start_time: {0}\n".format(start_time.strftime('%Y%m%d %H:%M:%S')))
    format_str_time = start_time.strftime('%Y%m%d-%H_%M_%S')
    path_video = r"{0}\{1}_pre.mp4".format(PATH_REC_FILES, format_str_time)
    path_audio = r"{0}\{1}_pre.mp3".format(PATH_REC_FILES, format_str_time)
    log_file_main.write("path pre: {0}  {1}\n".format(path_audio, path_video))
    concat_files_list = open(CONCAT_FILES_LIST, "w")  # 记录需要合并的两个文件的文件名，以便后面取出来直接合并
    concat_files_list.write("{0} {1}".format(path_video, path_audio))
    concat_files_list.close()
    process_video = multiprocessing.Process(target=auto_rec_ffmpeg_video, args=(URL, path_video, PATH_LOG))  # 多进程录制音频，视频
    process_audio = multiprocessing.Process(target=auto_rec_ffmpeg_audio, args=(URL, path_audio, PATH_LOG_AUDIO))
    log_file_main.write("program will process ffmpeg\n")
    log_file_main.close()
    process_video.start()
    process_audio.start()
    process_video.join()
    process_audio.join()
    log_file_main = open(PATH_LOG, "a+")
    read_pre_files = open(CONCAT_FILES_LIST, "r")  # 取出之前的文件绝对路径名
    file_video_main, file_audio_main = read_pre_files.readline().split()
    log_file_main.write("file pre:{0} {1}\n".format(file_audio_main, file_video_main))
    file_out_main = os.path.dirname(file_video_main)
    file_out_name = os.path.basename(file_video_main)[0:-8]
    log_file_main.write("file out base name:{0}\n".format(file_out_name))
    log_file_main.write("file out dir name:{0}\n".format(file_out_main))
    file_out_main = r"{0}\{1}_ret.mp4".format(file_out_main, file_out_name)
    log_file_main.write("file out main ret:{0}\n".format(file_out_main))
    read_pre_files.close()
    process_concat = multiprocessing.Process(target=concat_mp4, args=(file_video_main, file_audio_main, file_out_main,
                                                                      PATH_LOG_CONCAT))  # 合成文件并且删除合成前文件
    process_concat.start()
    log_file_main.write("program end at: {0}\n".format(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
    log_file.write("\n")
    log_file_main.close()
