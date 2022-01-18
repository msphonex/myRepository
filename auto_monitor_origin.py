import cv2
import datetime

# url = "rtsp://admin:kdjfIEI_2837@192.168.0.64/Streaming/Channels/2"
url = "rtsp://admin:kdjfIEI_2837@192.168.50.64:554/h265/ch1/main/av_stream"
cap = cv2.VideoCapture(url)
log_file = open("F:\code\monitor\monitor.log", "a+")
# print (cap.isOpened())
# cv2.namedWindow("frame", 0)
# cv2.resizeWindow("frame", 1280, 720)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
# cap.set(cv2.CAP_PROP_FPS,25.0)
# cap.set(5,25.0)
# cap.set(3,1920)
# cap.set(4,1080)
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# fourcc_org = cap.get(cv2.CAP_PROP_FOURCC)
# print("fps:",fps,"\twidth:",width, "\theight:",height, "\tfourcc:", fourcc_org)
start_time = datetime.datetime.now()
log_file.write("program start_time: {0}\n".format(start_time.strftime('%Y%m%d %H:%M:%S')))
format_str_time = start_time.strftime('%Y%m%d-%H_%M_%S')
end_time = start_time + datetime.timedelta(hours=6)
log_file.write("program will end at: {0}\n".format(end_time.strftime('%Y%m%d %H:%M:%S')))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('F:\code\monitor\{0}.avi'.format(format_str_time), fourcc, 25.0, (1920,1080))
ret, frame = cap.read()
log_file.write("program will process loop\n")
while ret:
    ret, frame = cap.read()
    # cv2.imshow("frame", frame)
    out.write(frame)
    diff = end_time - datetime.datetime.now()
    if diff.seconds == 0:
        log_file.write("program will break loop\n")
        break
    # if cv2.waitKey(10) & 0xFF == ord('q'):
    #     break
    cv2.waitKey(10)
log_file.write("program run success! start_time: {0}  end_time: {1}\n".format(start_time.strftime('%Y%m%d %H:%M:%S'), datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')))
log_file.close()
cap.release()
out.release()
cv2.destroyAllWindows()
# end_time = datetime.datetime.now()
# duration = end_time - start_time
# print("start_time:", start_time, "\tend_time:", end_time, "\tduration:", duration.seconds)