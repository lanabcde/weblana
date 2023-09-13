from django.shortcuts import render
from django.template import context


def index(request):
    context = { 
        'nav': [
               ['/','Laman Utama'],
               ['/tentang','Tentang'],
               ['/kontak','Kontak'],
               ['/masuk','Masuk'],
        ]
    }
    return render(request,'index.html',context)


