from telegram import Bot
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Employee
import requests

def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})


def send_telegram_message(request):
    if request.method == 'POST':
        message = request.POST['message']
        bot = Bot(token=settings.TELEGRAM_TOKEN)

        employees = Employee.objects.all()


        for employee in employees:
            try:
                response = requests.post(settings.TELEGRAM_URL + '/sendMessage', data={
                    'chat_id': employee.telegram_id,
                    'text': message,
                    'parse_mode': "Markdown"
                })

                print(response.json())

                print(f"Сообщение отправлено пользователю: {employee.full_name}")
            except Exception as e:
                print(f"Ошибка при отправке сообщения пользователю {employee.full_name}: {e}")

        return redirect('index')
