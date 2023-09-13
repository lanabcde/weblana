from django.shortcuts import render

def masuk(request):
    context = { 
        'nav': [
               ['/','Laman Utama'],
               ['/tentang','Tentang'],
               ['/kontak','Kontak'],
               ['/masuk','Masuk'],
        ]
    }
    return render(request,'masuk/masuk.html',context)

# Create your views here.