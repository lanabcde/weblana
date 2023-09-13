from django.shortcuts import render
from django.shortcuts import render

def materi(request):
    context = { 
        'bab1': [
               ['/materi','Beranda'],
               ['/program','Pengenalan Program'],
               ['/kontak','Bahasa Pemorgraman'],
               ['/masuk','Interpreter dan Compiler'],

        ],
        'bab2': [
               ['/','Tipe Data'],
               ['/tentang','Varaibel'],
               ['/kontak','Operator'],
            
        ]
    }
    return render(request,'materi/p1_beranda.html',context)

def program(request):
  

    return render(request,'materi/p2_program.html')


def bahasa_pemrograman(request):
  

    return render(request,'materi/p3_bahasa_pemrograman.html')


def interpreter_compiler(request):
  

    return render(request,'materi/p4_interpreter_compiler.html')

def bahasa_python(request):
  

    return render(request,'materi/p5_bahasa_python.html')

def program_sederhana(request):
  

    return render(request,'materi/p7_program_sederhana.html')

def kuis_bab1(request):
  

    return render(request,'materi/kuis_bab1.html')

def beranda2(request):
  

    return render(request,'materi/p6_beranda2.html')

def tipe_data(request):
  

    return render(request,'materi/p8_tipe_data.html')

def variabel(request):
  

    return render(request,'materi/p9_variabel.html')

def operator(request):
  

    return render(request,'materi/p10_operator.html')

def kuis_bab2(request):
  

    return render(request,'materi/kuis_bab2.html')

def beranda3(request):
  

    return render(request,'materi/p11_beranda3.html')

def percabangan(request):
  

    return render(request,'materi/p12_percabangan.html')

def percabangan_if(request):
  

    return render(request,'materi/p_percabangan_if.html')

def percabangan_if_else(request):
  

    return render(request,'materi/p13_percabangan_if_else.html')

def percabangan_elif(request):
  

    return render(request,'materi/p14_percabangan_elif.html')

def kuis_bab3(request):
  

    return render(request,'materi/kuis_bab3.html')


def beranda4(request):
  

    return render(request,'materi/p15_beranda4.html')

def perulangan(request):
  

    return render(request,'materi/p16_perulangan.html')

def perulangan_while(request):
  

    return render(request,'materi/p17_perulangan_while.html')

def perulangan_for(request):
  

    return render(request,'materi/p18_perulangan_for.html')

def kuis_bab4(request):
  

    return render(request,'materi/kuis_bab4.html')

def beranda5(request):
  

    return render(request,'materi/p19_beranda5.html')

def fungsi(request):
  

    return render(request,'materi/p20_fungsi.html')

def membuat_fungsi(request):
  

    return render(request,'materi/p21_membuat_fungsi.html')

def cara_kerja_fungsi(request):
  

    return render(request,'materi/p22_cara_kerja_fungsi.html')










