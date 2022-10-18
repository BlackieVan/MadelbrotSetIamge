# MadelbrotSetIamge


该程序可在py文件同目录下生成一张曼德博集合的图片  
Will generate a nice image of Mandelbrot Set at the same directory of the .py file  

使用的语言是Python3  
Use Python3  

需要名为“Pillow”的图形库  
Needs "Pillow" libiary  
https://github.com/python-pillow/Pillow  

如果你不知道何为曼德博集合，请点击：https://baike.baidu.com/item/%E6%9B%BC%E5%BE%B7%E5%8D%9A%E9%9B%86%E5%90%88/5831843  
If you dont know about Mandelbrot Set,pls check https://en.wikipedia.org/wiki/Mandelbrot_set  

!!!此程序由于单线程运算，运行速度慢得离谱，图片大于1000x1000时，谨慎选择，以防砸电脑。  
!!!Due to single thread processing,this program runs stupidly slow,if choose size>1000x1000,prepare to fxxk up your computer.

更新1：  
增加了独立的颜色函数文件  
Update1:  
Add Standalone ColorFunction file  

更新2：
1)将图片生成路径改为Images
2)优化了一些颜色函数
3)增加了颜色函数测试文件，可在Images文件夹下生成一张颜色函数预览图。
Update2:
1)Modify the image directory to "Images"
2)Optimize some ColorFunction
3)Add ColorFunctionTest file,will generate a preview image of ColorFunction at "Images"

示例：  
Examples:  

![image](https://github.com/BlackieVan/MadelbrotSetIamge/blob/main/Examples/Mandelbrot_X-0.5000_Y0.0000_R1.0000_N100_W1000_H1000_1610692012.png)

![image](https://github.com/BlackieVan/MadelbrotSetIamge/blob/main/Examples/Mandelbrot_X0.3000_Y0.5500_R0.1000_N100_W1000_H1000_1611648033.png)

![image](https://github.com/BlackieVan/MadelbrotSetIamge/blob/main/Examples/Mandelbrot_X-0.4600_Y0.5800_R0.0100_N100_W1000_H1000_1611643273.png)