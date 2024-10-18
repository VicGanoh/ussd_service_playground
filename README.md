# USSD Playground

This project implements a USSD-based polling portal using the [Arkesel USSD API](https://developers.arkesel.com/) and their USSD app simulator for testing. It allows users to view poll options, vote for candidates, and check poll results through an interactive USSD menu.
Tested locally with [ngrok](https://www.ngrok.com)

## Features
- View poll options
- Vote for candidates
- Check poll results
- Navigate using USSD menus with `*` to go back

## Tech Stack
- **Python**: Backend API logic
- **Django/DRF**: Web framework for building APIs
- **Arkesel USSD API**: For sending and receiving USSD messages
- **ngrok**: Exposes local development server to Arkesel for testing
- **Cache/State Management**: Used to track user session data and responses

## Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/VicGanoh/ussd_service_playground.git
   cd ussd-service

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Expose your local server using ngrok
   - Install ngrok from [here](https://www.ngrok.com).
   - Run ngrok to expose your Django server to the internet:
     ```bash
     ngrok http 8000

## Arkesel API Setup
- Sign up at the Arkesel Developer Portal.
- Download the arkesel ussd simulator app and configure. Check it out [here](https://developers.arkesel.com/#tag/Overview)
- Set your ngrok public URL as the callback URL in your Arkesel account settings.

## Testing the Project Locally with Arkesel
- Use Arkesel’s USSD simulator or your mobile device to dial the USSD code (e.g., *928*93#) and follow the menu.
- Ngrok will forward the USSD requests from Arkesel to your local machine, allowing you to test your project in real-time.
