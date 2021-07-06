from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages

from .models import Bayi
from .services import deteksi_gizi_bayi_laki
from .forms import BayiForm

# Create your views here.
def index(request):
  # Mengambil semua data bayi
  bayis = Bayi.objects.all()
  
  gizi_bayi = dict()
  
  for bayi in bayis:
    bayi.status = deteksi_gizi_bayi_laki(bayi.umur, bayi.berat_badan, bayi.tinggi_badan)
    if bayi.jenis_kelamin == 'x' or bayi.jenis_kelamin == 'laki-laki':
      bayi.gender = 'laki-laki'
    
  context = {
    'bayis': bayis
  }
  
  return render(request, "gizibayi/index.html", context)


# Membuat View untuk halaman form tambah task
def create_view(request):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        # membuat objek dari class TaskForm
        form = BayiForm(request.POST)
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Task baru dengan data yang disubmit
            new_bayi = BayiForm(request.POST)
            # Simpan data ke dalam table tasks
            new_bayi.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Menambah Task baru.')
            return redirect('gizibayi:home')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = BayiForm()
    # merender template form dengan memparsing data form
    return render(request, 'gizibayi/form.html', {'form': form})
  
def update_view(request, bayi_id):
    try:
        # mengambil data task yang akan diubah berdasarkan task id
        task = Bayi.objects.get(pk=bayi_id)
    except Bayi.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        form = BayiForm(request.POST, instance=task)
        if form.is_valid():
            # Simpan perubahan data ke dalam table tasks
            form.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Mengubah Task.')
            return redirect('gizibayi:home')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = BayiForm(instance=task)
    # merender template form dengan memparsing data form
    return render(request, 'gizibayi/form.html', {'form': form})
