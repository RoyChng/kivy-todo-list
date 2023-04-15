from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField

class MainApp(MDApp):
    dialog = None
    tasks = [
         "Walk the dog",
         "Purchase books",
         "Wrap Christmas presents",
         "Prepare dinner",
         "Attend meeting"
    ]
    def build(self):
            return Builder.load_file("todolist.kv")
    
    def save_todo_item(self, _):
        if not self.dialog: return
        text = self.content.text
        self.root.ids.todo_list.add_widget(
                OneLineListItem(text=text)
        )
        self.tasks.append(text)
        self.dialog.dismiss()

    def close_dialog(self, _):
        if not self.dialog: return
        self.dialog.dismiss()
    
    def show_dialog(self):
        if not self.dialog:
            dialog = BoxLayout(orientation="horizontal", spacing="12dp", size_hint_y=None, height="80dp")
            self.content = MDTextField(hint_text="Task")
            dialog.add_widget(self.content)
            self.dialog = MDDialog(
                title="Add Task:",
                type="custom",
                content_cls=dialog,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press = self.close_dialog
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press = self.save_todo_item
                    ),
                ],
            )
        else: 
             self.content.text = ""
        self.dialog.open()
    
    def on_start(self):
           for task in self.tasks:
            self.root.ids.todo_list.add_widget(
                OneLineListItem(text=task)
            )
        
if __name__ == "__main__":
      MainApp().run()
    