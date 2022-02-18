import cv2
import datetime
import signal
import sys

# def quit(signum, frame):
#     print("ctrl c quit!")
#     sys.exit(0)


def auto_rec():
    url = "rtsp://admin:kdjfIEI_2837@192.168.50.64:554/h265/ch1/main/av_stream"
    cap = cv2.VideoCapture(url)
    log_file = open("F:\code\monitor\monitor.log", "a+")
    start_time = datetime.datetime.now()
    log_file.write("program start_time: {0}\n".format(start_time.strftime('%Y%m%d %H:%M:%S')))
    format_str_time = start_time.strftime('%Y%m%d-%H_%M_%S')
    end_time = start_time + datetime.timedelta(hours=6)
    log_file.write("program will end at: {0}\n".format(end_time.strftime('%Y%m%d %H:%M:%S')))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('F:\code\monitor\{0}.avi'.format(format_str_time), fourcc, 25.0, (1920,1080))
    ret, frame = cap.read()
    log_file.write("program will process loop\n")
    try:
        while ret:
            ret, frame = cap.read()
            # cv2.imshow("frame", frame)
            out.write(frame)
            diff = end_time - datetime.datetime.now()
            if diff.seconds == 0:
                log_file.write("program will break loop\n")
                log_file.write("cap.release\n")
                cap.release()
                log_file.write("out.release\n")
                out.release()
                log_file.write("destroyallwindows\n")
                cv2.destroyAllWindows()
                log_file.write("program run success! start_time: {0}  end_time: {1}\n".format(start_time.strftime('%Y%m%d %H:%M:%S'), datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
                log_file.write("\n")
                log_file.close()
                return True
            cv2.waitKey(9)
    except KeyboardInterrupt:
        log_file.write("program will break by exception\n")
        log_file.write("cap.release\n")
        cap.release()
        log_file.write("out.release\n")
        out.release()
        log_file.write("destroyallwindows\n")
        cv2.destroyAllWindows()
        log_file.write(
            "program run success! start_time: {0}  end_time: {1}\n".format(start_time.strftime('%Y%m%d %H:%M:%S'),
                                                                           datetime.datetime.now().strftime(
                                                                               '%Y%m%d %H:%M:%S')))
        log_file.write("\n")
        log_file.close()
        sys.exit(0)


if __name__ == '__main__':
    exec_flag = True
    # a = '1'
    # signal.signal(signal.SIGINT,quit)
    while exec_flag:
        exec_flag = auto_rec()
        # a = input("input:")
