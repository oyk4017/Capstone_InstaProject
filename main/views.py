from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
from urllib.parse import quote_plus

from .models import InsertDb # 모델에서 Resource를 불러온다


def get(request):
 #'광운대맛집': 'kw', '외대맛집': 'hufs', '경희대맛집': 'khu', '시립대맛집':'uos', '서울대맛집': 'snu', '홍대맛집': 'hu', '연대맛집': 'yon', '이대맛집': 'ewha', '한양대맛집':'hy', '건대맛집추천':'ku', '덕성여대맛집': 'dswu', '국민대맛집': 'kmu', '성신여대맛집': 'sswu', '한성대맛집':'hsu', '숙대맛집':'sook','고대맛집': 'kor','동덕여대맛집':'ddwu', '서울여대맛집':'swu', '서강대맛집':'sgu'
    insta = InsertDb.objects.all()
    insta_list = {'insta_list' : insta}
    #광운대
    kw = InsertDb.objects.filter(univ="광운대").order_by('-like_num')[:8]
    kw_list = {'kw_list' : kw}
    #한국외대
    hufs = InsertDb.objects.filter(univ="한국외대").order_by('-like_num')[:8]
    hufs_list = {'hufs_list' : hufs}
    #경희대
    khu = InsertDb.objects.filter(univ="경희대").order_by('-like_num')[:8]
    khu_list = {'khu_list' : khu}
    #서울시립대
    uos = InsertDb.objects.filter(univ="서울시립대").order_by('-like_num')[:8]
    uos_list = {'uos_list' : uos}
    #서울대
    snu = InsertDb.objects.filter(univ="서울대").order_by('-like_num')[:8]
    snu_list = {'snu_list' : snu}
    #홍익대
    hu = InsertDb.objects.filter(univ="홍익대").order_by('-like_num')[:8]
    hu_list = {'hu_list' : hu}
    #연세대
    yon = InsertDb.objects.filter(univ="연세대").order_by('-like_num')[:8]
    yon_list = {'yon_list' : yon}
    #이화여대
    ewha = InsertDb.objects.filter(univ="이화여대").order_by('-like_num')[:8]
    ewha_list = {'ewha_list' : ewha}
    #한양대
    hy = InsertDb.objects.filter(univ="한양대").order_by('-like_num')[:8]
    hy_list = {'hy_list' : hy}
    #건국대
    ku = InsertDb.objects.filter(univ="건국대").order_by('-like_num')[:8]
    ku_list = {'ku_list' : ku}
    #덕성여대
    dswu = InsertDb.objects.filter(univ="덕성여대").order_by('-like_num')[:8]
    dswu_list = {'dswu_list' : dswu}
    #국민대
    kmu = InsertDb.objects.filter(univ="국민대").order_by('-like_num')[:8]
    kmu_list = {'kmu_list' : kmu}
    #성신여대
    sswu = InsertDb.objects.filter(univ="성신여대").order_by('-like_num')[:8]
    sswu_list = {'sswu_list' : sswu}
    #한성대
    hsu = InsertDb.objects.filter(univ="한성대").order_by('-like_num')[:8]
    hsu_list = {'hsu_list' : hsu}
    #숙명여대
    sook = InsertDb.objects.filter(univ="숙명여대").order_by('-like_num')[:8]
    sook_list = {'sook_list' : sook}
    #고려대
    kor = InsertDb.objects.filter(univ="고려대").order_by('-like_num')[:8]
    kor_list = {'kor_list' : kor}
    #동덕여대
    ddwu = InsertDb.objects.filter(univ="동덕여대").order_by('-like_num')[:8]
    ddwu_list = {'ddwu_list' : ddwu}
    #서울여대
    swu = InsertDb.objects.filter(univ="서울여대").order_by('-like_num')[:8]
    swu_list = {'swu_list' : swu}
    #서강대
    sgu = InsertDb.objects.filter(univ="서강대").order_by('-like_num')[:8]
    sgu_list = {'sgu_list' : sgu}
    
    insta_list['kw']=kw
    insta_list['hufs']=hufs
    insta_list['khu']=khu
    insta_list['uos']=uos

    insta_list['snu']=snu
    insta_list['hu']=hu
    insta_list['yon']=yon
    insta_list['ewha']=ewha
    insta_list['hy']=hy
    insta_list['ku']=ku

    insta_list['dswu']=dswu
    insta_list['kmu']=kmu
    insta_list['sswu']=sswu
    insta_list['hsu']=hsu
    insta_list['sook']=sook

    insta_list['kor']=kor
    insta_list['ddwu']=ddwu
    insta_list['swu']=swu
    insta_list['sgu']=sgu

    return render(request, 'main/index.html',insta_list)