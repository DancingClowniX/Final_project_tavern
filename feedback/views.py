from django.shortcuts import render
from feedback.forms import *
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import datetime

@login_required
def feedback(request):
    # передать в шаблон
    data = {
        'add_feedback_form': AddFeedbackForm()
    }
    if request.method == 'POST':
        # ------------------- CREATE ---------------------#
       # text_feedback = request.POST.get('text')
       # Feedback.objects.create(text=text_feedback)

        form = AddFeedbackForm(request.POST, request.FILES) # словарь со всеми параметрами запроса
        if form.is_valid():
            form.save()
            return HttpResponse(f"""
            <h2>Ваш отзыв успешно отправлен</h2>
            <a href=""><button>Вернуться на страницу с отзывами</button></a>
    """)

        form.add_error(None, "Ошибка добавления данных")
        data[ 'add_feedback_form'] = form
        return render(request, 'feedback.html', data)


    elif request.method == 'GET':
        # ------------------- READ ---------------------#


        return render(request, 'feedback.html', data)


@login_required
def editFeedback(request, feedback_id):
    feedbackData = Feedback.objects.get(id=feedback_id)
    # отобразить инфомарцию о текущем отзыве
    data = {"id": feedback_id,
            "text": feedbackData.text,
            'add_feedback_form': AddFeedbackForm(),
            "date_created": feedbackData.date_created}
    if request.method == "GET":

        # отобразить форму
        return render(request, 'editFeedback.html', data)

    # ------------------- UPDATE ---------------------#
    if request.method == 'POST':
        # обработать редактирование
        form = AddFeedbackForm(request.POST)  # словарь со всеми параметрами запроса
        if form.is_valid():
            feedbackData.text = request.POST.get('text')# заменить на form , сейчас вместо редактирования создает новый отзыв
            feedbackData.rating = request.POST.get('rating')#
            feedbackData.date_updated = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            feedbackData.save()
            return HttpResponseRedirect("../../")

        form.add_error(None, "Ошибка добавления данных")
        data['add_feedback_form'] = form
        return render(request, 'editFeedback.html', data)



# удаление данных из бд
@login_required
def deleteFeedback(request, feedback_id):
    try:
        Feedback.objects.get(id=feedback_id).delete()
        return HttpResponseRedirect("../../") # возвращаемся на главную страницу приложения
    except Feedback.DoesNotExist:
        return HttpResponseNotFound("""
        <h2>Такой отзыв не был найден</h2>
          <a href="../../"><button>Вернуться на страницу с отзывами</button></a>
        """)