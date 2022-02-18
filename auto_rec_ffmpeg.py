import ffmpy3

ff = ffmpy3.FFmpeg(
    inputs={'rtsp://admin:QYJUPD@192.168.50.116:554/h265/ch1/main/av_stream': '-rtsp_transport tcp -t 60'},
    outputs={r'F:\code\monitor\test.mp4': '-map 0:0 -c:v:0 libx265 -y'}
)
print(ff.cmd)
ff.run()
