#!/usr/bin/python
# -*- coding: utf-8 -*-

# Module importieren
import os
import sys
import curses

def tune_in(text, url):
  os.system('killall mplayer')
  ansage(text)
  play(url)

def play(url):
  os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 ' + url + ' < /dev/null > /dev/null &')	

def ansage(text):
  play('~/internet_radio/ansagen/' + text + '.mp3')

#Lautstaerke setzen
volume = 50 
os.system('amixer set Master ' + str(volume))
# Curses Modus starten
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
# Standardsender OE1
tune_in('oe1', 'http://mp3stream3.apasf.apa.at:8000')

# Texthilfe
pad = curses.newpad(30,10)

while True:
  c = stdscr.getch()

# lauter	
  if c == curses.KEY_RIGHT:
      if volume < 80:
        volume = volume + 5
        ansage('lauter')
        os.system('amixer set Master ' + str(volume))
# leister			
  elif c == curses.KEY_DOWN:
      if volume > 0:		
        volume = volume - 5
        ansage('leiser')
        os.system('amixer set Master ' + str(volume))
# Sender je nach gedrueckter Taste abspielen			
  elif c == ord('1'):
    tune_in('oe1', 'http://mp3stream3.apasf.apa.at:8000')
  elif c == ord('2'):
    tune_in('radio_wien', '-playlist https://oe2wshoutcast.sf.apa.at/listen.pls')
  elif c == ord('3'):
    tune_in('oe3', '-playlist http://mp3stream7.apasf.apa.at:8000/listen.pls')
  elif c == ord('4'):
    tune_in('fm4', 'http://mp3stream1.apasf.apa.at/stream.mp3')
  elif c == ord('5'):
    tune_in('radio_salzburg', '-playlist http://194.232.200.147:8000/listen.pls')
  elif c == ord('6'):
    tune_in('radio_oberösterreich', '-playlist http://194.232.200.148:8000/listen.pls')
  elif c == ord('7'):
    tune_in('radio_burgenland', 'http://194.232.200.146:8000/')
  elif c == ord('8'):
    tune_in('radio_steiermark', 'http://mp3stream9.apasf.apa.at/')
  elif c == ord('9'):
    tune_in('radio_kaernten', 'mms://apasf.apa.at/radio_kaernten')
  elif c == ord('0'):
    tune_in('radio_noe', 'http://mp3stream8.apasf.apa.at/')
  elif c == 195: # Umlauts
    c = stdscr.getch()
    if c == 188: # ü
      tune_in('dlf', '-playlist https://www.deutschlandradio.de/streaming/dlf.m3u')
    if c == 182: # ö
      tune_in('antenne_kärnten', 'http://live.antenne.at/as')
    if c == 164: # ä
      tune_in('hr1', 'http://hr-hr1-live.cast.addradio.de/hr/hr1/live/mp3/128/stream.mp3')
  elif c == ord('p') or c == ord('P'):
    tune_in('hr2', 'http://hr-hr2-live.cast.addradio.de/hr/hr2/live/mp3/128/stream.mp3')
  elif c == ord('z') or c == ord('Z'):
    tune_in('hr3', 'http://hr-hr3-live.cast.addradio.de/hr/hr3/live/mp3/128/stream.mp3')
  elif c == ord('b')  or c == ord('B'):
    tune_in('hr4', 'http://hr-hr4-live.cast.addradio.de/hr/hr4/live/mp3/128/stream.mp3')
  elif c == ord('m') or c == ord('M'):
    tune_in('hr_info', 'http://hr-hrinfo-live.cast.addradio.de/hr/hrinfo/live/mp3/128/stream.mp3')
  elif c == ord(','):
    tune_in('ndr1_niedersachsen', 'https://ndr-ndr1niedersachsen-hannover.sslcast.addradio.de/ndr/ndr1niedersachsen/hannover/mp3/128/stream.mp3')
  elif c == ord('.'):
    tune_in('mdr_sachsen', 'http://mdr-284280-0.cast.mdr.de/mdr/284280/0/mp3/high/stream.mp3')
  elif c == ord('j') or c == ord('J'):
    tune_in('mdr_classic', 'http://mdr-284350-0.cast.mdr.de/mdr/284350/0/mp3/high/stream.mp3')
  elif c == ord('u') or c == ord('U'):
    tune_in('bayern1', 'http://br-br1-obb.cast.addradio.de/br/br1/obb/mp3/128/stream.mp3')
  elif c == ord('i') or c == ord('I'):
    tune_in('bayern2', 'http://br-br2-sued.cast.addradio.de/br/br2/sued/mp3/128/stream.mp3')
  elif c == ord('a') or c == ord('A'):
    tune_in('bayern3', 'http://br-br3-live.cast.addradio.de/br/br3/live/mp3/128/stream.mp3')
  elif c == ord('e') or c == ord('E'):
    tune_in('bayern4', 'http://br-brklassik-live.cast.addradio.de/br/brklassik/live/mp3/128/stream.mp3')
  elif c == ord('o') or c == ord('O'):
    tune_in('bayern5', 'http://br-b5aktuell-live.cast.addradio.de/br/b5aktuell/live/mp3/128/stream.mp3')
  elif c == ord('s') or c == ord('S'):
    tune_in('mdr_info', '-playlist http://avw.mdr.de/livestreams/mdr_info_live_128.pls')
  elif c == ord('n') or c == ord('N'):
    tune_in('rbb_info', 'http://rbb.ic.llnwd.net/stream/rbb_inforadio_mp3_m_a')
  elif c == ord('r') or c == ord('R'):
    tune_in('rbb_kultur', 'http://rbb.ic.llnwd.net/stream/rbb_kulturradio_mp3_m_a')
  elif c == ord('t') or c == ord('T'):
    tune_in('rbb_radio1', 'http://rbb.ic.llnwd.net/stream/rbb_radioeins_mp3_m_a')
  elif c == ord('d') or c == ord('D'):
    tune_in('ndr1_welle_nord', 'http://ndrstream.ic.llnwd.net/stream/ndrstream_ndr1wellenord_hi_mp3')
  elif c == ord('y') or c == ord('Y'):
    tune_in('wdr2', 'http://wdr-mp3-m-wdr2-koeln.akacast.akamaistream.net/7/812/119456/v1/gnl.akacast.akamaistream.net/wdr-mp3-m-wdr2-koeln')
  elif c == ord('x') or c == ord('X'):
    tune_in('bbc_news', 'http://mp33.bbc.streamuk.com:80/')
  elif c == ord('v') or c == ord('V'):
    tune_in('bbc_uk', 'http://mp32.bbc.streamuk.com:80/')
  elif c == ord('l') or c == ord('L'):
    tune_in('bbc_radio1' ,'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_lc1_radio1_p?s=1324848510&e=1324862910&h=39cf8a445c2808660e0b92d4611d68a8')
  elif c == ord('c') or c == ord('C'):
    tune_in('bbc_radio2', 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_lc1_radio2_p?s=1324848689&e=1324863089&h=d5a1c35aef07079446c6f72d9c961987')
  elif c == ord('w') or c == ord('W'):
    tune_in('bbc_radio4', 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_lc1_radio4_p?s=1324848717&e=1324863117&h=7f5a83962dc491d17ee360c935059bae')
  elif c == ord('k') or c == ord('K'):
    tune_in('bbc_radio5' ,'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_lc1_5live_p?s=1324848792&e=1324863192&h=b215d7cef4dd16c1da9995d772518812')
  elif c == ord('h') or c == ord('H'):
    tune_in('bbc_radio5', 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_lc1_radio3_p?s=1324848737&e=1324863137&h=aeb3fb200c9ce4802c4c6af3cdc4fe6c')
  elif c == ord('g') or c == ord('G'):
    tune_in('radio_ooe', 'http://orfradio.liwest.at/liveLQ.m3u')
  elif c == ord('f') or c == ord('F'):
    tune_in('radio_tirol', 'mms://apasf.apa.at/radio_tirol_worldwide')
  elif c == ord('q') or c == ord('Q'):
    tune_in('radio_vorarlberg', 'mms://apasf.apa.at/radio_vbg_worldwide')	
# Wartungsmodus mit PAGE DOWN (d.h. Programm sauber beenden)		
  elif c == curses.KEY_NPAGE:
    os.system('killall mplayer')
    break
# Curses Modus sauber beenden		
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
