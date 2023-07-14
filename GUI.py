from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QComboBox
import tensorflow as tf
import numpy as np
import tensorflow_hub as hub
import tensorflow_text as text

print ("Loading Models.....")
Model2=tf.keras.models.load_model("./Bert_uncased_model_Tiwtter.h5",custom_objects={'KerasLayer':hub.KerasLayer})

Model1=tf.keras.models.load_model("./Bert_uncased_model_Reddit.h5",custom_objects={'KerasLayer':hub.KerasLayer})
classes=['Neutral', 'Positive', 'Negative']

def show_message():
    message = input_box.text()
    selected_option = dropdown.currentIndex()
    Model=Model2
    if (selected_option==1):
        Model=Model1
    ans=Model.predict([message])
    i=np.argmax(ans)
    catagorie=classes[i]
    percentage=str(int(ans[0][i]*100))+" %"
    show_text=catagorie+" - "+percentage
    label.setText(show_text)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Sentiment Analysis")
window.setFixedSize(600, 300)  # Set a fixed window size

layout = QVBoxLayout()

label1 = QLabel("Enter a text:")
label1.setFont(QFont("Arial", 14))  # Increase the font size
layout.addWidget(label1)

dropdown = QComboBox()
dropdown.addItem("Bert uncased model Tiwtter (Model 2)")
dropdown.addItem("Bert uncased model Reddit (Model 1)")
dropdown.setFont(QFont("Arial", 12))  # Increase the font size
layout.addWidget(dropdown)

input_box = QLineEdit()
input_box.setFont(QFont("Arial", 14))  # Increase the font size
layout.addWidget(input_box)

button = QPushButton("Classify")
button.clicked.connect(show_message)
button.setFont(QFont("Arial", 14))  # Increase the font size
layout.addWidget(button)

layout.addStretch()

label = QLabel("")
label.setFont(QFont("Arial", 12))  # Increase the font size
layout.addWidget(label)
label.setContentsMargins(150, 0, 250, 0)  # Add 15-pixel padding


layout.addStretch()  # Add a stretchable space at the end to center-align the widgets

window.setLayout(layout)
window.show()
app.exec_()
