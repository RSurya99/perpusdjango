from django.shortcuts import render, redirect, HttpResponse
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BookResource

def exportXls(request):
    buku = BookResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type ='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=laporan-buku.xls'
    return response

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi kesalahan saat pembuatan akun")
            return redirect('signup')
    else:
        form = UserCreationForm()
        context = {
            'form': form,
        }
    return render(request, 'signup.html', context)


@login_required(login_url=settings.LOGIN_URL)
def hapusBuku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    messages.success(request, "Data berhasil dihapus")
    return redirect('buku')
    
@login_required(login_url=settings.LOGIN_URL)
def ubahBuku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbarui")
            return redirect('ubah-buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        context = {
            'form': form,
            'buku': buku,
        }
    return render(request, template, context)
    
@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    # books = Buku.objects.filter(kelompok_id__nama='Produktif')[:5]
    books = Buku.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'buku.html', context)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request, 'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def tambahBuku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()
            message = "Data berhasil disimpan"
            context = {
                'form': form,
                'message': message,
            }
            return render(request, 'tambah-buku.html', context)
    else: 
        form = FormBuku()

        context = {
            'form': form,
        }

    return render(request, 'tambah-buku.html', context)