from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
import re

class CalculatorApp(App):
    def build(self):
        # Set window size for better mobile experience
        Window.size = (400, 600)
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Display area
        self.display = TextInput(
            multiline=False,
            readonly=True,
            font_size=40,
            halign='right',
            foreground_color=(0, 1, 0, 1),  # Green text
            background_color=(0, 0, 0, 1),  # Black background
            size_hint_y=None,
            height=100
        )
        
        main_layout.add_widget(self.display)
        
        # Button layout (grid for calculator buttons)
        button_layout = GridLayout(cols=4, spacing=10, size_hint_y=2)
        
        # Define buttons
        buttons = [
            'C', 'CE', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '00', '0', '.', '='
        ]
        
        # Add buttons to grid
        for button_text in buttons:
            button = Button(
                text=button_text,
                font_size=30,
                background_color=self.get_button_color(button_text)
            )
            
            # Bind button press to function
            button.bind(on_press=lambda instance: self.on_button_click(instance.text))
            button_layout.add_widget(button)
        
        main_layout.add_widget(button_layout)
        
        return main_layout
    
    def get_button_color(self, text):
        """Return different colors for different types of buttons"""
        if text in ['+', '-', '*', '/', '=', '%']:
            return (1, 0.5, 0, 1)  # Orange for operators
        elif text == 'C' or text == 'CE':
            return (1, 0, 0, 1)  # Red for clear buttons
        else:
            return (0.5, 0.5, 0.5, 1)  # Gray for numbers
    
    def on_button_click(self, button_text):
        """Handle button clicks"""
        current = self.display.text
        
        if button_text == 'C':
            # Clear everything
            self.display.text = ''
        elif button_text == 'CE':
            # Clear last entry
            self.display.text = current[:-1]
        elif button_text == '=':
            # Calculate result using safer evaluation
            try:
                result = self.evaluate_expression(current)
                self.display.text = str(result)
            except Exception:
                self.display.text = 'Error'
        elif button_text == '%':
            # Handle percentage
            try:
                result = self.evaluate_expression(current) / 100
                self.display.text = str(result)
            except Exception:
                self.display.text = 'Error'
        else:
            # Append button text to display
            self.display.text = current + button_text

    def evaluate_expression(self, expression):
        """Safely evaluate a mathematical expression"""
        # Remove any spaces
        expression = expression.replace(' ', '')
        
        # Replace display symbols with Python operators
        expression = expression.replace('×', '*').replace('÷', '/')
        
        # Validate the expression contains only allowed characters
        if not re.match(r'^[0-9+\-*/%.]+$', expression):
            raise ValueError("Invalid characters in expression")
        
        # Check for valid syntax (basic validation)
        if '..' in expression:
            raise ValueError("Invalid decimal format")
        
        # Use eval with a restricted namespace for safety
        allowed_names = {
            "__builtins__": {},
            "abs": abs,
            "round": round,
        }
        
        result = eval(expression, allowed_names)
        
        # Format result to avoid very long decimals
        if isinstance(result, float) and result.is_integer():
            return int(result)
        elif isinstance(result, float):
            # Limit decimal places to avoid floating point precision issues
            return round(result, 10)
        else:
            return result


if __name__ == '__main__':
    CalculatorApp().run()