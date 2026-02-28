import yt_dlp as dlp
import os
url = input("Enter valid youtube video url: ")
save_folder = r"C:\Users\khawa\OneDrive\Desktop\yt downloader"

if not os.path.exists(save_folder):#chk for folder created or noit if not then create it
    os.makedirs(save_folder)


with dlp.YoutubeDL() as ydl:
    print("please wait fetching data..." )
    information = ydl.extract_info(url, download = False) #video data fetch
    qualities = information.get('formats' , None) 
    print("avaliable qualities: ")
    valid_ids=[]
    for i in qualities:#print qualities and format ids
        f_id = i.get('format_id', None)
        res = i.get('resolution',None)
        extension = i.get('ext',None)
        note = i.get('format_note',None)
        if f_id and res and extension:
            print(f"{f_id} : {res} : {extension} : {note}")
            valid_ids.append(f_id)
    choice = input("Enter the format id of the quality you want to download: ")#user choice
    if choice  in valid_ids:
        
        
        ydl_option = {'format': f'{choice}+bestaudio/best'
                      ,'outtmpl': os.path.join(save_folder, '%(title)s.%(ext)s')
                      ,'merge_output_format': 'mp4'
                      ,'ignoreerrors': False,
                      'postprocessors': [{
                         'key': 'FFmpegVideoConvertor',
                         'preferedformat': 'mp4',
                        }],}
                      
        
        try:
            with dlp.YoutubeDL(ydl_option) as dl:
                dl.download([url])
        except Exception as e:
            print(f"\n✗ Download failed invalid! link: {str(e)}")
               
        
