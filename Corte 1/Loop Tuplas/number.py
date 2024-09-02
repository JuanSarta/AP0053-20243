{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyMfK9Rs7oYI4rgnL5GpiUB1"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":1,"metadata":{"id":"lRw-ZQXTuyQi","executionInfo":{"status":"ok","timestamp":1725280521561,"user_tz":300,"elapsed":640,"user":{"displayName":"Juan Sarta","userId":"04879527621587975078"}},"outputId":"96503826-686a-411a-d35e-4111cf6f5523","colab":{"base_uri":"https://localhost:8080/","height":435}},"outputs":[{"output_type":"display_data","data":{"text/plain":["<Figure size 640x480 with 1 Axes>"],"image/png":"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\n"},"metadata":{}}],"source":["import random\n","from matplotlib import pyplot as plt\n","\n","# Add your code below:\n","numbers_a = range(1, 13)\n","numbers_b = [random.randint(1, 1000) for i in range(12)]\n","plt.plot(numbers_a, numbers_b)\n","plt.show()"]}]}