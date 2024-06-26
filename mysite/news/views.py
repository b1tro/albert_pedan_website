from django.shortcuts import render
from .models import News

def main_page(request):
    page_name = "МКУ г. Казань"
    title = 'УПРАВЛЕНИЕ ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ И СВЯЗИ Г. КАЗАНИ'
    text = ('Добро пожаловать на сайт управления информационных технологий и связи г. Казань! '
            'Мы являемся ведущей компанией в области разработки и внедрения IT-решений на территории республики Татарстан. '
            'Наша цель - помочь нашим клиентам оптимизировать процессы связи и информационных технологий для повышения эффективности и конкурентоспособности их бизнеса. Мы предлагаем широкий спектр услуг, начиная от создания и развития веб-сайтов, разработки мобильных приложений, до внедрения сложных корпоративных информационных систем. Наша команда специалистов обладает высоким уровнем квалификации и опыта, что позволяет нам решать даже самые сложные задачи в области IT и связи. Мы стремимся к постоянному развитию и совершенствованию наших услуг, следуя последним тенденциям и технологиям в сфере информационных технологий. Мы гордимся своими успешными проектами и довольными клиентами, которые доверяют нам свои задачи и предпочитают нас другим компаниям. Если Вам нужна качественная разработка IT-проекта или консультации по управлению информационными технологиями, обращайтесь к нам - мы поможем воплотить ваши идеи в жизнь!')
    return render(request, "main.html", {
        'title': title,
        'text': text,
        'page_name': page_name,
    })

def news(request):
    news = News.objects.all()
    page_name = 'Новости'
    return render(request, "news.html", {'page_name': page_name,
                                                                'title': page_name,
                                                                'news': news})
def about(request):
    page_name = 'Контакты'
    return render(request, "about.html", {'page_name': page_name,
                                         'title': page_name})