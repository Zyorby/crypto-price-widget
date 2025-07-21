import customtkinter as ctk
import requests


# CustomTkinter example application
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")

        self.button = ctk.CTkButton(self, text="my button", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")

app = App()
app.mainloop()


#testing coingecko API
url = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=amp-token&names=AMP&symbols=amp&include_market_cap=false&include_24hr_change=true"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
print(response.text)