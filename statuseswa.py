import os
import glob
import shutil
print('[#] WHATSAPP STATUSES DOWNLOADER [#] \n     [#] DEVELOPED BY M02K [#] \n     [#] For Android  Only [#]')
#logo
#importing required modules
#os for directory changing and creating folder
#glob for selecting * all videos 
#shutil for coping

file_path = '/storage/emulated/0/MSwhatsapp/'
#file path for saving satatus

a  = 0
#counting videos number

os.chdir('/storage/emulated/0/')
#directory change

try:
	os.mkdir('MSwhatsapp')
	#making folder if not exits
	print('FOLDER CREATED PATH : ',file_path)
	#file path where folder is created
	
except:
	print('FOLDER ALREADY EXISTS path : ',file_path)
	#if folder is already created

os.chdir('/storage/emulated/0/WhatsApp/Media/.Statuses/')
#changing directory to whatsapp file for coping status videos 

videos = glob.glob('*.mp4')
#all videos with mp4 file format

for video in videos:
	#for looping video in whatsapp status folder
	a += 1
	
	#file numbering
	
	shutil.copy(video , file_path)
	#copy video  to folder 

print(a , ' Videos Successfully Downloaded')
#video copied to file_path successfuly

print('[#] Facebook : muqadashussain.khaskheli.9 [✓] \n[#] Instagram : @muqadas_khaskheli [✓] \n[#] Github : m02k [✓]')