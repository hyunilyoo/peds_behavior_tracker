# Detecting Pedestrian Intent
## Description
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
### Results on videos
![](test_videos/test_video_1.gif)
![](test_videos/test_video_2.gif)
![](test_videos/test_video_3.gif)
