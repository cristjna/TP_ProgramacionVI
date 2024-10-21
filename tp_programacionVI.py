import flet as ft

def main(page):
    # Configuraciones iniciales de la página
    page.title = "Lista de Compras"
    page.window_width = 600
    page.window_height = 400
    page.scroll = "adaptive"
    page.bgcolor = "#2C1A47"  # Fondo morado oscuro para la temática de Halloween

    # Lista para almacenar las tareas y el elemento seleccionado para modificar
    tasks = []  # Almacena los objetos de cada tarea (Checkbox)
    selected_task = None  # Variable para guardar la tarea que se desea modificar

    # Función para agregar una tarea
    # 1. he agregado una función para manejar el evento de clic en el botón "Agregar".
    #    Esta función toma el valor ingresado en el campo de texto y lo añade a una lista de tareas.
    def add_clicked(e):
        if new_task.value:
            # 2. Ahora, las tareas se añaden con un Checkbox que incluye el texto ingresado.
            #    Además, se le ha añadido un color de marca de verificación y estilo de texto.
            task = ft.Checkbox(
                label=new_task.value, 
                check_color="#FF7518",  # Naranja para la marca de verificación (temática Halloween)
                label_style=ft.TextStyle(color="#FFFFFF")  # Texto de la tarea en blanco
            )
            tasks.append(task)
            task_list.controls.append(
                ft.Row([
                    task, 
                    # 3. he añadido un botón para eliminar cada tarea de la lista con un ícono de basura.
                    ft.IconButton(
                        ft.icons.DELETE, 
                        on_click=lambda e, t=task: delete_task(t), 
                        icon_color="#FF7518"  # Naranja para el ícono de eliminar
                    )
                ])
            )
            # Limpiar el campo de texto después de agregar una tarea
            new_task.value = ""
            new_task.focus()
            page.update()

    # Función para eliminar una tarea
    # 4. he agregado esta función para manejar la eliminación de una tarea cuando se hace clic en el ícono de basura.
    def delete_task(task):
        tasks.remove(task)
        task_list.controls = [
            ft.Row([
                t, 
                ft.IconButton(
                    ft.icons.DELETE, 
                    on_click=lambda e, t=t: delete_task(t), 
                    icon_color="#FF7518"
                )
            ]) for t in tasks
        ]
        page.update()

    # Función para seleccionar una tarea y modificar su texto
    # 5. Añadí esta función para permitir que el usuario seleccione una tarea y la edite.
    def modify_clicked(e):
        nonlocal selected_task
        for task in tasks:
            if task.value:
                selected_task = task
                new_task.value = task.label
                new_task.focus()
                page.update()
                break

    # Función para guardar los cambios de una tarea seleccionada
    # 6. he creado esta función para guardar las modificaciones realizadas en la tarea seleccionada.
    def save_clicked(e):
        nonlocal selected_task
        if selected_task and new_task.value:
            selected_task.label = new_task.value
            new_task.value = ""
            selected_task = None
            page.update()

    # Cambiar color de fondo al pasar el mouse
    # 7. Agregué esta función para que los botones cambien de color al pasar el mouse por encima, mejorando la experiencia del usuario.
    def change_button_color(e, button, color):
        button.bgcolor = color
        page.update()

    # 8. Elementos de la interfaz se han modificado para incluir más botones y un nuevo campo de texto.
    new_task = ft.TextField(
        hint_text="Guárdalo antes de que desaparezca...", 
        width=300, 
        bgcolor="#4B3060",  # Fondo morado suave para el campo de texto
        color="#FFFFFF"  # Texto blanco para el campo de texto
    )
    
    button_color = "#FF7518"  # Naranja brillante para los botones
    hover_color = "#D35400"  # Naranja más oscuro para hover

    # 9. he creado tres botones para agregar, modificar y guardar.
    add_button = ft.ElevatedButton(
        "Agregar", 
        on_click=add_clicked, 
        bgcolor=button_color,  # Botón naranja brillante
        color="#000000"  # Texto negro para contraste
    )
    modify_button = ft.ElevatedButton(
        "Modificar", 
        on_click=modify_clicked, 
        bgcolor=button_color,  # Botón naranja brillante
        color="#000000"
    )
    save_button = ft.ElevatedButton(
        "Guardar", 
        on_click=save_clicked, 
        bgcolor=button_color,  # Botón naranja brillante
        color="#000000"
    )

    # Añadir eventos de mouse para cambiar el color de los botones
    add_button.on_mouse_enter = lambda e: change_button_color(e, add_button, hover_color)
    add_button.on_mouse_leave = lambda e: change_button_color(e, add_button, button_color)
    
    modify_button.on_mouse_enter = lambda e: change_button_color(e, modify_button, hover_color)
    modify_button.on_mouse_leave = lambda e: change_button_color(e, modify_button, button_color)
    
    save_button.on_mouse_enter = lambda e: change_button_color(e, save_button, hover_color)
    save_button.on_mouse_leave = lambda e: change_button_color(e, save_button, button_color)
    
    # 10. he agregado un logo y un mensaje de bienvenida dentro de un contenedor, ajustando el texto y el tamaño.
    logo = ft.Image(src="./logo3.png", width=100, height=100)
    header_text = ft.Text(
        "¡Bienvenidos a la Lista de Compras de Halloween!", 
        size=20, 
        weight=ft.FontWeight.BOLD,
        color="#FF7518"  # Naranja para el texto de la bienvenida
    )
    header = ft.Row(
        [logo, header_text],
        alignment="center"
    )

    # 11. he agregado un contenedor para mostrar la lista de tareas guardadas.
    task_list = ft.Column(spacing=5)

    # 12. Contenedor principal para organizar los elementos de la interfaz.
    content = ft.Container(
        content=ft.Column(
            [
                header,
                ft.Divider(height=20, color="#FF7518"),  # Divisor naranja
                new_task,
                ft.Divider(height=20, color="#FF7518"),
                task_list,  # Aquí se mostrarán las tareas agregadas
                ft.Divider(height=20, color="#FF7518"),
                ft.Row(
                    [
                        add_button,
                        modify_button,
                        save_button
                    ],
                    alignment="center",
                    spacing=10
                ),
            ],
            alignment="center",
            spacing=10
        ),
        alignment=ft.alignment.center,
        expand=True
    )

    # 13. finalmente, agrego el contenedor principal a la página.
    page.add(content)

ft.app(main)
