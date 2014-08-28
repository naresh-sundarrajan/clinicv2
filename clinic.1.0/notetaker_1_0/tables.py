import django_tables2 as tables
from notetaker_1_0.models import Note

class NoteTable(tables.Table):
    class Meta:
        model = Note
        fields = ('title', 'text','date','patient_id', )
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}