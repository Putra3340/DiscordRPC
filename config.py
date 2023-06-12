def missing_cfg():
    print("hey..how tf the cfg file lost?")
    print("i got you..i will make another one 4 u")
    file = open("main.cfg", "w")
    # Write data to the file
    file.write("--Putra3340 Simple CFG FILE--\n\n")
    file.write("client-id=994223622170357761\n")
    file.write("state=this is state\n")
    file.write("details=this is detail\n")
    file.write("large_image=genshin\n")
    file.write("large_text=this is large text\n")
    file.write("small_image=image\n")
    file.write("small_text=this is small_text\n")
    file.write("party_id=idk\n")
    file.write("button1=subcreb\n")
    file.write("button1_link=https://www.youtube.com/@PutraNjir/\n")
    file.write("button2=subrek\n")
    file.write("button2_link=https://www.youtube.com/@PutraNjir/\n\n")
    file.write("--Description--\n")
    file.write("Don't leave it empty or get error\n")
    file.write("if you didn't use small_image fill it with null\n")
    file.write("large_image is asset that on the application\n")
    file.write("small_image is asset that on the application\n")



    # Close the file
    file.close()