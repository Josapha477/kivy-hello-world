from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HelloWorldApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.message = Label(
            text="Hello World!",
            font_size="32sp",
            bold=True
        )

        button = Button(
            text="Cliquer ici",
            font_size="20sp",
            size_hint=(1, 0.25)
        )

        button.bind(on_press=self.change_message)

        layout.add_widget(self.message)
        layout.add_widget(button)

        return layout

    def change_message(self, instance):
        self.message.text = "Bienvenue dans Kivy !"


if __name__ == "__main__":
    HelloWorldApp().run()
