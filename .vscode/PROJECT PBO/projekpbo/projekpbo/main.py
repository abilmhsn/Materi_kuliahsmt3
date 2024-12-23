from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


# Screen untuk Login
class LoginScreen(BoxLayout):
    def __init__(self, switch_screen_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.switch_screen_callback = switch_screen_callback

        self.add_widget(Label(text="Username:"))
        self.username_input = TextInput(hint_text="Masukkan Username", multiline=False)
        self.add_widget(self.username_input)

        self.add_widget(Label(text="Password:"))
        self.password_input = TextInput(hint_text="Masukkan Password", multiline=False, password=True)
        self.add_widget(self.password_input)

        self.login_button = Button(text="Login")
        self.login_button.bind(on_press=self.validate_login)
        self.add_widget(self.login_button)

    def validate_login(self, instance):
        # Validasi login sederhana
        username = self.username_input.text
        password = self.password_input.text

        if username == "admin" and password == "1234":
            self.switch_screen_callback("pemesanan")
        else:
            self.add_widget(Label(text="Login gagal. Coba lagi!", color=(1, 0, 0, 1)))


# Screen untuk Pemesanan Baju
class PemesananScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.add_widget(Label(text="Form Pemesanan Baju"))
        self.add_widget(Label(text="Nama Lengkap:"))
        self.nama_input = TextInput(hint_text="Masukkan Nama Lengkap", multiline=False)
        self.add_widget(self.nama_input)

        self.add_widget(Label(text="Alamat Email:"))
        self.email_input = TextInput(hint_text="Masukkan Email", multiline=False)
        self.add_widget(self.email_input)

        self.add_widget(Label(text="Pilih Baju:"))
        self.baju_spinner = TextInput(hint_text="Masukkan jenis baju (e.g., Jas Formal)", multiline=False)
        self.add_widget(self.baju_spinner)

        self.submit_button = Button(text="Kirim Pemesanan")
        self.submit_button.bind(on_press=self.submit_order)
        self.add_widget(self.submit_button)

    def submit_order(self, instance):
        nama = self.nama_input.text
        email = self.email_input.text
        baju = self.baju_spinner.text

        if nama and email and baju:
            print(f"Pemesanan berhasil: {nama}, {email}, {baju}")
            self.add_widget(Label(text="Pemesanan berhasil!", color=(0, 1, 0, 1)))
        else:
            self.add_widget(Label(text="Harap lengkapi semua data!", color=(1, 0, 0, 1)))


# Screen Manager untuk mengatur navigasi
class RentalScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.login_screen = Screen(name="login")
        self.login_screen.add_widget(LoginScreen(self.switch_screen))
        self.add_widget(self.login_screen)

        self.pemesanan_screen = Screen(name="pemesanan")
        self.pemesanan_screen.add_widget(PemesananScreen())
        self.add_widget(self.pemesanan_screen)

    def switch_screen(self, screen_name):
        self.current = screen_name


# Aplikasi utama
class RentalApp(App):
    def build(self):
        return RentalScreenManager()


if __name__ == "__main__":
    RentalApp().run()

