Andrew Ho, Tu Yu Hsien, Jessica Bojorquez


### 1. Abstract
A new gesture based embedded system is proposed that acts as an alternative assistive input for personal computers (PCs). The sensor inputs from a web camera and Arduino are collected by a Raspberry Pi, where image recognition and data processing is performed in real time, and corresponding events are sent to the PC wirelessly to realize with minimal delay. This system is a standalone device that consists of the Raspberry Pi, Arduino and a web camera as aforementioned, and includes BLE and Wi-Fi connectivity. On the PC side, users are able to specify the mapping of specific functionalities and keystrokes to the recognized gestures, allowing for customization based on their preferences and common actions. Although similar systems have been implemented before, the novelties in the system proposed are the use of video for gesture input instead of ultrasonic data, the customizability of control tailored to each user, and the portability of the wireless device.

### 2. Introduction and Proposal
As computer usage has increased due to the move to remote learning and
working, methods to improve workflow through human computer interaction can be explored. One method of doing so is to enhance the methods of input for personal computers. For certain tasks, instead of using a conventional mouse and keyboard, which can be performed through a tedious series of clicks or a complicated keyboard shortcut for performing simple tasks, such as controlling music playback or capturing a screenshot. Therefore, this project explores the possibility of using gesture and other sensor-based input methods through the use of a separate embedded companion device. This device should allow for controls of computer functionalities through simple gestures recognized by the camera, which is parsed on device locally and transmitted through a command to the computer. 

The device is composed of four components: the main personal computer, Raspberry Pi, Arduino Nano 33 BLE Sense, and a USB web camera. The following figure below demonstrates the interaction between them:

![alt text](https://user-images.githubusercontent.com/73715503/98816959-62ed9900-2464-11eb-850f-447bb0f56d50.PNG)


The Raspberry Pi acts as a central control for the system, and the web camera and Arduino are connected to the Raspberry Pi to feed inputs into it. The Raspberry Pi takes in the continuous video stream of the web camera and sensor data and continuously runs static image recognition with OpenCV. This is done locally to reduce the processing load on the PC and prevent any heavy network usage when unneeded. Sensors on the Arduino are used to assist with the gesture controls, most importantly preventing false positives in triggering of recognition, which can be activated through the detection of a hand with the proximity sensor or a voice activated method, which would require an either an outgoing internet connection to call voice recognition APIs or be performed locally. 

Once a gesture is detected, it performs the specified task previously defined by the user, by default sending a set of keystrokes to the computer, which recognizes the Raspberry Pi as a keyboard input source. Examples of this flow would be to map gestures to perform screenshots, control online presentation slides, mute and unmute video calls, adjust volume, and play, pause, and other actions in regards to multimedia playback. These specific settings are stored on the Raspberry Pi and can be accessed through the PC to adjust them. 

### 3. Prior Works
#### A basic hand gesture control system for PC applications
This paper explores the problems that can come up when exploring computer applications that are controlled via gestures that are both composed of static symbols and dynamic motions [1]. The dynamic motion model they use in this paper is done in real time and with a linear-in-parameter dynamic system, which is a linear state space model whose dynamics vary as a function of certain time-varying parameters called scheduling parameters. Some of the computer programs that this paper aims to control with hand gestures are browsers and PowerPoint, but they express that this can be expanded to other applications and other I/O forms as well, such as mouse, keyboard and voice. Some of the benefits of such system are that these interfaces can by used by the many people who cannot adequately use typical computer interaction techniques, while at a low common cost.

#### Arduino based Hand Gesture Control of Your Computer
This is a project that use an Arduino to implement a hand getsture control. Some of the functionality they experimented with was switching between tabs, scrolling on a webpage, shifting between applications, and video commands. Ultrasonic Sensors, an Arduino, and a few connecting wires were used to detect hand gestures and feed into the computer. The program ran by the arduino used in this project converts distances measured by the sensors and applies them to the appropiate commands. Some of the complications they found were the distance between the hand gesture and the Ultrasonic Sensors. [2]

#### Robust Part-Based Hand Gesture Recognition Using Kinect Sensor 
This prior work focuses on building a robust part-based hand gesture recognition systems using Kinect sensor [3]. As stated in this prior work ", the hand is a smaller object with more complex articulations and more easily affected by segmentation errors", hence this paper explores potential solutions for some of these errors. This paper also attempts to solve the problem of differnt hand shapes by applying the distance metric, Finger-Earth Mover's Distance. The Finger-Earth Mover's Distance is a distance metric that treats each finger as a cluster and penalize the empty finger-hole. This helps in the case that it the sensor may only match finger parts and not the whole hand, and it helps better distinguish the hand gestures that have slight differences. [3]

#### Training a Neural Network to Detect Hand Gestures with OpenCV in Python
This article shows the way to detect some simple hand gesture by using Python and Opencv to capture the image. 
The paper mainly focus on how to train the model from the large picture set get from Kaggle (Also, we could use our own dataset instead, this will increase the amount of gestures we can detect) and turn to its CNN network. 
The trained model used Opencv to capture our gesture image and translate to the CNN to decide which gesture are we showing and what function should reach out base on the image it get. It is a way to achieve hand gestures since the Resberry pi we are going to use is also good with Python. [4]

#### Install OpenCV 4 on your Raspberry Pi
A guidline on how to install opencv on the Resberry Pi to do image detection, and set the environment for the board to run correctly.[5]

### 4. Technical Approach and Implemenetation
#### Why Raspberry Pie and Arduino?
Arduino is a microcontroller, it does not run an operating system but it is power efficient. Raspberry Pie is a full computer, we set up our arduino in the Raspberry Pi. Combined together, raspberry pie offers a friendly environment for developing code, while Arduino handles precise real-time control of the motors.

### 5. Hardware set up 
#### Raspberry Pie
<span style="font-size: 0.75em">
    <img alt="Photo from www.raspberrypi.org" src="https://www.raspberrypi.org/homepage-9df4b/static/eef5d5d91acb34be0d7443b02cece1d1/8924f/8c67a3e02f41441dae98f8b91c792c1e1b4afef1_770a5842.jpg">
</span>


Raspberry Pi is a single board computer that has an ARMv6 700 MHz single-core processor, a VideoCore IV GPU and 512MB of RAM. For data storage and operating system, it uses an SC card. The OS installer used for our RPi3 was New Out Of Box Software (NOOBS), which allowed us to install a working Operatins System. The working OS that we isntalled is is Raspbian, which is a lightweight linux OS based on Debian. The Raspberry Pi used for this project isRaspberry Pi 3 Model B+ (RPi3). [6] Although it is possible for a 64-bit operating system to be installed in our RPi3, the 32-bit operating system was used, as it is also the OS that the RPi3 chooses by default. The 64-bit operatin system could have been installed later, but the 32-bit seemed to work fine. The benefit of having a 64-bit operatin system is that the OS can access 264 memory addresses, which is 18-Quintillion bytes of RAM, more than 4 GB of RAM. [7] A 64-bit processor will store more computational values and handle more data at once when compared to a 32-bit processor. This means that it will access more than four billion times the physical memory of a 32-bit processor. [8]

Our team opted to use Python for our learning algorithm, hence we installed Python 3 in our Raspberry Pi. Tensorflow occupies about 1 GB of our microSD cards, and it is a library whos main focus is deep learning. Because this library consumes a large amount of resources, executing tensorflow in our Raspberry Pi can be slow and it should not be expected to get fast results. Our small embedded device is only be able to deploy the most common models. According to qengineeding.eu, it will not be possible to train new models, or perform transfer learning. They advice to run pre-built deep learning models, conver frozen TensorFlow models to TensorFlow Lite flat buffer models.[9]

Our group worked on the hardware enviroment set up individually, therefore the Tensorflow version installed in our Raspberry Pi were 2.1 and 2.3. The instroduced some challenges, as our model was trained in version 2.3.1 and hence, some adjustements had to be done in order to ensure the model would predict in our Raspberry Pi. Tensorflow open-source software library has evolved and become quite large, therefore building it  on a simple 32-bit machine has become a difficult task. Rhaspberry Pi offers a faster and smaller version of Tensorflow, TensorFlow Lite, it uses less resources as it is designed for smalle computers. We opted for the normal Tensorflow library, since it was beneficial to perform training in our labtops for higher accuracy and speed purposes. Since our trainind was done in our labtops, our training model json file had to be modified in order to work on out rhaspberry pi. The modification to the rhaspberry pie would not have been necessay had we had the same version of tensorlow, but as we had to work distanced, our final hardware enviroments were set up differently. (discuss more of the saveModelArch.py)


#### Specifications
The Raspberry Pi 3 Model B+:
1.  Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @ 1.4GHz
2.  1GB LPDDR2 SDRAM
3.  2.4GHz and 5GHz IEEE 802.11.b/g/n/ac wireless LAN, Bluetooth 4.2, BLE
4.  Gigabit Ethernet over USB 2.0 (maximum throughput 300 Mbps)
5.  Extended 40-pin GPIO header
6.  Full-size HDMI
7.  4 USB 2.0 ports
8.  CSI camera port for connecting a Raspberry Pi camera
9.  DSI display port for connecting a Raspberry Pi touchscreen display
10. 4-pole stereo output and composite video port
11. Micro SD port for loading your operating system and storing data
12. 5V/2.5A DC power input
13. Power-over-Ethernet (PoE) support (requires separate PoE HAT)


#### Arduino

(to-do)

#### Specifications
Arduino NANO 33 BLE
1. Microcontroller	nRF52840 (datasheet)
2. Operating Voltage	3.3V
3. Input Voltage (limit)	21V
4. DC Current per I/O Pin	15 mA
5. Clock Speed	64MHz
6. CPU Flash Memory	1MB (nRF52840)
7. SRAM	256KB (nRF52840)
8. EEPROM	none
9. Digital Input / Output Pins	14
10. PWM Pins	all digital pins
11. UART	1
12. SPI	1
13. I2C	1
14. Analog Input Pins	8 (ADC 12 bit 200 ksamples)
15. Analog Output Pins	Only through PWM (no DAC)
16. External Interrupts	all digital pins
17. LED_BUILTIN	13
18. USB	Native in the nRF52840 Processor
19. IMU	LSM9DS1 (datasheet)
20. Length	45 mm
21. Width	18 mm
22. Weight	5 gr (with headers)


### 6. Analysis
Computer vision is a fast growing field. Applications in computer vision focuses on analysing amagery data to understand past events, and in most cases they use that understanding to predict future events. Due to the high demand of powerful hardware and software for computer vision, programming languages now offer a great range of libraries to support the process. One of the great challenges of computer vision is the high demand in computational power, as  the computer vision process requires high power for both image process and computation. According to algorithmia.com, one of the most popular languages for Aritificial intelligence applications is Python, but there are also other programs such as R, Java, Scala, and Rust. The reason why Python is one of the most popular programming languages for computer vision is that they have the most user friendly syntax, largest libraries and frameworks, dynamic applicability to a large amount of AI algorithms, and is very simple to read and write. [13] Some application areas for computer visions technology are video surveillance, biometrics, automotive, photography, movie production, Web search, medicine, augmented reality gaming, new user interfaces, and many more. [15]

#### Python
The language used in this project is Python. One of the main reasons why computer vision may be slow in Python is that Python has a global interpreter lock (GIL), a mutex/lock that every thread must acquire before they execute code. The reason for the global interpreter pointer is that python's memory management depends on reference counting. The reference counting keeps track of how many references there are to any memory location at all times. To avoid race conditions, the python designers decided to add the global interpreter lock to their design. 

Even though developers are not directly interacting with GIL when developing computer vision software, GIL can become a performance bottleneck when running multi-threaded code. Whenever we add references, this counter increments or decrements. An example of the problem with this implementation is that if we try to increment local variables, we first need the semaphore lock for the memory location, hence, executing code will be to slow. To avoid race conditions on the reference counter, we always have only one thread running at a time. The second reason for this lock is that in Python, many of the libraries are accessing C libraries, which were not created with thread safety in mind. Since we indirectly use these C libraries, Python code will not always be thread safe. Therefore, we have just one thread running at once and that give marely an illusion of multi-threaded programs in Python. Multithreading in computer vision is essential, as computer vision requires a vast amount of computation. As a consequence being able to access C code in python, the single-threaded code in python can be very fast, since the memory management model is simple and has this global interpreter. The trade off is that multi-threaded programs in in Python are not realistically running multiple-threads.

After discussing the python memory management model, one may wonder why use python for computer vision purposes if it has such a big impact on efficiency? As discussed in the later sections, Python, while also being a clear and syntax friendly high level language, offers different libraries for machine learning, tensor flow, neural networks, and other artificial intelligence applications. Although computing power is essential in these applications, the big tradeoff is simplicity for writting code and libraries that are essential tools for applications such as our hand gesture recognition system. 


#### OpenCV
OpenCV stands for Open Source Computer Vision Library, its applications are mainly for computer vision and machine learning purposes. Accorging to opencv.org, the library offers mroe than 2500 obtimized algorithms. The set of algorithms offered by openCV can be applied "to detect and recognize faces, identify objects, classify human actions in videos, track camera movements, track moving objects, extract 3D models of objects, produce 3D point clouds from stereo cameras, stitch images together to produce a high resolution image of an entire scene, find similar, images from an image database, remove red eyes from images taken using flash, follow eye movements, recognize scenery and establish markers to overlay it with augmented reality". [16] Becuase of the broad offereing of openCV, we decided to use this popular set of libraries for our gesture based embedded system, which aims to detect hand gestures to trigger desired behaviour in our computer. 


#### TensorFlow
To install TensorFlow, instead of installing from scratch, we used a short-cut provided by qengineering.edu. The installation process uses a Google software installer called Bazel, which generates a wheel. A Bazel is an open source build/test tool, it can be comparable to Make, Mave, and Graddle. Bazeil is a highlevel build ldanuge that "supports projects multiple languages and builds outputs for multiple platforms". [12] A wheel is part of the Python ecosystem and helps make isntallations faster stable in the package distribution process. [11] If we had opted for installing TensorFlow from scratch in the Rpi3, the process would have taken many hours and we would have generated many intermediate files that would have taken to much spaced in the SD memory card. [9]


#### Python Image Recognition
Our project makes use of the OpenCV and Tensor flow libraries in Python. A description of each algorithm is described next.

#### Code Algorithm for Raspberry Pi
Pseudo code for the algorithm that runs in the Raspberry Pi 3:

    Use pygame to build a prediction window

    Intialize a window or screen for display 

    Read the trained model

        Load a json file suing json.load()
    
        Load weights on the loaded model using a .h5 file, which contains multidimensional arrays of scientific data.
    
    Capture first image using USB camera

    Adjust the threshold variable for binarization using openCV globa variable cv2.THRESH_BINARY 

    If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).


    In a loop:

        Read frame of picture using the cap.read() method from openCV library
    
        Display image using cv2.rectable() method, it takes in the image, start_point coordinate, end_point coordinate, color in form of a tuple, and thickness
        
        Handle region on interest
    
            Resize and change color to greyscale using cv2.resize() and cv2.cvtColor()
        
            Make black and white for better predition 
        
            In this binarization
        
                If the grey scale value is greater than the set-threshold-value, we set the color to the maximun grey (white)
            
                If the value is less than the set-threshold-value, we set colot to zero (black)
            
        Resize resulting image
    
        Predict using the model.predict() method 

        Sort for printing
 
 
Explanation to some of the main functions used from openCV library are:

cv2.read() 

This method grabs, decodes and returns the next video frame. It does not take arguments and instead it gets called by the created image object. If anything goes wrong with this method call, the method returns false. 

cv2.cvtColor()

This method produces an image in black and white, which allows for better prediction. Accoring to "Color-to-Grayscale: Does the Method Matter in Image Recognition?", the main reason to use grayscale is to extract descriptors instead of operating in color images, the effect is simplification of algorithm and reduction of computation. [17]

cv2.resize()

This method scales the image being analized in each loop. This reduces the number of pixels from an image, which helps reduce the time of training a model. This is becuase, if training using neural networks for example, there is less number of input nodes that would have otherwise increased the complecity of the model. This may also be necessary to meet size requirement by a method, and openCV offers interpolation methods to resize an image. [18]

cv2.away(time_value) 

This method waits for a key event. It is due to Python's implementation of switching "threads" (as discussed in the python section) and it is necessary to process the event loop. If this method is not called, other main events, such as redraw, resize, and input event will not be called. [19]

Note: After describing the process for training input, one can see that  a black background may increase the quality of our predictions.

#### Code Algorithm for Training in Labtop
The initial part of the code will be similar to the one ran in the raspberry pi, as we initially take video input using the labtop camera.

(to-do)

### 6 Conclusion and Future Works
Our project consisted of a gesture based embedded system that acted as an assistant for user input through video camera. The Arduno contributed to our system by providing sensor data to the raspberry pi and therefore improving accuracy to our model. This was essential to reach our point of accuracy, as the model did not perform with high accuracy until the Arduino was added to the system. Our Raspberry pi collected image recognition from the USC video camera and performed data analysing in real time. The connections of our system included BLE and Wi-Fi. Due to the limitations of hardware and python language speed, out team opted for training our model in our labtops and then transfering that model to our raspberry pi, which required to perform the process of serialization to adjut the trained model to the new enviroment. 

There is always ways to make interfaces more user friendly and effective. For this project, future works can involve more options for hand gestures, which would give more functionality to the system. Additionally, improving the algorithm to make it faster at detecting hand gestures would be beneficial to the system.

### 7. Contributions
### 8. References

[1] C.J. Cohen, G. Beach, G. Foulk "A basic hand gesture control system for PC applications"  Proceedings 30th Applied Imagery Pattern Recognition Workshop (AIPR 2001). Analysis and Understanding of Time Varying Imagery

[2] "Arduino based Hand Gesture Control of Your Computer" Electronics Hub, October 06, 2019

[3] Zhou Ren, Junsong Yuan, Member, IEEE, Jingjing Meng, Member, IEEE, and Zhengyou Zhang, Fellow, IEEE "Robust Part-Based Hand Gesture Recognition Using Kinect Sensor" IEEE TRANSACTIONS ON MULTIMEDIA, VOL. 15, NO. 5, AUGUST 2013

[4] "Training a Neural Network to Detect Gestures with OpenCV in Python", Brenner Heintz, December 18, 2018

[5] "Install OpenCV 4 on your Raspberry Pi", Adrian Rosebrock, September 26, 2018

[6] http://meseec.ce.rit.edu/551-projects/spring2017/2-3.pdf

[7] https://www.geeksforgeeks.org/difference-32-bit-64-bit-operating-systems

[8] https://www.digitaltrends.com/computing/32-bit-vs-64-bit-operating-systems/

[9] https://qengineering.eu/install-tensorflow-2.2.0-on-raspberry-pi-4.html

[10] https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/

[11] https://realpython.com/python-wheels/

[12] https://www.bazel.build/

[13] https://algorithmia.com

[15] Pulli, Kari "Realtime Computer Vision with OpenCV" AMCQUEUE, 2012

[16] https://opencv.org/about/

[17] Kanan, Christopher "Color-to-Grayscale: Does the Method Matter in Image Recognition?". PLOS ONE. January 10, 2012. 

[18] https://www.geeksforgeeks.org/image-resizing-using-opencv-python/

[19] https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=waitkey#waitkey


