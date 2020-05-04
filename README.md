# Detecting Pedestrian behaviors
This is a project that makes object dection classifier on Pedestrian behaviors by using Tensorflow Object Detection API. I've followed https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10 instructions to set up Tensorflow Object Detection API and used LabelImg to annotate the pedestrian behaviors that I personally defined.
## Motivation
In Autonomous driving industry, the most important thing to consider is public safety. Therefore, prediction on other cars' and pedestrian's behaviors are one of the key features for public safety. 
It is important to predict the other cars' behaviors; however, predicting pedestrian behaviors might be more important to focus on because when an accident involves with predestrians, there is a high probability of that accident is being a fatal accident. If we can predict what is a pedestrian's intent on the public road, it will make easier for a self-driving car to maneuver around pedestrians.
## Pedestrian Behaviors
These are defined by me. The reason behind of these is if pedestrians are not aware of a self-driving car is approaching to them, they might suddenly change a direction of travelling or even come toward a self-driving car. And this can cause a harsh brake or even an accident due to the lack of time to react for a self-driving car. On the other hand, the self-driving car has to be very sensitive and that can cause unnecessary brakes or awkward nudges without the information of pedestrians are aware of a self-driving car. Therefore, I believe knowing whether pedestrians are aware of a self-driving car or not is essential for what actions a self-driving car to execute around pedestrians.  
```
1. n_looking/g: A pedestrian is not looking at the vehicle and crossing the road  
2. n_looking/ng: A pedestrian is not looking at the vehicle and not crossing the road  
3. looking/g: A pedestrian is looking at the vehicle and crossing the road  
4. looking/ng: A pedestrian is looking at the vehicle and not crossing the road  
```
## Process of Training a customized dataset
***1.*** Get clips of drive view videos that have pedestrian in it  
***2.*** Cut by frames of the clips  
***3.*** Annotate images with bounding boxes and labels (Pedestrian Behaviors)   
***4.*** Generate train and test tfrecord files based on images and xml files  
***5.*** Choose what model I'm going to use for object detection(Faster R-CNN)  
***6.*** Use Google Colab to train the model  
***7.*** Use the model to predict pedestrian behaviors on new images or videos  
## Structure 
```
├──README.md
├──Report.pdf: Explain how I approach this project in slides format
├──project_proposal.pdf: Explain what motivations are behind in this project
├──resize_img.py: Resize the pixel size of images if images are too big for training the model  
├──xml_to_csv.py: Convert xml files that are created when you labeled the image by LabelImg to csv files  
├──generate_tfrecord.py: Convert csv files to tfrecord files which are propriate train the model on Tensorflow  
├──training_on_colab.ipynb: Contains commends that enable Colab to access cloud powered GPU to use Tensorflow-gpu, and train the model    
├──object_detection_image.py: Use trained model and execute the prediction on a single image  
├──object_detection_video.py: Use trained model and execuete the prediction on frames of a video  
├──create_video.py: Use frames from the output of object_detection_video.py to create a video  
├──training: Contains config file for faster-rcnn-inception-v2-coco-2018-01-28 and labelmap.pbtxt  
├──test_imgs: Results on images  
└──test_videos: Results on videos  
```
### Results on videos
![](test_videos/test_video_1.gif)
![](test_videos/test_video_2.gif)
![](test_videos/test_video_3.gif)
