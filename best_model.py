class LostPassportModel(models.Model):
    src_id = models.CharField(max_length=24, db_index=True, verbose_name='Унікальний ідентифікатор запису', unique=True)
    src_ovd = models.CharField(max_length=400, verbose_name='Назва підрозділу, що зареєстрував інформацію')
    src_d_series = models.CharField(max_length=10, db_index=True, verbose_name='Серія документу')
    src_d_number = models.CharField(max_length=20, db_index=True, verbose_name='Номер документу')
    src_d_type = models.CharField(max_length=40, verbose_name='Тип документу')
    src_d_status = models.CharField(max_length=40, verbose_name='Статус документу')
    src_theft_data = models.DateField(verbose_name='Дата заяви про викрадення/втрату', db_index=True)
    src_insert_date = models.DateField(verbose_name='Дата внесення інформації')

    search_phrase = models.CharField(max_length=30, verbose_name='Індексоване поле', db_index=True, blank=True)

    class Meta:
        db_table = 'sf_services_lost_passports'
        ordering = ['src_theft_data']

    def save(self, *args, **kwargs):
        if not self.search_phrase:
            self.search_phrase = f"{cyrillic_to_similar_lat(self.src_d_series)}{self.src_d_number}"
        super().save(*args, **kwargs)
