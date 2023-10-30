import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"'{text_field.value}'"
        page.update()

    t=ft.Text()
    page.title = "Flet counter example"
    text_field=ft.TextField(label="Nombre", text_align="center", width=300) 
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(ft.Row(controls=[text_field,b,t]))
ft.app(target=main)




#Exercici 1: visualitzar noms de cada persona de la classe amb diferents colors
    #t = ft.Text(value="Hello, world!", color="green")
    #y = ft.Text(value="Francesc El millor profe del món",color="red")
    #page.controls.append(t)
    #page.controls.append(y)
    #page.update()


#Exercici 2: Enseñar a fer un contador fins a 9, i després l'heu de modificar fins a 100, i després 
#fer un temporizador de 100s
# t = ft.Text()
# t.color="red"
# page.add(t)
# for i in range(10):
#     t.value = f"Step {i}"
#     page.update()
#     time.sleep(1)
# pass


#Exercici 3: Estudiar les diferents files i com podem organitzar els textos

# page.add(
# ft.Row(controls=[
#     ft.Text("A"),
#     ft.Text("B"),
#     ft.Text("C")
# ]),
# ft.Row(controls=[
#     ft.Text("A"),
#     ft.Text("B"),
#     ft.Text("C")
# ]),
# ft.Row(controls=[
#     ft.TextField(label="Your name"),
#     ft.ElevatedButton(text="Say my name!")
# ])


#Exercici 4: Fer exercici de clicar un boto, i que surti un missatge per pantalla de que s'ha clicat
# def button_clicked(e):
#     page.add(ft.Text("Clicked!"))

# page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

#Exercici 5: Fer una llista de la compra fàcil
    # def add_clicked(e):
    #     page.add(ft.Checkbox(label=new_task.value))
    #     new_task.value = ""
    #     new_task.focus()
    #     new_task.update()
        

    # new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    # page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
    
    
#TESTING ON ANDROID

# python3 -m venv .venv
# source .venv/bin/activate


# pip install flet --upgrade


# flet --version


# flet create my-app
# cd my-app

# flet run --android


#TESTING ON IOS

