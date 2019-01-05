#!/usr/bin/python

# Module importieren
import os
import sys
import curses

#Lautstaerke setzen
volume = 100 
os.system('amixer set Master ' + str(volume))
# Curses Modus starten
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
# Standardsender OE1
os.system ('mplayer -really-quiet -ao alsa ./ansagen/oe1.mp3 < /dev/null > /dev/null &')
os.system('mplayer -really-quiet -nolirc -ao alsa -cache 1024 http://mp3stream3.apasf.apa.at:8000 < /dev/null > /dev/null &')
# Texthilfe
pad = curses.newpad(30,10)

while True:
	c = stdscr.getch()
# lauter	
	if c == curses.KEY_RIGHT:
	    if volume < 64:
			volume = volume + 4
			os.system ('mplayer -really-quiet -ao alsa ./ansagen/lauter.mp3 < /dev/null > /dev/null &')
			os.system('amixer set Master ' + str(volume))			
# leister			
	if c == curses.KEY_DOWN:
	    if volume > 0:		
			volume = volume - 4
			os.system ('mplayer -really-quiet -ao alsa ./ansagen/leiser.mp3 < /dev/null > /dev/null &')
			os.system('amixer set Master ' + str(volume))
# Sender je nach gedrueckter Taste abspielen			
	elif c == ord('1'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/oe1.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 1024 http://mp3stream3.apasf.apa.at:8000 < /dev/null > /dev/null &')
	elif c == ord('2'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/radio_wien.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 mms://apasf.apa.at/radio_wien_worldwide < /dev/null > /dev/null &')
	elif c == ord('y') or c == ord('Y'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/dlf.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://dradio.ic.llnwd.net/stream/dradio_dlf_m_a < /dev/null > /dev/null &')
	elif c == ord('x') or c == ord('X'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/dw.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://dw-radio-german-mp3.akacast.akamaistream.net/7/506/135361/v1/gnl.akacast.akamaistream.net/dw-radio-german-mp3 < /dev/null > /dev/null &')
	elif c == ord('c') or c == ord('C'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/hr1.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://gffstream.ic.llnwd.net/stream/gffstream_mp3_w67b < /dev/null > /dev/null &')
	elif c == ord('v') or c == ord('V'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/hr2.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://gffstream.ic.llnwd.net/stream/gffstream_mp3_w68b < /dev/null > /dev/null &')
	elif c == ord('b') or c == ord('B'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/hr3.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://gffstream.ic.llnwd.net/stream/gffstream_mp3_w69b < /dev/null > /dev/null &')
	elif c == ord('n')  or c == ord('N'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/hr4.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://gffstream.ic.llnwd.net/stream/gffstream_mp3_w70b < /dev/null > /dev/null &')
	elif c == ord('m') or c == ord('M'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/hr_info.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://gffstream.ic.llnwd.net/stream/gffstream_mp3_w71b < /dev/null > /dev/null &')
	elif c == ord(','):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/ndr1_niedersachsen.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://ndrstream.ic.llnwd.net/stream/ndrstream_ndr1niedersachsen_hi_mp3 < /dev/null > /dev/null &')
	elif c == ord('.'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/mdr_sachsen.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 -playlist http://avw.mdr.de/livestreams/mdr1_radio_sachsen_live_128.pls < /dev/null > /dev/null &')
	elif c == ord('-'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/mdr_classic.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 -playlist http://avw.mdr.de/livestreams/mdr_klassik_live_128.pls < /dev/null > /dev/null &')
	elif c == ord('h') or c == ord('H'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/mdr_info.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 -playlist http://avw.mdr.de/livestreams/mdr_info_live_128.pls < /dev/null > /dev/null &')
	elif c == ord('j') or c == ord('J'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/rbb_info.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://rbb.ic.llnwd.net/stream/rbb_inforadio_mp3_m_a < /dev/null > /dev/null &')
	elif c == ord('k') or c == ord('K'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/rbb_kultur.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://rbb.ic.llnwd.net/stream/rbb_kulturradio_mp3_m_a < /dev/null > /dev/null &')
	elif c == ord('l') or c == ord('L'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/rbb_radio1.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://rbb.ic.llnwd.net/stream/rbb_radioeins_mp3_m_a < /dev/null > /dev/null &')
	elif c == ord('+'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/ndr1_welle_nord.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://ndrstream.ic.llnwd.net/stream/ndrstream_ndr1wellenord_hi_mp3 < /dev/null > /dev/null &')
	elif c == ord('#'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/wdr2.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://wdr-mp3-m-wdr2-koeln.akacast.akamaistream.net/7/812/119456/v1/gnl.akacast.akamaistream.net/wdr-mp3-m-wdr2-koeln < /dev/null > /dev/null &')
	elif c == ord('q') or c == ord('Q'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bbc_news.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://mp33.bbc.streamuk.com:80/ < /dev/null > /dev/null &')
	elif c == ord('w') or c == ord('W'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bbc_uk.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://mp32.bbc.streamuk.com:80/ < /dev/null > /dev/null &')
	elif c == ord('e') or c == ord('E'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bbc_radio1.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_lc1_radio1_p?s=1324848510&e=1324862910&h=39cf8a445c2808660e0b92d4611d68a8" < /dev/null > /dev/null &')
	elif c == ord('r') or c == ord('R'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bbc_radio2.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_lc1_radio2_p?s=1324848689&e=1324863089&h=d5a1c35aef07079446c6f72d9c961987" < /dev/null > /dev/null &')
	elif c == ord('t') or c == ord('T'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bbc_radio4.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_lc1_radio4_p?s=1324848717&e=1324863117&h=7f5a83962dc491d17ee360c935059bae" < /dev/null > /dev/null &')
	elif c == ord('z') or c == ord('Z'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bbc_radio5.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_lc1_5live_p?s=1324848792&e=1324863192&h=b215d7cef4dd16c1da9995d772518812" < /dev/null > /dev/null &')
	elif c == ord('u') or c == ord('U'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bbc_radio3.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_lc1_radio3_p?s=1324848737&e=1324863137&h=aeb3fb200c9ce4802c4c6af3cdc4fe6c" < /dev/null > /dev/null &')
	elif c == ord('a') or c == ord('A'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bayern1.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://gffstream.ic.llnwd.net/stream/gffstream_w10b < /dev/null > /dev/null &')
	elif c == ord('s') or c == ord('S'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bayern2.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://gffstream.ic.llnwd.net/stream/gffstream_w11b < /dev/null > /dev/null &')
	elif c == ord('d') or c == ord('D'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bayern3.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://gffstream.ic.llnwd.net/stream/gffstream_w12b < /dev/null > /dev/null &')
	elif c == ord('f') or c == ord('F'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bayern4.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://gffstream.ic.llnwd.net/stream/gffstream_w13b < /dev/null > /dev/null &')
	elif c == ord('g') or c == ord('G'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/bayern5.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -really-quiet -nolirc -ao alsa -cache 128 http://gffstream.ic.llnwd.net/stream/gffstream_w13b < /dev/null > /dev/null &')
	elif c == ord('3'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/oe3.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -nolirc -really-quiet -ao alsa -cache 128 mms://apasf.apa.at/OE3_Live_Audio &')
	elif c == ord('4'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/fm4.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -nolirc -really-quiet -ao alsa -cache 128 mms://apasf.apa.at/fm4_live_worldwide &')
	elif c == ord('5'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/radio_salzburg.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -nolirc -really-quiet -ao alsa -cache 128 mms://apasf.apa.at/radio_salzburg &')
	elif c == ord('6'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/dw.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -nolirc -really-quiet -ao alsa -cache 128 http://dw-radio-german-mp3.akacast.akamaistream.net/7/506/135361/v1/gnl.akacast.akamaistream.net/dw-radio-german-mp3 &')
	elif c == ord('7'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/radio_burgenland.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -nolirc -really-quiet -ao alsa -cache 128 mms://apasf.apa.at/radio_bgl_worldwide &')
	elif c == ord('8'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/radio_steiermark.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -nolirc -really-quiet -ao alsa -cache 128 http://mp3stream9.apasf.apa.at:8000/listen.pls &')
	elif c == ord('9'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/radio_kaernten.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -nolirc -really-quiet -ao alsa -cache 128 mms://apasf.apa.at/radio_kaernten &')
	elif c == ord('0'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/radio_noe.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -nolirc -really-quiet -ao alsa -cache 128 mms://radio-noe.streaming.kabsi.at/radio_noe &')
	elif c == ord('i') or c == ord('I'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/radio_ooe.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -nolirc -really-quiet -ao alsa -cache 128 -playlist http://orfradio.liwest.at/liveLQ.m3u &')
	elif c == ord('o') or c == ord('O'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/radio_tirol.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -nolirc -really-quiet -ao alsa -cache 128 mms://apasf.apa.at/radio_tirol_worldwide &')
	elif c == ord('p') or c == ord('P'):
		os.system('killall mplayer')
		os.system ('mplayer -really-quiet -ao alsa ./ansagen/radio_vorarlberg.mp3 < /dev/null > /dev/null &')
		os.system('mplayer -nolirc -really-quiet -ao alsa -cache 128 mms://apasf.apa.at/radio_vbg_worldwide &')	
# Wartungsmodus mit PAGE DOWN (d.h. Programm sauber beenden)		
	elif c == curses.KEY_NPAGE:
		os.system('killall mplayer')
		break
# Curses Modus sauber beenden		
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
