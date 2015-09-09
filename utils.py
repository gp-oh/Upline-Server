from converter import Converter
import urllib2, uuid, os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import transaction
from boto.s3.connection import S3Connection, Bucket, Key
from django.conf import settings

@transaction.atomic
def convert_audio(audio):
    audio_name = audio.audio.url.split('/')[-1]
    audiofile = urllib2.urlopen(audio.audio.url)
    output = open(audio_name,'wb')
    output.write(audiofile.read())
    output.close()

    c = Converter()
    conv = c.convert(audio_name, audio_name.rsplit( ".", 1 )[ 0 ]+'.mp3', {
        'format': 'mp3',
        'audio': {
            'codec': 'mp3',
            'samplerate': 11025,
            'channels': 1
        }})

    for timecode in conv:
        print "Converting (%f) ...\r" % timecode

    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    b = Bucket(conn, settings.AWS_STORAGE_BUCKET_NAME)
    k = Key(b)
    k.key = str(audio.audio)
    b.delete_key(k)

    mp3_file = open(audio_name.rsplit( ".", 1 )[ 0 ]+'.mp3','r')
    audio.audio = SimpleUploadedFile(name=str(uuid.uuid4())+'.mp3', content=mp3_file.read(), content_type='audio/mpeg3')
    audio.conevrted = True
    audio.save()
    mp3_file.close()
    os.unlink(audio_name.rsplit( ".", 1 )[ 0 ]+'.mp3')
    os.unlink(audio_name)

@transaction.atomic
def convert_video(video):

    video_name = video.video.url.split('/')[-1]
    videofile = urllib2.urlopen(video.video.url)
    output = open(video_name,'wb')
    output.write(videofile.read())
    output.close()

    c = Converter()
    conv = c.convert(video_name, video_name.rsplit( ".", 1 )[ 0 ]+'.mp4', {
        'format': 'mp4',
        'audio': {
            'codec': 'mp3',
            'samplerate': 11025,
            'channels': 1
        },
        'video': {
            'codec': 'h264',
        }})

    for timecode in conv:
        print "Converting (%f) ...\r" % timecode

    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    b = Bucket(conn, settings.AWS_STORAGE_BUCKET_NAME)
    k = Key(b)
    k.key = str(video.video)
    b.delete_key(k)

    mp4_file = open(video_name.rsplit( ".", 1 )[ 0 ]+'.mp4','r')

    c.thumbnail(video_name.rsplit( ".", 1 )[ 0 ]+'.mp4', 10, video_name.rsplit( ".", 1 )[ 0 ]+'.png')
    thumbnail_file = mp4_file = open(video_name.rsplit( ".", 1 )[ 0 ]+'.png','r')

    video.video = SimpleUploadedFile(name=str(uuid.uuid4())+'.mp4', content=mp4_file.read(), content_type='video/mp4')
    video.thumbnail = SimpleUploadedFile(name=str(uuid.uuid4())+'.png', content=thumbnail_file.read(), content_type='image/png')
    video.save()
    mp4_file.close()
    thumbnail_file.close()
    os.unlink(video_name.rsplit( ".", 1 )[ 0 ]+'.mp4')
    os.unlink(video_name.rsplit( ".", 1 )[ 0 ]+'.png')
    os.unlink(video_name)
