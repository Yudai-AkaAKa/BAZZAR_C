# Generated by Django 4.1.3 on 2023-01-27 05:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=50, verbose_name='メニュー名')),
                ('size', models.CharField(max_length=3, verbose_name='サイズ')),
                ('price', models.IntegerField(verbose_name='値段')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真3')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真4')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真5')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False, verbose_name='storeid')),
                ('store_name', models.CharField(max_length=30, verbose_name='店舗名')),
                ('postal_code', models.CharField(max_length=8, verbose_name='郵便番号')),
                ('adress1', models.CharField(max_length=20, verbose_name='住所(xx県xx市)')),
                ('adress2', models.CharField(max_length=20, verbose_name='住所(xx丁目xx番地)')),
                ('adress3', models.CharField(max_length=20, verbose_name='住所(ビル名など)')),
                ('phone_number', models.CharField(max_length=13, verbose_name='電話番号')),
                ('seat', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='席数')),
                ('seat_reservationable', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='予約可能な席数')),
                ('bussiness_hours_start', models.CharField(choices=[('１時', '１時'), ('2時', '2時'), ('3時', '3時'), ('4時', '4時'), ('5時', '5時'), ('6時', '6時'), ('7時', '7時'), ('8時', '8時'), ('9時', '9時'), ('10時', '10時'), ('11時', '11時'), ('12時', '12時'), ('13時', '13時'), ('14時', '14時'), ('15時', '15時'), ('16時', '16時'), ('17時', '17時'), ('18時', '18時'), ('19時', '19時'), ('20時', '20時'), ('21時', '21時'), ('22時', '22時'), ('23時', '23時'), ('24時', '24時')], default='選択してください', max_length=3, verbose_name='営業開始')),
                ('start_minute', models.CharField(choices=[('00分', '00分'), ('15分', '15分'), ('30分', '30分'), ('45分', '45分')], default='選択してください', max_length=3, verbose_name='')),
                ('bussiness_hours_end', models.CharField(choices=[('１時', '１時'), ('2時', '2時'), ('3時', '3時'), ('4時', '4時'), ('5時', '5時'), ('6時', '6時'), ('7時', '7時'), ('8時', '8時'), ('9時', '9時'), ('10時', '10時'), ('11時', '11時'), ('12時', '12時'), ('13時', '13時'), ('14時', '14時'), ('15時', '15時'), ('16時', '16時'), ('17時', '17時'), ('18時', '18時'), ('19時', '19時'), ('20時', '20時'), ('21時', '21時'), ('22時', '22時'), ('23時', '23時'), ('24時', '24時')], default='選択してください', max_length=3, verbose_name='営業終了')),
                ('end_minute', models.CharField(choices=[('00分', '00分'), ('15分', '15分'), ('30分', '30分'), ('45分', '45分')], default='選択してください', max_length=3, verbose_name='')),
                ('holiday1', models.CharField(choices=[('月曜日', '月曜日'), ('火曜日', '火曜日'), ('水曜日', '水曜日'), ('木曜日', '木曜日'), ('金曜日', '金曜日'), ('土曜日', '土曜日'), ('日曜日', '日曜日'), ('祝日', '祝日'), ('なし', 'なし')], default='祝日', max_length=4, verbose_name='定休日1')),
                ('holiday2', models.CharField(choices=[('月曜日', '月曜日'), ('火曜日', '火曜日'), ('水曜日', '水曜日'), ('木曜日', '木曜日'), ('金曜日', '金曜日'), ('土曜日', '土曜日'), ('日曜日', '日曜日'), ('祝日', '祝日'), ('なし', 'なし')], default='なし', max_length=4, verbose_name='定休日2')),
                ('holiday3', models.CharField(choices=[('月曜日', '月曜日'), ('火曜日', '火曜日'), ('水曜日', '水曜日'), ('木曜日', '木曜日'), ('金曜日', '金曜日'), ('土曜日', '土曜日'), ('日曜日', '日曜日'), ('祝日', '祝日'), ('なし', 'なし')], default='なし', max_length=4, verbose_name='定休日3')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真3')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真4')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真5')),
                ('photo6', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真6')),
                ('photo7', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真7')),
                ('photo8', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真8')),
                ('photo9', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真9')),
                ('photo10', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='写真10')),
                ('about', models.TextField(max_length=300, verbose_name='紹介文')),
                ('bp_id', models.ForeignKey(max_length=16, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='事業者ID')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='予約者名')),
                ('reservation_mail', models.CharField(blank=True, max_length=40, null=True, verbose_name='予約者メールアドレス')),
                ('reservation_day', models.DateField(default=django.utils.timezone.now, verbose_name='予約希望日')),
                ('reservation_phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='予約者電話番号')),
                ('reservation_hour', models.CharField(choices=[('１時', '１時'), ('2時', '2時'), ('3時', '3時'), ('4時', '4時'), ('5時', '5時'), ('6時', '6時'), ('7時', '7時'), ('8時', '8時'), ('9時', '9時'), ('10時', '10時'), ('11時', '11時'), ('12時', '12時'), ('13時', '13時'), ('14時', '14時'), ('15時', '15時'), ('16時', '16時'), ('17時', '17時'), ('18時', '18時'), ('19時', '19時'), ('20時', '20時'), ('21時', '21時'), ('22時', '22時'), ('23時', '23時'), ('24時', '24時')], default='選択してください', max_length=3, verbose_name='予約希望時間')),
                ('reservation_minute', models.CharField(choices=[('00分', '00分'), ('15分', '15分'), ('30分', '30分'), ('45分', '45分')], default='選択してください', max_length=3, verbose_name='')),
                ('nop', models.IntegerField(verbose_name='予約人数')),
                ('menu1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_1', to='comp.menu', verbose_name='メニュー1')),
                ('menu2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_2', to='comp.menu', verbose_name='メニュー2')),
                ('menu3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_3', to='comp.menu', verbose_name='メニュー3')),
                ('menu4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_4', to='comp.menu', verbose_name='メニュー4')),
                ('menu5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='menu_5', to='comp.menu', verbose_name='メニュー5')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comp.store', verbose_name='店舗ID')),
                ('user_id', models.ForeignKey(blank=True, max_length=16, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザーID')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comp.store', verbose_name='店舗ID'),
        ),
        migrations.CreateModel(
            name='Kuchikomi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='評価点数')),
                ('impression', models.TextField(max_length=2000, verbose_name='評価内容')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comp.store', verbose_name='店舗ID')),
                ('user_id', models.ForeignKey(max_length=16, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザーID')),
            ],
        ),
    ]
