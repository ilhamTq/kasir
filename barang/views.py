from django.shortcuts import render, redirect
from barang.models import Produk, Kategori

def list_barang(request):
    template_name = 'list_barang.html'
    list_produk = Produk.objects.all()
    context = {
        'title':'ini adalah halaman barang',
        'produk':list_produk
    }
    return render(request, template_name, context)

def barang_add(request):
    template_name = 'barang_add.html'
    kategori = Kategori.objects.all()
    if request.method == "POST":
        input_kategori = request.POST.get('kategori')
        input_nama = request.POST.get('nama')
        input_deskripsi = request.POST.get('deskripsi')
        input_jumlah = request.POST.get('jumlah')
        
        #Panggil kategori terlebih dahulu
        get_kategori = Kategori.objects.get(nama=input_kategori)
        
        #simpan produk karena terdapat relasi ke tabel kategori
        Produk.objects.create(
            nama = input_nama,
            deskripsi = input_deskripsi,
            jumlah = input_jumlah,
            kategori = get_kategori,
        )
        return redirect(list_barang)
    context = {
        'title':'ini adalah halaman tambah barang',
        'kategori':kategori
    }
    return render(request, template_name, context)

def barang_update(request, id):
    template_name = 'barang_add.html'
    kategori = Kategori.objects.all()
    get_produk = Produk.objects.get(id=id)
    if request.method == "POST":
        input_kategori = request.POST.get('kategori')
        input_nama = request.POST.get('nama')
        input_deskripsi = request.POST.get('deskripsi')
        input_jumlah = request.POST.get('jumlah')
        
        #Panggil kategori terlebih dahulu
        get_kategori = Kategori.objects.get(nama=input_kategori)
        
        #simpan produk karena terdapat relasi ke tabel kategori
        get_produk.nama = input_nama
        get_produk.deskripsi = input_deskripsi
        get_produk.jumlah = input_jumlah
        get_produk.kategori = get_kategori
        get_produk.save()
        return redirect(list_barang)
    context = {
        'title':'ini adalah halaman tambah barang',
        'kategori':kategori,
        'get_produk':get_produk,
    }
    return render(request, template_name, context)
def barang_delete(request, id):
    produk = Produk.objects.get(id=id).delete()
    return redirect(list_barang)