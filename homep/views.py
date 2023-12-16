from django.shortcuts import render
import speedtest as sptest

from .models import SpeedTestResult

# Create your views here.
def index(request):
    return render(request, 'homep/index.html')


def speedtest_view(request):
    st = sptest.Speedtest()
    download_speed = st.download() / 1_000_000  # in Mbps
    upload_speed = st.upload() / 1_000_000  # in Mbps

    # Save results to the database
    SpeedTestResult.objects.create(download_speed=download_speed, upload_speed=upload_speed)

    return render(request, 'homep/speedtest.html', {'download_speed': download_speed, 'upload_speed': upload_speed})