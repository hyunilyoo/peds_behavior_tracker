# Detecting Pedestrian behaviors
This is a project that makes object dection classifier on Pedestrian behaviors by using Tensorflow Object Detection API. I've followed https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10 instructions to set up Tensorflow Object Detection API and used LabelImg to annotate the pedestrian behaviors that I personally defined.
## Process of Training a customized dataset
***1.*** Get clips of drive view videos that have pedestrian in it
***2.*** Cut by frames of the clips
***3.*** Annotate images with bounding boxes and labels (Pedestrian Behaviors) 
***4.*** Generate train and test tfrecord files based on images and xml files
***5.*** Choose what model I'm going to use for object detection(Faster R-CNN)
***6.*** Use Google Colab to train the model
***7.*** Use the model to predict pedestrian behaviors on new images or videos

## Structure 
'''
***1. resize_img.py:*** Resize the pixel size of images if images are too big for training the model.  
***2. xml_to_csv.py:*** Convert xml files that are created when you labeled the image by LabelImg to csv files.  
***3. generate_tfrecord.py:*** Convert csv files to tfrecord files which are propriate train the model on Tensorflow.  
***4. training_on_colab.ipynb:*** Contains commends that enable Colab to access cloud powered GPU to use Tensorflow-gpu, and train the model.    
***5. object_detection_image.py:*** Use trained model and execute the prediction on a single image.  
***6. object_detection_video.py:*** Use trained model and execuete the prediction on frames of a video.  
***7. create_video.py:*** Use frames from the output of object_detection_video.py to create a video.  
***8. training:*** Contains config file for faster-rcnn-inception-v2-coco-2018-01-28 and labelmap.pbtxt.  
***9. test_imgs:*** Results on images  
***10. test_videos:*** Results on videos  
'''
### Results on videos
![](test_videos/test_video_1.gif)
![](test_videos/test_video_2.gif)
![](test_videos/test_video_3.gif)
