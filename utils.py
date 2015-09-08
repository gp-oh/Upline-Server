from converter import Converter

def convert_audio(audio):
    c = Converter()
    conv = c.convert(audio, audio.rsplit( ".", 1 )[ 0 ]+'.mp3', {
        'format': 'mp3',
        'audio': {
            'codec': 'mp3',
            'samplerate': 11025,
            'channels': 1
        }})

    for timecode in conv:
        print "Converting (%f) ...\r" % timecode

def convert_video(video):
    c = Converter()
    conv = c.convert(video, video.rsplit( ".", 1 )[ 0 ]+'.mp4', {
        'format': 'mp4',
        'video': {
            'codec': 'h264',
        }})

    for timecode in conv:
        print "Converting (%f) ...\r" % timecode

    c.thumbnail(video.rsplit( ".", 1 )[ 0 ]+'.mp4', 10, video.rsplit( ".", 1 )[ 0 ]+'.png')