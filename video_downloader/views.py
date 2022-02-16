import youtube_dl
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from video_downloader.forms import DownloadForm


def download_video(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            options = {
                'outtmpl': '%(title)s-%(id)s.%(ext)s',
                'format': 'best'
            }
            with youtube_dl.YoutubeDL(options) as ydl:
                r = ydl.extract_info(url, download=False)
                video_url = r['url']
                file_name = 'video.mp4'
                r = HttpResponsePermanentRedirect(video_url)
                r['Content-Type'] = 'application/force-download'
                r['Content-Disposition'] = f'attachment; filename={file_name}'

                return r

        return render(request, 'index.html', {'form': form})
    form = DownloadForm()
    return render(request, 'index.html', {'form': form})
