import yt_dlp as yt_dlp

def download_playlist_Q1(playlist_url, output_path):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        'outtmpl': output_path + '/Q1_%(playlist_index)s.%(ext)s',
        'playlist_items': '0-2,4-11'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def download_playlist_Q2(playlist_url, output_path):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        'outtmpl': output_path + '/Q2_%(playlist_index)s.%(ext)s',
        'playlist_items': '1-11'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
        
def download_playlist_Q3(playlist_url, output_path):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        'outtmpl': output_path + '/Q3_%(playlist_index)s.%(ext)s',
        'playlist_items': '1-7,10-14'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    output_path = "./raw_audio/"
    playlist_url_Q1 = "https://www.youtube.com/playlist?list=PLGnjPtt6DJXTJNR59PPVagr-ZF-H19NBw"
    playlist_url_Q2 = "https://www.youtube.com/playlist?list=PLUM8x224JrX-x9FN3RezOItAWrNcFHC50"
    playlist_url_Q3 = "https://www.youtube.com/playlist?list=PLUM8x224JrX9QUSL-qHtdLvuo-EIcs-Co"
    
    download_playlist_Q1(playlist_url_Q1, output_path)
    download_playlist_Q2(playlist_url_Q2, output_path)
    download_playlist_Q3(playlist_url_Q3, output_path)
