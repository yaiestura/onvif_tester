import os
import subprocess

def start_stream(private_stream_url, output_dir, output_filename):
    cmd = ['ffmpeg',
        '-i', '"%s"' % private_stream_url,  
        '-ar', '44100', 
        '-acodec', 'aac', 
        '-ac', '1', 
        '-strict', '-2', 
        '-crf', '18', 
        '-c:v', 'copy', 
        '-preset', 'ultrafast', 
        '-flags', '-global_header', 
        '-fflags', 'flush_packets', 
        '-tune', 'zerolatency', 
        '-hls_time', '1', 
        '-hls_list_size', '3', 
        '-hls_wrap', '4', 
        '-hls_flags', 'delete_segments', 
        '-start_number', '0', 
        os.path.join(output_dir, output_filename),
        '>/dev/null 2>&1']

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    subprocess.Popen(' '.join(cmd), shell=True).pid


def stop_stream(ip, port):
    cam = '%s:%d' % (ip, port)
    cmd = ("for PID in $(ps -ax | grep -E 'ffmpeg.*%s' | awk '{ print $1 }');"
        " do kill -9 $PID >/dev/null 2>&1; done" % cam)
    subprocess.Popen(cmd, shell=True)



if __name__ == '__main__':
    private_stream_url = 'rtsp://admin:Supervisor@192.168.15.42:554/Streaming/Channels/101?transportmode=unicast&profile=Profile_1'
    output_dir = './streams'
    output_filename = '192.168.15.42:554_.m3u8'
    start_stream(private_stream_url, output_dir, output_filename)
    
