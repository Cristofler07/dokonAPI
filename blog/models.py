from django.db import models


class Maxsulot(models.Model):
    nomi = models.CharField(max_length=222)
    kodi = models.CharField(max_length=20)
    umumiySoni = models.IntegerField()
    kelgan_narxi = models.DecimalField(max_digits=10, decimal_places=2)
    sotish_narxi = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nomi


class Xodim(models.Model):
    familiyasi = models.CharField(max_length=20)
    ismi = models.CharField(max_length=20)
    id_raqami = models.CharField(max_length=10)
    oyligi = models.CharField(max_length=20)

    def __str__(self):
        return self.ismi


class Kirim(models.Model):
    maxsulot = models.ForeignKey(Maxsulot, on_delete=models.CASCADE)
    xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE)
    maxsulotSoni = models.IntegerField()
    kirim_sana = models.DateTimeField(auto_now_add=True)
    kirim_narxi = models.DecimalField(max_digits=10, decimal_places=2)
    foiz = int(30)
    ufoiz = int(100)

    def __str__(self):
        return str(self.maxsulot)


class Chiqim(models.Model):
    maxsulot = models.ForeignKey(Maxsulot, on_delete=models.CASCADE)
    maxsulotSoni = models.IntegerField()
    xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE)
    sotish_narxi = models.DecimalField(max_digits=10, decimal_places=2)
    sotish_vaqti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.maxsulot)
