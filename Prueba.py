import tkinter as tk
from tkinter import ttk

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class MyApp:
    def __init__(self, root):
        self.root = root
        self.questions = [
            "Pregunta 1",
            "Pregunta 2",
            "Pregunta 3",
            "Pregunta 4",
            "Pregunta 5",
            "Pregunta 6",
            "Pregunta 7",
            "Pregunta 8",
            "Pregunta 9",
            "Pregunta 10",
            "Pregunta 11",
            "Pregunta 12",
            "Pregunta 13"
        ]
        self.responses = {}

        scrollable_frame = ScrollableFrame(root)
        scrollable_frame.pack(side="top", fill="both", expand=True)

        # Crear botones para cada pregunta
        for i, question in enumerate(self.questions):
            label = tk.Label(scrollable_frame.scrollable_frame, text=question)
            label.pack()

            yes_button = tk.Button(scrollable_frame.scrollable_frame, text="Sí", command=lambda i=i: self.set_response(i, 'Sí'))
            yes_button.pack()

            no_button = tk.Button(scrollable_frame.scrollable_frame, text="No", command=lambda i=i: self.set_response(i, 'No'))
            no_button.pack()

        # Crear un botón para mostrar todas las respuestas
        self.show_responses_button = tk.Button(root, text="Mostrar respuestas", command=self.show_responses)
        self.show_responses_button.pack()

    def set_response(self, index, response):
        self.responses[index] = response

    def show_responses(self):
        for i, response in self.responses.items():
            print(f"Pregunta {i+1}: {response}")

root = tk.Tk()
app = MyApp(root)
root.mainloop()