# Generated by Django 4.1.7 on 2023-04-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_yn', models.CharField(db_column='USE_YN', max_length=100, verbose_name='사용여부')),
                ('entry_id', models.CharField(db_column='ENTRY_ID', max_length=20, verbose_name='등록자')),
                ('entry_date', models.DateTimeField(db_column='ENTRY_DATE', verbose_name='등록일')),
                ('updat_id', models.CharField(blank=True, db_column='UPDAT_ID', max_length=20, null=True, verbose_name='수정자')),
                ('updat_date', models.DateTimeField(blank=True, db_column='UPDAT_DATE', null=True, verbose_name='수정일')),
                ('type', models.CharField(db_column='TYPE', max_length=1, verbose_name='종류')),
                ('date', models.CharField(db_column='DATE', max_length=10, verbose_name='날짜')),
                ('schedule', models.CharField(db_column='SCHEDULE', max_length=100, verbose_name='일정')),
                ('loc', models.CharField(db_column='LOC', max_length=100, verbose_name='지역')),
                ('day', models.CharField(db_column='DAY', max_length=100, verbose_name='숙박일수')),
                ('hotel', models.CharField(db_column='HOTEL', max_length=100, verbose_name='호텔')),
                ('remark', models.CharField(db_column='REMARK', max_length=1000, verbose_name='REMARK')),
            ],
            options={
                'verbose_name': '수배내역 상세 ',
                'verbose_name_plural': '수배내역 상세목록',
                'db_table': 'booking_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookingMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_yn', models.CharField(db_column='USE_YN', max_length=100, verbose_name='사용여부')),
                ('entry_id', models.CharField(db_column='ENTRY_ID', max_length=20, verbose_name='등록자')),
                ('entry_date', models.DateTimeField(db_column='ENTRY_DATE', verbose_name='등록일')),
                ('updat_id', models.CharField(blank=True, db_column='UPDAT_ID', max_length=20, null=True, verbose_name='수정자')),
                ('updat_date', models.DateTimeField(blank=True, db_column='UPDAT_DATE', null=True, verbose_name='수정일')),
                ('ref', models.CharField(db_column='REF', max_length=100, verbose_name='ref')),
                ('product_name', models.CharField(db_column='PRODUCT_NAME', max_length=100, verbose_name='상품명')),
                ('url', models.CharField(db_column='URL', max_length=100, verbose_name='url')),
                ('kor_air_def', models.CharField(db_column='KOR_AIR_DEF', max_length=100, verbose_name='한국 출발일')),
                ('kor_air', models.CharField(db_column='KOR_AIR', max_length=100, verbose_name='한국 항공편')),
                ('kor_air_in', models.CharField(db_column='KOR_AIR_IN', max_length=100, verbose_name='한국 출발 공항')),
                ('kor_air_out', models.CharField(db_column='KOR_AIR_OUT', max_length=100, verbose_name='한국 도착 공항')),
                ('kor_air_time_dep', models.CharField(db_column='KOR_AIR_TIME_DEP', max_length=100, verbose_name='한국 출발시간')),
                ('kor_air_time_arri', models.CharField(db_column='KOR_AIR_TIME_ARRI', max_length=100, verbose_name='한국 도착시간')),
                ('loc_air_def', models.CharField(db_column='LOC_AIR_DEF', max_length=100, verbose_name='현지 출발일')),
                ('loc_air', models.CharField(db_column='LOC_AIR', max_length=100, verbose_name='현지 항공편')),
                ('loc_air_in', models.CharField(db_column='LOC_AIR_IN', max_length=100, verbose_name='현지 출발 공항')),
                ('loc_air_out', models.CharField(db_column='LOC_AIR_OUT', max_length=100, verbose_name='현지 도착 공항')),
                ('loc_air_time_dep', models.CharField(db_column='LOC_AIR_TIME_DEP', max_length=100, verbose_name='현지 출발시간')),
                ('loc_air_time_arri', models.CharField(db_column='LOC_AIR_TIME_ARRI', max_length=100, verbose_name='현지 도착시간')),
                ('breakfase', models.CharField(db_column='BREAKFAST', max_length=100, verbose_name='아침')),
                ('lunch', models.CharField(db_column='LUNCH', max_length=100, verbose_name='점심')),
                ('dinner', models.CharField(db_column='DINNER', max_length=100, verbose_name='저녁')),
                ('special', models.CharField(db_column='SPECIAL', max_length=1000, verbose_name='특식')),
                ('option', models.CharField(db_column='OPTION', max_length=1000, verbose_name='옵션')),
                ('shopping', models.CharField(db_column='SHOPPING', max_length=1000, verbose_name='쇼핑')),
                ('entrance', models.CharField(db_column='ENTRANCE', max_length=100, verbose_name='입장지')),
                ('bus', models.CharField(db_column='BUS', max_length=1000, verbose_name='버스')),
                ('kor_guide', models.CharField(db_column='KOR_GUIDE', max_length=1000, verbose_name='가이드')),
                ('loc_guide', models.CharField(db_column='LOC_GUIDE', max_length=1000, verbose_name='현지 가이드')),
                ('remark', models.CharField(db_column='REMARK', max_length=1000, verbose_name='REMARK')),
            ],
            options={
                'verbose_name': '수배내역',
                'verbose_name_plural': '수배내역 목록',
                'db_table': 'booking_master',
                'managed': False,
            },
        ),
    ]
