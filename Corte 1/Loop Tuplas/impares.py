{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPk22NPAiRtfeINcaz1xtU4"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":2,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"NgqymJQ5tlTE","executionInfo":{"status":"ok","timestamp":1725280243216,"user_tz":300,"elapsed":3471,"user":{"displayName":"Juan Sarta","userId":"04879527621587975078"}},"outputId":"75c17aa7-108b-4c08-b4d3-ffb02da3bc5f"},"outputs":[{"output_type":"stream","name":"stdout","text":["Enter a number of times: 10\n","<class 'int'>\n","10\n","i =  1\n","i =  2\n","i =  3\n","i =  4\n","i =  5\n","i =  6\n","i =  7\n","i =  8\n","i =  9\n","i =  10\n"]}],"source":["# for i in range (1,21):\n","#     residual = i%2\n","#     if residual == 0:\n","#         print(f'{i} is even')\n","#     else:\n","#         #print(f'{i} is odd')\n","#         print(str(i) + ' is odd')\n","\n","# for i in range (0,6):\n","#     result = i**3\n","#     print(result)\n","\n","times = input(\"Enter a number of times: \")\n","times = float(times)\n","times = int(times)\n","print(type(times))\n","print(times)\n","\n","if times == 0:\n","    print(\"Don't do anything\")\n","else:\n","    for i in range(1,times+1):\n","        print(\"i = \", i)"]}]}