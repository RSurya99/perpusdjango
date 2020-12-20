from import_export import resources
from perpustakaan.models import Buku
from import_export.fields import Field

class BookResource(resources.ModelResource):
    kelompok_id__nama = Field(attribute='kelompok_id', column_name='kelompok')

    class Meta:
        model = Buku
        fields = ['judul', 'penerbit', 'kelompok_id__nama', 'jumlah']
        export_order = ['judul', 'kelompok_id__nama', 'penerbit', 'jumlah']
