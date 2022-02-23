import cv2
import datetime
import sys
import queue
import multiprocessing as mp

URL = "rtsp://admin:QYJUPD@192.168.50.116:554/h265/ch1/main/av_stream"
PATH_LOG_RECEIVE = r"F:\code\monitor\monitor_ys_multi_receive.log"
PATH_LOG_OUT = r"F:\code\monitor\monitor_ys_multi_out.log"
PATH_OUT_FILE = r"F:\code\monitor"


def receive(q):
    log_file = open(PATH_LOG_RECEIVE, "a+")
    start_time = datetime.datetime.now()
    log_file.write("receive start_time: {0}\n".format(start_time.strftime('%Y%m%d %H:%M:%S')))
    end_time = start_time + datetime.timedelta(hours=6)
    cap = cv2.VideoCapture(URL)
    ret, frame = cap.read()
    q.put(frame)
    while ret:
        ret, frame = cap.read()
        q.put(frame)
        diff = end_time - datetime.datetime.now()
        if diff.seconds == 0:
            q.put(-1)
            log_file.write("receive will break loop\n")
            log_file.write("cap.release\n")
            cap.release()
            log_file.write("receive run success! start_time: {0}  end_time: {1}\n".format(start_time.strftime('%Y%m%d %H:%M:%S'), datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
            log_file.write("\n")
            log_file.close()
            break


def out_file(q):
    log_file = open(PATH_LOG_OUT, "a+")
    start_time = datetime.datetime.now()
    log_file.write("out start_time: {0}\n".format(start_time.strftime('%Y%m%d %H:%M:%S')))
    format_str_time = start_time.strftime('%Y%m%d-%H_%M_%S')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("{0}\{1}_ys_multi.avi".format(PATH_OUT_FILE, format_str_time), fourcc, 20.0, (1920, 1080))
    while True:
        if not q.empty():
            out_frame = q.get()
            if isinstance(out_frame, int):
                log_file.write("out_file will break loop\n")
                log_file.write("out.release\n")
                out.release()
                log_file.write("destroy all windows\n")
                cv2.destroyAllWindows()
                log_file.write("out_file run success! start_time: {0}  end_time: {1}\n".format(start_time.strftime('%Y%m%d %H:%M:%S'), datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
                log_file.write("\n")
                log_file.close()
                break
            else:
                out.write(out_frame)


if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=receive, args=(q,))
    p2 = mp.Process(target=out_file, args=(q,))
    p1.start()
    p2.start()
