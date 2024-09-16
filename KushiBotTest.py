import speedtest

def print_ascii_art():
    print("""

   __ __         __   _ ___       __ ______        __ 
  / //_/_ _____ / /  (_) _ )___  / //_  __/__ ___ / /_
 / ,< / // (_-</ _ \/ / _  / _ \/ __// / / -_|_-</ __/
/_/|_|\_,_/___/_//_/_/____/\___/\__//_/  \__/___/\__/ 
                                                      

    """)

class KushiCheck:
    def __init__(self):
        pass

    def test_internet_speed(self):
        st = speedtest.Speedtest()
        st.get_best_server()

        # Obtenir le ping
        ping_result = st.results.ping

        # Tester la vitesse de téléchargement
        download_speed = st.download() / 1_000_000  # Convertir en Mbps

        # Tester la vitesse d'upload
        upload_speed = st.upload() / 1_000_000  # Convertir en Mbps

        # Afficher les résultats
        print(f"Ping : {ping_result:.2f} ms")
        print(f"Vitesse de téléchargement : {download_speed:.2f} Mbps")
        print(f"Vitesse de téléversement : {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    print_ascii_art()
    print("welecome to  KushiBotCheck!\n")
    
    checker = KushiCheck()
    print("Power test for bot....")
    checker.test_internet_speed()
