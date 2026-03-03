from deepface import DeepFace

result: dict = DeepFace.verify(img1_path = "images/img1.jpg", img2_path = "images/img2.jpg")
