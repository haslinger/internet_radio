#!/usr/bin/python
# -*- coding: utf-8 -*-

# Module importieren
import os
import sys
import curses
import time

def tune_in(text, url):
  os.system('killall mpv')
  ansage(text)
  time.sleep(4)
  play(url)

def play(url):
  os.system('mpv --no-input-terminal ' + url + ' &')

def ansage(text):
  play('~/internet_radio/ansagen/' + text + '.mp3')

#Lautstaerke setzen
volume = 95 
os.system('amixer set Master ' + str(volume))
# Curses Modus starten
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
# Standardsender OE1
tune_in('oe1', 'https://orf-live.ors-shoutcast.at/oe1-q1a')

while True:
  c = stdscr.getch()

  # lauter
  if c == curses.KEY_RIGHT:
      if volume < 96:
        volume = volume + 5
        ansage('lauter')
        os.system('amixer set Master ' + str(volume))
  # leister
  elif c == curses.KEY_LEFT:
      if volume > 0:
        volume = volume - 5
        ansage('leiser')
        os.system('amixer set Master ' + str(volume))
  # Sender je nach gedrueckter Taste abspielen
  elif c == ord('1'):
    tune_in('oe1', 'https://orf-live.ors-shoutcast.at/oe1-q1a')
  elif c == ord('2'):
    tune_in('radio_wien', 'https://orf-live.ors-shoutcast.at/wie-q1a')
  elif c == ord('3'):
    tune_in('oe3', 'http://orf-live.ors-shoutcast.at/oe3-q2a')
  elif c == ord('4'):
    tune_in('fm4', 'https://orf-live.ors-shoutcast.at/fm4-q1a')
  elif c == ord('5'):
    tune_in('radio_salzburg', 'https://orf-live.ors-shoutcast.at/sbg-q1a')
  elif c == ord('6'):
    tune_in('radio_oberösterreich', 'https://orf-live.ors-shoutcast.at/ooe-q1a')
  elif c == ord('7'):
    tune_in('radio_burgenland', 'https://orf-live.ors-shoutcast.at/bgl-q1a')
  elif c == ord('8'):
    tune_in('radio_steiermark', 'https://orf-live.ors-shoutcast.at/stm-q1a')
  elif c == ord('9'):
    tune_in('radio_kaernten', 'https://orf-live.ors-shoutcast.at/ktn-q1a')
  elif c == ord('0'):
    tune_in('radio_noe', 'https://orf-live.ors-shoutcast.at/noe-q1a')
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
    tune_in('bayern1', 'https://streams.br.de/bayern1obb_2.m3u')
  elif c == ord('i') or c == ord('I'):
    tune_in('bayern2', 'https://streams.br.de/bayern2sued_2.m3u')
  elif c == ord('a') or c == ord('A'):
    tune_in('bayern3', 'https://streams.br.de/bayern3_2.m3u')
  elif c == ord('e') or c == ord('E'):
    tune_in('bayern4', 'https://streams.br.de/br-klassik_3.m3u')
  elif c == ord('o') or c == ord('O'):
    tune_in('bayern5', 'https://br-b5aktuell-live.cast.addradio.de/br/b5aktuell/live/mp3/mid')
  elif c == ord('s') or c == ord('S'):
    tune_in('mdr_aktuell', 'http://mdr-284340-0.cast.mdr.de/mdr/284340/0/mp3/high/stream.mp3')
  elif c == ord('n') or c == ord('N'):
    tune_in('rbb_info', 'http://www.inforadio.de/live.m3u')
  elif c == ord('r') or c == ord('R'):
    tune_in('rbb_kultur', 'http://www.rbbkultur.de/live.m3u')
  elif c == ord('t') or c == ord('T'):
    tune_in('rbb_radio1', 'http://www.radioeins.de/livemp3')
  elif c == ord('d') or c == ord('D'):
    tune_in('ndr1_welle_nord', 'http://ndr-ndr1wellenord-kiel.cast.addradio.de/ndr/ndr1wellenord/kiel/mp3/128/stream.mp3')
  elif c == ord('y') or c == ord('Y'):
    tune_in('wdr2', 'http://wdr-wdr2-rheinland.icecast.wdr.de/wdr/wdr2/rheinland/mp3/128/stream.mp3')
  elif c == ord('x') or c == ord('X'):
    tune_in('bbc_world_service_for_europe', 'https://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/dash/nonuk/dash_low/cfs/bbc_world_service.mpd')
  elif c == ord('v') or c == ord('V'):
    tune_in('srf4', 'http://stream.srg-ssr.ch/drs4news/mp3_128.m3u')
  elif c == ord('l') or c == ord('L'):
    tune_in('bbc_radio1' ,'http://stream.live.vc.bbcmedia.co.uk/bbc_radio_one')
  elif c == ord('c') or c == ord('C'):
    tune_in('bbc_radio2', 'http://stream.live.vc.bbcmedia.co.uk/bbc_radio_two')
  elif c == ord('w') or c == ord('W'):
    tune_in('bbc_radio3', 'http://stream.live.vc.bbcmedia.co.uk/bbc_radio_three')
  elif c == ord('k') or c == ord('K'):
    tune_in('bbc_radio4', 'http://stream.live.vc.bbcmedia.co.uk/bbc_radio_fourfm')
  elif c == ord('h') or c == ord('H'):
    tune_in('bbc_radio5' ,'https://stream.live.vc.bbcmedia.co.uk/bbc_radio_five_live_online_nonuk')
  elif c == ord('g') or c == ord('G'):
    tune_in('radio_ooe', 'https://orf-live.ors-shoutcast.at/ooe-q1a')
  elif c == ord('f') or c == ord('F'):
    tune_in('radio_tirol', 'ttps://orf-live.ors-shoutcast.at/tir-q1a')
  elif c == ord('q') or c == ord('Q'):
    tune_in('radio_vorarlberg', 'https://orf-live.ors-shoutcast.at/vbg-q1a')

  # Wartungsmodus mit PAGE DOWN (d.h. Programm sauber beenden)
  elif c == curses.KEY_NPAGE:
    os.system('killall mpv')
    break

# Curses Modus sauber beenden
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

# Livestreams Bayern: https://www.br.de/unternehmen/inhalt/technik/hilfe-livestreams-br100.html
# Schweizer Radio Streams: https://www.broadcast.ch/fileadmin/kundendaten/Dokumente/Internet_Streaming/2021_01_links_for_streaming_internet_radio_de_fr_it_V006.pdf
# Streema: https://streema.com/radios