# Phi-3.5-mini-instruct Virtual Assistant 

## Step 1: Run Phi-3.5-mini-instruct on Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NeuralFalconYT/Phi-3.5-mini-instruct/blob/main/Phi_3_5_mini_instruct.ipynb) <br>
[Phi-3.5-mini-instruct Hugging Face](https://huggingface.co/microsoft/Phi-3.5-mini-instruct).

### Gradio Chat Interface
![chat](https://github.com/user-attachments/assets/88618a48-921c-4927-ac95-14dd17da20bb)
### Gradio API Interface
![api](https://github.com/user-attachments/assets/40a62200-d3ac-489c-85b7-2b0bdf1d7cfe)

## Step 2: Clone the Repository or Download ZIP
To clone the repository:
```
git clone https://github.com/NeuralFalconYT/Phi-3.5-mini-instruct.git
```
```
cd Phi-3.5-mini-instruct
```
Alternatively, download the ZIP file, extract the folder, and navigate to it:
```
cd Phi-3.5-mini-instruct
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

![3](https://github.com/user-attachments/assets/f0f64aea-09b1-4b49-b856-77481e3bb112)

![4](https://github.com/user-attachments/assets/22122dbf-0c1a-4927-a0e7-ac3bb8a603cd)

## Acknowledgments

I would like to express my sincere gratitude to the following people and organizations:
- **[hi-3.5-mini-instruct]**:[[Phi-3.5-mini-instruct](https://huggingface.co/microsoft/Phi-3.5-mini-instruct)].
- **[Anding Analytics]**: [[For Visualize Sound Code](https://youtu.be/675teI6-_-g?si=wT9mWgvrGRxasvNU)].


