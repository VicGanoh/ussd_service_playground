from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def index(request):

    if request == "POST":
        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number = request.POST.get("phoneNumber")
        text = request.POST.get("text")

        logging.info("session id %s", session_id)
        logging.info("service code %s", service_code)
        logging.info("phone_number %s", phone_number)
        logging.info("text %s", text)


        response: str = ""

        if text == "":
            response = "CON Welcome to THE POLL \nPlease select an option"
            response += "1. View Poll"
            response += "2.Vote"
            response += "3. View Results"
        elif text == "1":
            response = "END Poll Options"
            response += "1. John Paul"
            response += "2. Thomas Nketia"
            response += "3. Henry Baal"
        elif text == "2":
            response = " Choose your candidate"
            response += "1. John Paul"
            response += "2. Thomas Nketia"
            response += "3. Henry Baal"
        elif text == "2*1":
            response = "END Successfully voted for John Paul"
        elif text == "2*2":
            response = "END Successfully voted for Thomas Nketia"
        elif text == "2*3":
            response = "END Successfully voted for Henry Baal"
        elif text == "3":
            response = "END Poll Results"
            response += "1. John Paul - 50%"
            response += "2. Thomas Nketia - 30%"
            response += "3. Henry Baal - 20%"
            response += "Thank you."
        
        return HttpResponse(response)


