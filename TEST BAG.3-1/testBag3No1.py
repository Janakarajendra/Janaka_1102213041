from PIL import Image 
  
Original_Image = Image.open("baboon.png") 

rotated_image1 = Original_Image.rotate(180) 
  

rotated_image2 = Original_Image.transpose(Image.ROTATE_90) 
  
rotated_image3 = Original_Image.rotate(0) 

rotated_image1.show() 
rotated_image2.show() 
rotated_image3.show() 