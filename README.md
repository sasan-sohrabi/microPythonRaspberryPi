
# 🖥️ MicroPython on Raspberry Pi Project

Welcome to the **MicroPython on Raspberry Pi** repository! This project is designed to explore the use of MicroPython on Raspberry Pi, enabling hardware programming for IoT and automation projects. 

## 📚 Key Features

- **MicroPython Setup**: Get MicroPython running on Raspberry Pi for various IoT applications.
- **GPIO Control**: Manage and control GPIO pins using MicroPython to interact with sensors, motors, and other components.
- **Automated Scripts**: Implement automation tasks such as lighting control, environmental monitoring, etc.
- **IoT Capabilities**: Explore the basics of IoT by connecting Raspberry Pi to the internet and sending/receiving data.

## 🛠️ Technologies Used

- **MicroPython**: A lightweight implementation of Python optimized for microcontrollers.
- **Raspberry Pi**: A low-cost, single-board computer used for hardware programming.
- **Libraries**: MicroPython-specific libraries for GPIO control, communication, and more.
  
## 🚀 Getting Started

### Prerequisites

Make sure you have the following hardware and software:

- **Raspberry Pi (any version)**.
- **MicroSD card** with Raspbian OS or similar OS installed.
- **MicroPython** installed on your Raspberry Pi.
- **Basic Electronics**: Sensors, LEDs, Resistors, Jumper Wires, etc.

### Installation Steps

1. **Set up your Raspberry Pi**:
   Install Raspbian or another suitable OS on your Raspberry Pi and ensure you have access to the terminal.
   
2. **Install MicroPython**:
   Follow the instructions to install MicroPython:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install --user mpremote
   ```

3. **Clone the repository**:
   ```bash
   git clone https://github.com/sasan-sohrabi/microPythonRaspberryPi.git
   ```

4. **Upload scripts to Raspberry Pi**:
   Navigate to the folder where the MicroPython scripts are located, then upload them using `mpremote`:
   ```bash
   mpremote connect /dev/ttyACM0 cp <script_name.py> :
   ```

5. **Run MicroPython scripts**:
   Run the scripts directly on your Raspberry Pi:
   ```bash
   mpremote connect /dev/ttyACM0 run <script_name.py>
   ```

## 💡 Usage

You can use this project for several purposes, such as:

- **Controlling GPIO pins**: Programmatically control Raspberry Pi’s GPIO pins to interact with external components (LEDs, motors, etc.).
- **Reading sensor data**: Read data from sensors like temperature, humidity, or motion sensors.
- **Automating tasks**: Create automated routines like turning lights on/off based on sensor input.

