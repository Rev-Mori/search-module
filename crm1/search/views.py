from multiprocessing import context
from pickle import TRUE
from typing import Type
from django.shortcuts import render, HttpResponse
from django.conf import settings
# Create your views here.
import os
import re
import glob
from datetime import datetime, timedelta
from pathlib import Path

from .forms import RegForm, Logform


def login(request):
    form = Logform
    if request.method == 'POST':
        form = Logform(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = Logform()

    context = {'form': form}
    print('form', form)
    return render(request, 'login/login.html', context)


def register(request):
    form = RegForm()

    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = RegForm()

    context = {'form': form}
    print('form', form)
    return render(request, 'register/register.html', context)


def index(request):
    vid_path = ""
    img_path = ""

    EXTENSION1 = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG', '.jfif')
    EXTENSION2 = ('.mp4')
    EXTENSION3 = ('.txt')
    print(request)
    if request.method == 'GET':
        name = request.GET.get('search_name')
        full_image = request.GET.get('gridRadios1', None)
        cropped_image = request.GET.get('gridRadios2', None)
        videos = request.GET.get('gridRadios3', None)
        search_path = settings.BASE_DIR / "static"
        full_image_list = []
        cropped_image_list = []
        video_list = []
        date1_list = []
        date2_list = []
        format_data = "%Y-%m-%d"
        date_entry = request.GET.get('cdate', None)
        print("fyfgghihihi", date_entry)
        flag = False
        if date_entry is not None and date_entry != '':
            print(date_entry)
            date = datetime.strptime(date_entry, format_data).date()
            flag = True
            print(date)

        for (root, dirs, files) in os.walk(str(search_path), topdown=True):
            # print(root)
            #print('name', name, files)
            for file in files:
                # print("enter")

                file_path = os.path.join(root, file)
                # print("###############", os.path.getctime(file_path))
                # print(datetime.fromtimestamp(
                #     os.path.getctime(file_path)).date())
                if flag:
                    if date == datetime.fromtimestamp(os.path.getctime(file_path)).date():
                        if file.endswith(EXTENSION1):
                            img1_path = os.path.join(root, file)
                            img1_path = Path(img1_path)
                            img1_path = img1_path.relative_to(search_path)
                            date1_list.append(img1_path)

                        if file.endswith(EXTENSION2):
                            video1_path = os.path.join(root, file)
                            video1_path = Path(video1_path)
                            video1_path = video1_path.relative_to(search_path)
                            date2_list.append(video1_path)

            if full_image:
                for file in files:
                    if file.endswith(EXTENSION1):
                        img_path = os.path.join(root, file)
                        img_path = Path(img_path)
                        img_path = img_path.relative_to(search_path)
                        full_image_list.append(img_path)

            if cropped_image:
                for file in files:
                    if file.endswith(EXTENSION1):
                        cropped_image_list.append(file)

            if videos:
                for file in files:
                    if file.endswith(EXTENSION2):
                        video_path = os.path.join(root, file)
                        video_path = Path(video_path)
                        video_path = video_path.relative_to(search_path)
                        video_list.append(video_path)

            if name in files:
                if name.endswith(EXTENSION1):
                    # ext = name.split('.')[1]
                    # print(ext)
                    img_path = os.path.join(root, name)
                    img_path = Path(img_path)
                    img_path = img_path.relative_to(search_path)
                    img_path = str(img_path)
                    print("img path", img_path)
                elif name.endswith(EXTENSION2):
                    vid_path = os.path.join(root, name)
                    vid_path = Path(vid_path)
                    vid_path = vid_path.relative_to(search_path)
                    vid_path = str(vid_path)
                    print("vid path", vid_path)
        # if date:
        # for file in files:
        #     if name.endswith(EXTENSION3):
        #         print("###############", os.path.getctime(file))
            # if date == datetime.fromtimestamp(os.path.getctime(file)).date():
            #     date_l""ist.append(file)
            #     print(file)

    print("full_img", full_image_list)
    context1 = {'img_path': img_path, 'vid_path': vid_path,
                "full_image_list": full_image_list, "cropped_image_list": cropped_image_list, "video_list": video_list, "date1_list": date1_list, "date2_list": date2_list}

    return render(request, 'dashboard/index.html', context1)

    # insert the path to your directory
