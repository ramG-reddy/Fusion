# Register your models here.
from applications.ps1.models import IndentFile, StockEntry, StockItem, StockTransfer
from django.contrib import admin

admin.site.register(StockEntry)
admin.site.register(IndentFile)
admin.site.register(StockItem)
admin.site.register(StockTransfer)
