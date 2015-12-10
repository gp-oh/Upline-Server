from converter import Converter
import urllib2,urllib, uuid, os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import transaction
from boto.s3.connection import S3Connection, Bucket, Key
from django.conf import settings
from easy_thumbnails.files import get_thumbnailer
from mimetypes import MimeTypes
from PIL import Image

def convert_media(media):
    if media.media_type == 0:
        thumbnail_image(media)
    elif media.media_type == 1:
        convert_audio(media)
    elif media.media_type == 2:
        convert_video(media)

@transaction.atomic
def thumbnail_image(media):
    mime = MimeTypes()
    mime_type = mime.guess_type(media.media)
    image_name = media.media.split('/')[-1]
    urllib.urlretrieve(media.media, image_name)
    im1 = Image.open(image_name)    
    im1.thumbnail((400, 400), Image.ANTIALIAS)
    im1.save(image_name, "JPEG")
    im = open(image_name,'r')
    media.thumbnail = SimpleUploadedFile(name=str(uuid.uuid4())+image_name, content=im.read(), content_type=mime_type)
    media.converted = True
    media.save()
    os.unlink(image_name)

@transaction.atomic
def convert_audio(media):
    audio_name = media.media.split('/')[-1]
    audiofile = urllib2.urlopen(media.media)
    output = open(audio_name,'wb')
    output.write(audiofile.read())
    output.close()

    c = Converter()
    conv = c.convert(audio_name, audio_name.rsplit( ".", 1 )[ 0 ]+'1.mp3', {
        'format': 'mp3',
        'audio': {
            'codec': 'mp3'
        }})

    for timecode in conv:
        print "Converting (%f) ...\r" % timecode

    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    b = Bucket(conn, settings.AWS_STORAGE_BUCKET_NAME)
    k = Key(b)
    k.key = str(media.media.replace("https://upline-virtual.s3.amazonaws.com/",""))
    b.delete_key(k)

    k = Key(b)
    k.key = media.media.split('/')[-2]+"/"+audio_name.rsplit( ".", 1 )[ 0 ]+'.mp3'
    k.set_contents_from_filename(audio_name.rsplit( ".", 1 )[ 0 ]+'1.mp3')
    k.set_acl('public-read')


    media.converted = True
    media.media = "https://upline-virtual.s3.amazonaws.com/"+media.media.split('/')[-2]+"/"+audio_name.rsplit( ".", 1 )[ 0 ]+'.mp3'
    media.save()

    os.unlink(audio_name.rsplit( ".", 1 )[ 0 ]+'.mp3')
    os.unlink(audio_name)

@transaction.atomic
def convert_video(media):

    video_name = media.media.split('/')[-1]
    videofile = urllib2.urlopen(media.media)
    output = open(video_name,'wb')
    output.write(videofile.read())
    output.close()

    c = Converter()
    conv = c.convert(video_name, video_name.rsplit( ".", 1 )[ 0 ]+'1.mp4', {
        'format': 'mp4',
        'audio': {
            'codec': 'mp3'
        },
        'video': {
            'codec': 'h264'
        }})

    for timecode in conv:
        print "Converting (%f) ...\r" % timecode

    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    b = Bucket(conn, settings.AWS_STORAGE_BUCKET_NAME)
    k = Key(b)
    k.key = str(media.media.replace("https://upline-virtual.s3.amazonaws.com/",""))
    b.delete_key(k)

    k = Key(b)
    k.key = media.media.split('/')[-2]+"/"+video_name.rsplit( ".", 1 )[ 0 ]+'.mp4'
    k.set_contents_from_filename(video_name.rsplit( ".", 1 )[ 0 ]+'1.mp4')
    k.set_acl('public-read')


    c.thumbnail(video_name.rsplit( ".", 1 )[ 0 ]+'.mp4', 0, video_name.rsplit( ".", 1 )[ 0 ]+'.jpg')
    thumbnail_file = mp4_file = open(video_name.rsplit( ".", 1 )[ 0 ]+'.png','r')

    media.thumbnail = SimpleUploadedFile(name=str(uuid.uuid4())+'.jpg', content=thumbnail_file.read(), content_type='image/jpg')
    media.converted =True
    media.media = "https://upline-virtual.s3.amazonaws.com/"+media.media.split('/')[-2]+"/"+video_name.rsplit( ".", 1 )[ 0 ]+'.mp4'
    media.save()
    mp4_file.close()
    thumbnail_file.close()
    os.unlink(video_name.rsplit( ".", 1 )[ 0 ]+'1.mp4')
    os.unlink(video_name.rsplit( ".", 1 )[ 0 ]+'.jpg')
    os.unlink(video_name)
