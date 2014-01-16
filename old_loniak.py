#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import commands
import urllib
import random
from time import strftime
import time




INTERWAL=30 # seconds
MINPORT=10000
MAXPORT=10100
FOR_DOWNLOADDIR='/media/cryptex/www_cryptex/loniak/dump_point'
DOWNLOADEDDIR='/media/cryptex/www_cryptex/loniak/torrent_files'
OUTPUTDIR='/media/cryptex/www_cryptex/loniak/complete'
MAINLOG_PATH='/media/cryptex/www_cryptex/loniak/loniak.log'
CONFIG='/etc/loniak.conf'

log = open(MAINLOG_PATH,'a+')

PORT = random.randint(MINPORT, MAXPORT)


def turn_on_daemon():
    os.system('( deluge-web>/var/log/deluge.log)&')
    return;
    #os.system('( transmission-daemon --download-dir /media/cryptex/www_cryptex/loniak/complete --username loniak --password loniak --auth --port 6666 --incomplete-dir /media/cryptex/www_cryptex/loniak/incomplete -c /media/cryptex/www_cryptex/loniak/dump_point/ --allowed "*.*.*.*" )&')


def get_torrents():
    time = strftime("%Y-%m-%d %H:%M:%S")
    log.write(time+' Checking http://torrent.zoink.it/ for new torrents... \n')

    get_torrents_command = "lynx http://eztv.it/sort/100/ --dump"
    #get_torrents_command = "lynx http://thepiratebay.org/browse/205 --dump"


    torrents = commands.getoutput(get_torrents_command).replace("\n", ' ').split(" ")
    torrents = filter(lambda x: x.endswith('.torrent'), torrents)
    match = open(CONFIG).read().split("\n")
    match = filter(lambda x: x, match) # remove empty values
    #print match
    #print torrents
    torrents_list = set()

    for el in torrents:
        for reg in match:
            if reg in el:
                torrents_list.add(el)

    print torrents_list

    #let's download something random
    if random.randint(0,150) == 33:
        try:
            torrents_list.add( torrents[random.randint(0,len(torrents))] )
        except:
            pass

    for url in torrents_list:
        url = url.split(' ')
        url = url[-1]
        filename = url.split('/')
        filename = filename[-1]
        filename = urllib.unquote(filename)

        if os.path.isfile(DOWNLOADEDDIR+'/'+filename):
            print 'file '+ filename + ' is in the dir'
            pass
        else:
            os.system('wget \''+url+'\' -O \''+FOR_DOWNLOADDIR+'/'+filename+'\' >> '+MAINLOG_PATH+' 2>&1')
            print 'sciagam '+ url
    os.system('chmod 777 -R '+FOR_DOWNLOADDIR)

def download_torrents():
    time = strftime("%Y-%m-%d %H:%M:%S")
    log.write(time+' Looking for new torrents in :'+ FOR_DOWNLOADDIR + "\n")
    torrents = os.listdir(FOR_DOWNLOADDIR)
    #print torrents 

    for torrent in torrents:
        time = strftime("%Y-%m-%d %H:%M:%S")
        log.write(time+' Downloading:'+ torrent + "\n")
        #os.system( "mv \""+FOR_DOWNLOADDIR+'/'+torrent+"\" \""+DOWNLOADEDDIR+'/'+torrent +"\" >> "+MAINLOG_PATH + ' 2>&1')
        #log.write(time+" !! inicjuje log dla sciagania: http://pasazer.info/private/loniak/"+torrent+".log \n")
        #open(OUTPUTDIR+'/'+torrent+'.log','w')
        #os.chdir(OUTPUTDIR)
        #download_command = "(ctorrent \""+DOWNLOADEDDIR+"/"+torrent+"\" -e 0 -p "+str(PORT)+" -U 100 -S 192.168.1.100:6666 -X \"/home/sniku/loniak/smail.sh "+torrent+"\" >> \""+OUTPUTDIR+'/'+torrent+".log\" 2>&1 )&"
        #print download_command
        #os.system( download_command )

        commands.getoutput(' chmod 777 '+OUTPUTDIR+'/* -R ')
        #send_mail(torrent)

def send_mail(torrent):
    mail = open('/tmp/loniak.mail','w')
    mail.write(u'Sciagam plik '+torrent)
    mail.write(u"Log ze sciagania tego pliku mozesz na bierzaco ogladac tu:  http://pasazer.info/private/loniak/"+torrent+'.log'+"\n")
    mail.write(u"Log glowny loniaka:  http://pasazer.info/private/loniak/loniak.log\n")
    mail.write(u"Jak skoncze sciagac to plik bedzie do pobrania stad: http://pasazer.info/private/loniak/\n")
    mail.write(u"dostaniesz jeszcze jednego maila z potwierdzeniem sciagniecia pliku. \n")
    mail.write(u"Login: loniak Haslo: loniak. \n\n")

    mail.write(u"Pozdrawiam,\nTwoj loniak")
    mail.close() # close file

    emails = ['nale.sniku@gmail.com', 'rzepak@gmail.com']

    topic = "Loniak zaczal sciagac "+torrent

    for m in emails:
        log.write("Sending mail to "+ m + "\n")
        os.system("nail -A gmail -s '"+topic+"' "+m+" < /tmp/loniak.mail")

        #TODO: if torrent contains nupek, send to sad.manikin


##############
# exectution 
##############

#turn_on_ects()
turn_on_daemon()

while(True): # demon mode
    try:
        get_torrents()
        download_torrents()
        time.sleep(INTERWAL)
    except:
        pass
