# Use Any LLM as Voice Assistant 

## Step 1: Run any LLM on Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuralFalconYT/Voice-Assistant-Template/blob/main/Gradio_Server_Template.ipynb) <br>

### Gradio API Interface

![app](https://github.com/user-attachments/assets/0d5c8834-79c6-4da7-b553-e1c944f8e69d)

## Step 2: Clone the Repository or Download ZIP
To clone the repository:
```
git clone https://github.com/NeuralFalconYT/Voice-Assistant-Template.git
```
```
cd Voice-Assistant-Template
```
Alternatively, download the ZIP file, extract the folder, and navigate to it:
```
cd Voice-Assistant-Template
```
## Step 3: Install Required Packages
My Python version is ```Python 3.10```<br>
Install the necessary packages:
```
pip install -r requirements.txt
```
```
pip install PyAudio
```
[Fix PyAudio Installation Error](https://youtu.be/rIFL4vtX0iA?si=jtJwhCOAN5Okx8J-)
## Step 4: Create a .env File
Create a .env file and paste your username and password from the Colab notebook. 
![colab](https://github.com/user-attachments/assets/20c36df7-056d-48b5-b512-74f1285e8822)

The format should be:
```
USERNAME=admin
PASSWORD=admin
```
## Step 5: Run the GUI
You can use this template for any chatbot hosted on Gradio, where you have 'system role' and 'user message' as inputs and the model's response as the output.

To start the GUI, run:
```
python GUI.py
```
![app](https://github.com/user-attachments/assets/d6ae3efb-d194-46f5-bec8-4361025ba96e)

#### App URL:
You can find the App URL in the Colab Notebook.
![colab](https://github.com/user-attachments/assets/20c36df7-056d-48b5-b512-74f1285e8822)
#### System Role:
Enter your desired system role.
#### Language:
Select the language in which you want to communicate.
#### Gender:
Select the Gender for Edge Text to Speech.

Click the ```Start``` button to begin interacting with the virtual assistant.
Click the ```Stop``` button to end the interaction. Please note that it might take some time for the process to stop — just be patient.
## Step 6: Get Talking Head Avatar (Optional)
![Talking_Head_Avatar](https://github.com/user-attachments/assets/b1ea8927-f622-4b84-933e-13481a9ec199)<br>
Download [VMagicMirror](https://malaybaku.github.io/VMagicMirror/en/)<br>
Set up a VTUBER model & lip sync mic as Stereo Mix (Realtek(R) Audio)
## Step 7: Uninstall (Optional)
To uninstall, run:
```
pip uninstall -r requirements.txt
```
Then, delete the folder.
###### You can add your own TTS if you don't want to use Edge TTS. For that, you need to write code and either spend money to buy an API or use a faster open-source TTS.

![1](https://github.com/user-attachments/assets/9daef4b4-8d83-4b05-88ae-dd728cb22963)

![2](https://github.com/user-attachments/assets/3952d198-e78c-4d61-8cbd-372a9c806ca0)

![3](https://github.com/user-attachments/assets/4d355e0b-1317-45bd-81a6-8e192cd3c6c0)

![4](https://github.com/user-attachments/assets/22122dbf-0c1a-4927-a0e7-ac3bb8a603cd)

## Acknowledgments
- **[Anding Analytics]**: [[For Visualize Sound Code](https://youtu.be/675teI6-_-g?si=wT9mWgvrGRxasvNU)].


