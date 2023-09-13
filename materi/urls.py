from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path("",views.materi,name='materi'),    
     path("program",views.program,name="program"), 
     path("bahasa_pemrograman",views.bahasa_pemrograman,name="bahasa_pemrograman"), 
     path("interpreter_compiler",views.interpreter_compiler,name="interpreter_compiler"), 
     path("bahasa_python",views.bahasa_python,name="bahasa_python"),
     path("program_sederhana",views.program_sederhana,name="program_sederhana"),
     path("kuis_bab1",views.kuis_bab1,name="kuis_bab1"),
     path("beranda2",views.beranda2,name="beranda2"), 
     path("tipe_data",views.tipe_data,name="tipe_data"), 
     path("variabel",views.variabel,name="variabel"), 
     path("operator",views.operator,name="operator"), 
     path("kuis_bab2",views.kuis_bab2,name="kuis_bab2"), 
     path("beranda3",views.beranda3,name="beranda3"), 
     path("percabangan",views.percabangan,name="percabangan"), 
     path("percabangan_if",views.percabangan_if,name="percabangan_if"), 
     path("percabangan_if_else",views.percabangan_if_else,name="percabangan_if_else"), 
     path("percabangan_elif",views.percabangan_elif,name="percabangan_elif"), 
     path("kuis_bab3",views.kuis_bab3,name="kuis_bab3"), 
     path("beranda4",views.beranda4,name="beranda4"), 
     path("perulangan",views.perulangan,name="perulangan"), 
     path("perulangan_while",views.perulangan_while,name="perulangan_while"), 
     path("perulangan_for",views.perulangan_for,name="perulangan_for"), 
     path("kuis_bab4",views.kuis_bab4,name="kuis_bab4"), 
     path("beranda5",views.beranda5,name="beranda5"),
     path("fungsi",views.fungsi,name="fungsi"),
     path("membuat_fungsi",views.membuat_fungsi,name="membuat_fungsi"),
     path("cara_kerja_fungsi",views.cara_kerja_fungsi,name="cara_kerja_fungsi"), 
     
]
