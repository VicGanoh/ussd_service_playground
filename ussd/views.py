from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def ussd_app(request):

    if request == "POST":
        session_id = request.POST.get("sessionID")
        user_id = request.POST.get("userID")
        new_session = request.POST.get("newSession")
        phone_number = request.POST.get("msisdn")
        network_provider = request.POST.get("network")
        user_data = request.POST.get("userData")

        logging.info("session id %s", session_id)
        logging.info("user id %s", user_id)
        logging.info("phone_number %s", phone_number)
        logging.info("user_data %s", user_data)
        logging.info("new_session %s", new_session)
        logging.info("network_provider %s", network_provider)


        response: str = ""

        if user_data == "":
            response = "Welcome to THE POLL \nPlease select an option"
            response += "1. View Poll"
            response += "2.Vote"
            response += "3. View Results"
        elif user_data == "1":
            response = "Poll Options"
            response += "1. John Paul"
            response += "2. Thomas Nketia"
            response += "3. Henry Baal"
        elif user_data == "2":
            response = " Choose your candidate"
            response += "1. John Paul"
            response += "2. Thomas Nketia"
            response += "3. Henry Baal"
        elif user_data == "2*1":
            response = "Successfully voted for John Paul"
        elif user_data == "2*2":
            response = "Successfully voted for Thomas Nketia"
        elif user_data == "2*3":
            response = "Successfully voted for Henry Baal"
        elif user_data == "3":
            response = "Poll Results"
            response += "1. John Paul - 50%"
            response += "2. Thomas Nketia - 30%"
            response += "3. Henry Baal - 20%"
            response += "Thank you."
        
        return HttpResponse(response)
    return HttpResponse("Hello, world. You're at the polls index.")


