from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from .models import Bayi


# membuat class TaskForm untuk membuat task
class BayiForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Bayi
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('nama_bayi', 'jenis_kelamin', 'umur', 'berat_badan', 'tinggi_badan')
        # mengatur teks label untuk setiap field
        labels = {
            'nama_bayi': _('Nama Bayi'),
            'jenis_kelamin': _('Jenis Kelamin'),
            'umur': _('Umur'),
            'berat_badan': _('Berat Badan'),
            'tinggi_badan': _('Tinggi Badan')
        }
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'nama_bayi': {
                'required': _("Nama bayi harus diisi."),
            },
            'jenis_kelamin': {
                'required': _("Jenis Kelamin harus diisi."),
            },
            'umur': {
                'required': _("Umur harus diisi."),
            },
            'berat_badan': {
                'required': _("Berat Badan harus diisi."),
            },
            'tinggi_badan': {
                'required': _("Tinggi Badan harus diisi."),
            },
        }
