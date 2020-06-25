from django.db import models


class DocumentType(models.Model):
    """
    :param type_doc - Наименование.
    :param validity - Имеет срок действия.
    :param serial number - имеет сериию.
    """
    type_doc = models.TextField("Текст")
    validity = models.BooleanField("Имеет срок действия")
    serial_number = models.BooleanField("Имеет серию")

    def __str__(self):
        return f"{self.type_doc}"

    class Meta:
        verbose_name = "Тип документа"
        verbose_name_plural = "Тип документов"


class LostDocument(models.Model):
    """
    identifier - Идентификатор.
    serial_number_doc - Серия документа.
    number_doc - Номер документа.
    document_type - Тип документа.
    status - Статус.
    date_incident - Дата события.
    date_recording - Дата записи.
    ovd - Орган регистрации события.
    """
    identifier = models.CharField("Идентификатор", max_length=150, unique=True)
    serial_number_doc = models.CharField("Серия документа", max_length=255)
    number_doc = models.CharField("Номер документа", max_length=255,
                                  db_index=True)  # предлагаю его сделать db_index=True.
    document_type = models.ForeignKey(DocumentType, verbose_name="Тип документа", on_delete=models.CASCADE)
    status = models.CharField("Статус", max_length=150)
    date_incident = models.DateTimeField("Дата события", auto_now=False, auto_now_add=False)
    date_recording = models.DateTimeField("Дата записи", auto_now=False, auto_now_add=False)
    ovd = models.CharField("Орган регистрации события", max_length=150)

    def __str__(self):
        return f"{self.identifier}"

    class Meta:
        verbose_name = "Потерянный документ"
        verbose_name_plural = "Потерянные документы"
